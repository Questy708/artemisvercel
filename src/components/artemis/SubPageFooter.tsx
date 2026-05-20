'use client';

interface FooterProps {
  goToPage: (page: string) => void;
}

export default function SubPageFooter({ goToPage }: FooterProps) {
  const mainLinks = [
    { label: 'Education', page: 'education' },
    { label: 'Research', page: 'research' },
    { label: 'Innovation', page: 'innovation' },
    { label: 'Admissions + Aid', page: 'admissions' },
    { label: 'Campus Life', page: 'campus' },
    { label: 'Colleges', page: 'colleges' },
    { label: 'About', page: 'about' },
    { label: 'Journal', page: 'blog' },
  ];

  const quickLinks = [
    { label: 'Visit', page: 'visit-us' },
    { label: 'Events', page: 'campus' },
    { label: 'People', page: 'our-people' },
    { label: 'Jobs', page: 'jobs' },
    { label: 'Contact', page: 'contact-us' },
  ];

  const legalLinks = [
    { label: 'Privacy', page: 'policies' },
    { label: 'Accessibility', page: 'access-at-artemis' },
    { label: 'Sustainability', page: 'sustainability' },
  ];

  return (
    <footer className="bg-[#0a0a0a] text-white w-full shrink-0">
      <div className="max-w-[1400px] mx-auto w-full px-5 sm:px-8 lg:px-20">

        {/* Top: Logo + tagline */}
        <div className="py-10 border-b border-white/10 flex flex-col md:flex-row md:items-end md:justify-between gap-6">
          <div>
            <div className="flex items-center gap-3 mb-3">
              <svg width="32" height="32" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M20 3L4 9V19.5C4 28.5 11 35.5 20 37.5C29 35.5 36 28.5 36 19.5V9L20 3Z" stroke="rgba(255,255,255,0.3)" strokeWidth="1.8" fill="none"/>
                <path d="M20 5.5L6.5 10.8V19.5C6.5 27.2 12.4 33.2 20 35C27.6 33.2 33.5 27.2 33.5 19.5V10.8L20 5.5Z" fill="rgba(255,255,255,0.04)"/>
                <path d="M20 11L14 24H16.5L17.8 20.8H22.2L23.5 24H26L20 11ZM18.6 18.8L20 14.8L21.4 18.8H18.6Z" fill="rgba(255,255,255,0.4)"/>
                <line x1="12" y1="28" x2="28" y2="28" stroke="rgba(255,255,255,0.15)" strokeWidth="0.8"/>
                <circle cx="15" cy="30.5" r="0.8" fill="rgba(255,255,255,0.2)"/>
                <circle cx="20" cy="30.5" r="0.8" fill="rgba(255,255,255,0.2)"/>
                <circle cx="25" cy="30.5" r="0.8" fill="rgba(255,255,255,0.2)"/>
              </svg>
              <div className="leading-[1.15]">
                <div className="text-[11px] font-semibold tracking-tight text-white/50">University of</div>
                <div className="text-[14px] font-bold tracking-tight text-white/80">Artemis</div>
              </div>
            </div>
            <p className="text-xs text-white/25 max-w-sm leading-relaxed">A global collegiate university reimagining higher education for the 21st century and beyond.</p>
          </div>
          <div className="flex items-center gap-4">
            <button
              onClick={() => goToPage('fundraising')}
              className="border border-[#8A0000] text-[#8A0000] px-5 py-2 text-[10px] font-bold uppercase tracking-wider hover:bg-[#8A0000] hover:text-white transition-colors cursor-pointer"
            >
              Give to Artemis
            </button>
            <button
              onClick={() => goToPage('apply')}
              className="bg-[#8A0000] text-white px-5 py-2 text-[10px] font-bold uppercase tracking-wider hover:bg-[#6B0000] transition-colors cursor-pointer"
            >
              Apply
            </button>
          </div>
        </div>

        {/* Middle: Navigation grid */}
        <div className="py-8 grid grid-cols-2 sm:grid-cols-4 md:grid-cols-5 lg:grid-cols-8 gap-x-6 gap-y-4">
          {mainLinks.map((link, i) => (
            <button
              key={link.page}
              onClick={() => goToPage(link.page)}
              className="group cursor-pointer text-left"
            >
              <div className="text-[9px] font-mono text-white/15 mb-1">0{i + 1}</div>
              <div className="text-[11px] text-white/35 group-hover:text-white/80 transition-colors leading-tight">{link.label}</div>
            </button>
          ))}
        </div>

        {/* Quick links + Social + Legal */}
        <div className="py-6 border-t border-white/5 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
          <div className="flex flex-wrap items-center gap-x-5 gap-y-2">
            {quickLinks.map((link) => (
              <button
                key={link.page}
                onClick={() => goToPage(link.page)}
                className="text-[11px] text-white/25 hover:text-white/60 transition-colors cursor-pointer"
              >
                {link.label}
              </button>
            ))}
            <span className="text-white/10">|</span>
            {legalLinks.map((link) => (
              <button
                key={link.page}
                onClick={() => goToPage(link.page)}
                className="text-[11px] text-white/25 hover:text-white/60 transition-colors cursor-pointer"
              >
                {link.label}
              </button>
            ))}
          </div>

          {/* Social */}
          <div className="flex items-center gap-4 text-[11px] text-white/20">
            <a href="https://x.com/artemisuni" target="_blank" rel="noopener noreferrer" className="hover:text-white/60 transition-colors">X</a>
            <a href="https://facebook.com/artemisuni" target="_blank" rel="noopener noreferrer" className="hover:text-white/60 transition-colors">Facebook</a>
            <a href="https://linkedin.com/school/artemisuni" target="_blank" rel="noopener noreferrer" className="hover:text-white/60 transition-colors">LinkedIn</a>
            <a href="https://instagram.com/artemisuni" target="_blank" rel="noopener noreferrer" className="hover:text-white/60 transition-colors">Instagram</a>
          </div>
        </div>

        {/* Experimental: Artemis Project */}
        <div className="py-4 border-t border-white/5 flex items-center justify-between">
          <button
            onClick={() => goToPage('artemis-project')}
            className="flex items-center gap-2 text-[10px] text-white/20 hover:text-white/60 transition-colors cursor-pointer group"
          >
            <span className="w-5 h-5 rounded border border-white/10 group-hover:border-white/30 flex items-center justify-center text-[8px] font-bold font-mono">AP</span>
            <span className="uppercase tracking-widest font-mono">Artemis Project</span>
            <span className="text-[8px] text-white/10 group-hover:text-white/30 ml-1 uppercase tracking-wider">Experimental</span>
          </button>
        </div>

        {/* Bottom: Copyright */}
        <div className="py-5 border-t border-white/5 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2">
          <p className="text-[10px] text-white/15">&copy; {new Date().getFullYear()} University of Artemis. All rights reserved.</p>
          <p className="text-[10px] text-white/10 font-mono uppercase tracking-wider">Artemis Collegium &middot; Global</p>
        </div>
      </div>
    </footer>
  );
}
