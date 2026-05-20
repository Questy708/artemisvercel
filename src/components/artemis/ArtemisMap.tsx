'use client';

import { useState, useMemo } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { X } from 'lucide-react';

type LocationData = {
  id: string;
  name: string;
  x: number;
  y: number;
  labelPos: 'left' | 'right';
  description: string;
  industries: string[];
};

const locations: LocationData[] = [
  {
    id: 'malta',
    name: 'VALLETTA',
    x: 52,
    y: 39,
    labelPos: 'right',
    description: "The central governance hub of the Artemis Collegium Network. Home to the Chancellor's Office, the Central Council chambers, and the primary academic coordination centre for all founding micro-colleges.",
    industries: ['Governance', 'Policy', 'Central Administration']
  },
  {
    id: 'kigali',
    name: 'KIGALI',
    x: 56,
    y: 56,
    labelPos: 'right',
    description: 'A centre for sustainable technology and African studies. Kigali serves as a living laboratory for urban innovation, renewable energy systems, and community-driven development across East Africa.',
    industries: ['Sustainable Tech', 'Urban Innovation', 'African Studies']
  },
  {
    id: 'berlin',
    name: 'BERLIN',
    x: 51,
    y: 30,
    labelPos: 'right',
    description: 'The European innovation hub, housing the Forge incubator and the Center for Creative Industries. Berlin connects Artemis research to the European startup ecosystem and creative economy.',
    industries: ['Innovation', 'Creative Industries', 'Startup Ecosystem']
  },
  {
    id: 'sf',
    name: 'SAN FRANCISCO',
    x: 15,
    y: 37,
    labelPos: 'right',
    description: 'The Silicon Innovation Hub anchors Artemis on the US West Coast. Proximity to leading technology companies and venture capital enables translational research partnerships and student entrepreneurship.',
    industries: ['Silicon Innovation', 'Technology Transfer', 'Venture Partnerships']
  },
  {
    id: 'tokyo',
    name: 'TOKYO',
    x: 85,
    y: 37,
    labelPos: 'left',
    description: "The Pacific Robotics Node brings together Artemis researchers in autonomy, mechatronics, and physical AI. Tokyo's advanced manufacturing ecosystem provides unique prototyping capabilities.",
    industries: ['Robotics', 'Advanced Manufacturing', 'Autonomy']
  },
  {
    id: 'reykjavik',
    name: 'REYKJAVIK',
    x: 42,
    y: 18,
    labelPos: 'right',
    description: "The Arctic Research Hub focuses on cryosphere dynamics, geothermal energy, and climate feedback mechanisms. Iceland's extreme environment provides a natural laboratory for planetary science.",
    industries: ['Arctic Research', 'Geothermal Energy', 'Climate Science']
  },
  {
    id: 'singapore',
    name: 'SINGAPORE',
    x: 77,
    y: 55,
    labelPos: 'left',
    description: "The Smart Infrastructure Node connects Artemis to Southeast Asia's rapid urban development. Research focuses on intelligent transport, digital governance, and sustainable city design.",
    industries: ['Smart Cities', 'Digital Governance', 'Sustainable Design']
  },
  {
    id: 'saopaulo',
    name: 'SÃO PAULO',
    x: 31,
    y: 66,
    labelPos: 'right',
    description: 'The Latin American centre for biodiversity research, social innovation, and the Civic Guild training grounds. São Paulo connects Artemis to the environmental and social challenges of the Global South.',
    industries: ['Biodiversity', 'Social Innovation', 'Civic Engagement']
  }
];

export default function ArtemisMap() {
  const [activeLocationId, setActiveLocationId] = useState<string | null>(null);

  const activeLocationData = useMemo(
    () => locations.find(loc => loc.id === activeLocationId),
    [activeLocationId]
  );

  return (
    <section className="py-20 max-w-[1000px] mx-auto w-full">
      {/* Section Header */}
      <div className="mb-12 px-6 lg:px-16">
        <div className="mb-8 flex items-center space-x-3">
          <span className="w-8 h-[1px] bg-[#8A0000]"></span>
          <span className="text-[11px] font-bold uppercase tracking-[0.3em] text-[#8A0000]">Global Network</span>
        </div>
        <h2 className="text-[36px] md:text-[42px] font-extrabold leading-[1.05] tracking-tighter text-[#141414] mb-4 uppercase">
          Global Presence
        </h2>
        <p className="text-gray-500 max-w-lg text-[16px] leading-relaxed font-light">
          Founding nodes of the Artemis Collegium Network
        </p>
      </div>

      {/* Map Container */}
      <div
        className="relative w-full overflow-hidden bg-white"
        onClick={(e) => {
          if (e.target === e.currentTarget) {
            setActiveLocationId(null);
          }
        }}
      >
        <img
          src="https://cdn.prod.website-files.com/677376e1e97650585235ab96/677e1de06571eae8d537fc47_map.avif"
          alt="World Map"
          className="w-full h-auto pointer-events-none select-none opacity-80"
        />

        {locations.map((loc, index) => (
          <div
            key={loc.id}
            className={`absolute -translate-x-1/2 -translate-y-1/2 flex items-center justify-center ${activeLocationId === loc.id ? 'z-40' : 'z-10'}`}
            style={{ left: `${loc.x}%`, top: `${loc.y}%` }}
          >
            <motion.div
              initial={{ scale: 0, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              transition={{ type: "spring", stiffness: 350, damping: 25, delay: index * 0.1 }}
              className="relative flex items-center justify-center"
            >
              {/* Crimson Marker */}
              <button
                onClick={() => setActiveLocationId(activeLocationId === loc.id ? null : loc.id)}
                className="relative w-4 h-4 md:w-5 md:h-5 bg-[#8A0000] hover:bg-red-800 rounded-full shrink-0 cursor-pointer transition-colors border-[3px] border-transparent hover:border-black"
                aria-label={`View ${loc.name}`}
              />

              {/* Static Label (Always Visible) */}
              <div
                className={`absolute bg-black text-white font-mono text-xs md:text-sm font-bold tracking-[0.15em] px-3 py-1.5 whitespace-nowrap top-1/2 -translate-y-1/2 pointer-events-none shadow-sm
                  ${loc.labelPos === 'left' ? 'right-full mr-2 md:mr-3' : 'left-full ml-2 md:ml-3'}`}
              >
                {loc.name}
              </div>
            </motion.div>
          </div>
        ))}

        {/* Info Panel Overlay */}
        <AnimatePresence>
          {activeLocationData && (
            <motion.div
              initial={{ opacity: 0, x: 50 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: 50, transition: { duration: 0.2 } }}
              transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
              className="absolute top-4 bottom-4 right-4 md:w-80 lg:w-96 bg-white border border-gray-200 shadow-2xl p-6 md:p-8 flex flex-col z-50 overflow-y-auto"
            >
              <button
                onClick={() => setActiveLocationId(null)}
                className="absolute top-4 right-4 p-2 text-gray-400 hover:text-black transition-colors"
                aria-label="Close panel"
              >
                <X className="w-5 h-5" />
              </button>

              <h3 className="text-2xl font-medium uppercase tracking-tight text-black mb-6 mt-4">
                {activeLocationData.name}
              </h3>

              <div className="space-y-6">
                <div>
                  <h4 className="text-xs font-mono uppercase tracking-widest text-[#8A0000] mb-2">About</h4>
                  <p className="text-gray-600 text-sm leading-relaxed">
                    {activeLocationData.description}
                  </p>
                </div>

                <div>
                  <h4 className="text-xs font-mono uppercase tracking-widest text-[#8A0000] mb-3">Focus Areas</h4>
                  <ul className="flex flex-wrap gap-2">
                    {activeLocationData.industries.map((industry, i) => (
                      <li
                        key={i}
                        className="bg-gray-100 px-3 py-1.5 text-xs font-medium text-gray-800 rounded-sm"
                      >
                        {industry}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </section>
  );
}
