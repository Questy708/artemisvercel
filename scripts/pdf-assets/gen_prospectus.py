#!/usr/bin/env python3
"""Generate all 13 Artemis downloadable resource PDFs."""
import sys, os
sys.path.insert(0, '/home/z/my-project/scripts/pdf-assets')
from pdf_utils import *
from reportlab.platypus import Paragraph, Spacer, Image, Table, TableStyle, PageBreak, NextPageTemplate, KeepTogether
from reportlab.lib.units import mm

OUT = OUT_DIR

# ══════════════════════════════════════════════════════════════════
# 1. FOUNDING PROSPECTUS (14 pages)
# ══════════════════════════════════════════════════════════════════
def gen_founding_prospectus():
    doc = ArtemisDoc(
        os.path.join(OUT, 'artemis-founding-prospectus.pdf'),
        cover_title='FOUNDING\nPROSPECTUS',
        cover_subtitle='The University of Artemis  |  $100M Founding Campaign',
        cover_img='hero-university.jpg',
        cover_tagline='FOR CIVILIZATION  |  12 MONTHS  |  50 COLLEGES  |  100,000 STUDENTS',
        title_short='Founding Prospectus'
    )
    story = []
    # Cover page
    story.append(NextPageTemplate('content'))
    story.append(PageBreak())

    # Page 2: Table of Contents
    story.append(Paragraph('CONTENTS', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(12))
    toc_items = [
        '1. The Problem: Higher Education in Crisis',
        '2. The Vision: A New Kind of University',
        '3. The Financial Engine: Self-Sustaining from Day One',
        '4. Campaign Allocation: Where Every Dollar Goes',
        '5. The Five Pillars',
        '6. Campaign Timeline: 12 Months to Launch',
        '7. Naming Opportunities',
        '8. Giving Circles',
        '9. The Collegium Alliance',
        '10. Governance & Accountability',
        '11. Legal Structure & Tax Benefits',
        '12. The Ask',
    ]
    for item in toc_items:
        story.append(Paragraph(item, STYLES['toc_item']))
    story.append(sp(20))
    story.append(Paragraph('"The university that outlives its founders needs a corpus that outlives its donors."', STYLES['quote']))
    story.append(PageBreak())

    # Page 3: The Problem
    story.append(Paragraph('1. THE PROBLEM: HIGHER EDUCATION IN CRISIS', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(8))
    story.append(hero_image('students-africa.jpg', height=140))
    story.append(Paragraph('Students in Sub-Saharan Africa, where only 9% of college-age people are enrolled in higher education. Image: Unsplash', STYLES['caption']))
    story.append(sp(6))
    story.append(Paragraph(
        'Higher education is in crisis. Tuition has outpaced inflation by 4x since 1980. A billion people will reach university age by 2030, yet capacity has barely grown. The richest universities hoard endowments while the brightest minds in developing nations are locked out entirely. The global higher education market exceeds $2.5 trillion annually, yet it serves fewer than 220 million students.', STYLES['body']))
    story.append(Paragraph(
        'In Sub-Saharan Africa, only 9% of college-age people are enrolled. In South Asia, the figure is 25%. Meanwhile, US student debt exceeds $1.7 trillion. Employers report 40% of graduates lack workforce skills. The system is broken at both ends: too expensive for those who can access it, and inaccessible to those who cannot afford it. The existing model cannot scale to meet demand without pricing out the very students who need education most.', STYLES['body']))
    story.append(Paragraph(
        'The problem is not a lack of demand. The problem is a lack of supply at a price point that matches the economic reality of 90% of the world. Every year, millions of qualified students are turned away not because they lack ability, but because they lack the financial means to enroll. This represents not just a personal tragedy for each individual, but a civilizational loss of talent, innovation, and human potential on a scale we cannot afford to ignore.', STYLES['body']))

    # Stats row
    stats_data = [
        [Paragraph('<b>$2.5T</b>', STYLES['stat_num']), Paragraph('<b>9%</b>', STYLES['stat_num']),
         Paragraph('<b>$1.7T</b>', STYLES['stat_num']), Paragraph('<b>40%</b>', STYLES['stat_num'])],
        [Paragraph('Global HE market', STYLES['stat_label']), Paragraph('Sub-Saharan Africa enrollment', STYLES['stat_label']),
         Paragraph('US student debt', STYLES['stat_label']), Paragraph('Graduates lacking skills', STYLES['stat_label'])]
    ]
    stat_table = Table(stats_data, colWidths=[(PAGE_W - 2*MARGIN)/4]*4)
    stat_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(sp(8))
    story.append(stat_table)
    story.append(PageBreak())

    # Page 4: The Vision
    story.append(Paragraph('2. THE VISION: A NEW KIND OF UNIVERSITY', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(8))
    story.append(hero_image('campus-venice.jpg', height=150))
    story.append(Paragraph('Venice, Italy — site of the first Central Node. Image: Unsplash', STYLES['caption']))
    story.append(sp(6))
    story.append(Paragraph(
        'The University of Artemis re-engineers humanity\'s approach to learning. It operates as the Artemis Collegium — an alliance of 10 residential colleges across 6 continents, connected by a synchronous global campus. Students rotate through 6 cities over 4 years. The curriculum is built on four pillars: epistemology, computational thinking, global systems, and creative expression. Students declare missions, not majors.', STYLES['body']))
    story.append(Paragraph(
        'Artemis is not an online university. It is not a MOOC platform. It is a residential, tutorial-based, research-active university that costs $3,000 per year — accessible to 90% of qualified students worldwide. The model achieves this through three structural innovations: repurposed buildings instead of new construction (eliminating 80% of capital costs), a tutorial system with a 1:7 faculty-to-student ratio (maximising instructional quality per dollar), and a global rotation model that distributes fixed costs across 50 colleges in 35 countries.', STYLES['body']))
    story.append(Paragraph(
        'The Collegium structure means each college is independently chartered, locally embedded, and globally connected. A student in Kigali attends the same tutorial as a student in San Francisco. The synchronous campus eliminates the geographic monopoly on quality education. Faculty rotate across colleges, bringing diverse perspectives to every tutorial. Research is conducted in 19 Centers of Inquiry, each producing open-access knowledge under a 7-year mandatory release policy. This is not incremental reform. This is a new operating system for higher education.', STYLES['body']))

    # Key model stats
    story.append(sp(6))
    model_data = [
        [Paragraph('<b>Key Model Parameters</b>', STYLES['table_header']), Paragraph('', STYLES['table_header'])],
        [Paragraph('Annual Tuition', STYLES['table_cell']), Paragraph('$3,000/year', STYLES['table_cell'])],
        [Paragraph('Students Year 1', STYLES['table_cell']), Paragraph('100,000', STYLES['table_cell'])],
        [Paragraph('Colleges at Launch', STYLES['table_cell']), Paragraph('50', STYLES['table_cell'])],
        [Paragraph('Continents', STYLES['table_cell']), Paragraph('6', STYLES['table_cell'])],
        [Paragraph('Countries', STYLES['table_cell']), Paragraph('35', STYLES['table_cell'])],
        [Paragraph('Faculty-to-Student Ratio', STYLES['table_cell']), Paragraph('1:7 (tutorial model)', STYLES['table_cell'])],
        [Paragraph('Year 1 Revenue', STYLES['table_cell']), Paragraph('$300M', STYLES['table_cell'])],
        [Paragraph('Year 1 Surplus', STYLES['table_cell']), Paragraph('$38M', STYLES['table_cell'])],
        [Paragraph('Year 5 Revenue', STYLES['table_cell']), Paragraph('$1.88B', STYLES['table_cell'])],
        [Paragraph('Year 5 Endowment', STYLES['table_cell']), Paragraph('$1.35B', STYLES['table_cell'])],
    ]
    story.append(make_table(model_data, col_widths=[(PAGE_W - 2*MARGIN)*0.5, (PAGE_W - 2*MARGIN)*0.5]))
    story.append(PageBreak())

    # Page 5: Financial Engine
    story.append(Paragraph('3. THE FINANCIAL ENGINE', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(8))
    story.append(Paragraph(
        'The University of Artemis is designed to be self-sustaining from Year 1. The founding campaign of $100M is not an operating budget — it is seed capital. Once the university opens its doors, tuition revenue covers all operating costs and generates a surplus that grows the endowment, funds scholarships, and expands the college network. This is the financial engine that makes the model permanent.', STYLES['body']))
    story.append(sp(6))
    story.append(chart_image('revenue_projection_bar.png', height=190))
    story.append(Paragraph('5-year revenue projection showing tuition and other revenue streams growing from $305M to $1.88B.', STYLES['caption']))
    story.append(sp(6))
    story.append(Paragraph(
        'The key insight is scale. At 100,000 students paying $3,000/year, Year 1 revenue is $300M. Operating costs are approximately $262M (faculty compensation, operations, scholarships, and overhead). This produces a surplus of $38M in Year 1 — before any endowment distributions, before any ancillary revenue, before any cost optimisation. By Year 5, with 300,000 students across 70 colleges, revenue reaches $1.88B with a surplus exceeding $500M. The endowment, seeded at $3M from the founding campaign and grown by $60M+ per year from surplus, reaches $1.35B by Year 5.', STYLES['body']))
    story.append(sp(4))
    story.append(chart_image('surplus_endowment_growth.png', height=185))
    story.append(Paragraph('Surplus and endowment growth trajectory over the first 5 years of operation.', STYLES['caption']))
    story.append(PageBreak())

    # Page 6: Campaign Allocation
    story.append(Paragraph('4. CAMPAIGN ALLOCATION', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(8))
    story.append(Paragraph(
        'The $100M founding campaign is allocated across five pillars, each representing a critical component of the university\'s launch. The allocation reflects the reality of what it takes to go from zero to a fully operational institution serving 100,000 students in 12 months. Properties consume 82% of the budget because physical space is the rate-limiting factor: without rooms, there are no tutorials; without buildings, there are no colleges. The remaining 18% covers the bridge costs — faculty compensation before tuition flows, scholarships for the first cohort, research seed funds, and the initial endowment deposit.', STYLES['body']))
    story.append(sp(6))
    story.append(chart_image('campaign_allocation_donut.png', height=230))
    story.append(Paragraph('$100M campaign allocation by pillar. Place (82%), Minds (7%), Access (5%), Excellence (3%), Progress (3%).', STYLES['caption']))
    story.append(sp(8))

    # Pillar detail table
    pillar_data = [
        [Paragraph('<b>Pillar</b>', STYLES['table_header']), Paragraph('<b>Amount</b>', STYLES['table_header']),
         Paragraph('<b>%</b>', STYLES['table_header']), Paragraph('<b>Purpose</b>', STYLES['table_header'])],
        [Paragraph('Place (50 Colleges)', STYLES['table_cell']), Paragraph('$82M', STYLES['table_cell']),
         Paragraph('82%', STYLES['table_cell']), Paragraph('Property acquisition and repurposing across 35 countries', STYLES['table_cell'])],
        [Paragraph('Minds (Faculty)', STYLES['table_cell']), Paragraph('$7M', STYLES['table_cell']),
         Paragraph('7%', STYLES['table_cell']), Paragraph('3-month faculty compensation bridge before tuition revenue', STYLES['table_cell'])],
        [Paragraph('Access (Scholarships)', STYLES['table_cell']), Paragraph('$5M', STYLES['table_cell']),
         Paragraph('5%', STYLES['table_cell']), Paragraph('Year 1 scholarship seed for 10,000 students', STYLES['table_cell'])],
        [Paragraph('Excellence (Research)', STYLES['table_cell']), Paragraph('$3M', STYLES['table_cell']),
         Paragraph('3%', STYLES['table_cell']), Paragraph('Centers of Inquiry startup and research infrastructure', STYLES['table_cell'])],
        [Paragraph('Progress (Innovation)', STYLES['table_cell']), Paragraph('$3M', STYLES['table_cell']),
         Paragraph('3%', STYLES['table_cell']), Paragraph('Endowment seed, technology infrastructure, innovation labs', STYLES['table_cell'])],
    ]
    story.append(make_table(pillar_data, col_widths=[100, 55, 35, (PAGE_W - 2*MARGIN) - 190]))
    story.append(PageBreak())

    # Page 7: Five Pillars Detail
    story.append(Paragraph('5. THE FIVE PILLARS IN DETAIL', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(6))

    pillars = [
        ('PLACE: THE 50 COLLEGES — $82M', 'campus-modern.jpg',
         'A university without a physical place is a YouTube channel. Community requires co-location. Tutorials require rooms. We are not building campuses — we are finding existing buildings and giving them a second life as Colleges. Repurposed convents, warehouses, offices, factories. Each one acquired. Each one owned. Each one permanent. Properties are 82 cents of every dollar raised because they are the asset. Even at 50% naming uptake, the gifts cover the property costs. Named gifts are endowments — the property is the asset. Donor names a College; the College owns the building. The College generates tuition revenue from Day 1, creating a self-sustaining unit within the larger network. Each College serves between 1,100 and 2,500 students depending on its tier and location, with the three Central Nodes hosting up to 5,000 students each.'),
        ('MINDS: FACULTY LAUNCH — $7M', 'professor-teaching.jpg',
         '2,000 faculty must be hired, onboarded, and in place before students arrive. This pillar covers roughly 3 months of faculty compensation before tuition revenue flows. After Day 1, the P&L covers all faculty compensation from tuition. This is a one-time bridge, not an ongoing cost. A $5M Distinguished Professorship at 4.5% yield generates $225K/year — enough to sustain one position in perpetuity. The naming gifts are endowments; the $7M pre-launch cost is the bridge that gets us from signed contracts to tuition revenue. Faculty recruitment focuses on career-level academics with demonstrated teaching excellence and active research agendas.'),
        ('ACCESS: YEAR 1 SCHOLARSHIPS — $5M', 'scholarship-student.jpg',
         '$3,000/year is accessible to 90% of qualified students worldwide. The remaining 10% — approximately 10,000 students in Year 1 — need financial assistance. After Year 1, the $262M annual surplus funds 13,300 scholarships per year at $3,000 each. This $5M bridges the first cohort. Your seed gift does not run a programme — it launches a permanent scholarship machine. After Year 1, the surplus self-funds scholarships at $40M/year and growing. The scholarship programme is not charity — it is an investment in talent that pays dividends in research output, alumni networks, and institutional reputation.'),
        ('EXCELLENCE: RESEARCH & INQUIRY — $3M', 'research-lab.jpg',
         'Research seed funds, visiting fellowships, the Artemis Press, Centers of Inquiry. The mechanisms that turn a good university into an inevitable one. 19 Centers of Inquiry and 42 Active Projects need startup capital: research equipment, fieldwork budgets, database subscriptions, publication subsidies, and the open knowledge infrastructure that powers the 7-year release. After Year 1, faculty time (already compensated) covers most ongoing project work. This $3M is the seed that makes every Center operational from Day 1, establishing Artemis as a research-active institution from the moment it opens.'),
        ('PROGRESS: INNOVATION & INFRASTRUCTURE — $3M', 'innovation-tech.jpg',
         'Innovation labs, the Global Challenge Fund, technology infrastructure, and the seed endowment. The university that outlives its founders needs a corpus that outlives its donors. After Year 1, the surplus builds the endowment at $60M/year. But the first deposit comes from the founding campaign. $3M at 4.5% = $135K/year in perpetuity from Day 1 — enough to fund 11 full scholarships forever, before any surplus is generated. Founders\' Circle gifts are cumulative across all pillars, meaning the founding campaign\'s impact compounds across every dimension of the university.'),
    ]

    for title, img, desc in pillars:
        story.append(Paragraph(title, STYLES['h3']))
        story.append(hero_image(img, height=110))
        story.append(Paragraph(desc, STYLES['body']))
        story.append(sp(6))

    story.append(PageBreak())

    # Page 8-9: Timeline
    story.append(Paragraph('6. CAMPAIGN TIMELINE: 12 MONTHS TO LAUNCH', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(8))
    story.append(chart_image('timeline_gantt.png', height=160))
    story.append(Paragraph('The 12-month campaign timeline from quiet phase to university launch.', STYLES['caption']))
    story.append(sp(8))

    phases = [
        ('THE QUIET PHASE — Months 1-3 — Target: $50M',
         'No public announcement. No website. No press. The quiet phase secures lead gifts before the world knows we exist. This is standard practice — Yale secured $3.5B before announcing "For Humanity." Harvard, Stanford, and every major university campaign begins with a quiet phase. The purpose is simple: lead donors want to know they are part of something real before the public arrives. The quiet phase gives us time to cultivate relationships, refine the case, and secure the anchor commitments that make the public phase credible.',
         ['Lead donor cultivation and solicitation across 10 primary prospects',
          '$50M in binding commitments secured from Founders\' and Guardians\' Circle donors',
          'Campaign cabinet fully operational with regional chairs in 6 continents',
          'Legal entity established in Delaware; fiscal sponsorship activated']),
        ('THE PUBLIC PHASE — Months 4-6 — Target: $85M',
         'The campaign goes public. Website launches. Events held. Press engaged. The full case statement reaches every major prospect worldwide. Regional events in 35 countries simultaneously announce the campaign. The public phase is designed to create momentum — each new commitment inspires the next. The case statement, the prospectus you are reading now, becomes the primary tool for major gift officers and volunteer solicitors around the world.',
         ['Public website and all campaign materials live in 12 languages',
          'Regional launch events across all 35 countries',
          '$85M cumulative commitments — 85% of the campaign goal secured',
          'Media coverage in major global outlets']),
        ('CLOSE & CAPITALISE — Months 7-9 — Target: $100M',
         'All $100M commitments secured. Properties acquired. Legal incorporation across 25 jurisdictions. The foundation is poured. This phase is about execution: converting pledges to payments, closing on properties, filing incorporation documents, and beginning the physical transformation of buildings into Colleges. Every property is acquired, not leased — permanent ownership is non-negotiable.',
         ['All $100M commitments secured and documented',
          'Properties acquired and repurposing begun in 35 locations',
          'Legal incorporation across 25 countries completed',
          'Faculty recruitment pipeline at 2,000 committed hires']),
        ('BUILD & LAUNCH — Months 10-12 — Target: $100M (Operational)',
         'Faculty onboarded. Colleges opened. Students arriving. The university becomes operational. The match lights the fuel. This is not a soft launch or a pilot — it is a full-scale opening with 100,000 students, 2,000 faculty, and 50 Colleges across 6 continents. The founding campaign\'s $100M has been converted into permanent physical infrastructure, operational systems, and a self-sustaining financial engine.',
         ['Faculty onboarded and in place at all 50 Colleges',
          'Colleges opened, operational, and welcoming students',
          'Students arriving — the University of Artemis is live',
          'First tutorials conducted, first research projects initiated']),
    ]

    for title, desc, deliverables in phases:
        story.append(Paragraph(title, STYLES['h3']))
        story.append(Paragraph(desc, STYLES['body']))
        for d in deliverables:
            story.append(Paragraph(f'<bullet>&bull;</bullet> {d}', STYLES['bullet']))
        story.append(sp(8))

    story.append(PageBreak())

    # Page 10: Naming Opportunities
    story.append(Paragraph('7. NAMING OPPORTUNITIES', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(8))
    story.append(Paragraph(
        'Every naming opportunity at the University of Artemis is permanent. Your name does not grace a building for 20 years — it becomes part of the institution\'s foundation for as long as the university exists. Named gifts are endowments: the asset (property, position, program) generates value in perpetuity, and your name is inseparable from that value. Below is the complete catalogue of naming opportunities, from the apex — a Central Node — to the most direct: a student scholarship.', STYLES['body']))
    story.append(sp(6))
    story.append(chart_image('naming_opportunities_bar.png', height=180))
    story.append(Paragraph('Naming opportunities by tier and amount.', STYLES['caption']))
    story.append(sp(6))

    naming_data = [
        [Paragraph('<b>Opportunity</b>', STYLES['table_header']), Paragraph('<b>Amount</b>', STYLES['table_header']),
         Paragraph('<b>Description</b>', STYLES['table_header'])],
        [Paragraph('Central Node', STYLES['table_cell']), Paragraph('$25M', STYLES['table_cell_right']),
         Paragraph('Name one of 3 Central Nodes (Venice, San Francisco, Singapore). ~5,000 students. The apex of the network.', STYLES['table_cell'])],
        [Paragraph('Tier A College', STYLES['table_cell']), Paragraph('$10M', STYLES['table_cell_right']),
         Paragraph('Name a flagship College in a global knowledge capital. ~2,500 students.', STYLES['table_cell'])],
        [Paragraph('Center of Inquiry', STYLES['table_cell']), Paragraph('$10M', STYLES['table_cell_right']),
         Paragraph('Name one of 19 permanently endowed research centres.', STYLES['table_cell'])],
        [Paragraph('Tier B College', STYLES['table_cell']), Paragraph('$5M', STYLES['table_cell_right']),
         Paragraph('Name a College in a major global city. ~2,000 students.', STYLES['table_cell'])],
        [Paragraph('Distinguished Prof.', STYLES['table_cell']), Paragraph('$5M', STYLES['table_cell_right']),
         Paragraph('Endow a faculty position in perpetuity at 4.5% yield ($225K/yr).', STYLES['table_cell'])],
        [Paragraph('Degree Program', STYLES['table_cell']), Paragraph('$3M', STYLES['table_cell_right']),
         Paragraph('Name one of 55 degree programs. Your name with every graduate.', STYLES['table_cell'])],
        [Paragraph('Tier C College', STYLES['table_cell']), Paragraph('$2M', STYLES['table_cell_right']),
         Paragraph('Name a College in cities like Kigali, Dhaka, Kampala. ~1,100 students.', STYLES['table_cell'])],
        [Paragraph('Scholarship Fund', STYLES['table_cell']), Paragraph('$12K', STYLES['table_cell_right']),
         Paragraph('Fund one student\'s full 4-year scholarship. The most direct impact.', STYLES['table_cell'])],
    ]
    story.append(make_table(naming_data, col_widths=[95, 55, (PAGE_W - 2*MARGIN) - 150]))
    story.append(PageBreak())

    # Page 11: Giving Circles
    story.append(Paragraph('8. GIVING CIRCLES', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(8))
    story.append(chart_image('giving_circles_bar.png', height=170))
    story.append(Paragraph('Giving circles by minimum gift threshold (log scale).', STYLES['caption']))
    story.append(sp(6))

    circles = [
        ("The Founders' Circle — $10M+",
         ['Name engraved on the university\'s founding document at Venice Central Node',
          'Permanent seat on Board of Visitors',
          'Private annual dinner with the President at rotating Central Node',
          'Named endowment fund or equivalent naming opportunity',
          'Recognition plaque at all 50 Colleges',
          'Biographical feature in annual campaign report']),
        ("The Guardians' Circle — $5M - $9.9M",
         ['Named College or Center of Inquiry',
          'Recognition plaque at all 50 Colleges',
          'Annual Guardian\'s Lecture — a public lecture series named by you',
          'Annual private briefing with the President',
          'Named endowment fund']),
        ("The Builders' Circle — $1M - $4.9M",
         ['Named Professorship, Scholarship Fund, or major program',
          'Recognition plaque at all 50 Colleges',
          'Annual Builder\'s Report — detailed impact report on your named gift',
          'Invitation to annual gathering',
          'Feature in campaign newsletter']),
        ("The Fellows' Circle — $100K - $999K",
         ['Named scholarship fund or tutorial room at chosen College',
          'Recognition at chosen College',
          'Annual Fellow\'s Newsletter from the President',
          'Invitation to regional events']),
        ("Friends of Artemis — $10K - $99K",
         ['Name in founding Donor Roll (permanent digital and print record)',
          'Digital certificate of founding support',
          'Quarterly progress updates',
          'Invitation to online events']),
        ("The 99 — $99",
         ['Waitlist priority for enrollment',
          'Digital recognition on community wall',
          'Monthly community updates',
          'The knowledge that you were first in line']),
    ]
    for circle_name, benefits in circles:
        story.append(Paragraph(circle_name, STYLES['h3']))
        for b in benefits:
            story.append(Paragraph(f'<bullet>&bull;</bullet> {b}', STYLES['bullet']))
        story.append(sp(4))

    story.append(PageBreak())

    # Page 12: Collegium Alliance
    story.append(Paragraph('9. THE COLLEGIUM ALLIANCE', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(8))
    story.append(hero_image('globe-global.jpg', height=140))
    story.append(Paragraph('The Artemis Collegium spans 6 continents, 35 countries, and 50 Colleges at launch. Image: Unsplash', STYLES['caption']))
    story.append(sp(6))
    story.append(Paragraph(
        'The Artemis Collegium is the alliance structure that connects all 50 Colleges into a single, synchronous global campus. Unlike a franchise model or a consortium of independent institutions, the Collegium operates as one university with multiple physical locations. Students are enrolled at the University of Artemis, not at a specific College. They rotate through Colleges during their 4-year program, experiencing 6 different cities and cultural contexts while maintaining academic continuity through the shared curriculum and tutorial system.', STYLES['body']))
    story.append(Paragraph(
        'Each College is led by a Dean and governed by a local advisory board, ensuring cultural responsiveness and community engagement. Academic standards, faculty qualifications, and degree requirements are set centrally by the Academic Senate, guaranteeing that a degree from Artemis means the same thing regardless of where a student completed their tutorials. The three Central Nodes — Venice, San Francisco, and Singapore — serve as the administrative, research, and cultural hubs of the network, hosting the largest student populations and the most advanced research facilities.', STYLES['body']))

    # Central nodes table
    nodes_data = [
        [Paragraph('<b>Central Node</b>', STYLES['table_header']), Paragraph('<b>Students</b>', STYLES['table_header']),
         Paragraph('<b>Role</b>', STYLES['table_header']), Paragraph('<b>Regional Focus</b>', STYLES['table_header'])],
        [Paragraph('Venice, Italy', STYLES['table_cell']), Paragraph('~5,000', STYLES['table_cell']),
         Paragraph('European hub; governance headquarters; founding document location', STYLES['table_cell']),
         Paragraph('Europe, Middle East, Africa', STYLES['table_cell'])],
        [Paragraph('San Francisco, USA', STYLES['table_cell']), Paragraph('~5,000', STYLES['table_cell']),
         Paragraph('Americas hub; innovation centre; technology infrastructure', STYLES['table_cell']),
         Paragraph('North America, South America', STYLES['table_cell'])],
        [Paragraph('Singapore', STYLES['table_cell']), Paragraph('~5,000', STYLES['table_cell']),
         Paragraph('Asia-Pacific hub; research gateway; admissions centre', STYLES['table_cell']),
         Paragraph('East Asia, South Asia, Oceania', STYLES['table_cell'])],
    ]
    story.append(sp(8))
    story.append(make_table(nodes_data, col_widths=[90, 60, 180, 140]))
    story.append(PageBreak())

    # Page 13: Governance & Accountability
    story.append(Paragraph('10. GOVERNANCE & ACCOUNTABILITY', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(8))
    story.append(Paragraph(
        'The University of Artemis is structured to ensure no single individual can control the institution. Governance is distributed across three bodies: the Board of Trustees (financial and legal oversight), the Academic Senate (academic standards and curriculum), and the Board of Visitors (donor and alumni advisory). No individual controls more than one-third of Board of Trustees seats, and a majority of trustees must be independent — defined as having no financial relationship with the university beyond their board service.', STYLES['body']))

    account_data = [
        [Paragraph('<b>Guarantee</b>', STYLES['table_header']), Paragraph('<b>Commitment</b>', STYLES['table_header'])],
        [Paragraph('Board Independence', STYLES['table_cell']), Paragraph('No single individual controls more than one-third of board seats. Majority independent directors required.', STYLES['table_cell'])],
        [Paragraph('Annual Audit', STYLES['table_cell']), Paragraph('Full independent audit by a Big Four firm. Published annually. No exceptions. Every dollar tracked and reported.', STYLES['table_cell'])],
        [Paragraph('Public Reporting', STYLES['table_cell']), Paragraph('Every dollar received and disbursed is published in an annual impact report, available to every donor and the public.', STYLES['table_cell'])],
        [Paragraph('Donor Transparency', STYLES['table_cell']), Paragraph('All gifts above $10,000 are listed by name (unless anonymous requested) in the annual report. Gift restrictions are honoured in perpetuity.', STYLES['table_cell'])],
        [Paragraph('Open Knowledge', STYLES['table_cell']), Paragraph('All research produced at Artemis is released under open-access terms within 7 years of publication. Knowledge is a public good.', STYLES['table_cell'])],
    ]
    story.append(sp(6))
    story.append(make_table(account_data, col_widths=[120, (PAGE_W - 2*MARGIN) - 120]))

    # Legal Structure
    story.append(sp(14))
    story.append(Paragraph('11. LEGAL STRUCTURE & TAX BENEFITS', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(8))
    story.append(hero_image('law-justice.jpg', height=120))
    story.append(Paragraph('Legal structure across three jurisdictions ensures global tax deductibility. Image: Unsplash', STYLES['caption']))
    story.append(sp(4))

    legal_data = [
        [Paragraph('<b>Jurisdiction</b>', STYLES['table_header']), Paragraph('<b>Entity</b>', STYLES['table_header']),
         Paragraph('<b>Classification</b>', STYLES['table_header']), Paragraph('<b>Key Benefit</b>', STYLES['table_header'])],
        [Paragraph('United States', STYLES['table_cell']), Paragraph('Delaware Non-Stock Corp', STYLES['table_cell']),
         Paragraph('501(c)(3)', STYLES['table_cell']), Paragraph('Tax-deductible donations; world\'s largest philanthropy market ($499B)', STYLES['table_cell'])],
        [Paragraph('England & Wales', STYLES['table_cell']), Paragraph('CIO', STYLES['table_cell']),
         Paragraph('Charity Commission', STYLES['table_cell']), Paragraph('Gift Aid: 25% government top-up on donations', STYLES['table_cell'])],
        [Paragraph('Switzerland', STYLES['table_cell']), Paragraph('Fondation', STYLES['table_cell']),
         Paragraph('Geneva Canton', STYLES['table_cell']), Paragraph('Neutral jurisdiction; no capital gains tax on endowment', STYLES['table_cell'])],
    ]
    story.append(make_table(legal_data, col_widths=[80, 110, 90, (PAGE_W - 2*MARGIN) - 280]))
    story.append(PageBreak())

    # Page 14: The Ask
    story.append(Paragraph('12. THE ASK', STYLES['h1']))
    story.append(section_divider())
    story.append(sp(8))
    story.append(hero_image('graduation-joy.jpg', height=150))
    story.append(Paragraph('Every great university starts with a first believer. Image: Unsplash', STYLES['caption']))
    story.append(sp(6))
    story.append(Paragraph(
        'The University of Artemis is asking for $100M in 12 months. Not to build a campus. Not to fund a decade of operations. But to acquire the permanent physical infrastructure that makes a self-sustaining university possible. After launch, the financial engine takes over: tuition covers all costs, generates a growing surplus, funds scholarships, builds the endowment, and expands the college network. The $100M is the seed. The institution is the harvest.', STYLES['body']))
    story.append(Paragraph(
        '70% of the campaign will come from 10 lead donors. This is how founding campaigns work. Yale\'s $7B campaign was led by 12 donors who gave 60% of the total. Harvard\'s $9B campaign followed the same pattern. We are not asking for small donations to fund operations. We are asking for transformative gifts to create permanent infrastructure. Each naming opportunity is an endowment — the asset generates value in perpetuity, and the donor\'s name is inseparable from that value.', STYLES['body']))
    story.append(sp(6))
    story.append(chart_image('donor_segments_pie.png', height=200))
    story.append(Paragraph('Donor segments: $100M campaign by source.', STYLES['caption']))
    story.append(sp(8))

    story.append(Paragraph(
        '<b>Contact:</b>  donate@artemisui.org  |  www.artemisui.org  |  University of Artemis, c/o Delaware Non-Stock Corporation', STYLES['body_center']))
    story.append(sp(6))
    story.append(Paragraph(
        '"For Civilization."', STYLES['quote']))

    doc.build(story)
    print(f"  Founding Prospectus generated: {os.path.getsize(os.path.join(OUT, 'artemis-founding-prospectus.pdf'))//1024}KB")


if __name__ == '__main__':
    gen_founding_prospectus()
