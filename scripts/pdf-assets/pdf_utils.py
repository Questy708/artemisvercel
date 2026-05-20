"""
Shared utilities for Artemis PDF generation.
All 13 PDFs share a common visual language: crimson accents, clean white space,
professional typography, and consistent branding.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, inch, cm
from reportlab.lib.colors import HexColor, white, black, Color
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable, Frame, PageTemplate, BaseDocTemplate,
    NextPageTemplate
)
from reportlab.platypus.flowables import Flowable
from reportlab.pdfgen import canvas
from reportlab.lib.validators import Auto
from PIL import Image as PILImage
import os

# ─── Colors ───
CRIMSON = HexColor('#8A0000')
DARK_CRIMSON = HexColor('#6B0000')
LIGHT_CRIMSON = HexColor('#f5e6e6')
GOLD = HexColor('#c9a84c')
CHARCOAL = HexColor('#2d2d2d')
SLATE = HexColor('#475569')
LIGHT_GRAY = HexColor('#f8f9fa')
MID_GRAY = HexColor('#6b7280')
BORDER_GRAY = HexColor('#e2e8f0')
TEAL = HexColor('#0e7490')
NAVY = HexColor('#1a1a2e')
WHITE = white

PAGE_W, PAGE_H = A4
MARGIN = 18*mm

# ─── Font paths ───
FONT_DIR = '/usr/share/fonts/truetype'
SERIF = os.path.join(FONT_DIR, 'liberation/LiberationSerif-Regular.ttf')
SERIF_BOLD = os.path.join(FONT_DIR, 'liberation/LiberationSerif-Bold.ttf')
SERIF_ITALIC = os.path.join(FONT_DIR, 'liberation/LiberationSerif-Italic.ttf')
SERIF_BOLD_ITALIC = os.path.join(FONT_DIR, 'liberation/LiberationSerif-BoldItalic.ttf')
SANS = os.path.join(FONT_DIR, 'english/Carlito-Regular.ttf')
SANS_BOLD = os.path.join(FONT_DIR, 'english/Carlito-Bold.ttf')
SANS_ITALIC = os.path.join(FONT_DIR, 'english/Carlito-Italic.ttf')
SANS_BOLD_ITALIC = os.path.join(FONT_DIR, 'english/Carlito-BoldItalic.ttf')

# Register fonts
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def register_fonts():
    pdfmetrics.registerFont(TTFont('Tinos', SERIF))
    pdfmetrics.registerFont(TTFont('Tinos-Bold', SERIF_BOLD))
    pdfmetrics.registerFont(TTFont('Tinos-Italic', SERIF_ITALIC))
    pdfmetrics.registerFont(TTFont('Tinos-BoldItalic', SERIF_BOLD_ITALIC))
    pdfmetrics.registerFont(TTFont('Carlito', SANS))
    pdfmetrics.registerFont(TTFont('Carlito-Bold', SANS_BOLD))
    pdfmetrics.registerFont(TTFont('Carlito-Italic', SANS_ITALIC))
    pdfmetrics.registerFont(TTFont('Carlito-BoldItalic', SANS_BOLD_ITALIC))
    pdfmetrics.registerFontFamily('Tinos', normal='Tinos', bold='Tinos-Bold',
                                   italic='Tinos-Italic', boldItalic='Tinos-BoldItalic')
    pdfmetrics.registerFontFamily('Carlito', normal='Carlito', bold='Carlito-Bold',
                                   italic='Carlito-Italic', boldItalic='Carlito-BoldItalic')

register_fonts()

# ─── Paths ───
IMG_DIR = '/home/z/my-project/scripts/pdf-assets/images'
CHART_DIR = '/home/z/my-project/scripts/pdf-assets/charts'
OUT_DIR = '/home/z/my-project/public/resources'

# ─── Styles ───
def make_styles():
    s = {}
    s['cover_title'] = ParagraphStyle('cover_title', fontName='Carlito-Bold', fontSize=36,
        leading=42, textColor=WHITE, alignment=TA_LEFT, spaceAfter=8)
    s['cover_subtitle'] = ParagraphStyle('cover_subtitle', fontName='Carlito', fontSize=16,
        leading=22, textColor=HexColor('#ffffffcc'), alignment=TA_LEFT, spaceAfter=6)
    s['cover_tag'] = ParagraphStyle('cover_tag', fontName='Carlito-Bold', fontSize=11,
        leading=14, textColor=CRIMSON, alignment=TA_LEFT, spaceBefore=0, spaceAfter=12)
    s['h1'] = ParagraphStyle('h1', fontName='Carlito-Bold', fontSize=24, leading=30,
        textColor=CRIMSON, spaceAfter=10, spaceBefore=20)
    s['h2'] = ParagraphStyle('h2', fontName='Carlito-Bold', fontSize=18, leading=24,
        textColor=CHARCOAL, spaceAfter=8, spaceBefore=14)
    s['h3'] = ParagraphStyle('h3', fontName='Carlito-Bold', fontSize=14, leading=18,
        textColor=CRIMSON, spaceAfter=6, spaceBefore=10)
    s['body'] = ParagraphStyle('body', fontName='Tinos', fontSize=10.5, leading=16,
        textColor=CHARCOAL, alignment=TA_JUSTIFY, spaceAfter=8)
    s['body_center'] = ParagraphStyle('body_center', fontName='Tinos', fontSize=10.5, leading=16,
        textColor=CHARCOAL, alignment=TA_CENTER, spaceAfter=8)
    s['body_small'] = ParagraphStyle('body_small', fontName='Tinos', fontSize=9, leading=13,
        textColor=SLATE, alignment=TA_JUSTIFY, spaceAfter=6)
    s['caption'] = ParagraphStyle('caption', fontName='Carlito-Italic', fontSize=8.5, leading=12,
        textColor=MID_GRAY, alignment=TA_CENTER, spaceAfter=10)
    s['stat_num'] = ParagraphStyle('stat_num', fontName='Carlito-Bold', fontSize=32, leading=38,
        textColor=CRIMSON, alignment=TA_CENTER)
    s['stat_label'] = ParagraphStyle('stat_label', fontName='Carlito', fontSize=9, leading=12,
        textColor=SLATE, alignment=TA_CENTER)
    s['quote'] = ParagraphStyle('quote', fontName='Tinos-Italic', fontSize=12, leading=18,
        textColor=SLATE, alignment=TA_CENTER, leftIndent=30, rightIndent=30, spaceAfter=12, spaceBefore=8)
    s['bullet'] = ParagraphStyle('bullet', fontName='Tinos', fontSize=10.5, leading=16,
        textColor=CHARCOAL, alignment=TA_LEFT, leftIndent=18, bulletIndent=6,
        spaceAfter=4)
    s['footer'] = ParagraphStyle('footer', fontName='Carlito', fontSize=7.5, leading=10,
        textColor=MID_GRAY, alignment=TA_CENTER)
    s['table_header'] = ParagraphStyle('table_header', fontName='Carlito-Bold', fontSize=9,
        leading=12, textColor=WHITE, alignment=TA_LEFT)
    s['table_cell'] = ParagraphStyle('table_cell', fontName='Tinos', fontSize=9.5,
        leading=13, textColor=CHARCOAL, alignment=TA_LEFT)
    s['table_cell_right'] = ParagraphStyle('table_cell_right', fontName='Tinos', fontSize=9.5,
        leading=13, textColor=CHARCOAL, alignment=TA_RIGHT)
    s['toc_item'] = ParagraphStyle('toc_item', fontName='Tinos', fontSize=11, leading=20,
        textColor=CHARCOAL, alignment=TA_LEFT, leftIndent=10)
    return s

STYLES = make_styles()

# ─── Custom Flowables ───
class ColorBar(Flowable):
    """Full-width colored bar."""
    def __init__(self, color=CRIMSON, height=4):
        Flowable.__init__(self)
        self.color = color
        self.bar_height = height
    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        return (self.width, self.bar_height)
    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, self.width, self.bar_height, fill=1, stroke=0)

class StatBox(Flowable):
    """Stat with large number and label beneath."""
    def __init__(self, number, label, width=120, color=CRIMSON):
        Flowable.__init__(self)
        self.number = number
        self.label = label
        self.box_width = width
        self.color = color
    def wrap(self, availWidth, availHeight):
        return (self.box_width, 60)
    def draw(self):
        c = self.canv
        c.setFont('Carlito-Bold', 28)
        c.setFillColor(self.color)
        c.drawCentredString(self.box_width/2, 30, self.number)
        c.setFont('Carlito', 8)
        c.setFillColor(SLATE)
        c.drawCentredString(self.box_width/2, 12, self.label)

class ImageWithOverlay(Flowable):
    """Image with a dark gradient overlay at the bottom for text readability."""
    def __init__(self, img_path, width, height, overlay_height=60):
        Flowable.__init__(self)
        self.img_path = img_path
        self.img_width = width
        self.img_height = height
        self.overlay_height = overlay_height
    def wrap(self, availWidth, availHeight):
        return (self.img_width, self.img_height)
    def draw(self):
        c = self.canv
        c.drawImage(self.img_path, 0, 0, width=self.img_width, height=self.img_height,
                    preserveAspectRatio=True, anchor='c')
        # Gradient overlay at bottom
        steps = 10
        for i in range(steps):
            alpha = 0.7 * (i / steps)
            c.setFillColor(Color(0, 0, 0, alpha))
            y = self.overlay_height * (1 - i/steps)
            c.rect(0, 0, self.img_width, y, fill=1, stroke=0)


# ─── Helpers ───
def get_img(name):
    return os.path.join(IMG_DIR, name)

def get_chart(name):
    return os.path.join(CHART_DIR, name)

def hero_image(img_name, width=None, height=160):
    """Create a full-width hero image flowable."""
    path = get_img(img_name)
    if not os.path.exists(path):
        return Spacer(1, 10)
    w = width or (PAGE_W - 2*MARGIN)
    # Calculate aspect-ratio-preserved dimensions
    from PIL import Image as PILImage
    pil = PILImage.open(path)
    img_w, img_h = pil.size
    ratio = min(w / img_w, height / img_h)
    final_w = img_w * ratio
    final_h = img_h * ratio
    return Image(path, width=final_w, height=final_h)

def chart_image(chart_name, width=None, height=200):
    """Create a chart image flowable."""
    path = get_chart(chart_name)
    if not os.path.exists(path):
        return Spacer(1, 10)
    w = width or (PAGE_W - 2*MARGIN)
    from PIL import Image as PILImage
    pil = PILImage.open(path)
    img_w, img_h = pil.size
    ratio = min(w / img_w, height / img_h)
    final_w = img_w * ratio
    final_h = img_h * ratio
    return Image(path, width=final_w, height=final_h)

def section_divider():
    return ColorBar(CRIMSON, 2)

def sp(h=8):
    return Spacer(1, h)

def make_table(data, col_widths=None, header=True):
    """Create a styled table with optional header row."""
    t = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    style_cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), CRIMSON),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Carlito-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTNAME', (0, 1), (-1, -1), 'Tinos'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('LEADING', (0, 0), (-1, -1), 13),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_GRAY),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_GRAY]),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]
    t.setStyle(TableStyle(style_cmds))
    return t

def footer_text(text='University of Artemis  |  www.artemisui.org  |  donate@artemisui.org'):
    return Paragraph(text, STYLES['footer'])

def build_cover(canvas_obj, doc, title, subtitle, img_name, tagline=None):
    """Draw a full-bleed cover page with image background."""
    c = canvas_obj
    c.saveState()
    # Full-bleed image
    img_path = get_img(img_name)
    if os.path.exists(img_path):
        c.drawImage(img_path, 0, 0, width=PAGE_W, height=PAGE_H,
                    preserveAspectRatio=True, anchor='c')
    # Dark overlay
    steps = 20
    for i in range(steps):
        alpha = 0.75 * (i / steps)
        c.setFillColor(Color(0, 0, 0, alpha))
        y = PAGE_H * (1 - i/steps)
        c.rect(0, y - PAGE_H/steps, PAGE_W, PAGE_H/steps, fill=1, stroke=0)
    # Crimson accent line
    c.setStrokeColor(CRIMSON)
    c.setLineWidth(3)
    c.line(MARGIN, PAGE_H - 120, MARGIN + 60, PAGE_H - 120)
    # Title
    c.setFont('Carlito-Bold', 34)
    c.setFillColor(WHITE)
    y_title = PAGE_H - 160
    for line in title.split('\n'):
        c.drawString(MARGIN, y_title, line)
        y_title -= 42
    # Subtitle
    c.setFont('Carlito', 15)
    c.setFillColor(HexColor('#ffffffcc'))
    c.drawString(MARGIN, y_title - 10, subtitle)
    # Tagline
    if tagline:
        c.setFont('Carlito-Bold', 10)
        c.setFillColor(CRIMSON)
        c.drawString(MARGIN, y_title - 40, tagline)
    # Bottom bar
    c.setFillColor(CRIMSON)
    c.rect(0, 0, PAGE_W, 30, fill=1, stroke=0)
    c.setFont('Carlito', 8)
    c.setFillColor(WHITE)
    c.drawCentredString(PAGE_W/2, 10, 'www.artemisui.org  |  donate@artemisui.org')
    c.restoreState()

def standard_page(canvas_obj, doc, title_short='University of Artemis'):
    """Standard page template with header/footer."""
    c = canvas_obj
    c.saveState()
    # Header line
    c.setStrokeColor(BORDER_GRAY)
    c.setLineWidth(0.5)
    c.line(MARGIN, PAGE_H - 14*mm, PAGE_W - MARGIN, PAGE_H - 14*mm)
    # Header text
    c.setFont('Carlito', 7.5)
    c.setFillColor(MID_GRAY)
    c.drawString(MARGIN, PAGE_H - 12*mm, title_short)
    c.drawRightString(PAGE_W - MARGIN, PAGE_H - 12*mm, 'University of Artemis')
    # Footer
    c.setStrokeColor(BORDER_GRAY)
    c.line(MARGIN, 14*mm, PAGE_W - MARGIN, 14*mm)
    c.setFont('Carlito', 7)
    c.setFillColor(MID_GRAY)
    c.drawCentredString(PAGE_W/2, 9*mm, f'www.artemisui.org  |  Page {doc.page}')
    # Crimson accent at top
    c.setFillColor(CRIMSON)
    c.rect(0, PAGE_H - 3, PAGE_W, 3, fill=1, stroke=0)
    c.restoreState()


class ArtemisDoc(BaseDocTemplate):
    """Custom document template with cover + standard pages."""
    def __init__(self, filename, cover_title='', cover_subtitle='', cover_img='hero-university.jpg',
                 cover_tagline=None, title_short='University of Artemis', **kw):
        self.cover_title = cover_title
        self.cover_subtitle = cover_subtitle
        self.cover_img = cover_img
        self.cover_tagline = cover_tagline
        self.title_short = title_short
        BaseDocTemplate.__init__(self, filename, pagesize=A4,
            leftMargin=MARGIN, rightMargin=MARGIN,
            topMargin=20*mm, bottomMargin=20*mm, **kw)
        # Cover frame (full page)
        cover_frame = Frame(MARGIN, 20*mm, PAGE_W - 2*MARGIN, PAGE_H - 40*mm,
                           id='cover')
        # Content frame
        content_frame = Frame(MARGIN, 20*mm, PAGE_W - 2*MARGIN, PAGE_H - 40*mm,
                             id='content')
        cover_template = PageTemplate(id='cover', frames=[cover_frame],
            onPage=lambda c, d: build_cover(c, d, self.cover_title,
                self.cover_subtitle, self.cover_img, self.cover_tagline))
        content_template = PageTemplate(id='content', frames=[content_frame],
            onPage=lambda c, d: standard_page(c, d, self.title_short))
        self.addPageTemplates([cover_template, content_template])

    def afterFlowable(self, flowable):
        pass
