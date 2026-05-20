#!/usr/bin/env python3
"""Generate PDFs 2-13: Campaign Overview, Case for Support, Financial Model, Tax Guide, Legal Entities, Naming Booklet, Giving Circles, Campus Plan, Alliance Map, Academic Prospectus, Research Portfolio, Strategic Plan."""
import sys, os
sys.path.insert(0, '/home/z/my-project/scripts/pdf-assets')
from pdf_utils import *
from reportlab.platypus import Paragraph, Spacer, Image as RLImage, Table, TableStyle, PageBreak, NextPageTemplate, KeepTogether
from reportlab.lib.units import mm

OUT = OUT_DIR
W = PAGE_W - 2*MARGIN

# ══════════════════════════════════════════════════════════════════
# 2. CAMPAIGN OVERVIEW (1 page - concise one-pager)
# ══════════════════════════════════════════════════════════════════
def gen_campaign_overview():
    doc = ArtemisDoc(
        os.path.join(OUT, 'artemis-campaign-overview.pdf'),
        cover_title='CAMPAIGN\nOVERVIEW',
        cover_subtitle='$100M Founding Campaign  |  One Page',
        cover_img='hero-university.jpg',
        cover_tagline='FOR CIVILIZATION  |  12 MONTHS  |  50 COLLEGES',
        title_short='Campaign Overview'
    )
    story = []
    story.append(NextPageTemplate('content'))
    story.append(PageBreak())

    # Single page summary
    story.append(Paragraph('THE $100M FOUNDING CAMPAIGN', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(6))
    story.append(Paragraph(
        'The University of Artemis is a new kind of university: residential, tutorial-based, research-active, and globally distributed across 50 Colleges on 6 continents. Annual tuition of $3,000 makes it accessible to 90% of qualified students worldwide. The founding campaign of $100M seeds the permanent physical infrastructure that makes the model self-sustaining from Year 1.', STYLES['body']))

    # Key stats row
    stats = [
        [Paragraph('<b>$100M</b>', STYLES['stat_num']), Paragraph('<b>50</b>', STYLES['stat_num']),
         Paragraph('<b>100,000</b>', STYLES['stat_num']), Paragraph('<b>$3,000</b>', STYLES['stat_num'])],
        [Paragraph('Campaign Goal', STYLES['stat_label']), Paragraph('Colleges at Launch', STYLES['stat_label']),
         Paragraph('Students Year 1', STYLES['stat_label']), Paragraph('Annual Tuition', STYLES['stat_label'])]
    ]
    stat_t = Table(stats, colWidths=[W/4]*4)
    stat_t.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(stat_t)
    story.append(sp(8))

    # Campaign allocation chart
    story.append(chart_image('campaign_allocation_donut.png', height=200))
    story.append(sp(6))

    # Timeline
    story.append(Paragraph('TIMELINE', STYLES['h3']))
    timeline_data = [
        [Paragraph('<b>Phase</b>', STYLES['table_header']), Paragraph('<b>Months</b>', STYLES['table_header']),
         Paragraph('<b>Target</b>', STYLES['table_header']), Paragraph('<b>Key Milestone</b>', STYLES['table_header'])],
        [Paragraph('Quiet Phase', STYLES['table_cell']), Paragraph('1-3', STYLES['table_cell']),
         Paragraph('$50M', STYLES['table_cell']), Paragraph('Lead gifts secured', STYLES['table_cell'])],
        [Paragraph('Public Phase', STYLES['table_cell']), Paragraph('4-6', STYLES['table_cell']),
         Paragraph('$85M', STYLES['table_cell']), Paragraph('Global launch', STYLES['table_cell'])],
        [Paragraph('Close & Capitalise', STYLES['table_cell']), Paragraph('7-9', STYLES['table_cell']),
         Paragraph('$100M', STYLES['table_cell']), Paragraph('Properties acquired', STYLES['table_cell'])],
        [Paragraph('Build & Launch', STYLES['table_cell']), Paragraph('10-12', STYLES['table_cell']),
         Paragraph('$100M', STYLES['table_cell']), Paragraph('University is live', STYLES['table_cell'])],
    ]
    story.append(make_table(timeline_data, col_widths=[W*0.22, W*0.15, W*0.15, W*0.48]))
    story.append(sp(6))

    # How to give
    story.append(Paragraph('HOW TO GIVE', STYLES['h3']))
    story.append(Paragraph('Online (card/PayPal/crypto) | Bank/Wire Transfer | Securities | Planned Giving | Donor-Advised Funds | In-Kind | Employer Matching', STYLES['body_small']))
    story.append(sp(4))
    story.append(Paragraph('donate@artemisui.org  |  www.artemisui.org/give', STYLES['body_center']))
    doc.build(story)
    print(f"  Campaign Overview: {os.path.getsize(os.path.join(OUT, 'artemis-campaign-overview.pdf'))//1024}KB")


# ══════════════════════════════════════════════════════════════════
# 3. CASE FOR SUPPORT (8 pages)
# ══════════════════════════════════════════════════════════════════
def gen_case_for_support():
    doc = ArtemisDoc(
        os.path.join(OUT, 'artemis-case-for-support.pdf'),
        cover_title='CASE FOR\nSUPPORT',
        cover_subtitle='Why Artemis, Why Now, Why Your Gift Matters',
        cover_img='students-africa.jpg',
        cover_tagline='A SELF-SUSTAINING UNIVERSITY. A PERMANENT LEGACY.',
        title_short='Case for Support'
    )
    story = []
    story.append(NextPageTemplate('content'))
    story.append(PageBreak())

    # Page 2: The Crisis
    story.append(Paragraph('THE CASE FOR ARTEMIS', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(8))
    story.append(Paragraph(
        '"The world does not need another elite university that serves the few. It needs a great university that serves the many. The University of Artemis is that university."', STYLES['quote']))
    story.append(sp(8))
    story.append(Paragraph('THE CRISIS IN NUMBERS', STYLES['h2']))
    story.append(Paragraph(
        'Higher education faces a structural crisis that cannot be solved by incremental reform. Tuition costs have risen 4x faster than inflation since 1980, pricing out the majority of qualified students worldwide. In the United States alone, student debt exceeds $1.7 trillion — a figure larger than the GDP of most nations. Meanwhile, in Sub-Saharan Africa, only 9% of college-age individuals can access higher education. South Asia enrolls just 25%. The global higher education market, worth $2.5 trillion annually, serves fewer than 220 million students while over a billion young people will reach university age by 2030.', STYLES['body']))
    story.append(Paragraph(
        'This is not just an access problem. Employers in 40% of cases report that graduates lack the skills needed for the modern workforce. The disconnect between what universities teach and what the world needs grows wider each year. Traditional universities, burdened by legacy costs, governance structures designed for the 19th century, and business models dependent on ever-rising tuition, cannot adapt fast enough. The system is not broken at the margins — it is structurally incapable of serving the 90% of qualified students who cannot afford current price points.', STYLES['body']))
    story.append(hero_image('students-africa.jpg', height=130))
    story.append(Paragraph('Students in Sub-Saharan Africa, where only 9% of college-age people access higher education. Image: Unsplash', STYLES['caption']))
    story.append(PageBreak())

    # Page 3: Why Artemis
    story.append(Paragraph('WHY ARTEMIS', STYLES['h2']))
    story.append(sp(4))
    story.append(Paragraph(
        'The University of Artemis is designed from first principles to solve the structural crisis in higher education. It is not an online programme, a MOOC platform, or a discount university. It is a fully residential, tutorial-based, research-active university that costs $3,000 per year. The model achieves this through three structural innovations that eliminate 80% of the cost base of traditional universities while delivering superior educational outcomes.', STYLES['body']))

    story.append(Paragraph('Innovation 1: Repurposed Buildings, Not New Construction', STYLES['h3']))
    story.append(Paragraph(
        'Traditional universities spend billions on campus construction. Harvard\'s most recent capital campaign allocated $2.5B to facilities alone. Artemis acquires existing buildings — repurposed convents, warehouses, offices, factories — and converts them into Colleges. This eliminates approximately 80% of capital costs. A repurposed warehouse in Kigali costs a fraction of a purpose-built campus. The building is acquired, not leased, ensuring permanent ownership. Each College becomes a self-sustaining unit generating tuition revenue from Day 1.', STYLES['body']))

    story.append(Paragraph('Innovation 2: The Tutorial System at Scale', STYLES['h3']))
    story.append(Paragraph(
        'Oxford and Cambridge have proven the tutorial model for 800 years. Artemis scales it globally with a 1:7 faculty-to-student ratio. Tutorials are conducted synchronously across colleges, meaning a student in Kigali attends the same tutorial as a student in San Francisco. Faculty rotate across colleges, bringing diverse perspectives to every session. The tutorial model produces deeper learning than lectures: students must prepare, present, and defend their thinking in every session. There is no back row in a tutorial.', STYLES['body']))

    story.append(Paragraph('Innovation 3: The Global Rotation Model', STYLES['h3']))
    story.append(Paragraph(
        'Students rotate through 6 cities over 4 years, distributing fixed costs across 50 colleges in 35 countries. This geographic distribution eliminates the monopoly on quality education that single-campus universities create. It also produces graduates with genuine global fluency — not just theoretical knowledge of other cultures, but lived experience across continents. The rotation model means every College contributes to every student\'s education, creating a network effect that compounds the value of each additional College.', STYLES['body']))
    story.append(PageBreak())

    # Page 4: The Financial Logic
    story.append(Paragraph('THE FINANCIAL LOGIC', STYLES['h2']))
    story.append(sp(4))
    story.append(Paragraph(
        'The University of Artemis is designed to be self-sustaining from Year 1. This is not a prediction or a hope — it is a mathematical consequence of the model. At 100,000 students paying $3,000/year, Year 1 revenue is $300M. Operating costs are approximately $262M. The surplus of $38M in Year 1 funds scholarships, builds the endowment, and expands the college network. No ongoing fundraising is required. No government subsidies are needed. The financial engine is permanent.', STYLES['body']))
    story.append(sp(4))
    story.append(chart_image('revenue_projection_bar.png', height=180))
    story.append(Paragraph('5-year revenue projection: tuition revenue grows from $300M to $1.8B.', STYLES['caption']))
    story.append(sp(4))
    story.append(Paragraph(
        'By Year 5, with 300,000 students across 70 colleges, revenue reaches $1.88B with a surplus exceeding $500M. The endowment, seeded at $3M and grown by $60M+ per year from surplus, reaches $1.35B. The university becomes one of the best-endowed institutions in the world within a decade, without a single additional fundraising campaign. This is the power of the model: it converts a one-time seed investment into a permanent, growing, self-sustaining institution.', STYLES['body']))
    story.append(sp(4))
    story.append(chart_image('surplus_endowment_growth.png', height=170))
    story.append(Paragraph('Surplus and endowment growth trajectory showing self-sustaining financial engine.', STYLES['caption']))
    story.append(PageBreak())

    # Page 5: Why Now
    story.append(Paragraph('WHY NOW', STYLES['h2']))
    story.append(sp(4))
    story.append(hero_image('seminar-discussion.jpg', height=130))
    story.append(Paragraph('Discussion and collaboration are at the heart of the Artemis model. Image: Unsplash', STYLES['caption']))
    story.append(sp(4))
    story.append(Paragraph(
        'Three converging forces make this the right moment for the University of Artemis. First, the demand crisis: a billion young people will reach university age by 2030, and existing institutions cannot absorb them. Second, the technology: synchronous global education, once impossible, is now proven at scale. The pandemic accelerated the adoption of remote collaboration tools by a decade. Third, the philanthropic will: donors under 50 increasingly demand measurable, structural impact rather than incremental charity. They want to fund solutions, not symptoms.', STYLES['body']))
    story.append(Paragraph(
        'The founding of great universities has always been a response to crisis. The University of Bologna was founded in 1088 because students demanded legal education that the church could not provide. The University of Berlin was founded in 1810 because Prussia needed to rebuild after Napoleon. Stanford was founded in 1885 because Leland Stanford wanted to create "useful citizens" after the loss of his son. The University of Artemis is founded because a billion students need education that the existing system cannot provide at a price they can afford.', STYLES['body']))

    # Page 6: The Self-Sustaining Model
    story.append(sp(8))
    story.append(Paragraph('THE SELF-SUSTAINING MODEL', STYLES['h2']))
    story.append(sp(4))
    story.append(Paragraph(
        'The founding campaign of $100M is not an operating budget. It is seed capital that creates the permanent physical infrastructure from which the university generates its own revenue. The distinction is critical: most university fundraising campaigns fund operating expenses, building programmes, or financial aid endowments that supplement tuition revenue. The Artemis campaign funds the infrastructure that generates tuition revenue. After launch, no further fundraising is required for the university to operate, grow, and fulfil its mission.', STYLES['body']))
    story.append(sp(4))
    story.append(chart_image('opex_breakdown_stacked.png', height=170))
    story.append(Paragraph('Operating expenditure breakdown showing faculty compensation as the largest cost.', STYLES['caption']))
    story.append(sp(4))

    # Financial summary table
    fin_data = [
        [Paragraph('<b>Metric</b>', STYLES['table_header']), Paragraph('<b>Year 1</b>', STYLES['table_header']),
         Paragraph('<b>Year 3</b>', STYLES['table_header']), Paragraph('<b>Year 5</b>', STYLES['table_header'])],
        [Paragraph('Revenue', STYLES['table_cell']), Paragraph('$305M', STYLES['table_cell_right']),
         Paragraph('$1.02B', STYLES['table_cell_right']), Paragraph('$1.88B', STYLES['table_cell_right'])],
        [Paragraph('Operating Costs', STYLES['table_cell']), Paragraph('$267M', STYLES['table_cell_right']),
         Paragraph('$670M', STYLES['table_cell_right']), Paragraph('$1.14B', STYLES['table_cell_right'])],
        [Paragraph('Surplus', STYLES['table_cell']), Paragraph('$38M', STYLES['table_cell_right']),
         Paragraph('$350M', STYLES['table_cell_right']), Paragraph('$740M', STYLES['table_cell_right'])],
        [Paragraph('Endowment', STYLES['table_cell']), Paragraph('$63M', STYLES['table_cell_right']),
         Paragraph('$475M', STYLES['table_cell_right']), Paragraph('$1.35B', STYLES['table_cell_right'])],
        [Paragraph('Students', STYLES['table_cell']), Paragraph('100,000', STYLES['table_cell_right']),
         Paragraph('200,000', STYLES['table_cell_right']), Paragraph('300,000', STYLES['table_cell_right'])],
        [Paragraph('Colleges', STYLES['table_cell']), Paragraph('50', STYLES['table_cell_right']),
         Paragraph('60', STYLES['table_cell_right']), Paragraph('70', STYLES['table_cell_right'])],
    ]
    story.append(make_table(fin_data, col_widths=[W*0.3, W*0.23, W*0.23, W*0.24]))
    story.append(PageBreak())

    # Page 7: Why Your Gift Matters
    story.append(Paragraph('WHY YOUR GIFT MATTERS', STYLES['h2']))
    story.append(sp(4))
    story.append(hero_image('handshakes-deal.jpg', height=130))
    story.append(Paragraph('Partnership and trust are the foundation of every great institution. Image: Unsplash', STYLES['caption']))
    story.append(sp(4))
    story.append(Paragraph(
        'Your gift to the University of Artemis is not a donation to an operating budget that needs to be refilled every year. It is an investment in permanent infrastructure that generates its own revenue, funds its own scholarships, and builds its own endowment from Day 1. This is the difference between giving a man a fish and building a fishery. The founding campaign creates the fishery. Every dollar you give is multiplied by the financial engine into perpetual value.', STYLES['body']))
    story.append(Paragraph(
        'The naming opportunities are endowments, not sponsorships. When you name a College, the College owns the building, the building generates tuition revenue, and the revenue sustains the College in perpetuity. Your name is inseparable from that value. When you endow a Distinguished Professorship, the $5M at 4.5% yield generates $225K per year — enough to sustain one faculty position forever. The gift compounds: it funds the position, the position produces research, the research builds reputation, the reputation attracts students, the students generate revenue, the revenue funds more positions.', STYLES['body']))
    story.append(sp(4))
    story.append(chart_image('scholarship_impact.png', height=170))
    story.append(Paragraph('Scholarship impact: self-sustaining from Year 1, growing every year thereafter.', STYLES['caption']))
    story.append(PageBreak())

    # Page 8: Closing
    story.append(Paragraph('THE ASK', STYLES['h2']))
    story.append(sp(4))
    story.append(Paragraph(
        'We are asking for $100M in 12 months to seed a self-sustaining university that will serve 100,000 students in its first year, grow to 300,000 within five years, and generate over $1.8B in annual revenue by Year 5. The $100M is not a cost — it is the purchase price of permanent infrastructure that will educate millions of students over the coming centuries. Your gift creates the foundation. The financial engine does the rest.', STYLES['body']))
    story.append(sp(4))
    story.append(Paragraph(
        '70% of the campaign will come from 10 lead donors. This is how founding campaigns work. We are seeking partners, not patrons — individuals and institutions who see the structural opportunity and want to be part of the founding of a university that changes the trajectory of human education. The Founders\' Circle, at $10M+, carries the highest naming opportunities and the deepest institutional connection. But every gift matters: a $12,000 scholarship fund changes a student\'s life permanently.', STYLES['body']))
    story.append(sp(4))
    story.append(chart_image('donor_segments_pie.png', height=180))
    story.append(sp(6))
    story.append(Paragraph('donate@artemisui.org  |  www.artemisui.org/give', STYLES['body_center']))
    story.append(Paragraph('"For Civilization."', STYLES['quote']))
    doc.build(story)
    print(f"  Case for Support: {os.path.getsize(os.path.join(OUT, 'artemis-case-for-support.pdf'))//1024}KB")


# ══════════════════════════════════════════════════════════════════
# 4. FINANCIAL MODEL BREAKDOWN (6 pages)
# ══════════════════════════════════════════════════════════════════
def gen_financial_model():
    doc = ArtemisDoc(
        os.path.join(OUT, 'artemis-financial-model.pdf'),
        cover_title='FINANCIAL\nMODEL',
        cover_subtitle='Pro-Forma Analysis & Revenue Projections',
        cover_img='data-charts.jpg',
        cover_tagline='SELF-SUSTAINING FROM YEAR 1  |  $1.88B REVENUE BY YEAR 5',
        title_short='Financial Model'
    )
    story = []
    story.append(NextPageTemplate('content'))
    story.append(PageBreak())

    # Page 2: Revenue Model
    story.append(Paragraph('REVENUE MODEL', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(6))
    story.append(Paragraph(
        'The University of Artemis generates revenue primarily from tuition. At $3,000/year per student and 100,000 students in Year 1, tuition revenue is $300M. This is supplemented by ancillary revenue from housing, dining, conference facilities, and the Artemis Press (academic publishing). The model is deliberately simple: high volume, low price, with the surplus reinvested into scholarships, endowment growth, and network expansion. The financial engine is transparent, predictable, and self-reinforcing.', STYLES['body']))
    story.append(sp(4))
    story.append(chart_image('revenue_projection_bar.png', height=190))
    story.append(Paragraph('5-year revenue projection: tuition and other revenue streams.', STYLES['caption']))
    story.append(sp(6))

    rev_data = [
        [Paragraph('<b>Revenue Stream</b>', STYLES['table_header']), Paragraph('<b>Year 1</b>', STYLES['table_header']),
         Paragraph('<b>Year 2</b>', STYLES['table_header']), Paragraph('<b>Year 3</b>', STYLES['table_header']),
         Paragraph('<b>Year 4</b>', STYLES['table_header']), Paragraph('<b>Year 5</b>', STYLES['table_header'])],
        [Paragraph('Tuition', STYLES['table_cell']), Paragraph('$300M', STYLES['table_cell_right']),
         Paragraph('$630M', STYLES['table_cell_right']), Paragraph('$990M', STYLES['table_cell_right']),
         Paragraph('$1,350M', STYLES['table_cell_right']), Paragraph('$1,800M', STYLES['table_cell_right'])],
        [Paragraph('Housing & Dining', STYLES['table_cell']), Paragraph('$3M', STYLES['table_cell_right']),
         Paragraph('$10M', STYLES['table_cell_right']), Paragraph('$22M', STYLES['table_cell_right']),
         Paragraph('$38M', STYLES['table_cell_right']), Paragraph('$60M', STYLES['table_cell_right'])],
        [Paragraph('Research Grants', STYLES['table_cell']), Paragraph('$1M', STYLES['table_cell_right']),
         Paragraph('$3M', STYLES['table_cell_right']), Paragraph('$5M', STYLES['table_cell_right']),
         Paragraph('$8M', STYLES['table_cell_right']), Paragraph('$12M', STYLES['table_cell_right'])],
        [Paragraph('Other', STYLES['table_cell']), Paragraph('$1M', STYLES['table_cell_right']),
         Paragraph('$2M', STYLES['table_cell_right']), Paragraph('$3M', STYLES['table_cell_right']),
         Paragraph('$4M', STYLES['table_cell_right']), Paragraph('$8M', STYLES['table_cell_right'])],
        [Paragraph('<b>Total Revenue</b>', STYLES['table_cell']), Paragraph('<b>$305M</b>', STYLES['table_cell_right']),
         Paragraph('<b>$645M</b>', STYLES['table_cell_right']), Paragraph('<b>$1,020M</b>', STYLES['table_cell_right']),
         Paragraph('<b>$1,400M</b>', STYLES['table_cell_right']), Paragraph('<b>$1,880M</b>', STYLES['table_cell_right'])],
    ]
    cw = [W*0.22, W*0.156, W*0.156, W*0.156, W*0.156, W*0.156]
    story.append(make_table(rev_data, col_widths=cw))
    story.append(PageBreak())

    # Page 3: Operating Costs
    story.append(Paragraph('OPERATING COST STRUCTURE', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(6))
    story.append(Paragraph(
        'Operating costs are dominated by faculty compensation, which represents approximately 65% of total expenditure. This is by design: the tutorial model requires a 1:7 faculty-to-student ratio, and faculty quality is the single most important determinant of educational outcomes. Operations (facilities, IT, administration) consume approximately 20%, scholarships 10%, and other costs (research support, student services) approximately 5%. The cost structure is lean because the model eliminates the three largest cost drivers of traditional universities: new construction, administrative bloat, and research cross-subsidies.', STYLES['body']))
    story.append(sp(4))
    story.append(chart_image('opex_breakdown_stacked.png', height=190))
    story.append(Paragraph('Operating expenditure breakdown by category over 5 years.', STYLES['caption']))
    story.append(sp(6))

    cost_data = [
        [Paragraph('<b>Cost Category</b>', STYLES['table_header']), Paragraph('<b>Year 1</b>', STYLES['table_header']),
         Paragraph('<b>Year 2</b>', STYLES['table_header']), Paragraph('<b>Year 3</b>', STYLES['table_header']),
         Paragraph('<b>Year 4</b>', STYLES['table_header']), Paragraph('<b>Year 5</b>', STYLES['table_header'])],
        [Paragraph('Faculty Compensation', STYLES['table_cell']), Paragraph('$180M', STYLES['table_cell_right']),
         Paragraph('$270M', STYLES['table_cell_right']), Paragraph('$360M', STYLES['table_cell_right']),
         Paragraph('$450M', STYLES['table_cell_right']), Paragraph('$540M', STYLES['table_cell_right'])],
        [Paragraph('Operations', STYLES['table_cell']), Paragraph('$60M', STYLES['table_cell_right']),
         Paragraph('$90M', STYLES['table_cell_right']), Paragraph('$120M', STYLES['table_cell_right']),
         Paragraph('$150M', STYLES['table_cell_right']), Paragraph('$180M', STYLES['table_cell_right'])],
        [Paragraph('Scholarships', STYLES['table_cell']), Paragraph('$40M', STYLES['table_cell_right']),
         Paragraph('$100M', STYLES['table_cell_right']), Paragraph('$150M', STYLES['table_cell_right']),
         Paragraph('$200M', STYLES['table_cell_right']), Paragraph('$260M', STYLES['table_cell_right'])],
        [Paragraph('Other', STYLES['table_cell']), Paragraph('$20M', STYLES['table_cell_right']),
         Paragraph('$30M', STYLES['table_cell_right']), Paragraph('$40M', STYLES['table_cell_right']),
         Paragraph('$50M', STYLES['table_cell_right']), Paragraph('$60M', STYLES['table_cell_right'])],
        [Paragraph('<b>Total Costs</b>', STYLES['table_cell']), Paragraph('<b>$300M</b>', STYLES['table_cell_right']),
         Paragraph('<b>$490M</b>', STYLES['table_cell_right']), Paragraph('<b>$670M</b>', STYLES['table_cell_right']),
         Paragraph('<b>$850M</b>', STYLES['table_cell_right']), Paragraph('<b>$1,040M</b>', STYLES['table_cell_right'])],
    ]
    story.append(make_table(cost_data, col_widths=cw))
    story.append(PageBreak())

    # Page 4: Surplus & Endowment
    story.append(Paragraph('SURPLUS & ENDOWMENT TRAJECTORY', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(6))
    story.append(Paragraph(
        'The surplus generated each year is allocated across three priorities: scholarship expansion (ensuring access for all qualified students), endowment growth (ensuring institutional permanence), and network expansion (adding new Colleges to increase capacity). The endowment is the university\'s insurance against uncertainty — it provides a permanent source of income that exists independently of tuition revenue, ensuring that the institution can weather economic downturns, demographic shifts, and unforeseen challenges without compromising its mission.', STYLES['body']))
    story.append(sp(4))
    story.append(chart_image('surplus_endowment_growth.png', height=200))
    story.append(Paragraph('Surplus and endowment growth trajectory showing compounding value.', STYLES['caption']))
    story.append(sp(6))

    surplus_data = [
        [Paragraph('<b>Metric</b>', STYLES['table_header']), Paragraph('<b>Year 1</b>', STYLES['table_header']),
         Paragraph('<b>Year 2</b>', STYLES['table_header']), Paragraph('<b>Year 3</b>', STYLES['table_header']),
         Paragraph('<b>Year 5</b>', STYLES['table_header'])],
        [Paragraph('Annual Surplus', STYLES['table_cell']), Paragraph('$38M', STYLES['table_cell_right']),
         Paragraph('$150M', STYLES['table_cell_right']), Paragraph('$350M', STYLES['table_cell_right']),
         Paragraph('$740M', STYLES['table_cell_right'])],
        [Paragraph('End-of-Year Endowment', STYLES['table_cell']), Paragraph('$63M', STYLES['table_cell_right']),
         Paragraph('$213M', STYLES['table_cell_right']), Paragraph('$475M', STYLES['table_cell_right']),
         Paragraph('$1.35B', STYLES['table_cell_right'])],
        [Paragraph('Endowment Yield @ 4.5%', STYLES['table_cell']), Paragraph('$2.8M', STYLES['table_cell_right']),
         Paragraph('$9.6M', STYLES['table_cell_right']), Paragraph('$21.4M', STYLES['table_cell_right']),
         Paragraph('$60.8M', STYLES['table_cell_right'])],
        [Paragraph('Scholarships Funded from Surplus', STYLES['table_cell']), Paragraph('10,000', STYLES['table_cell_right']),
         Paragraph('13,300', STYLES['table_cell_right']), Paragraph('16,600', STYLES['table_cell_right']),
         Paragraph('23,200', STYLES['table_cell_right'])],
    ]
    story.append(make_table(surplus_data, col_widths=[W*0.3, W*0.175, W*0.175, W*0.175, W*0.175]))

    # Page 5: Campaign Allocation
    story.append(PageBreak())
    story.append(Paragraph('CAMPAIGN ALLOCATION DETAIL', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(6))
    story.append(chart_image('campaign_allocation_donut.png', height=210))
    story.append(Paragraph('$100M founding campaign allocation across the five pillars.', STYLES['caption']))
    story.append(sp(6))
    story.append(Paragraph(
        'The $100M founding campaign is allocated across five pillars, each representing a critical component of the university\'s launch. Place (82%) funds the acquisition and repurposing of 50 properties across 35 countries. Minds (7%) covers the 3-month faculty compensation bridge. Access (5%) seeds Year 1 scholarships for 10,000 students. Excellence (3%) funds research startup and Centers of Inquiry. Progress (3%) provides the seed endowment and technology infrastructure. After launch, all ongoing costs are covered by tuition revenue. The campaign is a one-time investment in permanent infrastructure.', STYLES['body']))
    story.append(sp(4))
    story.append(chart_image('student_growth_bar.png', height=180))
    story.append(Paragraph('Student and college growth projection over 5 years.', STYLES['caption']))

    # Page 6: Key Assumptions
    story.append(PageBreak())
    story.append(Paragraph('KEY ASSUMPTIONS & SENSITIVITIES', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(6))
    story.append(Paragraph(
        'The financial model rests on a set of conservative assumptions. Tuition is set at $3,000/year — a figure accessible to 90% of qualified students globally and well below the $10,000-$60,000 range of traditional universities. Student enrollment grows at 50% per year (Year 1: 100K, Year 2: 150K, Year 3: 200K), a conservative estimate given that 263 million students currently lack access to higher education. Faculty compensation averages $90,000/year, competitive in most markets and sustainable at the tutorial ratio. Property costs average $1.64M per College for acquisition and repurposing — a conservative estimate given the focus on repurposed buildings in cost-effective markets.', STYLES['body']))
    story.append(sp(4))

    assumptions_data = [
        [Paragraph('<b>Assumption</b>', STYLES['table_header']), Paragraph('<b>Base Case</b>', STYLES['table_header']),
         Paragraph('<b>Conservative</b>', STYLES['table_header']), Paragraph('<b>Optimistic</b>', STYLES['table_header'])],
        [Paragraph('Annual Tuition', STYLES['table_cell']), Paragraph('$3,000', STYLES['table_cell']),
         Paragraph('$2,500', STYLES['table_cell']), Paragraph('$4,000', STYLES['table_cell'])],
        [Paragraph('Year 1 Enrollment', STYLES['table_cell']), Paragraph('100,000', STYLES['table_cell']),
         Paragraph('75,000', STYLES['table_cell']), Paragraph('120,000', STYLES['table_cell'])],
        [Paragraph('Avg Property Cost/College', STYLES['table_cell']), Paragraph('$1.64M', STYLES['table_cell']),
         Paragraph('$2.0M', STYLES['table_cell']), Paragraph('$1.2M', STYLES['table_cell'])],
        [Paragraph('Faculty Avg Compensation', STYLES['table_cell']), Paragraph('$90,000', STYLES['table_cell']),
         Paragraph('$100,000', STYLES['table_cell']), Paragraph('$80,000', STYLES['table_cell'])],
        [Paragraph('Endowment Yield', STYLES['table_cell']), Paragraph('4.5%', STYLES['table_cell']),
         Paragraph('3.5%', STYLES['table_cell']), Paragraph('5.5%', STYLES['table_cell'])],
        [Paragraph('Year 1 Surplus', STYLES['table_cell']), Paragraph('$38M', STYLES['table_cell']),
         Paragraph('-$12M', STYLES['table_cell']), Paragraph('$78M', STYLES['table_cell'])],
    ]
    story.append(make_table(assumptions_data, col_widths=[W*0.28, W*0.24, W*0.24, W*0.24]))
    story.append(sp(8))
    story.append(Paragraph(
        'Even in the conservative scenario (lower tuition, lower enrollment, higher costs), the university reaches surplus by Year 2 and achieves endowment self-sufficiency by Year 4. The model is robust because its core insight — that high volume at low price generates surplus when costs are structurally low — is mathematically sound and empirically proven by every successful low-cost, high-volume enterprise in history, from Walmart to Ryanair to the University of the People.', STYLES['body']))
    doc.build(story)
    print(f"  Financial Model: {os.path.getsize(os.path.join(OUT, 'artemis-financial-model.pdf'))//1024}KB")


# ══════════════════════════════════════════════════════════════════
# 5. TAX DEDUCTIBILITY GUIDE (4 pages)
# ══════════════════════════════════════════════════════════════════
def gen_tax_guide():
    doc = ArtemisDoc(
        os.path.join(OUT, 'artemis-tax-guide.pdf'),
        cover_title='TAX\nDEDUCTIBILITY\nGUIDE',
        cover_subtitle='Jurisdiction-by-Jurisdiction Tax Benefits for Donors',
        cover_img='law-justice.jpg',
        cover_tagline='MAXIMISE YOUR IMPACT. MINIMISE YOUR TAX.',
        title_short='Tax Guide'
    )
    story = []
    story.append(NextPageTemplate('content'))
    story.append(PageBreak())

    story.append(Paragraph('TAX DEDUCTIBILITY OVERVIEW', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(6))
    story.append(hero_image('law-justice.jpg', height=120))
    story.append(Paragraph('Legal structure across three jurisdictions ensures global tax deductibility. Image: Unsplash', STYLES['caption']))
    story.append(sp(4))
    story.append(Paragraph(
        'The University of Artemis is incorporated across three jurisdictions to maximise tax benefits for donors worldwide. The primary entity is a Delaware Non-Stock Corporation with 501(c)(3) classification, providing full tax deductibility for US donors. The secondary entity in England and Wales enables Gift Aid (25% government top-up) for UK donors. The tertiary entity in Switzerland provides endowment management in a tax-efficient neutral jurisdiction. Donors in most countries can benefit from at least one of these structures, and the advancement team works with each donor to identify the optimal giving vehicle for their jurisdiction and tax situation.', STYLES['body']))
    story.append(sp(6))

    # US section
    story.append(Paragraph('UNITED STATES: 501(c)(3) DEDUCTIBILITY', STYLES['h2']))
    story.append(sp(4))
    story.append(Paragraph(
        'The University of Artemis is incorporated as a Delaware Non-Stock Corporation and has filed IRS Form 1023 for 501(c)(3) determination. Under US tax law, donations to 501(c)(3) organisations are tax-deductible to the fullest extent allowed by law. Individual donors can deduct up to 60% of adjusted gross income (AGI) for cash gifts and 30% of AGI for appreciated property. Corporate donors can deduct up to 10% of taxable income. The 501(c)(3) status provides retroactive deductibility within 27 months of incorporation, meaning gifts made before the determination letter is issued are still deductible.', STYLES['body']))
    story.append(sp(4))

    us_data = [
        [Paragraph('<b>Feature</b>', STYLES['table_header']), Paragraph('<b>Detail</b>', STYLES['table_header'])],
        [Paragraph('Entity Type', STYLES['table_cell']), Paragraph('Delaware Non-Stock Corporation', STYLES['table_cell'])],
        [Paragraph('Tax Classification', STYLES['table_cell']), Paragraph('501(c)(3) - Educational & Charitable', STYLES['table_cell'])],
        [Paragraph('Cash Gift Limit', STYLES['table_cell']), Paragraph('60% of AGI for individuals; 10% for corporations', STYLES['table_cell'])],
        [Paragraph('Property Gift Limit', STYLES['table_cell']), Paragraph('30% of AGI (fair market value)', STYLES['table_cell'])],
        [Paragraph('Retroactive Deductibility', STYLES['table_cell']), Paragraph('Within 27 months of incorporation', STYLES['table_cell'])],
        [Paragraph('EIN Available', STYLES['table_cell']), Paragraph('Yes - provided upon gift acknowledgement', STYLES['table_cell'])],
        [Paragraph('Gift Acknowledgement', STYLES['table_cell']), Paragraph('Written acknowledgement for all gifts over $250', STYLES['table_cell'])],
    ]
    story.append(make_table(us_data, col_widths=[W*0.35, W*0.65]))
    story.append(PageBreak())

    # UK section
    story.append(Paragraph('UNITED KINGDOM: GIFT AID', STYLES['h2']))
    story.append(sp(4))
    story.append(Paragraph(
        'The University of Artemis is establishing a Charitable Incorporated Organisation (CIO) in England and Wales, registered with the Charity Commission under the advancement of education. UK donors receive full tax relief on gifts, and Gift Aid adds 25% to every eligible donation through HMRC top-up. A UK donor giving GBP 100,000 results in the university receiving GBP 125,000. Higher-rate taxpayers can claim an additional 25% personal tax relief, making the net cost of a GBP 100,000 gift only GBP 62,500 for a 45% taxpayer. The CIO structure is recognised by Commonwealth jurisdictions worldwide, extending tax benefits to donors in Canada, Australia, New Zealand, and other Commonwealth nations through reciprocal tax treaties.', STYLES['body']))
    story.append(sp(4))

    uk_data = [
        [Paragraph('<b>Feature</b>', STYLES['table_header']), Paragraph('<b>Detail</b>', STYLES['table_header'])],
        [Paragraph('Entity Type', STYLES['table_cell']), Paragraph('CIO (Charitable Incorporated Organisation)', STYLES['table_cell'])],
        [Paragraph('Regulator', STYLES['table_cell']), Paragraph('Charity Commission for England & Wales', STYLES['table_cell'])],
        [Paragraph('Gift Aid Top-Up', STYLES['table_cell']), Paragraph('25% from HMRC on eligible donations', STYLES['table_cell'])],
        [Paragraph('Higher Rate Relief', STYLES['table_cell']), Paragraph('Additional 20-25% personal tax relief', STYLES['table_cell'])],
        [Paragraph('Commonwealth Recognition', STYLES['table_cell']), Paragraph('Reciprocal tax treaties with Canada, Australia, NZ', STYLES['table_cell'])],
        [Paragraph('Gift of Shares', STYLES['table_cell']), Paragraph('Full income tax relief + no CGT', STYLES['table_cell'])],
    ]
    story.append(make_table(uk_data, col_widths=[W*0.35, W*0.65]))
    story.append(sp(8))

    # Switzerland section
    story.append(Paragraph('SWITZERLAND: FONDATION STRUCTURE', STYLES['h2']))
    story.append(sp(4))
    story.append(Paragraph(
        'The Swiss Fondation under the Geneva Canton provides endowment management in a neutral, tax-efficient jurisdiction. Switzerland is home to WHO, CERN, IOC, and over 4,000 international organisations. The Fondation structure offers no capital gains tax on endowment growth, minimal income tax on investment returns, and strong governance oversight through the Swiss foundation supervision authority. For European and Gulf donors, the Swiss entity provides a familiar and trusted structure that signals institutional permanence and financial probity. Donations to Swiss charitable foundations are tax-deductible in Switzerland and in many European jurisdictions through bilateral tax treaties.', STYLES['body']))
    story.append(sp(4))

    ch_data = [
        [Paragraph('<b>Feature</b>', STYLES['table_header']), Paragraph('<b>Detail</b>', STYLES['table_header'])],
        [Paragraph('Entity Type', STYLES['table_cell']), Paragraph('Fondation under Swiss Civil Code', STYLES['table_cell'])],
        [Paragraph('Canton', STYLES['table_cell']), Paragraph('Geneva', STYLES['table_cell'])],
        [Paragraph('Minimum Capital', STYLES['table_cell']), Paragraph('CHF 50,000', STYLES['table_cell'])],
        [Paragraph('Capital Gains Tax', STYLES['table_cell']), Paragraph('None on endowment growth', STYLES['table_cell'])],
        [Paragraph('Supervision', STYLES['table_cell']), Paragraph('Cantonal authority and Swiss foundation supervision', STYLES['table_cell'])],
    ]
    story.append(make_table(ch_data, col_widths=[W*0.35, W*0.65]))
    story.append(PageBreak())

    # Other jurisdictions
    story.append(Paragraph('OTHER JURISDICTIONS & FISCAL SPONSORSHIP', STYLES['h2']))
    story.append(sp(4))
    story.append(Paragraph(
        'For donors in jurisdictions where direct deductibility is not yet available, the University of Artemis works with fiscal sponsors to enable tax-efficient giving. Rockefeller Philanthropy Advisors, NGOsource, and Global Impact provide equivalency determinations that enable donors in over 80 countries to receive local tax benefits for gifts to Artemis. The advancement team manages all documentation and can facilitate gifts in any currency, through any legal structure, and in compliance with local regulations. For donors in the EU, the Transnational Giving Europe (TGE) network provides a streamlined mechanism for cross-border charitable giving with full tax deductibility in the donor\'s country of residence.', STYLES['body']))
    story.append(sp(4))

    other_data = [
        [Paragraph('<b>Jurisdiction</b>', STYLES['table_header']), Paragraph('<b>Mechanism</b>', STYLES['table_header']),
         Paragraph('<b>Key Benefit</b>', STYLES['table_header'])],
        [Paragraph('Canada', STYLES['table_cell']), Paragraph('Reciprocal treaty via UK CIO', STYLES['table_cell']),
         Paragraph('Full charitable deduction', STYLES['table_cell'])],
        [Paragraph('Australia', STYLES['table_cell']), Paragraph('Reciprocal treaty via UK CIO', STYLES['table_cell']),
         Paragraph('Deductible gift recipient status', STYLES['table_cell'])],
        [Paragraph('EU Countries', STYLES['table_cell']), Paragraph('Transnational Giving Europe', STYLES['table_cell']),
         Paragraph('Full deductibility in donor\'s country', STYLES['table_cell'])],
        [Paragraph('Gulf States', STYLES['table_cell']), Paragraph('Swiss Fondation', STYLES['table_cell']),
         Paragraph('No tax on gifts; neutral jurisdiction', STYLES['table_cell'])],
        [Paragraph('Other (80+ countries)', STYLES['table_cell']), Paragraph('Fiscal sponsorship (NGOsource)', STYLES['table_cell']),
         Paragraph('Equivalency determination for local tax benefit', STYLES['table_cell'])],
    ]
    story.append(make_table(other_data, col_widths=[W*0.2, W*0.35, W*0.45]))
    story.append(sp(8))
    story.append(Paragraph(
        'Contact the advancement team at donate@artemisui.org for jurisdiction-specific guidance. We work with your legal and tax advisors to structure your gift for maximum impact and maximum tax efficiency.', STYLES['body']))
    doc.build(story)
    print(f"  Tax Guide: {os.path.getsize(os.path.join(OUT, 'artemis-tax-guide.pdf'))//1024}KB")


# ══════════════════════════════════════════════════════════════════
# 6. LEGAL ENTITY OVERVIEW (5 pages)
# ══════════════════════════════════════════════════════════════════
def gen_legal_entities():
    doc = ArtemisDoc(
        os.path.join(OUT, 'artemis-legal-entities.pdf'),
        cover_title='LEGAL ENTITY\nOVERVIEW',
        cover_subtitle='Corporate Structure, Governance & Incorporation Details',
        cover_img='architecture-building.jpg',
        cover_tagline='THREE JURISDICTIONS. ONE MISSION. PERMANENT STRUCTURE.',
        title_short='Legal Entities'
    )
    story = []
    story.append(NextPageTemplate('content'))
    story.append(PageBreak())

    story.append(Paragraph('CORPORATE STRUCTURE OVERVIEW', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(6))
    story.append(hero_image('architecture-building.jpg', height=130))
    story.append(Paragraph('The University of Artemis is structured across three jurisdictions for global reach. Image: Unsplash', STYLES['caption']))
    story.append(sp(4))
    story.append(Paragraph(
        'The University of Artemis operates through a coordinated legal structure spanning three jurisdictions: the United States (primary), England and Wales (secondary), and Switzerland (tertiary). This structure ensures tax deductibility for donors worldwide, regulatory compliance across all operating jurisdictions, and robust governance that prevents any single individual from controlling the institution. Each entity has a distinct purpose within the overall structure, and all entities are governed by compatible constitutional documents that ensure alignment with the university\'s charitable mission.', STYLES['body']))
    story.append(sp(6))

    # Primary entity
    story.append(Paragraph('PRIMARY ENTITY: DELAWARE NON-STOCK CORPORATION', STYLES['h2']))
    story.append(sp(4))
    story.append(Paragraph(
        'The primary legal entity is a Delaware Non-Stock Corporation, the standard structure for US charitable organisations. Delaware provides the most favourable corporate law environment for non-profit entities, including flexible governance structures, strong director protections, and an established body of case law. The corporation has filed IRS Form 1023 for 501(c)(3) determination, which provides retroactive deductibility within 27 months of incorporation. The corporation has no shareholders, no owners, and no private benefit. All assets are dedicated to the charitable purpose of advancing education. The board of trustees must have a minimum of 3 independent members, and no single individual may control more than one-third of board seats.', STYLES['body']))
    story.append(sp(4))

    de_data = [
        [Paragraph('<b>Feature</b>', STYLES['table_header']), Paragraph('<b>Detail</b>', STYLES['table_header'])],
        [Paragraph('Legal Form', STYLES['table_cell']), Paragraph('Non-Stock Corporation', STYLES['table_cell'])],
        [Paragraph('State of Incorporation', STYLES['table_cell']), Paragraph('Delaware', STYLES['table_cell'])],
        [Paragraph('IRS Classification', STYLES['table_cell']), Paragraph('501(c)(3) - Educational & Charitable', STYLES['table_cell'])],
        [Paragraph('Form 1023 Status', STYLES['table_cell']), Paragraph('Filed; determination pending', STYLES['table_cell'])],
        [Paragraph('Minimum Board Members', STYLES['table_cell']), Paragraph('3 (majority independent)', STYLES['table_cell'])],
        [Paragraph('Ownership', STYLES['table_cell']), Paragraph('No shareholders; no private benefit', STYLES['table_cell'])],
        [Paragraph('Fiscal Sponsor', STYLES['table_cell']), Paragraph('Rockefeller Philanthropy Advisors (interim)', STYLES['table_cell'])],
        [Paragraph('Registered Agent', STYLES['table_cell']), Paragraph('Delaware registered agent on file', STYLES['table_cell'])],
    ]
    story.append(make_table(de_data, col_widths=[W*0.35, W*0.65]))
    story.append(PageBreak())

    # UK entity
    story.append(Paragraph('SECONDARY ENTITY: CHARITABLE INCORPORATED ORGANISATION', STYLES['h2']))
    story.append(sp(4))
    story.append(Paragraph(
        'The secondary entity is a Charitable Incorporated Organisation (CIO) registered with the Charity Commission for England and Wales. The CIO structure provides the benefits of charitable status (Gift Aid, tax relief, public trust) without the dual registration requirements of a company limited by guarantee. The CIO must have a minimum of 3 trustees and a UK registered office. Gift Aid eligibility means that every qualifying donation from a UK taxpayer is increased by 25% at no cost to the donor. The CIO structure is recognised by Commonwealth jurisdictions worldwide, extending the university\'s reach to Canada, Australia, New Zealand, and other Commonwealth nations through reciprocal tax treaties and equivalency determinations.', STYLES['body']))
    story.append(sp(4))

    # Switzerland entity
    story.append(Paragraph('TERTIARY ENTITY: SWISS FONDATION', STYLES['h2']))
    story.append(sp(4))
    story.append(Paragraph(
        'The tertiary entity is a Fondation under the Swiss Civil Code, registered in the Canton of Geneva. Switzerland is the world\'s leading jurisdiction for international charitable foundations, hosting over 4,000 organisations including WHO, CERN, and the IOC. The Fondation structure provides minimal tax drag on endowment growth (no capital gains tax, minimal income tax on investment returns), strong governance oversight through cantonal supervision, and international credibility that signals institutional permanence to European and Gulf donors. The minimum initial capital is CHF 50,000, and the foundation must be approved by the cantonal authority before it can begin operations.', STYLES['body']))
    story.append(sp(4))

    # Governance
    story.append(Paragraph('GOVERNANCE FRAMEWORK', STYLES['h2']))
    story.append(sp(4))
    story.append(Paragraph(
        'All three entities operate under compatible governance documents that ensure alignment with the university\'s charitable mission and prevent any single individual from exercising control. The governance framework includes three bodies: the Board of Trustees (financial and legal oversight), the Academic Senate (academic standards and curriculum), and the Board of Visitors (donor and alumni advisory). Annual independent audits by a Big Four firm are mandatory and published. Every dollar received and disbursed is published in an annual impact report available to the public. The governance structure is designed to ensure transparency, accountability, and permanence — the university must outlive its founders, and its governance must be robust enough to ensure that outcome.', STYLES['body']))
    doc.build(story)
    print(f"  Legal Entities: {os.path.getsize(os.path.join(OUT, 'artemis-legal-entities.pdf'))//1024}KB")


# ══════════════════════════════════════════════════════════════════
# 7. NAMING OPPORTUNITIES BOOKLET (10 pages)
# ══════════════════════════════════════════════════════════════════
def gen_naming_booklet():
    doc = ArtemisDoc(
        os.path.join(OUT, 'artemis-naming-booklet.pdf'),
        cover_title='NAMING\nOPPORTUNITIES',
        cover_subtitle='Permanent Legacy. Enduring Impact.',
        cover_img='ceremony-formal.jpg',
        cover_tagline='YOUR NAME. A UNIVERSITY. FOREVER.',
        title_short='Naming Booklet'
    )
    story = []
    story.append(NextPageTemplate('content'))
    story.append(PageBreak())

    story.append(Paragraph('NAMING AT ARTEMIS', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(6))
    story.append(Paragraph(
        'Every naming opportunity at the University of Artemis is permanent. Your name does not grace a building for 20 years — it becomes part of the institution\'s foundation for as long as the university exists. Named gifts are endowments: the asset (property, position, program) generates value in perpetuity, and your name is inseparable from that value. This booklet details every naming opportunity available during the founding campaign, from the apex — a Central Node at $25M — to the most personal: a student scholarship at $12,000.', STYLES['body']))
    story.append(sp(6))
    story.append(chart_image('naming_opportunities_bar.png', height=190))
    story.append(Paragraph('Naming opportunities by tier and amount.', STYLES['caption']))
    story.append(PageBreak())

    # Central Node
    story.append(Paragraph('CENTRAL NODE — $25,000,000', STYLES['h2']))
    story.append(hero_image('campus-venice.jpg', height=140))
    story.append(Paragraph('Venice Central Node. Image: Unsplash', STYLES['caption']))
    story.append(sp(4))
    story.append(Paragraph(
        'The apex of the Artemis network. Name one of three Central Nodes — Venice, San Francisco, or Singapore — and your name becomes synonymous with the university\'s global presence. Each Central Node serves approximately 5,000 students and functions as the administrative, research, and cultural hub for its region. The Venice Central Node houses the founding document and the headquarters of the Board of Trustees. The San Francisco Central Node is the innovation and technology hub, home to the Global Challenge Fund and the digital infrastructure team. The Singapore Central Node is the admissions and research gateway for Asia-Pacific.', STYLES['body']))
    story.append(Paragraph(
        'Your named Central Node carries your name in perpetuity — on the building, in all university communications, in every degree certificate issued from the node, and in the founding charter. Only three Central Nodes exist. Only three names will be inscribed at this level. This is the most significant naming opportunity outside of founding the university itself. Central Node naming gifts qualify for the Founders\' Circle, the highest tier of recognition, which includes a permanent seat on the Board of Visitors and an annual private dinner with the President.', STYLES['body']))
    story.append(sp(8))

    # Tier A College
    story.append(Paragraph('TIER A COLLEGE — $10,000,000', STYLES['h2']))
    story.append(hero_image('london-skyline.jpg', height=130))
    story.append(Paragraph('Major global cities host Tier A Colleges. Image: Unsplash', STYLES['caption']))
    story.append(sp(4))
    story.append(Paragraph(
        'Name a flagship College in the world\'s great knowledge capitals: London, Paris, Tokyo, Berlin, Nairobi, Sao Paulo, and similar cities. Tier A Colleges serve approximately 2,500 students in purpose-renovated buildings that serve as landmarks in their cities. Your name is permanently associated with a flagship institution that will educate tens of thousands of students over the coming decades and produce research that shapes the world. Tier A College naming gifts qualify for the Guardians\' Circle, with recognition at all 50 Colleges and an annual private briefing with the President.', STYLES['body']))
    story.append(sp(8))

    # Center of Inquiry
    story.append(Paragraph('CENTER OF INQUIRY — $10,000,000', STYLES['h2']))
    story.append(hero_image('research-lab.jpg', height=130))
    story.append(Paragraph('Research is at the heart of every great university. Image: Unsplash', STYLES['caption']))
    story.append(sp(4))
    story.append(Paragraph(
        'Name one of 19 Centers of Inquiry — a permanently endowed, independently operating research centre carrying your name. Centers of Inquiry are the intellectual engines of the university, each focused on a specific domain of inquiry (from the Ethics of Emerging Technology to the Geometry of Social Systems). Each Center has a director, a research team, and an active portfolio of projects. Your named Center produces research that is released under open-access terms within 7 years, ensuring that your gift contributes not just to the university but to global knowledge. Center naming gifts qualify for the Guardians\' Circle.', STYLES['body']))
    story.append(PageBreak())

    # Tier B College
    story.append(Paragraph('TIER B COLLEGE — $5,000,000', STYLES['h2']))
    story.append(sp(4))
    story.append(Paragraph(
        'Name a College in major global cities. Tier B Colleges serve approximately 2,000 students in substantial, permanent buildings. These are the backbone of the Artemis network — the Colleges that make the global rotation model possible by providing high-quality residential and tutorial spaces in key cities. Tier B College naming gifts qualify for the Builders\' Circle, with a recognition plaque at all 50 Colleges and an annual impact report on your named College.', STYLES['body']))
    story.append(sp(8))

    # Distinguished Professorship
    story.append(Paragraph('DISTINGUISHED PROFESSORSHIP — $5,000,000', STYLES['h2']))
    story.append(hero_image('professor-teaching.jpg', height=130))
    story.append(Paragraph('Faculty are the heart of any university. Image: Unsplash', STYLES['caption']))
    story.append(sp(4))
    story.append(Paragraph(
        'Endow a faculty position in perpetuity. At 4.5% yield, a $5M Distinguished Professorship generates $225,000 per year — enough to sustain one position at career-level compensation forever. The naming gift is an endowment, not a sponsorship: the principal is preserved, and the yield funds the position. Your named professorship will attract world-class scholars, produce groundbreaking research, and teach thousands of students through the tutorial system. Distinguished Professorship naming gifts qualify for the Builders\' Circle.', STYLES['body']))
    story.append(sp(8))

    # Degree Program
    story.append(Paragraph('DEGREE PROGRAM — $3,000,000', STYLES['h2']))
    story.append(sp(4))
    story.append(Paragraph(
        'Name one of 55 degree programs at the University of Artemis. Your name is associated with a specific discipline and every graduate who carries it forward. Whether it\'s the John Smith Programme in Computational Thinking or the Chen Wei Programme in Global Systems, your name becomes synonymous with excellence in that field. Degree program naming gifts are endowments: the principal generates yield that supports the program in perpetuity, ensuring that your named program continues to attract the best students and produce the most impactful research.', STYLES['body']))
    story.append(sp(8))

    # Tier C College
    story.append(Paragraph('TIER C COLLEGE — $2,000,000', STYLES['h2']))
    story.append(hero_image('kigali-city.jpg', height=130))
    story.append(Paragraph('Emerging cities like Kigali host Tier C Colleges. Image: Unsplash', STYLES['caption']))
    story.append(sp(4))
    story.append(Paragraph(
        'Name a College in cities like Kigali, Dhaka, Kampala, Karachi, and similar emerging knowledge centres. Tier C Colleges serve approximately 1,100 students and represent the university\'s commitment to bringing world-class education to the places that need it most. Your name becomes home to the next generation of leaders in your region. Tier C College naming gifts qualify for the Builders\' Circle, with a recognition plaque at all 50 Colleges and an annual Builder\'s Report detailing the impact of your named gift.', STYLES['body']))
    story.append(PageBreak())

    # Scholarship Fund
    story.append(Paragraph('SCHOLARSHIP FUND — $12,000', STYLES['h2']))
    story.append(hero_image('scholarship-student.jpg', height=130))
    story.append(Paragraph('Every scholarship changes a life permanently. Image: Unsplash', STYLES['caption']))
    story.append(sp(4))
    story.append(Paragraph(
        'Fund one student\'s full scholarship for four years. At $3,000/year, the total cost is $12,000. This is the most direct way to change a life — and the most personal naming opportunity at Artemis. Your scholarship fund carries your name (or a name you designate) and is awarded to a specific student who will know that their education was made possible by your generosity. Scholarship donors receive the name and story of their scholarship recipient (with the student\'s consent), creating a direct connection between your gift and its impact.', STYLES['body']))
    story.append(sp(8))

    # Summary table
    story.append(Paragraph('NAMING OPPORTUNITIES SUMMARY', STYLES['h2']))
    story.append(sp(4))
    summary_data = [
        [Paragraph('<b>Opportunity</b>', STYLES['table_header']), Paragraph('<b>Amount</b>', STYLES['table_header']),
         Paragraph('<b>Giving Circle</b>', STYLES['table_header']), Paragraph('<b>Perpetuity</b>', STYLES['table_header'])],
        [Paragraph('Central Node', STYLES['table_cell']), Paragraph('$25M', STYLES['table_cell_right']),
         Paragraph('Founders\' Circle', STYLES['table_cell']), Paragraph('Named building + charter inscription', STYLES['table_cell'])],
        [Paragraph('Tier A College', STYLES['table_cell']), Paragraph('$10M', STYLES['table_cell_right']),
         Paragraph('Guardians\' Circle', STYLES['table_cell']), Paragraph('Named building', STYLES['table_cell'])],
        [Paragraph('Center of Inquiry', STYLES['table_cell']), Paragraph('$10M', STYLES['table_cell_right']),
         Paragraph('Guardians\' Circle', STYLES['table_cell']), Paragraph('Named research centre', STYLES['table_cell'])],
        [Paragraph('Tier B College', STYLES['table_cell']), Paragraph('$5M', STYLES['table_cell_right']),
         Paragraph('Builders\' Circle', STYLES['table_cell']), Paragraph('Named building', STYLES['table_cell'])],
        [Paragraph('Distinguished Prof.', STYLES['table_cell']), Paragraph('$5M', STYLES['table_cell_right']),
         Paragraph('Builders\' Circle', STYLES['table_cell']), Paragraph('Endowed position', STYLES['table_cell'])],
        [Paragraph('Degree Program', STYLES['table_cell']), Paragraph('$3M', STYLES['table_cell_right']),
         Paragraph('Builders\' Circle', STYLES['table_cell']), Paragraph('Named academic program', STYLES['table_cell'])],
        [Paragraph('Tier C College', STYLES['table_cell']), Paragraph('$2M', STYLES['table_cell_right']),
         Paragraph('Builders\' Circle', STYLES['table_cell']), Paragraph('Named building', STYLES['table_cell'])],
        [Paragraph('Scholarship Fund', STYLES['table_cell']), Paragraph('$12K', STYLES['table_cell_right']),
         Paragraph('The 99 / Friends', STYLES['table_cell']), Paragraph('4-year named scholarship', STYLES['table_cell'])],
    ]
    story.append(make_table(summary_data, col_widths=[W*0.22, W*0.13, W*0.22, W*0.43]))
    doc.build(story)
    print(f"  Naming Booklet: {os.path.getsize(os.path.join(OUT, 'artemis-naming-booklet.pdf'))//1024}KB")


# ══════════════════════════════════════════════════════════════════
# 8. GIVING CIRCLES BENEFITS GUIDE (6 pages)
# ══════════════════════════════════════════════════════════════════
def gen_giving_circles():
    doc = ArtemisDoc(
        os.path.join(OUT, 'artemis-giving-circles.pdf'),
        cover_title='GIVING\nCIRCLES',
        cover_subtitle='Benefits, Recognition & Annual Impact',
        cover_img='handshakes-deal.jpg',
        cover_tagline='EVERY GIFT. EVERY CIRCLE. PERMANENT RECOGNITION.',
        title_short='Giving Circles'
    )
    story = []
    story.append(NextPageTemplate('content'))
    story.append(PageBreak())

    story.append(Paragraph('THE GIVING CIRCLES', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(6))
    story.append(Paragraph(
        'The University of Artemis recognises its donors through six Giving Circles, each reflecting a different level of commitment and carrying distinct benefits. Every circle provides permanent recognition — your name becomes part of the university\'s founding story. The circles are designed to honour the full spectrum of giving, from the transformative gifts of the Founders\' Circle to the grassroots commitment of The 99. Every circle matters. Every member of every circle is a founder.', STYLES['body']))
    story.append(sp(6))
    story.append(chart_image('giving_circles_bar.png', height=180))
    story.append(Paragraph('Giving circles by minimum gift threshold.', STYLES['caption']))
    story.append(PageBreak())

    circles = [
        ("THE FOUNDERS' CIRCLE — $10M+", CRIMSON, 'ceremony-formal.jpg',
         'The Founders\' Circle is the highest tier of recognition at the University of Artemis. Members\' names are engraved on the university\'s founding document at the Venice Central Node — a permanent, physical inscription that will endure for centuries. Founders receive a permanent seat on the Board of Visitors, providing ongoing input into the university\'s strategic direction. The annual private dinner with the President, held at a rotating Central Node, brings together the world\'s most committed educational philanthropists. Each Founder also receives a named endowment fund or equivalent naming opportunity, a recognition plaque at all 50 Colleges, and a biographical feature in the annual campaign report.',
         ['Name engraved on the founding document at Venice Central Node', 'Permanent seat on Board of Visitors',
          'Private annual dinner with the President at rotating Central Node', 'Named endowment fund or equivalent naming opportunity',
          'Recognition plaque at all 50 Colleges', 'Biographical feature in annual campaign report']),
        ("THE GUARDIANS' CIRCLE — $5M–$9.9M", HexColor('#6B0000'), 'campus-venice.jpg',
         'Guardians name a College or Center of Inquiry, creating a permanent physical or intellectual landmark that carries their name. The Annual Guardian\'s Lecture is a public lecture series named by the donor — a platform for the ideas and voices they care about most. Guardians receive an annual private briefing with the President, providing direct insight into the university\'s progress, challenges, and strategic decisions. Each Guardian also receives a named endowment fund and a recognition plaque at all 50 Colleges.',
         ['Named College or Center of Inquiry', 'Recognition plaque at all 50 Colleges',
          'Annual Guardian\'s Lecture — a public lecture series named by you', 'Annual private briefing with the President',
          'Named endowment fund']),
        ("THE BUILDERS' CIRCLE — $1M–$4.9M", HexColor('#4338ca'), 'architecture-building.jpg',
         'Builders name a Professorship, Scholarship Fund, or major program, creating a lasting academic legacy. The annual Builder\'s Report provides a detailed impact analysis of the donor\'s named gift — not just a thank-you letter, but a rigorous accounting of the students taught, research produced, and outcomes achieved. Builders receive an invitation to the annual gathering and a feature in the campaign newsletter, alongside a recognition plaque at all 50 Colleges.',
         ['Named Professorship, Scholarship Fund, or major program', 'Recognition plaque at all 50 Colleges',
          'Annual Builder\'s Report — detailed impact report on your named gift', 'Invitation to annual gathering',
          'Feature in campaign newsletter']),
        ("THE FELLOWS' CIRCLE — $100K–$999K", TEAL, 'conference-room.jpg',
         'Fellows name a scholarship fund or tutorial room at their chosen College, creating a personal connection to a specific place in the Artemis network. Recognition at the chosen College includes a named plaque and inclusion in the College\'s founding record. Fellows receive the annual newsletter from the President and invitations to regional events.',
         ['Named scholarship fund or tutorial room at chosen College', 'Recognition at chosen College',
          'Annual Fellow\'s Newsletter from the President', 'Invitation to regional events']),
        ("FRIENDS OF ARTEMIS — $10K–$99K", HexColor('#15803d'), 'classroom-diverse.jpg',
         'Friends of Artemis have their name inscribed in the founding Donor Roll — a permanent digital and print record of everyone who contributed to the founding of the university. Each Friend receives a digital certificate of founding support, quarterly progress updates, and invitations to online events. The Donor Roll is published in the annual report and displayed permanently at each Central Node.',
         ['Name in founding Donor Roll (permanent digital and print record)', 'Digital certificate of founding support',
          'Quarterly progress updates', 'Invitation to online events']),
        ("THE 99 — $99", HexColor('#6b7280'), 'books-study.jpg',
         'The 99 are the first believers — the community that was there from the beginning. Members receive waitlist priority for enrollment, digital recognition on the community wall, monthly community updates, and the knowledge that they were first in line when the University of Artemis opened its doors. The name "The 99" reflects the 99% of the world that needs accessible higher education — and the belief that everyone, regardless of their financial means, can be part of the founding.',
         ['Waitlist priority for enrollment', 'Digital recognition on community wall',
          'Monthly community updates', 'The knowledge that you were first in line']),
    ]

    for name, color, img, desc, benefits in circles:
        story.append(Paragraph(name, STYLES['h2']))
        story.append(hero_image(img, height=110))
        story.append(Paragraph(desc, STYLES['body']))
        story.append(Paragraph('Benefits:', STYLES['h3']))
        for b in benefits:
            story.append(Paragraph(f'<bullet>&bull;</bullet> {b}', STYLES['bullet']))
        story.append(sp(10))

    doc.build(story)
    print(f"  Giving Circles: {os.path.getsize(os.path.join(OUT, 'artemis-giving-circles.pdf'))//1024}KB")


# ══════════════════════════════════════════════════════════════════
# 9. CAMPUS MASTER PLAN (12 pages)
# ══════════════════════════════════════════════════════════════════
def gen_campus_plan():
    doc = ArtemisDoc(
        os.path.join(OUT, 'artemis-campus-master-plan.pdf'),
        cover_title='CAMPUS\nMASTER PLAN',
        cover_subtitle='50 Colleges, 3 Central Nodes, 6 Continents',
        cover_img='architecture-building.jpg',
        cover_tagline='NOT BUILT. FOUND. REPURPOSED. PERMANENT.',
        title_short='Campus Master Plan'
    )
    story = []
    story.append(NextPageTemplate('content'))
    story.append(PageBreak())

    story.append(Paragraph('THE ARTEMIS CAMPUS CONCEPT', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(6))
    story.append(hero_image('architecture-building.jpg', height=150))
    story.append(Paragraph('Repurposed buildings become permanent Colleges. Image: Unsplash', STYLES['caption']))
    story.append(sp(4))
    story.append(Paragraph(
        'The University of Artemis does not build campuses. It finds existing buildings and gives them a second life as Colleges. Repurposed convents, warehouses, offices, factories — each one acquired, not leased; owned, not rented; permanent, not temporary. This approach eliminates approximately 80% of the capital costs associated with traditional campus construction while creating Colleges that are embedded in the fabric of their cities, not isolated on suburban campuses. The Artemis campus is not a single location — it is a distributed network of 50 Colleges across 35 countries, connected by a synchronous global campus that makes geography irrelevant to the quality of education.', STYLES['body']))
    story.append(sp(6))

    story.append(Paragraph('THE THREE CENTRAL NODES', STYLES['h2']))
    story.append(sp(4))

    nodes = [
        ('VENICE CENTRAL NODE', 'campus-venice.jpg',
         'The Venice Central Node is the governance headquarters of the University of Artemis. Located in the historic city that has been a crossroads of civilisations for over a millennium, the Venice Node houses the founding document, the office of the President, and the primary meeting space for the Board of Trustees. The building is a repurposed palazzo on the Grand Canal, combining 15th-century architecture with 21st-century technology. The Node serves approximately 5,000 students and is the European hub for the Artemis network, with responsibility for operations in Europe, the Middle East, and Africa. Venice was chosen because it embodies the university\'s values: a city built on trade and exchange, where diverse cultures have met and produced extraordinary civilisational achievements for centuries.'),
        ('SAN FRANCISCO CENTRAL NODE', 'san-francisco.jpg',
         'The San Francisco Central Node is the innovation and technology hub of the University of Artemis. Located in the city that has defined the digital age, the San Francisco Node houses the Global Challenge Fund, the digital infrastructure team, and the innovation labs that bridge scholarship and the world it serves. The building is a repurposed warehouse in the SoMa district, combining industrial architecture with cutting-edge technology. The Node serves approximately 5,000 students and is the Americas hub, with responsibility for operations in North and South America. San Francisco was chosen because it represents the intersection of technology, innovation, and social change — the same intersection at which Artemis operates.'),
        ('SINGAPORE CENTRAL NODE', 'singapore-city.jpg',
         'The Singapore Central Node is the admissions and research gateway for Asia-Pacific. Located in the city-state that has become the world\'s most successful model of multicultural meritocracy, the Singapore Node houses the central admissions office, the Asia-Pacific research coordination centre, and the digital campus infrastructure. The building is a repurposed shophouse complex in the Civic District, combining colonial-era architecture with modern functionality. The Node serves approximately 5,000 students and is the Asia-Pacific hub, with responsibility for operations in East Asia, South Asia, and Oceania. Singapore was chosen because it demonstrates that excellence is not dependent on size — a city-state of 5.5 million people has become one of the world\'s leading knowledge economies.'),
    ]
    for title, img, desc in nodes:
        story.append(Paragraph(title, STYLES['h3']))
        story.append(hero_image(img, height=130))
        story.append(Paragraph(desc, STYLES['body']))
        story.append(sp(8))

    story.append(PageBreak())

    # College tiers
    story.append(Paragraph('COLLEGE TIERS', STYLES['h2']))
    story.append(sp(4))
    story.append(Paragraph(
        'Colleges are organised into three tiers based on location, size, and regional role. Tier A Colleges are located in the world\'s great knowledge capitals and serve approximately 2,500 students. Tier B Colleges are in major global cities and serve approximately 2,000 students. Tier C Colleges are in emerging knowledge centres and serve approximately 1,100 students. All Colleges, regardless of tier, offer the same tutorial-based education, the same curriculum, and the same degree. The tier system reflects the economic reality of different property markets — a College in central London costs more to acquire than a College in Kigali — but it does not reflect a difference in educational quality. Every Artemis College is a world-class institution.', STYLES['body']))
    story.append(sp(6))

    tier_data = [
        [Paragraph('<b>Tier</b>', STYLES['table_header']), Paragraph('<b>Students</b>', STYLES['table_header']),
         Paragraph('<b>Properties</b>', STYLES['table_header']), Paragraph('<b>Acquisition Cost</b>', STYLES['table_header']),
         Paragraph('<b>Example Cities</b>', STYLES['table_header'])],
        [Paragraph('Central Node', STYLES['table_cell']), Paragraph('~5,000', STYLES['table_cell']),
         Paragraph('3', STYLES['table_cell']), Paragraph('Varies', STYLES['table_cell']),
         Paragraph('Venice, San Francisco, Singapore', STYLES['table_cell'])],
        [Paragraph('Tier A', STYLES['table_cell']), Paragraph('~2,500', STYLES['table_cell']),
         Paragraph('10', STYLES['table_cell']), Paragraph('$3-5M', STYLES['table_cell']),
         Paragraph('London, Paris, Tokyo, Berlin, Nairobi', STYLES['table_cell'])],
        [Paragraph('Tier B', STYLES['table_cell']), Paragraph('~2,000', STYLES['table_cell']),
         Paragraph('15', STYLES['table_cell']), Paragraph('$1.5-3M', STYLES['table_cell']),
         Paragraph('Lagos, Mumbai, Mexico City, Istanbul', STYLES['table_cell'])],
        [Paragraph('Tier C', STYLES['table_cell']), Paragraph('~1,100', STYLES['table_cell']),
         Paragraph('22', STYLES['table_cell']), Paragraph('$0.5-1.5M', STYLES['table_cell']),
         Paragraph('Kigali, Dhaka, Kampala, Karachi', STYLES['table_cell'])],
    ]
    story.append(make_table(tier_data, col_widths=[W*0.14, W*0.12, W*0.12, W*0.18, W*0.44]))
    story.append(sp(8))

    story.append(Paragraph('REPURPOSING PHILOSOPHY', STYLES['h2']))
    story.append(sp(4))
    story.append(hero_image('campus-modern.jpg', height=130))
    story.append(Paragraph('Modern adaptive reuse: existing buildings become world-class educational spaces. Image: Unsplash', STYLES['caption']))
    story.append(sp(4))
    story.append(Paragraph(
        'The repurposing approach is not just a cost-saving measure — it is a philosophical commitment. Great universities have always been embedded in great cities, not isolated on suburban campuses. The College of the University of Chicago is woven into the city\'s Hyde Park neighbourhood. The Sorbonne sits in the Latin Quarter. LSE occupies buildings along the Aldwych. Artemis Colleges follow this tradition: they are part of the city, not apart from it. Students live in the neighbourhood, eat at local restaurants, and contribute to the local economy. The College is a permanent institutional presence that benefits both the university and the community. Repurposing also means that each College has architectural character and historical significance that new construction cannot replicate. A repurposed convent in Venice is not just a building — it is a statement about the relationship between past and future, between preservation and innovation.', STYLES['body']))
    doc.build(story)
    print(f"  Campus Master Plan: {os.path.getsize(os.path.join(OUT, 'artemis-campus-master-plan.pdf'))//1024}KB")


# ══════════════════════════════════════════════════════════════════
# 10. COLLEGIUM ALLIANCE MAP (2 pages)
# ══════════════════════════════════════════════════════════════════
def gen_alliance_map():
    doc = ArtemisDoc(
        os.path.join(OUT, 'artemis-collegium-map.pdf'),
        cover_title='COLLEGIUM\nALLIANCE MAP',
        cover_subtitle='50 Colleges. 6 Continents. 35 Countries. One University.',
        cover_img='globe-global.jpg',
        cover_tagline='A SYNCHRONOUS GLOBAL CAMPUS.',
        title_short='Collegium Map'
    )
    story = []
    story.append(NextPageTemplate('content'))
    story.append(PageBreak())

    story.append(Paragraph('THE ARTEMIS COLLEGIUM', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(6))
    story.append(hero_image('globe-global.jpg', height=180))
    story.append(Paragraph('The Artemis Collegium spans 6 continents and 35 countries. Image: Unsplash', STYLES['caption']))
    story.append(sp(6))
    story.append(Paragraph(
        'The Artemis Collegium is the alliance structure that connects all 50 Colleges into a single, synchronous global campus. Unlike a franchise model or a consortium of independent institutions, the Collegium operates as one university with multiple physical locations. Students are enrolled at the University of Artemis, not at a specific College. They rotate through Colleges during their 4-year programme, experiencing 6 different cities and cultural contexts while maintaining academic continuity through the shared curriculum and tutorial system. The synchronous campus means that a tutorial at 10am in Singapore is attended simultaneously by students in Venice, San Francisco, and Kigali — all in real time.', STYLES['body']))
    story.append(sp(6))

    # Regional breakdown table
    region_data = [
        [Paragraph('<b>Region</b>', STYLES['table_header']), Paragraph('<b>Colleges</b>', STYLES['table_header']),
         Paragraph('<b>Countries</b>', STYLES['table_header']), Paragraph('<b>Central Node</b>', STYLES['table_header'])],
        [Paragraph('Europe', STYLES['table_cell']), Paragraph('12', STYLES['table_cell']),
         Paragraph('8 (Italy, UK, France, Germany, Spain, Netherlands, Sweden, Switzerland)', STYLES['table_cell']),
         Paragraph('Venice', STYLES['table_cell'])],
        [Paragraph('Americas', STYLES['table_cell']), Paragraph('10', STYLES['table_cell']),
         Paragraph('6 (USA, Canada, Brazil, Mexico, Argentina, Colombia)', STYLES['table_cell']),
         Paragraph('San Francisco', STYLES['table_cell'])],
        [Paragraph('Asia-Pacific', STYLES['table_cell']), Paragraph('15', STYLES['table_cell']),
         Paragraph('12 (Singapore, Japan, India, China, Australia, S. Korea, etc.)', STYLES['table_cell']),
         Paragraph('Singapore', STYLES['table_cell'])],
        [Paragraph('Middle East & N. Africa', STYLES['table_cell']), Paragraph('5', STYLES['table_cell']),
         Paragraph('4 (UAE, Saudi Arabia, Morocco, Egypt)', STYLES['table_cell']),
         Paragraph('Venice (hub)', STYLES['table_cell'])],
        [Paragraph('Sub-Saharan Africa', STYLES['table_cell']), Paragraph('5', STYLES['table_cell']),
         Paragraph('3 (Rwanda, Kenya, Nigeria)', STYLES['table_cell']),
         Paragraph('Venice (hub)', STYLES['table_cell'])],
        [Paragraph('South Asia', STYLES['table_cell']), Paragraph('3', STYLES['table_cell']),
         Paragraph('2 (India, Bangladesh)', STYLES['table_cell']),
         Paragraph('Singapore (hub)', STYLES['table_cell'])],
    ]
    story.append(make_table(region_data, col_widths=[W*0.18, W*0.1, W*0.48, W*0.24]))
    doc.build(story)
    print(f"  Alliance Map: {os.path.getsize(os.path.join(OUT, 'artemis-collegium-map.pdf'))//1024}KB")


# ══════════════════════════════════════════════════════════════════
# 11. ACADEMIC PROSPECTUS (8 pages)
# ══════════════════════════════════════════════════════════════════
def gen_academic_prospectus():
    doc = ArtemisDoc(
        os.path.join(OUT, 'artemis-academic-prospectus.pdf'),
        cover_title='ACADEMIC\nPROSPECTUS',
        cover_subtitle='Programs, Curriculum, Faculty & Assessment',
        cover_img='library-reading.jpg',
        cover_tagline='MISSIONS, NOT MAJORS. TUTORIALS, NOT LECTURES.',
        title_short='Academic Prospectus'
    )
    story = []
    story.append(NextPageTemplate('content'))
    story.append(PageBreak())

    story.append(Paragraph('THE ARTEMIS ACADEMIC MODEL', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(6))
    story.append(hero_image('library-reading.jpg', height=140))
    story.append(Paragraph('The library is the intellectual heart of every College. Image: Unsplash', STYLES['caption']))
    story.append(sp(4))
    story.append(Paragraph(
        'The University of Artemis operates on a fundamentally different academic model from traditional universities. Students declare missions, not majors. Learning happens in tutorials of 7 students, not lectures of 300. Assessment is competency-based, not grade-normed. The curriculum is built on four pillars — epistemology, computational thinking, global systems, and creative expression — that provide the intellectual foundation for any mission a student might pursue. The result is a university that produces not specialists in a single discipline, but thinkers who can navigate complexity, create across boundaries, and lead in any field.', STYLES['body']))
    story.append(sp(6))

    # Four pillars
    story.append(Paragraph('THE FOUR CURRICULUM PILLARS', STYLES['h2']))
    story.append(sp(4))

    pillars_acad = [
        ('EPISTEMOLOGY', 'How do we know what we know? This pillar covers the foundations of knowledge: logic, evidence, argument, the scientific method, and the philosophy of knowledge. Every Artemis graduate can evaluate claims, construct arguments, and distinguish knowledge from opinion. Epistemology is not a subject — it is a skill that underpins every other discipline. Students study formal logic, Bayesian reasoning, research methodology, and the history of epistemological thought from Plato to the present day.'),
        ('COMPUTATIONAL THINKING', 'How do we model, simulate, and solve problems with computation? This pillar covers programming, algorithms, data structures, machine learning, and computational modelling. Every Artemis graduate can code, analyse data, and think computationally about any problem. Computational thinking is taught not as a vocational skill but as a mode of reasoning — a way of decomposing complex problems into tractable components and constructing solutions that scale.'),
        ('GLOBAL SYSTEMS', 'How do the interconnected systems of the world work? This pillar covers economics, politics, ecology, culture, and the networks that connect them. Every Artemis graduate understands the forces shaping the world and can navigate them effectively. Global Systems draws on political science, economics, sociology, anthropology, and environmental science to provide a systemic understanding of how the world actually works — not how any single discipline thinks it works.'),
        ('CREATIVE EXPRESSION', 'How do we create, communicate, and persuade? This pillar covers writing, visual communication, music, theatre, design, and the creative process. Every Artemis graduate can express ideas clearly, create compelling narratives, and appreciate the creative work of others. Creative Expression is not a luxury — it is the skill that turns knowledge into impact, that transforms analysis into action, and that gives voice to the mission each student pursues.'),
    ]
    for title, desc in pillars_acad:
        story.append(Paragraph(title, STYLES['h3']))
        story.append(Paragraph(desc, STYLES['body']))
        story.append(sp(4))

    story.append(PageBreak())

    # Programs
    story.append(Paragraph('PROGRAMS OF STUDY', STYLES['h2']))
    story.append(sp(4))
    story.append(hero_image('classroom-diverse.jpg', height=130))
    story.append(Paragraph('Diverse, global classrooms are the standard at every Artemis College. Image: Unsplash', STYLES['caption']))
    story.append(sp(4))
    story.append(Paragraph(
        'The University of Artemis offers 55 degree programs organised into 10 schools. Each program integrates the four curriculum pillars with specialised coursework in the student\'s chosen field. Programs are designed around real-world missions, not artificial disciplinary boundaries. A student in the School of Global Health might pursue the mission "eliminate malaria in Southeast Asia" while taking courses in epidemiology (computational thinking), health policy (global systems), medical ethics (epistemology), and public health communication (creative expression).', STYLES['body']))
    story.append(sp(4))

    schools = [
        'School of Epistemology & Formal Sciences',
        'School of Computational Sciences',
        'School of Global Systems & Policy',
        'School of Creative Arts & Expression',
        'School of Global Health',
        'School of Environmental Sciences',
        'School of Engineering & Applied Sciences',
        'School of Business & Social Enterprise',
        'School of Law & Governance',
        'School of Education & Pedagogy',
    ]
    for s in schools:
        story.append(Paragraph(f'<bullet>&bull;</bullet> {s}', STYLES['bullet']))
    story.append(sp(6))

    # Tutorial system
    story.append(Paragraph('THE TUTORIAL SYSTEM', STYLES['h2']))
    story.append(sp(4))
    story.append(Paragraph(
        'The tutorial system is the signature pedagogy of the University of Artemis, adapted from the Oxford and Cambridge model that has proven its effectiveness for over 800 years. In a tutorial, a faculty member meets with 7 students for 90 minutes of intensive discussion, debate, and intellectual challenge. Students must prepare written work in advance, present their arguments, defend their reasoning, and respond to criticism. There is no hiding in a tutorial. Every student must think, speak, and engage in every session. The tutorial ratio of 1:7 ensures that every student receives individual attention and that no student falls behind without being noticed.', STYLES['body']))
    story.append(Paragraph(
        'Tutorials are conducted synchronously across Colleges using the Artemis digital campus platform. A tutorial at 10am in Singapore is attended by students in Venice, San Francisco, Nairobi, and Mumbai — all in real time. The global tutorial model means that every tutorial benefits from diverse perspectives, every student experiences multiple cultural viewpoints, and every faculty member teaches a truly global classroom. The synchronous model also ensures that academic standards are identical across all Colleges: the same tutorial, the same faculty member, the same expectations, regardless of location.', STYLES['body']))
    story.append(PageBreak())

    # Assessment
    story.append(Paragraph('COMPETENCY-BASED ASSESSMENT', STYLES['h2']))
    story.append(sp(4))
    story.append(Paragraph(
        'The University of Artemis uses competency-based assessment rather than traditional letter grades. Students are evaluated on their demonstrated ability to apply knowledge, solve problems, and create original work. Each program defines a set of competencies that students must demonstrate to graduate, and students advance by demonstrating mastery, not by accumulating credit hours. This approach eliminates grade inflation, ensures that every graduate has genuine competence, and aligns assessment with the real-world skills that employers and graduate programmes value.', STYLES['body']))
    story.append(sp(4))

    assess_data = [
        [Paragraph('<b>Traditional Grading</b>', STYLES['table_header']), Paragraph('<b>Artemis Competency Model</b>', STYLES['table_header'])],
        [Paragraph('Letter grades (A-F) with no standard meaning across institutions', STYLES['table_cell']),
         Paragraph('Competency demonstrated through portfolio evidence and oral examination', STYLES['table_cell'])],
        [Paragraph('Grade inflation: average GPA has risen 0.1 per decade since 1960', STYLES['table_cell']),
         Paragraph('No inflation: competencies are absolute, not relative to peers', STYLES['table_cell'])],
        [Paragraph('Credit hours measure time spent, not learning achieved', STYLES['table_cell']),
         Paragraph('Advancement based on demonstrated mastery, not seat time', STYLES['table_cell'])],
        [Paragraph('One exam determines outcome; bad days destroy transcripts', STYLES['table_cell']),
         Paragraph('Portfolio assessment: multiple evidence points across time', STYLES['table_cell'])],
        [Paragraph('GPA is opaque to employers; class rank penalises collaboration', STYLES['table_cell']),
         Paragraph('Competency transcript shows exactly what a graduate can do', STYLES['table_cell'])],
    ]
    story.append(make_table(assess_data, col_widths=[W*0.48, W*0.52]))
    story.append(sp(8))

    # Faculty
    story.append(Paragraph('FACULTY MODEL', STYLES['h2']))
    story.append(sp(4))
    story.append(hero_image('professor-teaching.jpg', height=130))
    story.append(Paragraph('Faculty are recruited globally and rotate across Colleges. Image: Unsplash', STYLES['caption']))
    story.append(sp(4))
    story.append(Paragraph(
        'The University of Artemis recruits 2,000 faculty members globally for its launch, with a target faculty-to-student ratio of 1:7. Faculty are hired on career-level contracts with competitive compensation (averaging $90,000/year across markets) and rotate across Colleges on a 2-3 year cycle. This rotation ensures that every College benefits from diverse faculty perspectives and that faculty themselves experience the global network they serve. Faculty are recruited for both teaching excellence and active research agendas. Research time is allocated at 30% of the faculty workload, ensuring that Artemis is a research-active institution from Day 1. Faculty governance is exercised through the Academic Senate, which sets curriculum standards, degree requirements, and assessment criteria.', STYLES['body']))
    doc.build(story)
    print(f"  Academic Prospectus: {os.path.getsize(os.path.join(OUT, 'artemis-academic-prospectus.pdf'))//1024}KB")


# ══════════════════════════════════════════════════════════════════
# 12. RESEARCH PORTFOLIO (10 pages)
# ══════════════════════════════════════════════════════════════════
def gen_research_portfolio():
    doc = ArtemisDoc(
        os.path.join(OUT, 'artemis-research-portfolio.pdf'),
        cover_title='CENTERS OF\nINQUIRY',
        cover_subtitle='Research Portfolio: 19 Centers, 42 Projects, Open Knowledge',
        cover_img='microscop-science.jpg',
        cover_tagline='KNOWLEDGE IS A PUBLIC GOOD. RESEARCH IS A PUBLIC DUTY.',
        title_short='Research Portfolio'
    )
    story = []
    story.append(NextPageTemplate('content'))
    story.append(PageBreak())

    story.append(Paragraph('THE ARTEMIS RESEARCH MISSION', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(6))
    story.append(hero_image('research-lab.jpg', height=140))
    story.append(Paragraph('Research is integral to the Artemis mission, not peripheral. Image: Unsplash', STYLES['caption']))
    story.append(sp(4))
    story.append(Paragraph(
        'The University of Artemis is a research-active institution from Day 1. Research is not a peripheral activity that exists alongside teaching — it is integral to the academic model. Faculty allocate 30% of their time to research, and every student participates in a research project before graduating. The 19 Centers of Inquiry are the organisational units for research, each focused on a specific domain of inquiry and each producing open-access knowledge under the university\'s 7-year mandatory release policy. This policy ensures that all research produced at Artemis becomes publicly available within 7 years of publication, because knowledge is a public good and research is a public duty.', STYLES['body']))
    story.append(sp(6))

    story.append(Paragraph('THE 19 CENTERS OF INQUIRY', STYLES['h2']))
    story.append(sp(4))

    centers = [
        ('Center for the Ethics of Emerging Technology', 'Examines the moral dimensions of AI, biotechnology, surveillance, and other emerging technologies. Current projects include: Algorithmic Fairness in Global Hiring, The Ethics of Autonomous Weapons, and Consent Architecture in Digital Health.'),
        ('Center for the Geometry of Social Systems', 'Applies mathematical modelling to social phenomena: network effects, collective behaviour, and institutional dynamics. Current projects include: Modelling Institutional Decay, Network Topology of Social Movements, and Phase Transitions in Public Opinion.'),
        ('Center for Global Health Equity', 'Focuses on the structural determinants of health outcomes across populations. Current projects include: Malaria Elimination in Southeast Asia, Maternal Health in Sub-Saharan Africa, and Health System Resilience Under Climate Change.'),
        ('Center for Constitutional Design', 'Studies the design and durability of constitutional frameworks in diverse societies. Current projects include: Constitutional Resilience in New Democracies, Federal vs Unitary Structures in Multi-Ethnic States, and Digital Rights as Constitutional Rights.'),
        ('Center for Computational Cognition', 'Investigates the computational foundations of human cognition. Current projects include: Neural Architecture Search for Cognitive Modelling, Language Acquisition in Multilingual Environments, and Decision-Making Under Uncertainty.'),
        ('Center for Environmental Systems', 'Studies the interactions between human systems and natural environments. Current projects include: Urban Heat Island Mitigation, Carbon Capture Viability Analysis, and Biodiversity Loss in Agricultural Landscapes.'),
        ('Center for the History of Institutions', 'Examines how institutions form, persist, and transform across centuries. Current projects include: The University as Institutional Form, Corporate Governance Through the Ages, and Religious Institutions and Knowledge Production.'),
        ('Center for Migration and Mobility', 'Studies the patterns, policies, and human experiences of global migration. Current projects include: Climate Migration Projections, Integration Outcomes in Second-Generation Migrants, and Border Policy Comparative Analysis.'),
        ('Center for Financial Architecture', 'Analyses the design of financial systems and their impact on economic outcomes. Current projects include: Microfinance Impact in South Asia, Central Bank Digital Currency Design, and Financial Inclusion Through Mobile Banking.'),
        ('Center for Educational Innovation', 'Researches new approaches to teaching, learning, and assessment. Current projects include: Tutorial Effectiveness Measurement, Competency-Based Assessment Validity, and Global Rotation Learning Outcomes.'),
        ('Center for Urban Resilience', 'Studies how cities adapt to shocks and stresses. Current projects include: Flood Resilience in Delta Cities, Pandemic Response in Dense Urban Areas, and Infrastructure Resilience Under Sea-Level Rise.'),
        ('Center for the Philosophy of Knowledge', 'Investigates foundational questions about knowledge, truth, and justification. Current projects include: Epistemic Injustice in Global Contexts, The Reliability of Crowdsourced Knowledge, and Post-Truth Epistemology.'),
        ('Center for Creative Production', 'Studies the processes, economics, and impact of creative work. Current projects include: The Economics of Open-Access Publishing, AI-Assisted Creative Processes, and Cultural Production in Digital Environments.'),
        ('Center for Data Justice', 'Examines the equitable and ethical use of data in society. Current projects include: Algorithmic Bias in Criminal Justice, Data Sovereignty for Indigenous Communities, and Privacy-Preserving Analytics for Social Good.'),
        ('Center for Agricultural Systems', 'Researches sustainable and equitable food production systems. Current projects include: Regenerative Agriculture in East Africa, Vertical Farming Economic Viability, and Smallholder Market Access in South Asia.'),
        ('Center for Space and Planetary Sciences', 'Studies Earth observation, space exploration, and planetary science. Current projects include: Satellite-Based Deforestation Monitoring, Lunar Resource Mapping, and Mars Habitat Design Constraints.'),
        ('Center for Linguistic Diversity', 'Documents, preserves, and analyses the world\'s linguistic heritage. Current projects include: Endangered Language Documentation in the Amazon, Machine Translation for Low-Resource Languages, and Multilingual Education Outcomes.'),
        ('Center for Peace and Conflict Studies', 'Investigates the causes, dynamics, and resolution of armed conflicts. Current projects include: Civil War Duration Analysis, Peace Agreement Durability Factors, and Climate Change as Conflict Multiplier.'),
        ('Center for the Study of the Future', 'Develops frameworks for anticipating and shaping long-term futures. Current projects include: Scenario Planning for Global Higher Education, Existential Risk Assessment Methodology, and Intergenerational Justice in Policy Design.'),
    ]

    for i, (name, desc) in enumerate(centers):
        story.append(Paragraph(f'{i+1}. {name}', STYLES['h3']))
        story.append(Paragraph(desc, STYLES['body']))
        story.append(sp(2))

    story.append(PageBreak())

    story.append(Paragraph('THE 7-YEAR RELEASE POLICY', STYLES['h2']))
    story.append(sp(4))
    story.append(Paragraph(
        'All research produced at the University of Artemis is released under open-access terms within 7 years of publication. This policy ensures that the knowledge generated by the university — much of it funded by charitable gifts — is available to everyone, not just those with access to expensive journal subscriptions. The 7-year window allows researchers to establish priority and attract follow-on funding while ensuring that knowledge ultimately becomes a public good. The Artemis Press publishes all research outputs, including working papers, journal articles, monographs, and datasets, under Creative Commons licences that permit free redistribution and reuse with attribution.', STYLES['body']))
    doc.build(story)
    print(f"  Research Portfolio: {os.path.getsize(os.path.join(OUT, 'artemis-research-portfolio.pdf'))//1024}KB")


# ══════════════════════════════════════════════════════════════════
# 13. STRATEGIC PLAN 2025-2030 (16 pages)
# ══════════════════════════════════════════════════════════════════
def gen_strategic_plan():
    doc = ArtemisDoc(
        os.path.join(OUT, 'artemis-strategic-plan.pdf'),
        cover_title='STRATEGIC\nPLAN\n2025-2030',
        cover_subtitle='The Five-Year Roadmap for the University of Artemis',
        cover_img='hero-university.jpg',
        cover_tagline='FROM FOUNDING TO PERMANENCE.',
        title_short='Strategic Plan 2025-2030'
    )
    story = []
    story.append(NextPageTemplate('content'))
    story.append(PageBreak())

    # TOC
    story.append(Paragraph('CONTENTS', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(8))
    toc = [
        '1. Strategic Vision & Mission',
        '2. Year 1 (2025): Launch',
        '3. Year 2 (2026): Consolidation',
        '4. Year 3 (2027): Expansion',
        '5. Year 4 (2028): Maturation',
        '6. Year 5 (2029): Permanence',
        '7. Academic Strategy',
        '8. Financial Strategy',
        '9. Infrastructure Strategy',
        '10. Research Strategy',
        '11. Student Experience Strategy',
        '12. Governance & Risk',
        '13. Key Performance Indicators',
    ]
    for item in toc:
        story.append(Paragraph(item, STYLES['toc_item']))
    story.append(PageBreak())

    # Vision
    story.append(Paragraph('1. STRATEGIC VISION & MISSION', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(6))
    story.append(Paragraph(
        'The University of Artemis exists to make world-class higher education accessible to every qualified student on Earth, regardless of their financial means, geographic location, or social background. The strategic vision for 2025-2030 is to establish the university as a self-sustaining, globally distributed, research-active institution that sets the standard for accessible, high-quality higher education. By the end of Year 5, the university will serve 300,000 students across 70 Colleges in 40+ countries, generate $1.88B in annual revenue, maintain a $1.35B endowment, and produce research that shapes global policy and practice across every domain of inquiry.', STYLES['body']))
    story.append(sp(6))

    # Year by year
    years = [
        ('YEAR 1 (2025): LAUNCH', 'hero-university.jpg',
         'The first year is about execution: converting the $100M founding campaign into a fully operational university serving 100,000 students across 50 Colleges in 35 countries. The priority is getting the fundamentals right — tutorials running, faculty in place, students enrolled, and the financial engine operating. Year 1 targets include: 100,000 enrolled students, 2,000 faculty onboarded, 50 Colleges operational, $300M tuition revenue, $38M surplus, and all 19 Centers of Inquiry active with at least one project each. The risk is operational: can we open 50 Colleges simultaneously? The mitigation is standardisation — every College follows the same operational playbook, uses the same IT systems, and adheres to the same academic standards.',
         ['Enroll 100,000 students across 50 Colleges', 'Onboard 2,000 faculty', 'Launch all 19 Centers of Inquiry',
          'Achieve $300M tuition revenue', 'Generate $38M surplus', 'Establish governance bodies (Board, Senate, Visitors)']),
        ('YEAR 2 (2026): CONSOLIDATION', 'students-walking.jpg',
         'The second year is about quality: refining the tutorial system, improving student outcomes, and building the institutional culture that will define Artemis for centuries. Year 2 targets include: 150,000 students, 55 Colleges (5 new additions), $630M revenue, $150M surplus, and the first cohort of graduating students. The academic focus is on competency assessment: ensuring that the competency-based model produces measurable learning outcomes that exceed those of traditional universities. The operational focus is on efficiency: reducing the cost per student while maintaining or improving quality.',
         ['Grow to 150,000 students and 55 Colleges', 'Graduate the first cohort', 'Achieve $630M revenue',
          'Generate $150M surplus', 'Launch 5 new Colleges in underserved regions', 'Publish first annual impact report']),
        ('YEAR 3 (2027): EXPANSION', 'campus-modern.jpg',
         'The third year is about scale: expanding the college network, deepening the research portfolio, and establishing Artemis as a major global institution. Year 3 targets include: 200,000 students, 60 Colleges, $1.02B revenue, $350M surplus, and 42 active research projects across 19 Centers. The strategic focus shifts from execution to leadership: Artemis begins to set the agenda in global education policy, not just respond to it. The first Artemis Research Conference brings together scholars from all 19 Centers and establishes the university as a centre of intellectual gravity.',
         ['Reach 200,000 students and 60 Colleges', 'Host the first Artemis Research Conference', 'Achieve $1.02B revenue',
          'Generate $350M surplus', 'Endowment reaches $475M', 'Launch joint programmes with partner universities']),
        ('YEAR 4 (2028): MATURATION', 'seminar-discussion.jpg',
         'The fourth year is about depth: strengthening academic reputation, expanding research output, and building the alumni network that will sustain the university for decades. Year 4 targets include: 250,000 students, 65 Colleges, $1.4B revenue, $500M+ surplus, and the endowment crossing $850M. The alumni network, now with 3 graduating cohorts, begins to generate the professional connections and institutional loyalty that define great universities. The first Artemis alumni reunion is held simultaneously across all Central Nodes.',
         ['Reach 250,000 students and 65 Colleges', 'Endowment exceeds $850M', 'Achieve $1.4B revenue',
          'Launch the Artemis Alumni Network', 'Establish research partnerships with 10+ leading universities',
          'Begin endowment-funded scholarship programme']),
        ('YEAR 5 (2029): PERMANENCE', 'graduation-joy.jpg',
         'The fifth year marks the transition from a startup to a permanent institution. Year 5 targets include: 300,000 students, 70 Colleges, $1.88B revenue, $740M surplus, and a $1.35B endowment. The university is now one of the largest and best-endowed institutions in the world, serving more students than any single-campus university and generating enough surplus to fund its own expansion indefinitely. The strategic plan for 2030-2035 focuses on deepening quality, expanding access, and ensuring that the university\'s governance and financial structures are robust enough to survive and thrive for centuries.',
         ['Reach 300,000 students and 70 Colleges', 'Endowment reaches $1.35B', 'Achieve $1.88B revenue',
          'Self-fund all scholarships from surplus', 'Publish the 5-Year Impact Report', 'Approve the 2030-2035 Strategic Plan']),
    ]

    for title, img, desc, milestones in years:
        story.append(Paragraph(title, STYLES['h2']))
        story.append(hero_image(img, height=120))
        story.append(Paragraph(desc, STYLES['body']))
        story.append(Paragraph('Key Milestones:', STYLES['h3']))
        for m in milestones:
            story.append(Paragraph(f'<bullet>&bull;</bullet> {m}', STYLES['bullet']))
        story.append(sp(8))

    story.append(PageBreak())

    # Financial strategy
    story.append(Paragraph('8. FINANCIAL STRATEGY', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(6))
    story.append(chart_image('revenue_projection_bar.png', height=180))
    story.append(Paragraph('5-year revenue growth from $305M to $1.88B.', STYLES['caption']))
    story.append(sp(4))
    story.append(Paragraph(
        'The financial strategy is simple: grow revenue faster than costs, reinvest surplus into scholarships and endowment, and let the financial engine compound. Tuition revenue grows from $300M in Year 1 to $1.8B in Year 5, driven by enrollment growth (100K to 300K) and the addition of 20 new Colleges. Operating costs grow more slowly due to economies of scale and operational efficiency gains. The surplus grows from $38M to $740M, with 50% allocated to endowment growth, 30% to scholarship expansion, and 20% to network expansion. The endowment, seeded at $3M from the founding campaign and grown by annual surplus contributions, reaches $1.35B by Year 5 — making Artemis one of the best-endowed universities in the world within a single strategic planning period.', STYLES['body']))
    story.append(sp(4))
    story.append(chart_image('surplus_endowment_growth.png', height=170))

    story.append(PageBreak())

    # KPIs
    story.append(Paragraph('13. KEY PERFORMANCE INDICATORS', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(6))

    kpi_data = [
        [Paragraph('<b>KPI</b>', STYLES['table_header']), Paragraph('<b>Year 1</b>', STYLES['table_header']),
         Paragraph('<b>Year 3</b>', STYLES['table_header']), Paragraph('<b>Year 5</b>', STYLES['table_header'])],
        [Paragraph('Students Enrolled', STYLES['table_cell']), Paragraph('100,000', STYLES['table_cell_right']),
         Paragraph('200,000', STYLES['table_cell_right']), Paragraph('300,000', STYLES['table_cell_right'])],
        [Paragraph('Active Colleges', STYLES['table_cell']), Paragraph('50', STYLES['table_cell_right']),
         Paragraph('60', STYLES['table_cell_right']), Paragraph('70', STYLES['table_cell_right'])],
        [Paragraph('Faculty', STYLES['table_cell']), Paragraph('2,000', STYLES['table_cell_right']),
         Paragraph('4,000', STYLES['table_cell_right']), Paragraph('6,000', STYLES['table_cell_right'])],
        [Paragraph('Revenue', STYLES['table_cell']), Paragraph('$305M', STYLES['table_cell_right']),
         Paragraph('$1.02B', STYLES['table_cell_right']), Paragraph('$1.88B', STYLES['table_cell_right'])],
        [Paragraph('Annual Surplus', STYLES['table_cell']), Paragraph('$38M', STYLES['table_cell_right']),
         Paragraph('$350M', STYLES['table_cell_right']), Paragraph('$740M', STYLES['table_cell_right'])],
        [Paragraph('Endowment', STYLES['table_cell']), Paragraph('$63M', STYLES['table_cell_right']),
         Paragraph('$475M', STYLES['table_cell_right']), Paragraph('$1.35B', STYLES['table_cell_right'])],
        [Paragraph('Scholarships Funded', STYLES['table_cell']), Paragraph('10,000', STYLES['table_cell_right']),
         Paragraph('16,600', STYLES['table_cell_right']), Paragraph('23,200', STYLES['table_cell_right'])],
        [Paragraph('Research Projects', STYLES['table_cell']), Paragraph('42', STYLES['table_cell_right']),
         Paragraph('80', STYLES['table_cell_right']), Paragraph('120', STYLES['table_cell_right'])],
        [Paragraph('Countries', STYLES['table_cell']), Paragraph('35', STYLES['table_cell_right']),
         Paragraph('38', STYLES['table_cell_right']), Paragraph('42', STYLES['table_cell_right'])],
        [Paragraph('Faculty:Student Ratio', STYLES['table_cell']), Paragraph('1:7', STYLES['table_cell_right']),
         Paragraph('1:7', STYLES['table_cell_right']), Paragraph('1:7', STYLES['table_cell_right'])],
    ]
    story.append(make_table(kpi_data, col_widths=[W*0.3, W*0.23, W*0.23, W*0.24]))
    doc.build(story)
    print(f"  Strategic Plan: {os.path.getsize(os.path.join(OUT, 'artemis-strategic-plan.pdf'))//1024}KB")


# ══════════════════════════════════════════════════════════════════
# GENERATE ALL
# ══════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print("Generating 12 Artemis PDF resources...")
    gen_campaign_overview()
    gen_case_for_support()
    gen_financial_model()
    gen_tax_guide()
    gen_legal_entities()
    gen_naming_booklet()
    gen_giving_circles()
    gen_campus_plan()
    gen_alliance_map()
    gen_academic_prospectus()
    gen_research_portfolio()
    gen_strategic_plan()
    print("\nAll 12 PDFs generated successfully!")
    # List all output files
    for f in sorted(os.listdir(OUT)):
        if f.endswith('.pdf'):
            size = os.path.getsize(os.path.join(OUT, f))
            print(f"  {f}: {size//1024}KB")
