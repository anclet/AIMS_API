
# # db.py
# from typing import Dict, Any
# from datetime import datetime


# # AIMS Rwanda Complete Database Structure
# aims_db: Dict[str, Any] = {
#     "overview": {
#         "institution_name": "African Institute for Mathematical Sciences (AIMS) Rwanda",
#         "location": "Remera, KN3, Kigali, Rwanda",
#         "established": 2016,
#         "mission": "To empower talented young Africans to be creative leaders in science and technology.",
#         "vision": "A prosperous Africa, propelled by innovative education and mathematical science.",
#         "focus_areas": [
#             "Mathematical Sciences",
#             "Climate Science",
#             "Machine Intelligence",
#             "Big Data",
#             "Computational Methods",
#             "STEM Education",
#             "AI Research"
#         ],
#         "values": [
#             "Excellence",
#             "Equity and Inclusion",
#             "Pan-Africanism",
#             "Integrity"
#         ],
#         "campus_info": {
#             "address": "AIMS Rwanda Centre, Sector Remera, KN3 Kigali, Rwanda",
#             "facilities": ["Research Centre", "Incubator", "Computer Labs", "Lecture Halls", "Student Accommodation"],
#             "capacity": "100+ postgraduate students annually"
#         }
#     },

#     "governance": {
#         "centre_president": "Prof. Dr. Sam Yala",
#         "description": "AIMS Rwanda is guided by a team of academic leaders and administrators, ensuring academic excellence and strategic direction."
#     },

#     "partners": [
#         "National Institute of Statistics of Rwanda (NISR)",
#         "Mastercard Foundation",
#         "Google",
#         "Facebook",
#         "Next Einstein Forum (NEF)",
#         "Open Quantum Institute (OQI)"
#     ],

#     "initiatives": [
#         "Next Einstein Forum (NEF)",
#         "Quantum Leap Africa (QLA)",
#         "Teacher Training Program",
#         "Incubator – Eureka Mu Rugo"
#     ],

#     "programs": [
#         {
#             "program_id": "MSC_MATH",
#             "name": "Master of Science in Mathematical Sciences",
#             "duration": "1 year",
#             "type": "Masters",
#             "focus_areas": ["Estimation", "Modelling", "Data Analysis", "Foundational Mathematics"],
#             "prerequisites": ["4-year degree in Mathematics", "Engineering", "Physics or related"],
#             "application_deadline": "2025-03-31",
#             "start_date": "2025-09-01",
#             "tuition_fee": "Fully funded (scholarships available)",
#             "description": "Structured program designed to build problem-solving capacity with a core set of mathematical tools.",
#             "career_outcomes": ["PhD", "Data Scientist", "Quantitative Analyst", "Lecturer"],
#             "requirements": {
#                 "gpa": "3.0 minimum",
#                 "english_proficiency": "Not mandatory but may require language classes",
#                 "letters_of_recommendation": 2,
#                 "personal_statement": True
#             }
#         },
#         {
#             "program_id": "MSC_MATH_CLIMATE",
#             "name": "Master’s in Mathematical Sciences – Climate Science Stream",
#             "duration": "1 year",
#             "type": "Masters",
#             "focus_areas": ["Climate Modelling", "Environmental Data", "Sustainable Development"],
#             "prerequisites": ["4-year degree in Science/Engineering with math component"],
#             "application_deadline": "2025-03-31",
#             "start_date": "2025-09-01",
#             "tuition_fee": "Fully funded",
#             "description": "Prepares students to tackle climate change through advanced mathematical tools.",
#             "career_outcomes": ["Climate Analyst", "Environmental Consultant", "Policy Advisor"],
#             "requirements": {
#                 "gpa": "3.0 minimum",
#                 "english_proficiency": "Not required",
#                 "letters_of_recommendation": 2,
#                 "personal_statement": True
#             }
#         },
#         {
#             "program_id": "MSC_COOP",
#             "name": "Co-operative Education Program (Mathematical Sciences)",
#             "duration": "18 months",
#             "type": "Masters",
#             "focus_areas": ["Big Data", "Cybersecurity", "Industry Applications"],
#             "prerequisites": ["Degree in science or engineering with mathematics"],
#             "application_deadline": "2025-03-29",
#             "start_date": "2025-09-01",
#             "tuition_fee": "Full/Partial scholarship",
#             "description": "Blends academic training with six-month industry placements for real-world experience.",
#             "career_outcomes": ["Industry Researcher", "Data Engineer", "AI Specialist"],
#             "requirements": {
#                 "gpa": "3.0 minimum",
#                 "english_proficiency": "Not required",
#                 "letters_of_recommendation": 2,
#                 "personal_statement": True
#             }
#         },
#         {
#             "program_id": "AMMI",
#             "name": "African Master’s in Machine Intelligence (AMMI)",
#             "duration": "1 year",
#             "type": "Masters",
#             "focus_areas": ["Machine Learning", "Deep Learning", "AI Ethics", "Applications of ML in Africa"],
#             "prerequisites": ["Strong background in mathematics and programming"],
#             "application_deadline": "2025-03-31",
#             "start_date": "2025-09-01",
#             "tuition_fee": "Fully funded",
#             "description": "State-of-the-art AI training with support from Google and Facebook, led by world-class faculty.",
#             "career_outcomes": ["AI Researcher", "ML Engineer", "PhD", "Tech Entrepreneur"],
#             "requirements": {
#                 "gpa": "3.5 minimum",
#                 "english_proficiency": "Not required",
#                 "letters_of_recommendation": 2,
#                 "personal_statement": True
#             }
#         }
#     ],

#     "research": {
#         "research_focus": [
#             "Data Science",
#             "Quantum Information",
#             "Smart Systems",
#             "AI for Sustainable Development"
#         ],
#         "research_entities": [
#             "Research Chairs",
#             "Research Fellows",
#             "Research Conferences",
#             "Research Publications"
#         ]
#     },

#     "students": {
#         "total_trained": 412,
#         "multicultural_environment": True,
#         "features": [
#             "24-hour tutor-student interaction",
#             "Pan-African representation",
#             "Global faculty"
#         ]
#     },

#     "alumni": {
#         "total_graduates": "3500+ across Africa",
#         "fields": ["ICT", "Data Science", "Engineering", "Education", "Research"]
#     },

#     "staff": {
#         "visiting_lecturers": "International scholars from partner institutions",
#         "tutors": "Resident academic staff supporting students daily",
#         "support": "Admin and operations team"
#     },

#     "calendar": {
#         "academic_year": "September to August",
#         "events": [
#             {
#                 "name": "International Day of Women and Girls in Science",
#                 "date": "February 9, 2024"
#             },
#             {
#                 "name": "Siyakhula Festival",
#                 "date": "March 17–22, 2024"
#             },
#             {
#                 "name": "International Day of Mathematics",
#                 "date": "March 14, 2024"
#             },
#             {
#                 "name": "8th Cohort Graduation",
#                 "date": "July 2024"
#             }
#         ]
#     },

#     "contact": {
#         "email": "info@aims.ac.rw",
#         "phone": "+250 788 312 469",
#         "address": "AIMS Rwanda Centre, Sector Remera, KN3 Kigali, Rwanda",
#         "faq": "https://aims.ac.rw/faqs",
#         "support_form": "https://aims.ac.rw/contact-us"
#     }
# }

#db.py
from typing import Dict, Any, List
from datetime import datetime

# AIMS Rwanda Enhanced Complete Database Structure
aims_db: Dict[str, Any] = {
    "about_aims": {
        "institution_name": "African Institute for Mathematical Sciences (AIMS) Rwanda",
        "location": "Remera, KN3, Kigali, Rwanda",
        "established": 2016,
        "establishment_context": "Established with the support of the government of Rwanda as the fifth Center of Excellence under the AIMS Global network",
        "network_centers": ["South Africa", "Senegal", "Ghana", "Cameroon", "Rwanda"],
        "mission": "To empower talented young Africans to be creative leaders in science and technology.",
        "vision": "A prosperous Africa, propelled by innovative education and mathematical science.",
        "focus_areas": [
            "Mathematical Sciences",
            "Climate Science",
            "Machine Intelligence",
            "Big Data",
            "Computational Methods",
            "STEM Education",
            "AI Research"
        ],
        "values": [
            "Excellence",
            "Equity and Inclusion",
            "Pan-Africanism",
            "Integrity"
        ],
        "campus_info": {
            "address": "AIMS Rwanda Centre, Sector Remera, KN3 Kigali, Rwanda",
            "facilities": ["Research Centre", "Incubator", "Computer Labs", "Lecture Halls", "Student Accommodation"],
            "capacity": "100+ postgraduate students annually"
        },
        "key_achievements": {
            "graduates_since_inception": "450+ students",
            "women_participation": "38%",
            "strategic_alignment": "Leverages Rwanda's brilliant young talent for ICT, Science and private sector growth targets"
        },
        "unique_model": {
            "pan_african_focus": True,
            "broad_curriculum": True,
            "independent_critical_thinking": True,
            "modern_computation_techniques": True,
            "research_components": True,
            "student_support": [
                "Full bursary support",
                "Continuous access to computing, internet and electricity",
                "Close interaction with full-time tutors",
                "Visiting professors",
                "Highly conducive environment"
            ]
        }
    },

    "leadership": {
        "centre_president": {
            "name": "Prof. Dr. Sam Yala",
            "title": "AIMS Network President and AIMS Rwanda Centre President",
            "tenure": "Since 2018",
            "background": {
                "experience": "15+ years dual professional track in academia and high-tech industry in Europe and Africa",
                "specialization": "Advanced technologies and innovation, including blockchain and crypto security",
                "leadership_expertise": "Leading multidisciplinary and multicultural teams in academia and industry"
            },
            "education": [
                "PhD in Applied Sciences from Louvain School of Engineering",
                "Business Administration degree from Louvain School of Management"
            ],
            "academic_position": "Professor of Electronics and Computer Security",
            "research_focus": [
                "Digital control engineering using power electronics",
                "Applied cryptography and computer security"
            ],
            "responsibilities": "Oversees and advances the organization's mission of empowering talented young Africans to become creative leaders in science and technology"
        },
        "research_and_innovation_president": {
            "name": "Prof. Wilfred Ndifon",
            "title": "AIMS Research and Innovation Centre President and Chief Scientific Officer, AIMS Global Network",
            "specialization": "Theoretical biologist conducting research at the interface of mathematical and biological sciences",
            "education": [
                "M.Sc from Princeton University",
                "PhD from Princeton University"
            ],
            "mentorship": "Mentored dozens of AIMS students, several obtained PhD degrees under his supervision and progressed to productive careers in academia and industry"
        },
        "academic_director": {
            "name": "Prof. Blaise Tchapnda",
            "title": "Academic Director, AIMS Rwanda",
            "responsibilities": "Responsible for all academic matters at AIMS Rwanda",
            "specialization": "Analysis of hyperbolic Differential equations such as Einstein's equations of General Relativity",
            "education": [
                "M.Sc. in Mathematics from University of Yaounde, Cameroon",
                "PhD in Mathematics from University of Yaounde, Cameroon",
                "Second PhD in Mathematics from Technical University of Berlin"
            ],
            "fellowships_and_associations": [
                "Postdoctoral fellow with Max-Planck Institute for Gravitational Physics in Potsdam",
                "Junior associate with the Abdus Salam International Centre for Theoretical Physics (ICTP) of Trieste, Italy (2002-2010)",
                "Regular Associated with ICTP (2015-2020)"
            ],
            "previous_position": "Associate Professor of Mathematics with the University of Yaounde 1",
            "experience": "Over 25 years of experience in training students in Mathematics"
        }
    },

    "faculty_and_staff": {
        "senior_faculty": [
            {
                "name": "Dr. rer. nat. habil. Abebe Geletu W. Selassie",
                "title": "Professor - German Research Chair at AIMS Rwanda",
                "joined": "September 2021",
                "education": [
                    "B.Sc. in Mathematics (1987) from Addis Ababa University, Ethiopia",
                    "M.Sc. in Applied Optimization (1995) from Addis Ababa University, Ethiopia",
                    "Ph.D. in Computational Optimization (2004) from Technology University of Ilmenau, Germany",
                    "Habilitus in Systems Optimization (2018) from Technology University of Ilmenau, Germany"
                ],
                "career_background": [
                    "Lecturer at Haramaya University, Ethiopia (1989-1998)",
                    "Academic staff and senior research scientist at Technology University of Ilmenau, Germany (24 years)"
                ],
                "expertise": [
                    "Applied mathematics",
                    "Numerical methods of optimization",
                    "Stochastic optimization",
                    "Control engineering",
                    "Data-driven optimization",
                    "Machine learning",
                    "Image processing",
                    "Computer vision"
                ],
                "current_research_interests": [
                    "Mathematical optimization, intelligent and predictive control applications",
                    "Big-data analytics, data-driven methods, and machine learning applications",
                    "Optimization, AI and advanced technology implementation for African sustainability systems",
                    "Optimization and Deep Learning methods for image processing and computer vision",
                    "Systems development and modernization of African agrifood supply-chain"
                ]
            }
        ],
        "academic_staff": [
            {
                "name": "Dr. Leila Zahhafi",
                "title": "Former Head Tutor (2023-2024), AIMS Rwanda",
                "current_status": "PhD Graduate in Applied Mathematics and Computer Science, Currently doing Postdoctoral",
                "specialization": "Public key Cryptography",
                "background": "Academic journey spanning from engineering degree to active participation in various academic laboratories",
                "skills": [
                    "Mathematics",
                    "Cryptography",
                    "Research methodologies"
                ],
                "teaching_experience": "4 years as teaching assistant at AIMS Senegal and Rwanda",
                "mentoring_abilities": "Strong mentoring abilities supporting students in diverse mathematical disciplines",
                "research_interests": "Intersection of cryptography and machine learning"
            }
        ],
        "industry_initiative": [
            {
                "name": "Dr. Charles Lebon Mberi Kimpolo",
                "title": "Director of the Industry Initiative and Head of the Next Einstein Forum (NEF) at the Global Network Secretariat",
                "experience": "15+ years of industry experience in data analysis, business intelligence and project management",
                "education": "Ph.D. in Computational and Applied Mathematics from the University of the Witwatersrand, Johannesburg, South Africa",
                "responsibilities": [
                    "Strategic oversight and direction to the AIMS Industry Initiative across the Network",
                    "Broadening partnerships with industry in Africa and beyond",
                    "Leading implementation of Work Integrated Learning programs",
                    "Supporting AIMS graduates in transition to employment, entrepreneurship and further study"
                ],
                "vision": "Position AIMS-NEI as the industry's leading academic partner in Africa for industry and economic advancement",
                "expertise": [
                    "Data analysis",
                    "Business intelligence",
                    "Project management",
                    "Agile software development",
                    "Client engagement"
                ],
                "global_involvement": [
                    "Technical Advisory Group (TAG) of the Global Partnership for Sustainable Development Data",
                    "Programme Committee for the United Nations World Data Forum (UNWDF)",
                    "Global Strategy Council of the World Association for Cooperative Education (WACE)"
                ],
                "founded_initiatives": [
                    "Young African Technologists (YAT) - promoting education through technology in underprivileged African communities",
                    "Knowledge Sharing Campaign (KSC) - empowering African student diaspora and reversing brain drain"
                ]
            }
        ]
    },

    "initiatives": {
    "eureka_mu_rugo": {
        "name": "EurekaMuRugo",
        "type": "AIMS Rwanda Incubator",
        "launched": "April 2, 2025",
        "philosophy": "We aspire to be a home for ideas and innovation, right here in Africa",
        "core_belief": "Answer to pressing question: How do universities turn knowledge into real-world solutions?",
        "focus_areas": [
        "Empowering farmers with climate models",
        "Optimizing value chains with data science",
        "Mathematics at the heart of change"
        ],
        "program_structure": {
        "name": "Entrepreneurship & Innovation Programme",
        "purpose": "Nurture the next wave of entrepreneurs, helping them transform ideas into ventures that impact communities"
        },
        "inaugural_competition": {
        "date": "April 2, 2025",
        "format": "Innovation competition pitching",
        "winners": [
            {
            "team": "Oladimeji Samuel Sowole & Jonathan Enudeme",
            "status": "AIMS Alumni",
            "award": "6-month fellowship in AIMS Rwanda Incubator"
            },
            {
            "team": "Lucie Umuhoza & Jeannette Musabyimana",
            "status": "AIMS Alumni",
            "award": "6-month fellowship in AIMS Rwanda Incubator"
            }
        ]
        },
        "support_services": [
        "Mentorship",
        "Training",
        "Resources and support to make ideas market-ready"
        ],
        "mission": "Transform bold ideas into real-world impact through mathematical sciences and innovation"
    },
    "next_einstein_forum": {
        "name": "Next Einstein Forum (NEF)",
        "type": "Pan-African Science and Policy Platform",
        "launched": "2013",
        "philosophy": "Africa’s contribution to global science must be visible, celebrated and scaled.",
        "core_belief": "The next Einstein will be African.",
        "focus_areas": [
        "Public engagement in science",
        "Science policy advocacy",
        "Youth-driven research excellence"
        ],
        "program_structure": {
        "name": "NEF Global Gatherings & Ambassador Program",
        "purpose": "Bridge science, society, and policy through events, fellowships, and youth leadership"
        },
        "flagship_activities": {
        "events": ["NEF Global Gatherings", "Africa Science Week"],
        "fellowships": ["NEF Fellows Program"],
        "community": ["NEF Ambassadors in 54 African countries"]
        },
        "support_services": [
        "Research exposure",
        "Science communication",
        "Networking with policy makers and funders"
        ],
        "mission": "Position Africa as a global hub for science and innovation through advocacy and youth-led scientific excellence."
    },
    "quantum_leap_africa": {
        "name": "Quantum Leap Africa (QLA)",
        "type": "Research Institute under AIMS",
        "launched": "2016",
        "philosophy": "Africa must lead in future-defining technologies like quantum science.",
        "core_belief": "Quantum research is a frontier for solving complex challenges, from health to cybersecurity.",
        "focus_areas": [
        "Quantum computing",
        "Quantum cryptography",
        "Quantum machine learning"
        ],
        "program_structure": {
        "name": "Quantum Research and Education Initiative",
        "purpose": "Advance frontier research in quantum technologies while training Africa’s next quantum leaders"
        },
        "membership": {
        "joined_oqi": "December 3, 2024",
        "initiative": "Open Quantum Institute (OQI)"
        },
        "support_services": [
        "Collaborative research labs",
        "International conferences",
        "Graduate training and mentorship"
        ],
        "mission": "Position Africa at the forefront of quantum science through breakthrough research and capacity building."
    },
    "teacher_training_program": {
        "name": "Teacher Training Program",
        "type": "STEM Education Enhancement",
        "launched": "2018",
        "philosophy": "Strong foundations in math and science start with empowered teachers.",
        "core_belief": "Transforming STEM education begins with investing in educators.",
        "focus_areas": [
        "In-service teacher training",
        "Active learning pedagogy",
        "Digital classroom methods"
        ],
        "program_structure": {
        "name": "Teacher Capacity Building Initiative",
        "purpose": "Enhance the delivery of quality math and science education in secondary schools across Africa"
        },
        "impact_statistics": {
        "teachers_trained": "Over 1000 teachers",
        "regions_covered": ["Rwanda", "Ghana", "Cameroon"]
        },
        "support_services": [
        "Continuous professional development",
        "Training materials",
        "Pedagogical mentorship"
        ],
        "mission": "Equip African secondary school teachers with modern pedagogical skills to elevate STEM education quality."
    }
    },


    "governance": {
        "organizational_structure": "Guided by a team of academic leaders and administrators",
        "focus": "Ensuring academic excellence and strategic direction",
        "network_integration": "Part of the AIMS Global Network spanning across Africa"
    },

    "partners": [
        "Government of Rwanda",
        "National Institute of Statistics of Rwanda (NISR)",
        "Mastercard Foundation",
        "Google",
        "Facebook",
        "Next Einstein Forum (NEF)",
        "Open Quantum Institute (OQI)"
    ],

    "programs": [
        {
            "program_id": "MSC_MATH",
            "name": "Master of Science in Mathematical Sciences",
            "duration": "1 year",
            "type": "Masters",
            "focus_areas": ["Estimation", "Modelling", "Data Analysis", "Foundational Mathematics"],
            "prerequisites": ["4-year degree in Mathematics", "Engineering", "Physics or related"],
            "application_deadline": "2025-03-31",
            "start_date": "2025-09-01",
            "tuition_fee": "Fully funded (scholarships available)",
            "description": "Structured program designed to build problem-solving capacity with a core set of mathematical tools.",
            "career_outcomes": ["PhD", "Data Scientist", "Quantitative Analyst", "Lecturer"],
            "requirements": {
                "gpa": "3.0 minimum",
                "english_proficiency": "Not mandatory but may require language classes",
                "letters_of_recommendation": 2,
                "personal_statement": True
            }
        },
        {
            "program_id": "MSC_MATH_CLIMATE",
            "name": "Master's in Mathematical Sciences – Climate Science Stream",
            "duration": "1 year",
            "type": "Masters",
            "focus_areas": ["Climate Modelling", "Environmental Data", "Sustainable Development"],
            "prerequisites": ["4-year degree in Science/Engineering with math component"],
            "application_deadline": "2025-03-31",
            "start_date": "2025-09-01",
            "tuition_fee": "Fully funded",
            "description": "Prepares students to tackle climate change through advanced mathematical tools.",
            "career_outcomes": ["Climate Analyst", "Environmental Consultant", "Policy Advisor"],
            "requirements": {
                "gpa": "3.0 minimum",
                "english_proficiency": "Not required",
                "letters_of_recommendation": 2,
                "personal_statement": True
            }
        },
        {
            "program_id": "MSC_COOP",
            "name": "Co-operative Education Program (Mathematical Sciences)",
            "duration": "18 months",
            "type": "Masters",
            "focus_areas": ["Big Data", "Cybersecurity", "Industry Applications"],
            "prerequisites": ["Degree in science or engineering with mathematics"],
            "application_deadline": "2025-03-29",
            "start_date": "2025-09-01",
            "tuition_fee": "Full/Partial scholarship",
            "description": "Blends academic training with six-month industry placements for real-world experience.",
            "career_outcomes": ["Industry Researcher", "Data Engineer", "AI Specialist"],
            "requirements": {
                "gpa": "3.0 minimum",
                "english_proficiency": "Not required",
                "letters_of_recommendation": 2,
                "personal_statement": True
            }
        },
        {
            "program_id": "AMMI",
            "name": "African Master's in Machine Intelligence (AMMI)",
            "duration": "1 year",
            "type": "Masters",
            "focus_areas": ["Machine Learning", "Deep Learning", "AI Ethics", "Applications of ML in Africa"],
            "prerequisites": ["Strong background in mathematics and programming"],
            "application_deadline": "2025-03-31",
            "start_date": "2025-09-01",
            "tuition_fee": "Fully funded",
            "description": "State-of-the-art AI training with support from Google and Facebook, led by world-class faculty.",
            "career_outcomes": ["AI Researcher", "ML Engineer", "PhD", "Tech Entrepreneur"],
            "requirements": {
                "gpa": "3.5 minimum",
                "english_proficiency": "Not required",
                "letters_of_recommendation": 2,
                "personal_statement": True
            }
        }
    ],

    "research": {
        "research_focus": [
            "Data Science",
            "Quantum Information",
            "Smart Systems",
            "AI for Sustainable Development",
            "Climate Science and Environmental Modeling",
            "Cryptography and Computer Security",
            "Mathematical Optimization",
            "Machine Learning Applications"
        ],
        "research_entities": [
            "Research Chairs",
            "Research Fellows",
            "Research Conferences",
            "Research Publications"
        ],
        "specialized_research_areas": {
            "sustainability_systems": [
                "Smart water network systems",
                "Microgrid-based renewable energy generation and distribution",
                "African agrifood supply-chain modernization"
            ],
            "applied_mathematics": [
                "Hyperbolic differential equations",
                "Einstein's equations of General Relativity",
                "Computational optimization"
            ],
            "technology_applications": [
                "Image processing and computer vision",
                "Big-data analytics",
                "Predictive control systems"
            ]
        }
    },

    "students": {
        "total_trained": 450,
        "multicultural_environment": True,
        "women_participation_rate": "38%",
        "features": [
            "24-hour tutor-student interaction",
            "Pan-African representation",
            "Global faculty",
            "Full bursary support",
            "Continuous access to computing resources"
        ],
        "target_demographics": "Top African graduates with potential for leadership in science and technology",
        "career_pathways": ["Research", "Industry", "Civil Society", "Entrepreneurship"]
    },

    "alumni": {
        "total_graduates": "3500+ across Africa",
        "fields": ["ICT", "Data Science", "Engineering", "Education", "Research", "Entrepreneurship"],
        "impact": "Productive careers in academia and industry across the continent",
        "notable_achievements": "Several alumni have obtained PhD degrees and progressed to leadership positions"
    },

    "staff": {
        "visiting_lecturers": "International scholars from partner institutions",
        "tutors": "Resident academic staff supporting students daily",
        "support": "Admin and operations team",
        "research_chairs": "Specialized professors leading research initiatives",
        "industry_liaisons": "Professionals bridging academia and industry"
    },

    "calendar": {
        "academic_year": "September to August",
        "events": [
            {
                "name": "International Day of Women and Girls in Science",
                "date": "February 9, 2024"
            },
            {
                "name": "Siyakhula Festival",
                "date": "March 17 to 22, 2024"
            },
            {
                "name": "International Day of Mathematics",
                "date": "March 14, 2024"
            },
            {
                "name": "8th Cohort Graduation",
                "date": "July 28, 2024"
            },
            {
                "name": "EurekaMuRugo Incubator Launch",
                "date": "April 2, 2025"
            },
            {
                "name": "9th Cohort Graduation",
                "date": "July 27, 2025"
            }
        ]
    },

    "contact": {
        "email": "info@aims.ac.rw",
        "phone": "+250 788 312 469",
        "address": "AIMS Rwanda Centre, Sector Remera, KN3 Kigali, Rwanda",
        "faq": "https://aims.ac.rw/faqs",
        "support_form": "https://aims.ac.rw/contact-us"
    }
}