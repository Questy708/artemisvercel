import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

fm.fontManager.addfont('/usr/share/fonts/truetype/chinese/SarasaMonoSC-Regular.ttf')
fm.fontManager.addfont('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Sarasa Mono SC']
plt.rcParams['axes.unicode_minus'] = False

CRIMSON = '#8A0000'
DARK_CRIMSON = '#6B0000'
NAVY = '#1a1a2e'
CHARCOAL = '#2d2d2d'
GOLD = '#c9a84c'
TEAL = '#0e7490'
SLATE = '#475569'

OUT = '/home/z/my-project/scripts/pdf-assets/charts'

# 1. Campaign allocation donut
fig, ax = plt.subplots(figsize=(6, 6), facecolor='white')
labels = ['Place\n$82M', 'Minds\n$7M', 'Access\n$5M', 'Excellence\n$3M', 'Progress\n$3M']
sizes = [82, 7, 5, 3, 3]
colors = [CRIMSON, '#a83232', '#c44e4e', '#d47676', '#e4a0a0']
explode = (0.03, 0.03, 0.03, 0.03, 0.03)
wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.0f%%', startangle=90, pctdistance=0.78,
    textprops={'fontsize': 11, 'fontweight': 'bold', 'color': 'white'})
for t in texts:
    t.set_color(CHARCOAL)
    t.set_fontsize(10)
ax.set_title('$100M Campaign Allocation by Pillar', fontsize=16, fontweight='bold', color=CRIMSON, pad=20)
plt.tight_layout()
plt.savefig(f'{OUT}/campaign_allocation_donut.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()

# 2. Revenue projection bar chart
fig, ax = plt.subplots(figsize=(10, 5), facecolor='white')
years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']
tuition = [300, 630, 990, 1350, 1800]
other_rev = [5, 15, 30, 50, 80]
x = np.arange(len(years))
w = 0.35
bars1 = ax.bar(x - w/2, tuition, w, label='Tuition Revenue ($M)', color=CRIMSON, edgecolor='white', linewidth=0.5)
bars2 = ax.bar(x + w/2, other_rev, w, label='Other Revenue ($M)', color=GOLD, edgecolor='white', linewidth=0.5)
ax.set_xlabel('Year', fontsize=12, color=SLATE)
ax.set_ylabel('Revenue ($M)', fontsize=12, color=SLATE)
ax.set_title('5-Year Revenue Projection', fontsize=16, fontweight='bold', color=CRIMSON)
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='#e2e8f0')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 15, f'${int(bar.get_height())}M',
            ha='center', va='bottom', fontsize=9, fontweight='bold', color=CRIMSON)
plt.tight_layout()
plt.savefig(f'{OUT}/revenue_projection_bar.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()

# 3. Surplus and Endowment growth
fig, ax1 = plt.subplots(figsize=(10, 5), facecolor='white')
surplus = [0, 38, 150, 262, 378, 500]
endowment = [3, 63, 213, 475, 853, 1353]
years_s = ['Year 0\n(Founding)', 'Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']
ax1.fill_between(range(len(years_s)), surplus, alpha=0.3, color=CRIMSON)
ax1.plot(range(len(years_s)), surplus, 'o-', color=CRIMSON, linewidth=2.5, markersize=8, label='Annual Surplus ($M)')
ax1.set_xlabel('', fontsize=12)
ax1.set_ylabel('Annual Surplus ($M)', fontsize=12, color=CRIMSON)
ax1.tick_params(axis='y', labelcolor=CRIMSON)
ax1.set_xticks(range(len(years_s)))
ax1.set_xticklabels(years_s, fontsize=10)
ax2 = ax1.twinx()
ax2.fill_between(range(len(years_s)), endowment, alpha=0.15, color=NAVY)
ax2.plot(range(len(years_s)), endowment, 's--', color=NAVY, linewidth=2, markersize=7, label='Cumulative Endowment ($M)')
ax2.set_ylabel('Cumulative Endowment ($M)', fontsize=12, color=NAVY)
ax2.tick_params(axis='y', labelcolor=NAVY)
ax1.set_title('Surplus & Endowment Growth Trajectory', fontsize=16, fontweight='bold', color=CRIMSON, pad=15)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', frameon=True, facecolor='white', edgecolor='#e2e8f0')
ax1.spines['top'].set_visible(False)
plt.tight_layout()
plt.savefig(f'{OUT}/surplus_endowment_growth.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()

# 4. Donor segments breakdown
fig, ax = plt.subplots(figsize=(7, 5), facecolor='white')
segments = ['Lead Donors\n(10 gifts)', 'Major Donors\n(20 gifts)', 'Community\n(Unlimited)']
amounts = [70, 20, 10]
colors_seg = [CRIMSON, '#c44e4e', GOLD]
wedges, texts, autotexts = ax.pie(amounts, labels=segments, colors=colors_seg,
    autopct=lambda p: f'${int(p*1):.0f}M\n({p:.0f}%)', startangle=140,
    pctdistance=0.65, textprops={'fontsize': 11})
for at in autotexts:
    at.set_color('white')
    at.set_fontweight('bold')
ax.set_title('Donor Segments: $100M by Source', fontsize=15, fontweight='bold', color=CRIMSON, pad=15)
plt.tight_layout()
plt.savefig(f'{OUT}/donor_segments_pie.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()

# 5. Student growth projection
fig, ax = plt.subplots(figsize=(9, 5), facecolor='white')
years = ['Y1', 'Y2', 'Y3', 'Y4', 'Y5']
students = [100000, 150000, 200000, 250000, 300000]
colleges = [50, 55, 60, 65, 70]
ax.bar(years, students, color=CRIMSON, alpha=0.85, label='Students')
for i, (y, s) in enumerate(zip(years, students)):
    ax.text(i, s + 3000, f'{s//1000}K', ha='center', va='bottom', fontsize=10, fontweight='bold', color=CRIMSON)
ax2 = ax.twinx()
ax2.plot(years, colleges, 'D-', color=GOLD, linewidth=2.5, markersize=8, label='Colleges')
ax2.set_ylabel('Number of Colleges', fontsize=12, color=GOLD)
ax2.tick_params(axis='y', labelcolor=GOLD)
ax.set_ylabel('Students Enrolled', fontsize=12, color=CRIMSON)
ax.tick_params(axis='y', labelcolor=CRIMSON)
ax.set_title('Student & College Growth: 5-Year Projection', fontsize=15, fontweight='bold', color=CRIMSON)
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left', frameon=True, facecolor='white')
ax.spines['top'].set_visible(False)
plt.tight_layout()
plt.savefig(f'{OUT}/student_growth_bar.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()

# 6. OPEX breakdown stacked bar
fig, ax = plt.subplots(figsize=(9, 5), facecolor='white')
years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']
faculty = [180, 270, 360, 450, 540]
operations = [60, 90, 120, 150, 180]
scholarships = [40, 100, 150, 200, 260]
other = [20, 30, 40, 50, 60]
x = np.arange(len(years))
ax.bar(x, faculty, 0.6, label='Faculty Compensation', color=CRIMSON)
ax.bar(x, operations, 0.6, bottom=faculty, label='Operations', color='#c44e4e')
ax.bar(x, scholarships, 0.6, bottom=[f+o for f,o in zip(faculty, operations)], label='Scholarships', color=GOLD)
ax.bar(x, other, 0.6, bottom=[f+o+s for f,o,s in zip(faculty, operations, scholarships)], label='Other', color=SLATE)
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.set_ylabel('Expenditure ($M)', fontsize=12)
ax.set_title('Operating Expenditure Breakdown', fontsize=15, fontweight='bold', color=CRIMSON)
ax.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='#e2e8f0')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f'{OUT}/opex_breakdown_stacked.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()

# 7. Naming opportunities horizontal bar
fig, ax = plt.subplots(figsize=(9, 5), facecolor='white')
naming = ['Central Node', 'Tier A College', 'Center of Inquiry', 'Tier B College', 'Distinguished Prof.', 'Degree Program', 'Tier C College', 'Scholarship Fund']
amounts = [25, 10, 10, 5, 5, 3, 2, 0.012]
colors_bar = [CRIMSON, '#9e2020', '#b83838', '#c44e4e', '#d47676', '#e4a0a0', '#f0c4c4', GOLD]
ax.barh(naming, amounts, color=colors_bar, height=0.6, edgecolor='white', linewidth=0.5)
for i, (n, a) in enumerate(zip(naming, amounts)):
    label = f'${a:,.0f}M' if a >= 1 else f'${a*1000:,.0f}'
    ax.text(a + 0.3, i, label, va='center', fontsize=10, fontweight='bold', color=CHARCOAL)
ax.set_xlabel('Naming Gift Amount ($M)', fontsize=12)
ax.set_title('Naming Opportunities by Tier', fontsize=15, fontweight='bold', color=CRIMSON)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlim(0, 30)
plt.tight_layout()
plt.savefig(f'{OUT}/naming_opportunities_bar.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()

# 8. Giving circles comparison
fig, ax = plt.subplots(figsize=(9, 5), facecolor='white')
circles = ["Founders'\nCircle", "Guardians'\nCircle", "Builders'\nCircle", "Fellows'\nCircle", "Friends of\nArtemis", "The 99"]
min_gifts = [10, 5, 1, 0.1, 0.01, 0.000099]
colors_c = [CRIMSON, '#9e2020', '#4338ca', TEAL, '#15803d', '#6b7280']
ax.bar(circles, min_gifts, color=colors_c, width=0.6, edgecolor='white', linewidth=0.5)
ax.set_yscale('log')
ax.set_ylabel('Minimum Gift ($M)', fontsize=12)
ax.set_title('Giving Circles: Minimum Gift Thresholds', fontsize=15, fontweight='bold', color=CRIMSON)
for i, v in enumerate(min_gifts):
    label = f'${v:,.0f}M' if v >= 1 else f'${v*1000:,.0f}K' if v >= 0.001 else f'${v*1000000:,.0f}'
    ax.text(i, v * 1.3, label, ha='center', va='bottom', fontsize=9, fontweight='bold', color=CHARCOAL)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f'{OUT}/giving_circles_bar.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()

# 9. Timeline/Gantt-style chart
fig, ax = plt.subplots(figsize=(10, 4), facecolor='white')
phases = ['Quiet Phase', 'Public Phase', 'Close & Capitalise', 'Build & Launch']
starts = [0, 3, 6, 9]
durations = [3, 3, 3, 3]
targets = ['$50M', '$85M', '$100M', '$100M']
colors_g = [CRIMSON, '#9e2020', '#4338ca', TEAL]
for i, (ph, s, d, t, c) in enumerate(zip(phases, starts, durations, targets, colors_g)):
    ax.barh(i, d, left=s, height=0.5, color=c, edgecolor='white', linewidth=1)
    ax.text(s + d/2, i, f'{ph}\n{t}', ha='center', va='center', fontsize=9, fontweight='bold', color='white')
ax.set_xlabel('Month', fontsize=12)
ax.set_xlim(-0.5, 13)
ax.set_yticks(range(len(phases)))
ax.set_yticklabels(['' for _ in phases])
ax.set_xticks(range(0, 13, 3))
ax.set_xticklabels(['Month 0', 'Month 3', 'Month 6', 'Month 9', 'Month 12'])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_title('Campaign Timeline: 12 Months to Launch', fontsize=15, fontweight='bold', color=CRIMSON)
plt.tight_layout()
plt.savefig(f'{OUT}/timeline_gantt.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()

# 10. Scholarship impact chart
fig, ax = plt.subplots(figsize=(9, 5), facecolor='white')
years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']
scholarships_funded = [10000, 13300, 16600, 19900, 23200]
scholarship_budget = [5, 40, 66, 80, 93]
ax.bar(years, scholarships_funded, color=CRIMSON, alpha=0.85, label='Students on Scholarship')
for i, (y, s) in enumerate(zip(years, scholarships_funded)):
    ax.text(i, s + 300, f'{s//1000}K', ha='center', va='bottom', fontsize=10, fontweight='bold', color=CRIMSON)
ax2 = ax.twinx()
ax2.plot(years, scholarship_budget, 'o-', color=GOLD, linewidth=2.5, markersize=8, label='Scholarship Budget ($M)')
ax2.set_ylabel('Scholarship Budget ($M)', fontsize=12, color=GOLD)
ax2.tick_params(axis='y', labelcolor=GOLD)
ax.set_ylabel('Students Funded', fontsize=12, color=CRIMSON)
ax.tick_params(axis='y', labelcolor=CRIMSON)
ax.set_title('Scholarship Impact: Self-Sustaining from Year 1', fontsize=15, fontweight='bold', color=CRIMSON)
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left', frameon=True, facecolor='white')
ax.spines['top'].set_visible(False)
plt.tight_layout()
plt.savefig(f'{OUT}/scholarship_impact.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()

print("All 10 charts generated successfully!")
import os
for f in sorted(os.listdir(OUT)):
    print(f"  {f}: {os.path.getsize(os.path.join(OUT, f))//1024}KB")
