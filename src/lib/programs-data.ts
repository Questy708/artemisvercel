export interface ProgramData {
  title: string;
  directorName: string;
  directorLocation: string;
  coDirectorTitle?: string;
  coDirectorName?: string;
  coDirectorLocation?: string;
  website: string;
  overviewParagraphs: string[];
  requirementsParagraphs: string[];
  seniorRequirement: string;
  advising: string;
  summaryDistribution: string;
  summarySubstitution: string;
  summarySeniorReq: string;
  requirementsArray: string[];
  firstYearParagraphs: string[];
  certificateText?: string;
  certificateRequirements?: string;
  facultyProfessors: string;
  facultyAssociate: string;
  facultyAssistant?: string;
  facultyLecturers?: string;
  roadmapText: string;
  coursesLinks: { label: string; link: string }[];
}

export const programsData: Record<string, ProgramData> = {
  "African Studies (B.A.)": {
    title: "African Studies",
    directorName: "Dr. Amara Okoro",
    directorLocation: "Artemis Global Humanities Center, Valletta Campus",
    coDirectorTitle: "Director of the program in African Languages",
    coDirectorName: "Dr. Kwame Osei",
    coDirectorLocation: "Artemis Global Humanities Center, Valletta Campus",
    website: "www.artemisui.org/african-studies",
    overviewParagraphs: [
      "The program in African Studies enables students to undertake interdisciplinary study of the arts, history, cultures, politics, and development of Africa, specifically contextualized through Artemis University's global node framework.",
      "As a foundation, students in the program gain cross-disciplinary exposure to Africa. In the junior and senior years, students develop analytical ability and focus their studies on research in a particular discipline such as anthropology, art history, history, languages and literature, political science, or on topics such as global health, economic sustainability, or human rights.",
      "African Studies provides training of special interest to those considering admission to graduate or professional schools or careers in global governance, international relations, sustainable development, diplomacy, and culturally informed technology."
    ],
    requirementsParagraphs: [
      "The African Studies program consists of twelve term courses, including (1) one African Studies course in the humanities and one in the social sciences; (2) two years of an African language (Arabic, Kiswahili, Twi, Wolof, Yoruba, isiZulu, or others with permission of the director of undergraduate studies (DUS)); (3) one research methods course, AFST 5505; (4) four courses in an area of focus; and (5) AFST 4491, the senior capstone. The required courses represent the core of the program and are intended to expose the student both to the interdisciplinary nature of African studies and to the methodologies currently being brought to bear on the study of African cultures and societies.",
      "**Language requirement** African Studies majors are required to complete two years of college-level study (or the equivalent) of an African language, deeply integrated through Artemis's VR immersion modules and field placements. For the language requirement to be waived, a student must pass a placement test for admission into an advanced-level course.",
      "**Program in African languages** The language program offers instruction in five major languages from sub-Saharan Africa. Sequences are designed to enable students to achieve advanced competence in all skill areas by the end of the third year, and students are encouraged to spend a summer or term in Africa during their language study.",
      "**Credit/D/Fail** No more than one course taken for Credit/D/Fail may be applied toward the requirements of the major.",
      "**Outside credit** Courses taken at another institution or during an approved summer or term-time study abroad program may count toward the major requirements with DUS approval."
    ],
    seniorRequirement: "Students are required to complete a senior project (AFST 4491), working under the guidance of a faculty adviser, optionally incorporating a field study from an Artemis African partner node. A preliminary statement indicating the topic to be addressed and the name of the faculty adviser must be submitted to the DUS by the end of the second week of the fall term in the senior year.",
    advising: "Students planning to major in African Studies should consult the DUS as early as possible.",
    summaryDistribution: "1 AFST course in humanities and 1 in social sciences; 2 years of African lang; 4 courses and 1 research methods course in focus area",
    summarySubstitution: "If language req is waived, 4 addtl African Studies courses",
    summarySeniorReq: "Senior Capstone (AFST 4491)",
    requirementsArray: [
      "1 AFST course in the humanities",
      "1 AFST course in the social sciences",
      "4 courses studying an African language (two-years); other options with DUS approval",
      "1 research methods course, can be AFST 5505",
      "4 courses in chosen area of focus",
      "AFST 4491, Senior Capstone"
    ],
    firstYearParagraphs: [
      "The program in African Studies considers the arts, history, cultures, languages and literatures, politics, and development of Africa. Students in the program gain a cross-disciplinary exposure to Africa while focusing their studies in a particular discipline such as anthropology, art history, economics, history, languages and literatures, political science, or sociology, or in an interdisciplinary program within their broader collegiate environment at Artemis University. Artemis has unusually rich resources for the study of Africa; the Artemis Malta Central Node, notably, has one of the world's most comprehensive collections of African materials.",
      "Students should begin their language study as soon as possible, ideally taking advantage of our immersive language technologies. Those considering a major in African Studies should consult the DUS."
    ],
    certificateText: "The Department of African Studies offers a Certificate of Advanced Language Study in three major African languages—Kiswahili, Yoruba, and isiZulu, and students may pursue a Certificate of Advanced Language Study in each of these languages. A certificate adviser, typically the director of undergraduate studies (DUS), advises students on the certification process and certifies to the University Registrar's Office that students have completed the stated requirements before the end of eight terms of study. The Certificate of Advanced Language Study, once certified, is listed on the student's transcript.",
    certificateRequirements: "Students seeking to earn the certificate are required to take four courses beyond the L4 level in their chosen language, at least two of which must be Artemis courses designated as L5. All courses must be taken for a letter grade, and students must achieve a grade of B or above. With the approval of the adviser, one advanced non-L5 Artemis course, conducted in the target language, such as an independent study course, a graduate seminar, or an advanced seminar may count toward certification requirements.",
    facultyProfessors: "Dr. Kalu Diop (History & Digital Preservation), Dr. Amina Ghaffar (Anthropology), Dr. Samuel Nderitu (Political Science & Neo-Economics)",
    facultyAssociate: "Dr. Zinhle Mbeki (Sociology), Dr. Femi Ojo (Global Bio-Ethics)",
    facultyAssistant: "Dr. Tareq Hassan (Language Technologies)",
    facultyLecturers: "Dr. Kiarie Wanjogu (Kiswahili), Dr. Sandra Sanneh (isiZulu), Dr. Oluseye Adesola (Yoruba)",
    roadmapText: "See the Artemis Roadmap Library for a visual representation of the African Studies trajectory.",
    coursesLinks: [
      { label: "View African Studies Courses", link: "#" },
      { label: "View African Languages Courses", link: "#" }
    ]
  },
  "Computer Science (B.A. or B.S.)": {
    title: "Computer Science",
    directorName: "Dr. Elena Vasquez",
    directorLocation: "Artemis Computability Lab, Valletta Node",
    coDirectorTitle: "Assistant DUS",
    coDirectorName: "Dr. Rajan Mehta",
    coDirectorLocation: "Artemis Computability Lab, Valletta Node",
    website: "www.artemisui.org/cpsc",
    overviewParagraphs: [
      "The College of Computer Science at Artemis offers both B.S. and B.A. degree programs, with specialized cross-collegiate tracks linking our tech infrastructure with humanities, economics, and quantum mathematics.",
      "The major in Computer Science prepares students for an array of global pursuits, ranging from leading deep-tech research to driving computational policy in international bodies. Our Valletta campus provides a unique intersection for global tech innovation. Core requirements cover rigorous software engineering and theoretical foundations, while electives delve into distributed AI, quantum computing, and bio-informatics."
    ],
    requirementsParagraphs: [
      "The B.S. degree requires fourteen term courses, and the B.A. requires twelve. Both share a core encompassing data structures, algorithms, and systems architectures specific to the Artemis digital ecosystem.",
      "Beyond the core, students specialize through advanced electives to align with their residential college's focus."
    ],
    seniorRequirement: "Seniors must complete a capstone project (CPSC 490) addressing a global computational challenge under faculty supervision.",
    advising: "Students consult with the DUS and their Collegiate Dean to ensure prerequisites are met.",
    summaryDistribution: "B.S.: 14 courses; B.A.: 12 courses. Core includes intro programming, data structures, algorithms, and systems.",
    summarySubstitution: "Up to two related courses outside the department from partner global nodes.",
    summarySeniorReq: "Senior Project (CPSC 490)",
    requirementsArray: [
      "Core: Introductory Programming sequence",
      "Core: Data Structures and Algorithms",
      "Core: Computer Systems",
      "Electives: 8 courses for B.S., 6 courses for B.A.",
      "Senior Requirement: CPSC 490"
    ],
    firstYearParagraphs: [
      "Students with prior experience can enter directly into algorithms tracks. Beginners proceed through intensive foundational sequence taking advantage of Artemis immersive VR coding spheres.",
      "Mathematics forms a crucial foundation, and students must complete discrete math via the Artemis Core within two years."
    ],
    facultyProfessors: "Dr. Elena Vasquez (Distributed Systems), Dr. Nikolai Petrov (Quantum Computing), Dr. Celeste Moreau (Computational Theory)",
    facultyAssociate: "Dr. Hiroshi Tanaka (Machine Learning), Dr. Amara Diallo (Cybersecurity)",
    facultyLecturers: "Dr. Marcus Chen (Software Engineering), Dr. Fatima Al-Rashid (Data Science)",
    roadmapText: "The Artemis Roadmap Library visualizes pathways for both the B.S. and B.A. Computer Science sequences.",
    coursesLinks: [
      { label: "View Computer Science Courses", link: "#" },
      { label: "View Information Security Tracks", link: "#" },
      { label: "View Quantum Computing Electives", link: "#" }
    ]
  },
  "Cognitive Science (B.A. or B.S.)": {
    title: "Cognitive Science",
    directorName: "Dr. Miriam Falk",
    directorLocation: "Artemis Institute for Mind and Computation, Valletta Node",
    website: "www.artemisui.org/cogsci",
    overviewParagraphs: [
      "Cognitive science explores the nature of cognitive processes such as perception, reasoning, memory, attention, language, decision making, imagery, motor control, and problem solving. The goal of cognitive science, stated simply, is to understand how the mind works.",
      "At Artemis University, Cognitive Science is an inherently interdisciplinary endeavor, drawing on tools and ideas from fields such as psychology, computer science, linguistics, philosophy, economics, and neuroscience. Approaches include empirical studies of the ontogenetic and phylogenetic development of cognitive abilities, experimental work on cognitive processing in adults, attempts to understand perception and cognition based on patterns of breakdown in pathology, computational and robotic research that strives to simulate aspects of cognition and behavior, neuroscientific investigations of the neural bases of cognition using neural recording and brain scanning, and the development of philosophical theories of the nature of mind."
    ],
    requirementsParagraphs: [
      "**Prerequisite** An introductory survey course, CGSC 1100, is normally taken by the end of the fall term of the sophomore year and prior to admission to the major.",
      "The requirements of the major for the B.S. and B.A. degrees are the same, except for the senior requirement. Fifteen term courses, for a total of thirteen and one half course credits, are required for the major, including the introductory course and the senior requirement. Each major program must include the elements described below. The particular selection of courses must be approved by the director of undergraduate studies (DUS) in order to assure overall coherence.",
      "**Breadth requirement** A breadth requirement introduces students to the subfields of cognitive science. Each major is required to take a course from four of the following seven areas: Computer science, Economics and decision making, Linguistics, Neuroscience, Philosophy, Psychology, and Anthropology.",
      "**Depth requirement** Students fulfill a depth requirement by completing six courses that focus on a specific topic or area in cognitive science. The depth courses must be chosen from at least two disciplines, and are typically drawn from the seven cognitive science subfields. All six depth courses must be intermediate or advanced.",
      "**Skills requirement** Because formal techniques are fundamental to cognitive science, one skills course is required, preferably before the senior year.",
      "**Junior colloquium** In the junior year, students are required to take CGSC 3950, a half-credit colloquium in which majors discuss current issues and research in cognitive science and select a senior essay topic."
    ],
    seniorRequirement: "In the senior year, students take two half-credit capstone courses in which the senior essay is written. Students must take this course during their senior year. The B.S. degree requires empirical research (CGSC 4900 and 4910). The B.A. degree requires nonempirical research (CGSC 4800 and 4810).",
    advising: "Students may apply to enter the major at any point after the first year. Applications must include an official or unofficial transcript, a brief statement of purpose, and a list of the six upper-level courses that the student plans to take as part of the research focus.",
    summaryDistribution: "1 course each in 4 of 7 subfields; 6 courses in a specific topic area; 1 skills course; 1 junior colloquium.",
    summarySubstitution: "Courses taken during an approved global node study abroad program may count with DUS approval.",
    summarySeniorReq: "B.S.—CGSC 4900/4910; B.A.—CGSC 4800/4810",
    requirementsArray: [
      "Prerequisite: CGSC 1100",
      "Breadth: 1 course from 4 of 7 subfields",
      "Depth: 6 courses in a specific area",
      "Skills: 1 course in formal methods",
      "Junior Colloquium: CGSC 3950 (half-credit)",
      "Senior Requirement (B.S. empirical / B.A. non-empirical)"
    ],
    firstYearParagraphs: [
      "Cognitive science is an interdisciplinary field devoted to exploring the nature of cognitive processes such as perception, reasoning, memory, attention, language, imagery, motor control, and problem solving. The goal of cognitive science, stated simply, is to understand how the mind works.",
      "Students may apply to enter the major in Cognitive Science at any point after the first year. CGSC 1100 is prerequisite to the major. Interested students are also encouraged to take an introductory course in computer science, economics, linguistics, neuroscience, philosophy, or psychology."
    ],
    facultyProfessors: "Dr. Miriam Falk (Cognitive Psychology), Dr. Darius Okafor (Neuroscience of Decision-Making), Dr. Lena Strasser (Computational Linguistics), Dr. Priya Chakraborty (Philosophy of Mind)",
    facultyAssociate: "Dr. Yuki Morioka (Language Acquisition), Dr. Tomás Guerrero (Behavioral Economics), Dr. Sophie Laurent (Neural Computation)",
    facultyAssistant: "Dr. Caleb Winters (Perception & Action), Dr. Nadia Okonkwo (Developmental Cognition), Dr. Mateo Rivera (Social Neuroscience)",
    roadmapText: "See the Roadmap Library for a visual representation of the Cognitive Science pathways.",
    coursesLinks: [
      { label: "View Cognitive Science Courses", link: "#" },
      { label: "View Artificial Intelligence Seminars", link: "#" }
    ]
  },
  "Ethics, Politics, and Economics (B.A.)": {
    title: "Ethics, Politics, and Economics",
    directorName: "Dr. Isadora Venn",
    directorLocation: "Institution for Social and Policy Studies",
    website: "www.artemisui.org/epe",
    overviewParagraphs: [
      "The major in Ethics, Politics, and Economics (EP&E) joins the analytic rigor of the social sciences with the enduring normative questions of philosophy. It aims to develop thoughtful citizens and leaders who are equipped to analyze complex social problems using multiple disciplinary lenses.",
      "By integrating economic analysis, political science, and philosophical inquiry, EP&E students examine how institutions construct value, distribute resources, and justify authority in modern societies."
    ],
    requirementsParagraphs: [
      "The major requires fourteen term courses. Students must complete foundational prerequisites in microeconomics, macroeconomics, political philosophy, and quantitative/statistical methods.",
      "The core of the program includes a specialized interdisciplinary seminar (Classics of EP&E), three core courses combining the disciplines, and a customized concentration of four advanced courses surrounding a specific societal challenge or analytical theme."
    ],
    seniorRequirement: "The senior requirement consists of a two-term senior essay (EP&E 491 and 492). Students engage in original research, applying methodologies from at least two of the three disciplines to their chosen topic.",
    advising: "Admission to the major is competitive and typically occurs in the sophomore year. Advising is intensive, with students working closely with the DUS to hone their specialized concentration themes.",
    summaryDistribution: "14 courses including prerequisites. Core seminar, 3 multi-disciplinary core courses, 4 concentration electives.",
    summarySubstitution: "Varies depending on the individual concentration.",
    summarySeniorReq: "Two-term senior essay (EP&E 491 & 492)",
    requirementsArray: [
      "Prerequisites: Microeconomics, Macroeconomics, Intro Ethics/Political Philosophy, Statistics",
      "Core: Classics of EP&E seminar",
      "3 interdisciplinary core courses",
      "4 courses forming a coherent thematic concentration",
      "Two-term Senior Essay"
    ],
    firstYearParagraphs: [
      "First-year students interested in EP&E should focus on completing the introductory prerequisites in Economics, Political Science, and Philosophy.",
      "Strong writing and analytical skills are essential, and students are encouraged to seek out seminars that challenge their normative and empirical reasoning."
    ],
    facultyProfessors: "Dr. Isadora Venn (Political Philosophy), Dr. Kofi Mensah-Bonsu (Development Economics), Dr. Helena Schwarz (Normative Ethics)",
    facultyAssociate: "Dr. Rafael Coste (Comparative Politics), Dr. Anya Korova (Behavioral Economics)",
    roadmapText: "The Roadmap Library outlines typical trajectories, including the optimal timing for prerequisite completion before applying to the major.",
    coursesLinks: [
      { label: "View EP&E Core Seminars", link: "#" },
      { label: "View Related Philosophy Courses", link: "#" },
      { label: "View Related Economics Courses", link: "#" }
    ]
  }
};

export const generateProgramData = (programName: string): ProgramData => {
  const cleanName = programName.replace(/\s*\(.*?\)\s*/g, '');
  const isScience = programName.includes('B.S.') || programName.includes('Engineering') || programName.includes('Physics') || programName.includes('Biology');

  return {
    title: cleanName,
    directorName: "Prof. Elara Mediterranean",
    directorLocation: "Artemis Central Node, Valletta Campus, Room 148",
    coDirectorTitle: `Director of the program in Applied ${cleanName}`,
    coDirectorName: "Dr. Julian Vance",
    coDirectorLocation: "Global Synthesis Building, Valletta Campus, Room 138, 555-0192",
    website: `www.artemisui.org/academics/${cleanName.toLowerCase().replace(/[^a-z0-9]+/g, '-')}`,
    overviewParagraphs: [
      `The program in ${cleanName} enables students to undertake interdisciplinary study of the theories, history, practice, and development of ${cleanName}. As a foundation, students in the program gain cross-disciplinary exposure operating within Artemis University's collegiate system, anchored by our central node in Valletta, Malta. In the junior and senior years, students develop analytical ability and focus their studies on research in a particular discipline or on intersections with global health, decentralized economics, or sustainable development.`,
      `${cleanName} provides training of special interest to those considering admission to top-tier graduate or professional schools or careers in education, law, management, medicine, international relations, or forward-thinking global industries. The interdisciplinary structure of the program offers students an opportunity to satisfy the increasingly rigorous expectations of admissions committees and prospective employers for a broad liberal arts perspective that complements specialized knowledge of a field.`
    ],
    requirementsParagraphs: [
      `**Prerequisite** An introductory survey course is normally taken by the end of the fall term of the sophomore year and prior to admission to the major.`,
      `**Requirements of the Major** The ${cleanName} program consists of twelve term courses, including (1) one core course in the humanities and one in the social or empirical sciences; (2) two years of a foundational capability (such as a foreign language, advanced programming, or statistical logic, unless waived by examination); (3) one research methods course or an alternative course that either serves to deepen the area of focus or provide methodological tools for the senior essay, selected in consultation with the DUS; (4) four courses in an area of focus; and (5) the senior requirement. The required courses represent the core of the program and are intended to expose the student both to the interdisciplinary nature of ${cleanName} and to the methodologies currently being brought to bear on the study of the discipline.`,
      `**Foundational capability requirement** ${cleanName} majors are required to complete two years of college-level study (or the equivalent) of a foundational capability aligned with their track, and they are encouraged to continue beyond this level. For the requirement to be waived, a student must pass a placement test for admission into an advanced-level course. If the requirement is waived, students must substitute other ${cleanName} courses for the four required courses.`,
      `**Credit/D/Fail** No more than one course taken for Credit/D/Fail may be applied toward the requirements of the major.`,
      `**Outside credit** Courses taken at another institution or during an approved study abroad program at one of Artemis's orbital nodes may count toward the major requirements with DUS approval.`
    ],
    seniorRequirement: `Students are required to complete a senior essay or capstone project working under the guidance of a faculty adviser. With prior approval by the DUS, a combined senior essay may be submitted for those pursuing a second major. A preliminary statement indicating the topic to be addressed and the name of the faculty adviser must be submitted to the DUS by the end of the second week of the fall term in the senior year.`,
    advising: `Students planning to major in ${cleanName} should consult the DUS as early as possible.`,
    summaryDistribution: `1 core course in humanities and 1 in sciences; 2 years of foundational capability; 4 courses and 1 research methods course in focus area`,
    summarySubstitution: `If foundational req is waived, 4 addtl ${cleanName} courses`,
    summarySeniorReq: `Senior essay or capstone project`,
    requirementsArray: [
      `Prerequisite survey course`,
      `1 core course in the humanities`,
      `1 core course in the sciences`,
      `4 courses studying a foundational capability (two-years); other options with DUS approval`,
      `1 research methods course`,
      `4 courses in chosen area of focus`,
      `Senior Essay or Capstone Project`
    ],
    firstYearParagraphs: [
      `The program in ${cleanName} considers the theories, history, practice, and development of the field. Students in the program gain a cross-disciplinary exposure while focusing their studies in a particular discipline such as anthropology, structural economics, history, ${isScience ? 'computational modeling' : 'languages and literatures'}, political science, or sociology, or in an interdisciplinary program such as Global Systems. Artemis has unusually rich resources for the study of ${cleanName}; the Artemis Library and Digital Archives in Malta, notably, possess comprehensive collections.`,
      `Students should begin their foundational study as soon as possible. Those considering a major in ${cleanName} should consult the DUS.`
    ],
    certificateText: `The Department of ${cleanName} offers a Certificate of Advanced Study in specialized sub-fields. A certificate adviser, typically the director of undergraduate studies (DUS), advises students on the certification process and certifies to the University Registrar's Office that students have completed the stated requirements before the end of eight terms of study. The Certificate of Advanced Study, once certified, is listed on the student's transcript.`,
    certificateRequirements: `Students seeking to earn the certificate are required to take four courses beyond the introductory level in their chosen specialization, at least two of which must be Artemis courses designated as advanced (Level 5). All courses must be taken for a letter grade, and students must achieve a grade of B or above. With the approval of the adviser, one advanced non-Level 5 Artemis course, such as an independent study course, may count toward certification requirements.`,
    facultyProfessors: "Dr. Elara Mediterranean (Interdisciplinary Theory), Dr. Julian Vance (Applied Methodology), Dr. Cassandra Whitfield (Comparative Analysis)",
    facultyAssociate: "Dr. Renata Almeida (Global Systems), Dr. Henrik Johansson (Structural Frameworks)",
    facultyAssistant: "Dr. Priya Narayan (Emerging Methodologies), Dr. Kwame Asante (Field Applications)",
    facultyLecturers: "Dr. Sofia Petros (Laboratory Instruction), Dr. Daniel Okello (Practicum Coordination), Dr. Mei-Lin Zhao (Clinical Training)",
    roadmapText: `See the Roadmap Library for a visual representation of the ${cleanName} major.`,
    coursesLinks: [
      { label: `View ${cleanName} Courses`, link: "#" },
      { label: `View Related Methodology Courses`, link: "#" }
    ]
  };
};
