#!/usr/bin/env python3
"""
Generate 13 professional PDF resources for the University of Artemis Give page.
"""

import os, io, math
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable)
from reportlab.platypus.flowables import Flowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

OUT_DIR = '/home/z/my-project/public/resources'
CRIMSON = '#8A0000'; DARK = '#141414'; GRAY = '#6B7280'; LIGHT_GRAY = '#F3F4F6'
WIDTH, HEIGHT = A4

try:
    pdfmetrics.registerFont(TTFont('DejaVuSans', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
    BODY_FONT = 'DejaVuSans'; BOLD_FONT = 'DejaVuSans-Bold'
except: BODY_FONT = 'Helvetica'; BOLD_FONT = 'Helvetica-Bold'

fm.fontManager.addfont('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
fm.fontManager.addfont('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']; plt.rcParams['axes.unicode_minus'] = False

styles = getSampleStyleSheet()
style_title = ParagraphStyle('AT', parent=styles['Title'], fontName=BOLD_FONT, fontSize=28, leading=34, textColor=HexColor(DARK), spaceAfter=6)
style_subtitle = ParagraphStyle('AS', parent=styles['Normal'], fontName=BODY_FONT, fontSize=14, leading=20, textColor=HexColor(GRAY), spaceAfter=20)
style_h1 = ParagraphStyle('AH1', parent=styles['Heading1'], fontName=BOLD_FONT, fontSize=20, leading=26, textColor=HexColor(CRIMSON), spaceBefore=24, spaceAfter=10)
style_h2 = ParagraphStyle('AH2', parent=styles['Heading2'], fontName=BOLD_FONT, fontSize=14, leading=18, textColor=HexColor(DARK), spaceBefore=16, spaceAfter=8)
style_body = ParagraphStyle('AB', parent=styles['Normal'], fontName=BODY_FONT, fontSize=10, leading=15, textColor=HexColor(DARK), spaceAfter=8, alignment=TA_JUSTIFY)
style_body_small = ParagraphStyle('ABS', parent=style_body, fontSize=9, leading=13, spaceAfter=4)
style_bullet = ParagraphStyle('ABL', parent=style_body, leftIndent=20, bulletIndent=8, spaceAfter=4)
style_stat = ParagraphStyle('AST', parent=styles['Normal'], fontName=BOLD_FONT, fontSize=22, leading=28, textColor=HexColor(CRIMSON), alignment=TA_CENTER)
style_stat_label = ParagraphStyle('ASL', parent=styles['Normal'], fontName=BODY_FONT, fontSize=9, leading=12, textColor=HexColor(GRAY), alignment=TA_CENTER, spaceAfter=4)
style_caption = ParagraphStyle('AC', parent=styles['Normal'], fontName=BODY_FONT, fontSize=8, leading=11, textColor=HexColor(GRAY), alignment=TA_CENTER, spaceAfter=12)

class ColorBar(Flowable):
    def __init__(self, w, h, c):
        Flowable.__init__(self); self.width=w; self.height=h; self.color=HexColor(c)
    def draw(self):
        self.canv.setFillColor(self.color); self.canv.rect(0,0,self.width,self.height,fill=1,stroke=0)

class CrimsonLine(Flowable):
    def __init__(self, width=500):
        Flowable.__init__(self); self.width=width; self.height=2
    def draw(self):
        self.canv.setStrokeColor(HexColor(CRIMSON)); self.canv.setLineWidth(2); self.canv.line(0,1,self.width,1)

def add_page_number(canvas, doc):
    canvas.saveState(); canvas.setFont(BODY_FONT, 7); canvas.setFillColor(HexColor(GRAY))
    canvas.drawCentredString(WIDTH/2, 25, f"University of Artemis  |  Page {canvas.getPageNumber()}")
    canvas.setStrokeColor(HexColor(CRIMSON)); canvas.setLineWidth(2); canvas.line(40,HEIGHT-35,WIDTH-40,HEIGHT-35)
    canvas.restoreState()

def add_cover(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(HexColor(CRIMSON)); canvas.rect(0,HEIGHT-200,WIDTH,200,fill=1,stroke=0)
    canvas.setFillColor(white); canvas.setFont(BOLD_FONT,32); canvas.drawCentredString(WIDTH/2,HEIGHT-100,"UNIVERSITY OF ARTEMIS")
    canvas.setFont(BODY_FONT,12); canvas.drawCentredString(WIDTH/2,HEIGHT-130,"The Founding Campaign")
    canvas.setFont(BODY_FONT,10); canvas.drawCentredString(WIDTH/2,HEIGHT-160,"www.artemisui.org  |  donate@artemisui.org")
    canvas.setStrokeColor(HexColor(CRIMSON)); canvas.setLineWidth(1); canvas.line(40,40,WIDTH-40,40)
    canvas.restoreState()

def make_stat_block(stats):
    data = [[Paragraph(str(v), style_stat) for v,l in stats]]
    labels = [[Paragraph(l, style_stat_label) for v,l in stats]]
    cw = (WIDTH-80)/len(stats)
    t = Table(data+labels, colWidths=[cw]*len(stats))
    t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,0),12),('BOTTOMPADDING',(0,0),(-1,0),2),
        ('TOPPADDING',(0,1),(-1,1),2),('BOTTOMPADDING',(0,1),(-1,1),12),
        ('BACKGROUND',(0,0),(-1,-1),HexColor(LIGHT_GRAY)),
        ('LINEAFTER',(0,0),(-2,-1),0.5,HexColor('#E5E7EB'))]))
    return t

def gen_chart(func, name, dpi=150):
    path = os.path.join(OUT_DIR, f'_chart_{name}.png')
    fig = func(); fig.savefig(path, dpi=dpi, bbox_inches='tight', facecolor='white', edgecolor='none'); plt.close(fig)
    return path

def chart_allocation():
    fig,ax=plt.subplots(figsize=(6,4))
    ax.pie([82,7,5,3,3], explode=(0.05,0,0,0,0), labels=['Place\n(50 Colleges)','Minds\n(Faculty)','Access\n(Scholarships)','Excellence\n(Research)','Progress\n(Infrastructure)'], autopct='%1.0f%%', colors=['#8A0000','#6B0000','#4338CA','#0E7490','#15803D'], startangle=90, textprops={'fontsize':8})
    ax.set_title('$100M Campaign Allocation', fontsize=12, fontweight='bold', color='#141414')
    return fig

def chart_revenue():
    fig,ax=plt.subplots(figsize=(6,3.5))
    x=np.arange(5); w=0.35
    ax.bar(x-w/2,[300,340,385,435,490],w,label='Tuition Revenue ($M)',color='#8A0000')
    ax.bar(x+w/2,[262,298,337,381,430],w,label='Annual Surplus ($M)',color='#4338CA')
    ax.set_xticks(x); ax.set_xticklabels(['Yr 1','Yr 2','Yr 3','Yr 4','Yr 5'],fontsize=9)
    ax.set_ylabel('$ Millions',fontsize=9); ax.set_title('5-Year Revenue Projection',fontsize=12,fontweight='bold',color='#141414')
    ax.legend(loc='best',fontsize=8); ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    return fig

def chart_milestones():
    fig,ax=plt.subplots(figsize=(6,3))
    ax.fill_between([0,3,6,9,12],[0,50,85,100,100],step='post',alpha=0.15,color='#8A0000')
    ax.step([0,3,6,9,12],[0,50,85,100,100],where='post',color='#8A0000',linewidth=2)
    for m,c in zip([0,3,6,9,12],[0,50,85,100,100]): ax.annotate(f'${c}M',(m,c),textcoords="offset points",xytext=(0,10),ha='center',fontsize=8,fontweight='bold',color='#8A0000')
    ax.set_xlabel('Months',fontsize=9); ax.set_ylabel('Commitments ($M)',fontsize=9)
    ax.set_title('Campaign Timeline',fontsize=12,fontweight='bold',color='#141414'); ax.set_ylim(0,115)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    return fig

def chart_endowment():
    fig,ax=plt.subplots(figsize=(6,3))
    e=[3,63,126,192,262]; ax.fill_between(range(5),e,alpha=0.15,color='#8A0000')
    ax.plot(range(5),e,color='#8A0000',linewidth=2,marker='o',markersize=5)
    for i,v in enumerate(e): ax.annotate(f'${v}M',(i,v),textcoords="offset points",xytext=(0,10),ha='center',fontsize=8,fontweight='bold',color='#8A0000')
    ax.set_xticks(range(5)); ax.set_xticklabels(['Yr 1','Yr 2','Yr 3','Yr 4','Yr 5'],fontsize=9)
    ax.set_ylabel('Endowment ($M)',fontsize=9); ax.set_title('Endowment Growth (Surplus-Funded)',fontsize=12,fontweight='bold',color='#141414')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    return fig

def chart_students():
    fig,ax=plt.subplots(figsize=(6,3))
    s=[100,120,145,175,210]; ax.fill_between(range(5),s,alpha=0.12,color='#0E7490')
    ax.plot(range(5),s,color='#0E7490',linewidth=2,marker='s',markersize=5)
    for i,v in enumerate(s): ax.annotate(f'{v}K',(i,v),textcoords="offset points",xytext=(0,10),ha='center',fontsize=8,fontweight='bold',color='#0E7490')
    ax.set_xticks(range(5)); ax.set_xticklabels(['Yr 1','Yr 2','Yr 3','Yr 4','Yr 5'],fontsize=9)
    ax.set_ylabel('Students (K)',fontsize=9); ax.set_title('Projected Student Enrollment',fontsize=12,fontweight='bold',color='#141414')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    return fig

def chart_segments():
    fig,ax=plt.subplots(figsize=(6,2.5))
    segs=['Community\n($10K-$999K)','Major Donors\n($1M-$5M)','Lead Donors\n($10M+)']
    vals=[10,20,70]; cols=['#15803D','#4338CA','#8A0000']
    bars=ax.barh(segs,vals,color=cols,height=0.6)
    for b,v in zip(bars,vals): ax.text(b.get_width()+1,b.get_y()+b.get_height()/2.,f'${v}M ({v}%)',va='center',fontsize=8,fontweight='bold')
    ax.set_title('Donor Segments',fontsize=12,fontweight='bold',color='#141414'); ax.set_xlim(0,85)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    return fig

def chart_world_map():
    fig,ax=plt.subplots(figsize=(10,5))
    cities={'Venice':(12.3,45.4),'San Francisco':(-122.4,37.8),'Singapore':(103.8,1.3),'Berlin':(13.4,52.5),'Nairobi':(36.8,-1.3),'Sao Paulo':(-46.6,-23.5),'Vancouver':(-123.1,49.3),'London':(-0.1,51.5),'Mumbai':(72.9,19.1),'Kigali':(30.1,-1.9)}
    ax.set_xlim(-180,180); ax.set_ylim(-60,80); ax.set_facecolor('#F0F4F8'); fig.patch.set_facecolor('white')
    for city,(lon,lat) in cities.items():
        if city in ['Venice','San Francisco','Singapore']:
            ax.plot(lon,lat,'o',markersize=12,color='#8A0000',zorder=5)
            ax.annotate(city,(lon,lat),textcoords="offset points",xytext=(8,8),fontsize=8,fontweight='bold',color='#8A0000')
        else:
            ax.plot(lon,lat,'s',markersize=8,color='#4338CA',zorder=5)
            ax.annotate(city,(lon,lat),textcoords="offset points",xytext=(6,6),fontsize=7,color='#141414')
    ax.plot([],[],'o',markersize=10,color='#8A0000',label='Central Node'); ax.plot([],[],'s',markersize=8,color='#4338CA',label='College')
    ax.legend(loc='lower left',fontsize=9); ax.set_title('University of Artemis - Global Network',fontsize=14,fontweight='bold',color='#141414')
    ax.grid(True,alpha=0.2)
    return fig

print("Generating charts...")
charts = {n: gen_chart(f, n) for n,f in [('allocation',chart_allocation),('revenue',chart_revenue),('milestones',chart_milestones),('endowment',chart_endowment),('students',chart_students),('segments',chart_segments),('world_map',chart_world_map)]}
print("Charts done.")

def std_table(data, widths=None):
    if not widths: widths = [WIDTH/len(data[0])]*len(data[0])
    t = Table(data, colWidths=widths)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),HexColor(CRIMSON)),('TEXTCOLOR',(0,0),(-1,0),white),
        ('FONTNAME',(0,0),(-1,0),BOLD_FONT),('FONTSIZE',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),4),
        ('BOTTOMPADDING',(0,0),(-1,-1),4),('LINEBELOW',(0,0),(-1,-1),0.5,HexColor('#E5E7EB')),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[white,HexColor(LIGHT_GRAY)])]))
    return t

# 1. FOUNDING PROSPECTUS
def gen_founding_prospectus():
    p=os.path.join(OUT_DIR,'artemis-founding-prospectus.pdf')
    doc=SimpleDocTemplate(p,pagesize=A4,leftMargin=40,rightMargin=40,topMargin=50,bottomMargin=50)
    s=[]; s.append(Spacer(1,100)); s.append(Paragraph("FOUNDING PROSPECTUS",style_title)); s.append(CrimsonLine()); s.append(Spacer(1,12))
    s.append(Paragraph("The University of Artemis",ParagraphStyle('CS',parent=style_subtitle,fontSize=18,leading=24)))
    s.append(Paragraph("$100M Founding Campaign  |  12 Months  |  For Civilization",style_subtitle))
    s.append(Spacer(1,30)); s.append(make_stat_block([('$100M','Campaign Goal'),('50','Colleges'),('100,000','Students Year 1'),('6','Continents')]))
    s.append(Spacer(1,40)); s.append(Paragraph("donate@artemisui.org  |  www.artemisui.org",ParagraphStyle('CT',parent=style_body_small,alignment=TA_CENTER,textColor=HexColor(CRIMSON)))); s.append(PageBreak())
    s.append(Paragraph("THE PROBLEM",style_h1))
    s.append(Paragraph("Higher education is in crisis. Tuition has outpaced inflation by 4x since 1980. A billion people will reach university age by 2030, yet capacity has barely grown. The richest universities hoard endowments while the brightest minds in developing nations are locked out entirely. The global higher education market exceeds $2.5 trillion annually, yet it serves fewer than 220 million students. In Sub-Saharan Africa, only 9% of college-age people are enrolled. Employers report 40% of graduates lack workforce skills.",style_body))
    s.append(Paragraph("THE VISION",style_h1))
    s.append(Paragraph("The University of Artemis re-engineers humanity's approach to learning. It operates as the Artemis Collegium - an alliance of 10 residential colleges across 6 continents, connected by a synchronous global campus. Students rotate through 6 cities over 4 years. The curriculum is built on four pillars: epistemology, computational thinking, global systems, and creative expression. Students declare missions, not majors.",style_body))
    s.append(Paragraph("THE FINANCIAL MODEL",style_h1))
    s.append(Paragraph("Artemis is self-sustaining from Year 1. The $100M campaign launches a permanent institution. Tuition revenue of $300M/year covers all costs with $262M annual surplus. That surplus self-funds scholarships, builds the endowment, and seeds new Colleges.",style_body))
    s.append(Spacer(1,8)); s.append(Image(charts['revenue'],width=420,height=245)); s.append(Paragraph("5-Year Revenue and Surplus Projection",style_caption))
    s.append(make_stat_block([('$100M','Campaign'),('$300M/yr','Revenue'),('$262M/yr','Surplus'),('$1.5B','5-Year Total')])); s.append(PageBreak())
    s.append(Paragraph("CAMPAIGN ALLOCATION",style_h1))
    s.append(Image(charts['allocation'],width=400,height=270)); s.append(Paragraph("$100M Campaign Allocation by Pillar",style_caption))
    s.append(std_table([['Pillar','Amount','%','Purpose'],['Place (50 Colleges)','$82M','82%','Property acquisition and repurposing'],['Minds (Faculty)','$7M','7%','Faculty compensation bridge'],['Access (Scholarships)','$5M','5%','Year 1 scholarship seed'],['Excellence (Research)','$3M','3%','Centers of Inquiry startup'],['Progress (Innovation)','$3M','3%','Endowment seed, infrastructure']],widths=[120,50,30,240]))
    s.append(PageBreak())
    s.append(Paragraph("ACADEMIC DISTINCTION",style_h1))
    s.append(Paragraph("Artemis does not follow the lecture-and-exam paradigm. The four foundational pillars: epistemology, computational thinking, global systems, creative expression. Students declare a Mission rather than a major. Assessment is competency-based. Adaptive Paced Learning adapts to each student's rhythm. Nineteen Centers of Inquiry drive research.",style_body))
    s.append(Paragraph("CAMPAIGN MILESTONES",style_h1))
    s.append(Image(charts['milestones'],width=420,height=210)); s.append(Paragraph("Campaign Timeline and Cumulative Commitments",style_caption))
    s.append(Paragraph("NAMING OPPORTUNITIES",style_h1))
    s.append(std_table([['Opportunity','Amount','Scope'],['Central Node','$25M','Venice, San Francisco, or Singapore - ~5,000 students'],['Tier A College','$10M','Flagship city - ~2,500 students'],['Center of Inquiry','$10M','19 permanently endowed research centers'],['Tier B College','$5M','Major global city - ~2,000 students'],['Distinguished Professorship','$5M','Generates $225K/yr in perpetuity'],['Degree Program','$3M','55 degree programs'],['Tier C College','$2M','Emerging city - ~1,100 students'],['Scholarship Fund','$12K','Full scholarship, 4 years']],widths=[150,60,230]))
    s.append(PageBreak())
    s.append(Paragraph("GIVING CIRCLES",style_h1))
    s.append(std_table([['Circle','Range','Key Benefits'],["Founders' Circle",'$10M+','Named endowment, Board of Visitors seat'],["Guardians' Circle",'$5M-$9.9M','Named College or Center'],["Builders' Circle",'$1M-$4.9M','Named Professorship or Scholarship'],["Fellows' Circle",'$100K-$999K','Named scholarship or tutorial room'],['Friends of Artemis','$10K-$99K','Founding Donor Roll'],['The 99','$99+','Waitlist priority']],widths=[110,80,250]))
    s.append(Paragraph("GOVERNANCE & ACCOUNTABILITY",style_h1))
    s.append(Paragraph("Three legal entities: Delaware 501(c)(3) (primary), UK CIO (secondary), Swiss Fondation (tertiary). No individual controls more than one-third of board seats. Annual Big Four audit published publicly. Every dollar tracked in annual impact report.",style_body))
    s.append(Paragraph("THE ASK",style_h1))
    s.append(Paragraph("This is the zero-to-one moment. After this, Artemis is self-sustaining forever.",style_body))
    s.append(Spacer(1,16)); s.append(Paragraph("$100 MILLION. 12 MONTHS. FOR CIVILIZATION.",ParagraphStyle('Ask',parent=style_title,fontSize=24,alignment=TA_CENTER,textColor=HexColor(CRIMSON))))
    s.append(Spacer(1,16)); s.append(Paragraph("donate@artemisui.org  |  www.artemisui.org",ParagraphStyle('AC2',parent=style_body,alignment=TA_CENTER,textColor=HexColor(CRIMSON),fontSize=12)))
    doc.build(s,onFirstPage=add_cover,onLaterPages=add_page_number); print(f"  Created: {p}")

# 2. CAMPAIGN OVERVIEW
def gen_campaign_overview():
    p=os.path.join(OUT_DIR,'artemis-campaign-overview.pdf')
    doc=SimpleDocTemplate(p,pagesize=A4,leftMargin=35,rightMargin=35,topMargin=45,bottomMargin=35)
    s=[]; s.append(ColorBar(WIDTH-70,4,CRIMSON)); s.append(Spacer(1,8))
    s.append(Paragraph("UNIVERSITY OF ARTEMIS  |  CAMPAIGN OVERVIEW",ParagraphStyle('OT',parent=style_h2,fontSize=14,textColor=HexColor(CRIMSON))))
    s.append(Paragraph("$100M Founding Campaign  |  12 Months  |  For Civilization",ParagraphStyle('OS',parent=style_body_small,textColor=HexColor(GRAY)))); s.append(CrimsonLine()); s.append(Spacer(1,6))
    s.append(make_stat_block([('$100M','Goal'),('50','Colleges'),('100K','Students'),('6','Continents'),('35','Countries')])); s.append(Spacer(1,6))
    s.append(std_table([['Phase','Timeline','Target','Deliverable'],['Quiet Phase','Months 1-3','$50M','Lead gifts secured'],['Public Phase','Months 4-6','$85M','Website, events, press'],['Close & Capitalise','Months 7-9','$100M','Properties, legal'],['Build & Launch','Months 10-12','Live','Faculty, colleges, students']],widths=[95,75,55,215]))
    s.append(Spacer(1,6))
    s.append(std_table([['Pillar','Allocation','Purpose'],['Place','$82M (82%)','50 Colleges acquired and repurposed'],['Minds','$7M (7%)','Faculty launch bridge'],['Access','$5M (5%)','Year 1 scholarships'],['Excellence','$3M (3%)','19 Centers of Inquiry'],['Progress','$3M (3%)','Endowment seed']],widths=[80,80,280]))
    s.append(Spacer(1,6))
    s.append(Paragraph("How to Give: Online, wire, crypto, securities, planned giving, employer matching, DAFs, in-kind. US 501(c)(3) tax-deductible. UK Gift Aid (+25%).",style_body_small))
    s.append(Paragraph("donate@artemisui.org  |  www.artemisui.org",ParagraphStyle('OC',parent=style_body_small,textColor=HexColor(CRIMSON),alignment=TA_CENTER)))
    doc.build(s,onFirstPage=add_page_number,onLaterPages=add_page_number); print(f"  Created: {p}")

# 3. CASE FOR SUPPORT
def gen_case_for_support():
    p=os.path.join(OUT_DIR,'artemis-case-for-support.pdf')
    doc=SimpleDocTemplate(p,pagesize=A4,leftMargin=40,rightMargin=40,topMargin=50,bottomMargin=50)
    s=[]; s.append(Spacer(1,80)); s.append(Paragraph("CASE FOR SUPPORT",style_title)); s.append(CrimsonLine()); s.append(Paragraph("Why Artemis, Why Now, and Why Your Gift Creates a Self-Sustaining Institution",style_subtitle)); s.append(PageBreak())
    s.append(Paragraph("WHY NOW",style_h1)); s.append(Paragraph("The tools that make a global, residential, digitally-connected institution possible did not exist five years ago. They do now. By 2030, the global middle class will expand by 1.4 billion people, and with it the demand for quality higher education. Yet university capacity has barely kept pace. In Africa, enrollment rates remain below 10%. The opportunity cost of inaction is incalculable.",style_body))
    s.append(Paragraph("WHY ARTEMIS",style_h1)); s.append(Paragraph("Artemis is not another online university. It is a completely new model: residential, global, mission-driven, financially self-sustaining from Year 1. The Collegium model is proven - Oxford and Cambridge have operated this way for 800 years. Artemis adds scale (50 colleges), global reach (6 continents), and financial sustainability (tuition-funded surplus).",style_body))
    s.append(Paragraph("WHY YOUR GIFT MATTERS",style_h1)); s.append(Paragraph("Your gift is seed capital that launches a permanent institution. After Year 1, the $262M annual surplus funds scholarships, builds the endowment, and seeds new Colleges. Every campaign dollar unlocks $15 in 5-year surplus.",style_body))
    s.append(Image(charts['endowment'],width=400,height=200)); s.append(Paragraph("Endowment Growth - Surplus-Funded from Year 1",style_caption))
    s.append(Paragraph("THE SELF-SUSTAINING ENGINE",style_h1)); s.append(Paragraph("100,000 students at $3,000/year generates $300M. OPEX at 12.4% leaves $262M surplus. The surplus self-funds $40M/year scholarships, builds endowment at $60M/year, seeds every new College.",style_body))
    s.append(make_stat_block([('100,000','Students'),('$300M','Revenue'),('12.4%','OPEX'),('$262M','Surplus')]))
    s.append(Paragraph("A PERMANENT INSTITUTION",style_h1)); s.append(Paragraph("Three legal entities across three jurisdictions. Delaware 501(c)(3), UK CIO with Gift Aid, Swiss Fondation for endowment. No single controller. Annual Big Four audit. Complete transparency is structural.",style_body))
    s.append(Paragraph("THE INVITATION",style_h1)); s.append(Paragraph("This is the founding moment. Every great institution had a founding cohort who said yes before the buildings were built. They are the ones whose names are remembered.",style_body))
    s.append(Paragraph("donate@artemisui.org",ParagraphStyle('CC',parent=style_body,textColor=HexColor(CRIMSON),fontSize=12,alignment=TA_CENTER)))
    doc.build(s,onFirstPage=add_cover,onLaterPages=add_page_number); print(f"  Created: {p}")

# 4. FINANCIAL MODEL
def gen_financial_model():
    p=os.path.join(OUT_DIR,'artemis-financial-model.pdf')
    doc=SimpleDocTemplate(p,pagesize=A4,leftMargin=40,rightMargin=40,topMargin=50,bottomMargin=50)
    s=[]; s.append(Spacer(1,80)); s.append(Paragraph("FINANCIAL MODEL BREAKDOWN",style_title)); s.append(CrimsonLine()); s.append(Paragraph("Pro-Forma Financial Projections",style_subtitle)); s.append(PageBreak())
    s.append(Paragraph("CAMPAIGN ALLOCATION",style_h1)); s.append(Image(charts['allocation'],width=380,height=250)); s.append(Paragraph("$100M Campaign Allocation by Pillar",style_caption))
    s.append(std_table([['Category','Amount','%','Description'],['Property Acquisition','$78.95M','79%','50 Colleges, 35 countries'],['Faculty Pre-Launch','$6.9M','7%','2,000 faculty, 3 months'],['Hub Pre-Opening','$2.0M','2%','Operational costs'],['Legal Incorporation','$2.0M','2%','25 jurisdictions'],['Scholarship Seed','$5.0M','5%','10,000 students'],['Centers & Projects','$3.0M','3%','19 Centers, 42 Projects'],['Endowment Seed','$2.0M','2%','First perpetual deposit'],['IT + Furniture','$2.25M','2%','Digital backbone'],['TOTAL','$100M','100%','']],widths=[130,55,25,230]))
    s.append(Paragraph("5-YEAR REVENUE PROJECTION",style_h1)); s.append(Image(charts['revenue'],width=420,height=245)); s.append(Paragraph("Tuition Revenue and Annual Surplus",style_caption))
    s.append(Paragraph("ENDOWMENT GROWTH",style_h1)); s.append(Image(charts['endowment'],width=400,height=200)); s.append(Paragraph("Endowment Growth - Surplus-Funded",style_caption))
    s.append(Paragraph("KEY ASSUMPTIONS",style_h1)); s.append(Paragraph("Tuition: $3,000/yr. OPEX: 12.4%. Endowment yield: 4.5%. Student growth: 20% YoY. Scholarship rate: 10% Year 1, surplus-funded thereafter.",style_body))
    doc.build(s,onFirstPage=add_cover,onLaterPages=add_page_number); print(f"  Created: {p}")

# 5. TAX GUIDE
def gen_tax_guide():
    p=os.path.join(OUT_DIR,'artemis-tax-guide.pdf')
    doc=SimpleDocTemplate(p,pagesize=A4,leftMargin=40,rightMargin=40,topMargin=50,bottomMargin=50)
    s=[]; s.append(Spacer(1,80)); s.append(Paragraph("TAX DEDUCTIBILITY GUIDE",style_title)); s.append(CrimsonLine()); s.append(Paragraph("Jurisdiction-by-Jurisdiction Tax Benefits",style_subtitle)); s.append(PageBreak())
    s.append(Paragraph("UNITED STATES",style_h1)); s.append(Paragraph("Delaware Non-Stock Corporation, 501(c)(3). All donations tax-deductible. Cash: up to 60% AGI. Securities: up to 30% AGI. Retroactive deductibility within 27 months.",style_body))
    s.append(Paragraph("UNITED KINGDOM",style_h1)); s.append(Paragraph("Charitable Incorporated Organisation (CIO). Gift Aid adds 25% through HMRC. Higher-rate taxpayers claim additional 20% relief. A GBP 1M donation becomes GBP 1.25M.",style_body))
    s.append(Paragraph("SWITZERLAND",style_h1)); s.append(Paragraph("Fondation under Swiss Civil Code (Geneva Canton). Deductible from federal and cantonal income tax, typically up to 20% of net income. No capital gains tax on endowment growth.",style_body))
    s.append(Paragraph("EUROPEAN UNION",style_h1)); s.append(Paragraph("Under EU Non-Discrimination Treaty and bilateral tax treaties, EU residents may claim relief for donations to recognized charities in other member states. UK CIO facilitates across all 27 EU states.",style_body))
    s.append(Paragraph("REST OF WORLD",style_h1)); s.append(Paragraph("Fiscal sponsors: Rockefeller Philanthropy Advisors, NGOsource, Global Impact. NGOsource provides equivalency determinations for US foundations.",style_body))
    s.append(Paragraph("DISCLAIMER",style_h2)); s.append(Paragraph("This guide is for informational purposes only and does not constitute tax advice. Consult your own qualified tax advisor.",style_body_small))
    doc.build(s,onFirstPage=add_cover,onLaterPages=add_page_number); print(f"  Created: {p}")

# 6. LEGAL ENTITIES
def gen_legal_entities():
    p=os.path.join(OUT_DIR,'artemis-legal-entities.pdf')
    doc=SimpleDocTemplate(p,pagesize=A4,leftMargin=40,rightMargin=40,topMargin=50,bottomMargin=50)
    s=[]; s.append(Spacer(1,80)); s.append(Paragraph("LEGAL ENTITY OVERVIEW",style_title)); s.append(CrimsonLine()); s.append(Paragraph("Corporate Structure and Governance",style_subtitle)); s.append(PageBreak())
    for tier,name,cls,benefit,structs in [
        ("PRIMARY: UNITED STATES","Delaware Non-Stock Corporation","501(c)(3)","Tax-deductible donations in the $499B US philanthropy market.",
         ["Non-stock corporation - no shareholders","IRS Form 1023 filed","Retroactive deductibility 27 months","3+ independent board members required"]),
        ("SECONDARY: ENGLAND & WALES","Charitable Incorporated Organisation","Charity Commission","Gift Aid: GBP 1M becomes GBP 1.25M via HMRC top-up.",
         ["CIO or Company Limited by Guarantee","3+ trustees, UK registered office","Gift Aid - 25% government supplement","Commonwealth recognition"]),
        ("TERTIARY: SWITZERLAND","Fondation under Swiss Civil Code","International Foundation - Geneva","Endowment management in neutral jurisdiction. Home to WHO, CERN, IOC.",
         ["Minimum CHF 50,000 capital","Cantonal authority approval","No capital gains tax on endowment","Swiss foundation supervision"])]:
        s.append(Paragraph(tier,style_h1)); s.append(Paragraph(f"<b>{name}</b>",style_body)); s.append(Paragraph(f"Classification: {cls}",style_body_small)); s.append(Paragraph(f"Key Benefit: {benefit}",style_body))
        for st in structs: s.append(Paragraph(f"  - {st}",style_bullet))
    s.append(Paragraph("FISCAL SPONSORS",style_h1)); s.append(Paragraph("Rockefeller Philanthropy Advisors, NGOsource, and Global Impact facilitate tax-effective giving where direct deductibility is not yet available.",style_body))
    doc.build(s,onFirstPage=add_cover,onLaterPages=add_page_number); print(f"  Created: {p}")

# 7. NAMING BOOKLET
def gen_naming_booklet():
    p=os.path.join(OUT_DIR,'artemis-naming-booklet.pdf')
    doc=SimpleDocTemplate(p,pagesize=A4,leftMargin=40,rightMargin=40,topMargin=50,bottomMargin=50)
    s=[]; s.append(Spacer(1,80)); s.append(Paragraph("NAMING OPPORTUNITIES BOOKLET",style_title)); s.append(CrimsonLine()); s.append(Paragraph("A Complete Catalogue of Named Gift Opportunities",style_subtitle)); s.append(PageBreak())
    for title,desc in [("CENTRAL NODE - $25M","Name one of three Central Nodes - Venice, San Francisco, or Singapore. ~5,000 students. The apex of the Artemis network, bearing your name in perpetuity. Includes naming rights, permanent plaque, annual naming lecture, founding document inclusion."),
        ("TIER A COLLEGE - $10M","Name a flagship College in the world's great knowledge capitals. ~2,500 students. Building naming, recognition at all events, annual naming dinner."),
        ("CENTER OF INQUIRY - $10M","Name one of 19 Centers of Inquiry - permanently endowed, independently operating. Center directorship naming, annual research report, advisory board invitation."),
        ("TIER B COLLEGE - $5M","Name a College in major global cities. ~2,000 students. Permanent physical presence, building naming, recognition plaque."),
        ("DISTINGUISHED PROFESSORSHIP - $5M","At 4.5% yield, generates $225K/year in perpetuity. Annual named lecture, faculty recognition event."),
        ("DEGREE PROGRAM - $3M","Name one of 55 degree programs. Your name associated with a discipline and every graduate. Program page naming, annual graduate reception."),
        ("TIER C COLLEGE - $2M","Name a College in cities like Kigali, Dhaka, Kampala, Karachi. ~1,100 students. Building naming."),
        ("SCHOLARSHIP FUND - $12,000","Fund one student's full scholarship for 4 years. Named scholarship certificate, annual impact report from the scholar.")]:
        s.append(Paragraph(title,style_h1)); s.append(Paragraph(desc,style_body)); s.append(CrimsonLine(width=200))
    doc.build(s,onFirstPage=add_cover,onLaterPages=add_page_number); print(f"  Created: {p}")

# 8. GIVING CIRCLES
def gen_giving_circles():
    p=os.path.join(OUT_DIR,'artemis-giving-circles.pdf')
    doc=SimpleDocTemplate(p,pagesize=A4,leftMargin=40,rightMargin=40,topMargin=50,bottomMargin=50)
    s=[]; s.append(Spacer(1,80)); s.append(Paragraph("GIVING CIRCLES BENEFITS GUIDE",style_title)); s.append(CrimsonLine()); s.append(Paragraph("Recognition, Benefits, and Impact at Every Level",style_subtitle)); s.append(PageBreak())
    for title,color,benefits in [
        ("FOUNDERS' CIRCLE - $10M+",'#8A0000',["Name engraved on founding document at Venice Central Node","Permanent seat on Board of Visitors","Private annual dinner with President","Named endowment fund or naming opportunity","Recognition plaque at all 50 Colleges","Biographical feature in annual report"]),
        ("GUARDIANS' CIRCLE - $5M-$9.9M",'#6B0000',["Named College or Center of Inquiry","Recognition plaque at all 50 Colleges","Annual Guardian's Lecture named by you","Annual private briefing with President","Named endowment fund"]),
        ("BUILDERS' CIRCLE - $1M-$4.9M",'#4338CA',["Named Professorship, Scholarship, or program","Recognition plaque at all 50 Colleges","Annual Builder's Report on your named gift","Invitation to annual gathering","Feature in campaign newsletter"]),
        ("FELLOWS' CIRCLE - $100K-$999K",'#0E7490',["Named scholarship fund or tutorial room","Recognition at chosen College","Annual Fellow's Newsletter","Invitation to regional events"]),
        ("FRIENDS OF ARTEMIS - $10K-$99K",'#15803D',["Name in founding Donor Roll","Digital certificate of founding support","Quarterly progress updates","Invitation to online events"]),
        ("THE 99 - $99+",'#6B7280',["Waitlist priority for enrollment","Digital recognition on community wall","Monthly community updates","The knowledge that you were first in line"])]:
        s.append(ColorBar(500,3,color)); s.append(Paragraph(title,ParagraphStyle('CT2',parent=style_h1,textColor=HexColor(color))))
        for b in benefits: s.append(Paragraph(f"  - {b}",style_bullet))
        s.append(Spacer(1,8))
    doc.build(s,onFirstPage=add_cover,onLaterPages=add_page_number); print(f"  Created: {p}")

# 9. CAMPUS MASTER PLAN
def gen_campus_master_plan():
    p=os.path.join(OUT_DIR,'artemis-campus-master-plan.pdf')
    doc=SimpleDocTemplate(p,pagesize=A4,leftMargin=40,rightMargin=40,topMargin=50,bottomMargin=50)
    s=[]; s.append(Spacer(1,80)); s.append(Paragraph("CAMPUS MASTER PLAN",style_title)); s.append(CrimsonLine()); s.append(Paragraph("50 Colleges. 3 Central Nodes. 6 Continents.",style_subtitle)); s.append(PageBreak())
    s.append(Paragraph("THE CENTRAL NODES",style_h1))
    for t,d in [("VENICE CENTRAL NODE","The European anchor. Intersection of Western intellectual tradition and Mediterranean connectivity. Repurposed historic complex near the Grand Canal, ~5,000 students."),
        ("SAN FRANCISCO CENTRAL NODE","The Americas anchor. Center of technological innovation and venture capital. Repurposed industrial complex in SoMa district, ~5,000 students."),
        ("SINGAPORE CENTRAL NODE","The Asia-Pacific anchor. Bridge between East and West. Purpose-adapted complex in One North innovation district, ~5,000 students.")]:
        s.append(Paragraph(t,style_h2)); s.append(Paragraph(d,style_body))
    s.append(Paragraph("THE COLLEGIUM NETWORK",style_h1)); s.append(Paragraph("Seven additional Colleges across major knowledge capitals. Each is a self-contained academic community using adaptive reuse of existing buildings.",style_body))
    s.append(std_table([['City','Continent','Type','Capacity'],['Venice','Europe','Central Node','5,000'],['San Francisco','N. America','Central Node','5,000'],['Singapore','Asia','Central Node','5,000'],['Berlin','Europe','Tier A','2,500'],['Nairobi','Africa','Tier A','2,500'],['Sao Paulo','S. America','Tier A','2,500'],['Vancouver','N. America','Tier B','2,000'],['London','Europe','Tier A','2,500'],['Mumbai','Asia','Tier B','2,000'],['Kigali','Africa','Tier C','1,100']],widths=[90,80,80,60]))
    s.append(Paragraph("DESIGN PRINCIPLES",style_h1))
    for pr in ["Adaptive Reuse: Existing buildings repurposed, not demolished.","Residential Community: Living, dining, social, study spaces in every College.","Digital-First: High-bandwidth, AI-assisted tutorial systems, cross-campus collaboration.","Sustainability: LEED Gold target, solar arrays, rainwater harvesting, passive cooling."]:
        s.append(Paragraph(f"  - {pr}",style_bullet))
    doc.build(s,onFirstPage=add_cover,onLaterPages=add_page_number); print(f"  Created: {p}")

# 10. COLLEGIUM MAP
def gen_collegium_map():
    p=os.path.join(OUT_DIR,'artemis-collegium-map.pdf')
    doc=SimpleDocTemplate(p,pagesize=A4,leftMargin=40,rightMargin=40,topMargin=50,bottomMargin=50)
    s=[]; s.append(Spacer(1,60)); s.append(Paragraph("COLLEGIUM ALLIANCE MAP",style_title)); s.append(CrimsonLine()); s.append(Paragraph("10 Colleges | 6 Continents | 35 Countries",style_subtitle)); s.append(Spacer(1,20))
    s.append(Image(charts['world_map'],width=480,height=240)); s.append(Paragraph("The Artemis Collegium - Global College Network",style_caption))
    s.append(Paragraph("NETWORK STATISTICS",style_h1)); s.append(make_stat_block([('10','Colleges'),('3','Central Nodes'),('6','Continents'),('35','Countries'),('100K','Students')]))
    doc.build(s,onFirstPage=add_page_number,onLaterPages=add_page_number); print(f"  Created: {p}")

# 11. ACADEMIC PROSPECTUS
def gen_academic_prospectus():
    p=os.path.join(OUT_DIR,'artemis-academic-prospectus.pdf')
    doc=SimpleDocTemplate(p,pagesize=A4,leftMargin=40,rightMargin=40,topMargin=50,bottomMargin=50)
    s=[]; s.append(Spacer(1,80)); s.append(Paragraph("ACADEMIC PROSPECTUS",style_title)); s.append(CrimsonLine()); s.append(Paragraph("Programs, Curriculum, and the Artemis Approach",style_subtitle)); s.append(PageBreak())
    s.append(Paragraph("THE FOUR PILLARS",style_h1)); s.append(Paragraph("Every student masters four foundational pillars:",style_body))
    for t,d in [("Epistemology","How we know what we know. Knowledge creation, validation, revision. Distinguish knowledge from belief, evidence from assertion."),
        ("Computational Thinking","How to reason with and about algorithms. Not just programming but logical frameworks underpinning all digital systems, data science, and AI."),
        ("Global Systems","How interconnected systems shape the world. Economics, geopolitics, climate, public health as interacting complex systems."),
        ("Creative Expression","How to communicate vision and insight. Writing, visual design, data storytelling, public reasoning.")]:
        s.append(Paragraph(f"<b>{t}:</b> {d}",style_body))
    s.append(Paragraph("PURPOSE LEARNING",style_h1)); s.append(Paragraph("Students declare a Mission, not a major. A Mission is a real-world problem the student intends to solve. This transforms education from passive acquisition to active, purpose-driven inquiry.",style_body))
    s.append(Paragraph("PROGRAMS OF STUDY",style_h1))
    s.append(std_table([['Program','Level','Focus'],['African Studies','UG','Arts, history, cultures, politics of Africa'],['Computational Sciences','UG','Algorithms, AI, data science, quantum'],['Cognitive Science','UG','Consciousness, neuroscience, AI'],['Economics & Development','UG','Global systems, financial inclusion'],['Environmental Systems','UG','Climate adaptation, regenerative design'],['Comparative Literature','UG','Cross-cultural narrative, digital media'],['Philosophy & Ethics','Grad','AI ethics, governance, traditions'],['Urban Design','Grad','Sustainable cities, adaptive reuse'],['International Law','Grad','Refugee law, global governance'],['Neuroscience','Grad','Neural correlates, neurodiversity'],['Quantum Computing','Grad','Quantum algorithms, error correction'],['Public Health','Grad','Community health, traditional + modern']],widths=[130,35,275]))
    s.append(Paragraph("COMPETENCY-BASED GRADING",style_h1)); s.append(Paragraph("No letter grades, no class rankings. Students build a portfolio of demonstrated competencies. Adaptive Paced Learning adapts to each student's rhythm.",style_body))
    s.append(Paragraph("FACULTY",style_h1)); s.append(Paragraph("2,000 faculty across all disciplines, selected for academic distinction and mission alignment. Apply: faculty@artemisui.org",style_body))
    doc.build(s,onFirstPage=add_cover,onLaterPages=add_page_number); print(f"  Created: {p}")

# 12. RESEARCH PORTFOLIO
def gen_research_portfolio():
    p=os.path.join(OUT_DIR,'artemis-research-portfolio.pdf')
    doc=SimpleDocTemplate(p,pagesize=A4,leftMargin=40,rightMargin=40,topMargin=50,bottomMargin=50)
    s=[]; s.append(Spacer(1,80)); s.append(Paragraph("CENTERS OF INQUIRY",style_title)); s.append(CrimsonLine()); s.append(Paragraph("Research Portfolio: 19 Centers, 42 Active Projects",style_subtitle)); s.append(PageBreak())
    for title,director,desc in [("CENTER FOR SYNTHETIC INTELLIGENCE","Director: Dr. Kai Mueller (Berlin)","AI/human symbiotic reasoning, CoThink project, moral agency in AI, neuromorphic computing. Flagship: CoThink, real-time AI-human collaborative reasoning platform."),
        ("CENTER FOR BIO-REGENERATIVE ARTS","Director: Dr. Amara Osei (Nairobi)","Self-healing materials (BioCrete-2), living architecture, mycelium structures, bioremediation. Flagship: BioCrete-2, self-repairing concrete that sequesters carbon."),
        ("CENTER FOR COSMOLOGICAL HUMANITIES","Director: Prof. Elena Petrov (Venice)","Petabytes of telescope data, philosophical astrophysics, cosmology and human meaning. Flagship: Artemis Deep Field, JWST data for philosophical analysis."),
        ("CENTER FOR URBAN FUTURES","Director: Prof. Carlos Mendoza (Sao Paulo)","Climate adaptation, city planning, ClimatIQ, sustainable megacity infrastructure. Flagship: ClimatIQ, climate analytics for municipal decision-making.")]:
        s.append(Paragraph(title,style_h1)); s.append(Paragraph(director,style_body_small)); s.append(Paragraph(desc,style_body))
    s.append(Paragraph("ALL 19 CENTERS",style_h1))
    for c in ["Center for Synthetic Intelligence","Center for Bio-Regenerative Arts","Center for Cosmological Humanities","Center for Urban Futures","Center for Global Health Equity","Center for Quantum Information","Center for African Knowledge Systems","Center for Pacific Rim Studies","Center for Digital Humanities","Center for Regenerative Economics","Center for Consciousness Studies","Center for Comparative Governance","Center for Arctic and Climate Systems","Center for South Asian Philosophy","Center for Educational Innovation","Center for Migration and Belonging","Center for Music and Acoustic Research","Center for Food Systems","Center for Visual and Spatial Reasoning"]:
        s.append(Paragraph(f"  - {c}",style_bullet))
    s.append(Spacer(1,12)); s.append(Image(charts['students'],width=380,height=190)); s.append(Paragraph("Projected Student and Research Growth",style_caption))
    doc.build(s,onFirstPage=add_cover,onLaterPages=add_page_number); print(f"  Created: {p}")

# 13. STRATEGIC PLAN
def gen_strategic_plan():
    p=os.path.join(OUT_DIR,'artemis-strategic-plan.pdf')
    doc=SimpleDocTemplate(p,pagesize=A4,leftMargin=40,rightMargin=40,topMargin=50,bottomMargin=50)
    s=[]; s.append(Spacer(1,80)); s.append(Paragraph("STRATEGIC PLAN 2025-2030",style_title)); s.append(CrimsonLine()); s.append(Paragraph("The Five-Year Roadmap",style_subtitle)); s.append(PageBreak())
    s.append(Paragraph("YEAR 1: FOUNDATION",style_h1)); s.append(Paragraph("Secure $100M campaign, acquire 10 Colleges, hire 2,000 faculty. Operational with 100,000 students, generating $300M revenue and $262M surplus.",style_body))
    s.append(make_stat_block([('$100M','Campaign'),('10','Colleges'),('2,000','Faculty'),('100K','Students')]))
    s.append(Paragraph("YEAR 2: EXPANSION",style_h1)); s.append(Paragraph("20 Colleges, 120,000 students. Launch 42 Active Projects across 19 Centers. Endowment reaches $63M. First Forge venture spinouts.",style_body))
    s.append(Paragraph("YEAR 3: DEEPENING",style_h1)); s.append(Paragraph("30 Colleges, 145,000 students. First full graduate cohort. Endowment crosses $126M. Five+ university partnerships formalized.",style_body))
    s.append(Paragraph("YEAR 4: MATURATION",style_h1)); s.append(Paragraph("40 Colleges, 175,000 students. Measurable global research impact. 10+ Forge ventures. Endowment reaches $192M.",style_body))
    s.append(Paragraph("YEAR 5: PERMANENCE",style_h1)); s.append(Paragraph("50 Colleges, 210,000 students, 35 countries. Endowment at $262M, generating $11.8M perpetual annual yield. Fully self-sustaining.",style_body))
    s.append(Image(charts['endowment'],width=380,height=190)); s.append(Paragraph("Endowment Growth Trajectory",style_caption))
    s.append(Image(charts['students'],width=380,height=190)); s.append(Paragraph("Student Enrollment Growth",style_caption))
    s.append(Paragraph("STRATEGIC PRIORITIES",style_h1))
    for pr in ["Academic Excellence: Recruit mission-driven faculty, build competency-based assessment, launch 19 Centers.","Financial Sustainability: Self-sustaining by Year 1 end. Endowment to $262M by Year 5.","Global Access: $3,000/yr tuition, surplus-funded scholarships for 10% of students.","Institutional Permanence: Governance that outlasts founders. Annual audits. Complete transparency.","Innovation Pipeline: The Forge incubator, venture spinouts, 5% equity to endowment."]:
        s.append(Paragraph(f"  - {pr}",style_bullet))
    doc.build(s,onFirstPage=add_cover,onLaterPages=add_page_number); print(f"  Created: {p}")

if __name__ == '__main__':
    print("="*60); print("GENERATING ARTEMIS RESOURCE PDFs"); print("="*60)
    gen_founding_prospectus(); gen_campaign_overview(); gen_case_for_support(); gen_financial_model()
    gen_tax_guide(); gen_legal_entities(); gen_naming_booklet(); gen_giving_circles()
    gen_campus_master_plan(); gen_collegium_map(); gen_academic_prospectus(); gen_research_portfolio()
    gen_strategic_plan()
    print("\nALL 13 PDFs GENERATED SUCCESSFULLY")
