
import streamlit as st
from PIL import Image
import pandas as pd

#Page configuration
st.set_page_config(
    page_title="Your Name - Portfolio",
    page_icon="👋",
    layout="wide"
)


#Custom CSS for styling
def local_css():
    st.markdown("""
    <style>
        .main-header {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .section-header {
            font-size: 1.8rem;
            font-weight: bold;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid #4Df968;
            padding-bottom: 0.5rem;
        }
        .highlight {
            color: #4Df968;
        }
        .project-card {
            background-color: #f0f2f6;
            border-radius: 10px;
            padding: 1.5rem;
            margin-bottom: 1rem;
        }
        .skill-box {
            background-color: #e0e0e0;
            border-radius: 5px;
            padding: 0.5rem;
            margin: 0.25rem;
            display: inline-block;
        }
        .social-icons {
            font-size: 1.5rem;
            margin-right: 10px;
        }
        .cert-box {
            background-color: #f0f2f6;
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)


local_css()


# Profile header section with photo, name and social links
def profile_header():
    col1, col2 = st.columns([1, 3])

    with col1:
        # Replace with your own image path
        st.image("https://via.placeholder.com/300", width=200)

    with col2:
        st.markdown('<div class="main-header">Your Name</div>', unsafe_allow_html=True)
        st.markdown('### Data Scientist | ML Engineer | Python Developer')

        # Social media links
        social_html = """
        <div>
            <a href="https://linkedin.com/in/yourusername" target="_blank">
                <i class="social-icons">💼</i>LinkedIn
            </a>
            &nbsp;&nbsp;
            <a href="https://github.com/yourusername" target="_blank">
                <i class="social-icons">💻</i>GitHub
            </a>
            &nbsp;&nbsp;
            <a href="mailto:your.email@example.com" target="_blank">
                <i class="social-icons">📧</i>Email
            </a>
            &nbsp;&nbsp;
            <a href="https://twitter.com/yourusername" target="_blank">
                <i class="social-icons">🐦</i>Twitter
            </a>
        </div>
        """
        st.markdown(social_html, unsafe_allow_html=True)

        st.download_button(
            label="📄 Download Resume",
            data=open("your_resume.pdf", "rb").read() if False else b"Placeholder for resume data",
            file_name="your_name_resume.pdf",
            mime="application/pdf"
        )


# Summary section
def summary_section():
    st.markdown('<div class="section-header">Summary</div>', unsafe_allow_html=True)
    st.write("""
    Experienced data scientist with 5+ years of expertise in machine learning, data analysis, and software development.
    Proven track record of delivering impactful solutions across finance, e-commerce, and healthcare industries.
    Passionate about leveraging data to solve complex problems and drive business growth.
    Skilled in Python, SQL, machine learning frameworks, and cloud technologies.
    """)


# Education section
def education_section():
    st.markdown('<div class="section-header">Education</div>', unsafe_allow_html=True)

    education = [
        {
            "degree": "Master of Science in Data Science",
            "institution": "Example University",
            "location": "City, Country",
            "period": "2018 - 2020",
            "details": "GPA: 3.9/4.0\nSpecialization in Machine Learning\nRelevant coursework: Advanced Machine Learning, Deep Learning, Big Data Analytics, Statistical Methods"
        },
        {
            "degree": "Bachelor of Science in Computer Science",
            "institution": "Another University",
            "location": "City, Country",
            "period": "2014 - 2018",
            "details": "GPA: 3.8/4.0\nMinor in Mathematics\nRelevant coursework: Algorithms, Data Structures, Database Systems, Software Engineering"
        }
    ]

    for edu in education:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"### {edu['degree']}")
            st.markdown(f"**{edu['institution']}**, {edu['location']}")
            st.markdown(edu['details'])
        with col2:
            st.markdown(f"**{edu['period']}**")
        st.markdown("---")


# Experience section
def experience_section():
    st.markdown('<div class="section-header">Experience</div>', unsafe_allow_html=True)

    experiences = [
        {
            "title": "Senior Data Scientist",
            "company": "Example Corp",
            "location": "City, Country",
            "period": "Jan 2022 - Present",
            "description": """
            - Led a team of 5 data scientists in developing predictive models that increased customer retention by 20%
            - Implemented an end-to-end machine learning pipeline using AWS SageMaker, reducing model deployment time by 40%
            - Created a recommendation system that boosted product engagement by 15% and increased revenue by $1.2M annually
            - Collaborated with cross-functional teams to integrate data solutions into production systems
            """
        },
        {
            "title": "Data Scientist",
            "company": "Tech Solutions Inc.",
            "location": "City, Country",
            "period": "Mar 2020 - Dec 2021",
            "description": """
            - Developed NLP models to analyze customer feedback, identifying key improvement areas that increased satisfaction scores by 25%
            - Built and optimized ETL processes for data integration, improving data processing speed by 60%
            - Created interactive dashboards using Tableau to visualize KPIs for executive leadership
            - Mentored junior data analysts in machine learning techniques and best practices
            """
        },
        {
            "title": "Data Analyst",
            "company": "Analytics Firm",
            "location": "City, Country",
            "period": "Jun 2018 - Feb 2020",
            "description": """
            - Performed exploratory data analysis for client projects across retail, healthcare, and finance sectors
            - Developed SQL queries and data pipelines to extract insights from structured and unstructured data
            - Created statistical models to forecast sales trends, achieving 92% accuracy
            - Presented data-driven recommendations to stakeholders, resulting in 15% cost reduction
            """
        }
    ]

    for exp in experiences:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"### {exp['title']}")
            st.markdown(f"**{exp['company']}**, {exp['location']}")
            st.markdown(exp['description'])
        with col2:
            st.markdown(f"**{exp['period']}**")
        st.markdown("---")


# Skills section
def skills_section():
    st.markdown('<div class="section-header">Skills</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    # Technical Skills
    with col1:
        st.markdown("### Technical Skills")
        tech_skills = {
            "Python": 90,
            "SQL": 85,
            "R": 70,
            "TensorFlow/PyTorch": 80,
            "Scikit-Learn": 90,
            "Pandas/NumPy": 95,
            "Streamlit/Dash": 75,
            "Docker": 70
        }

        for skill, proficiency in tech_skills.items():
            st.markdown(f"**{skill}**")
            st.progress(proficiency / 100)

    # Data Science Skills
    with col2:
        st.markdown("### Data Science")
        ds_skills = {
            "Machine Learning": 90,
            "Deep Learning": 80,
            "NLP": 85,
            "Computer Vision": 75,
            "Statistical Analysis": 90,
            "Data Visualization": 85,
            "Feature Engineering": 90,
            "A/B Testing": 80
        }

        for skill, proficiency in ds_skills.items():
            st.markdown(f"**{skill}**")
            st.progress(proficiency / 100)

    # Other Skills & Tools
    with col3:
        st.markdown("### Tools & Platforms")
        other_skills = {
            "AWS": 80,
            "GCP": 70,
            "Azure": 65,
            "Git/GitHub": 90,
            "Tableau": 80,
            "Power BI": 75,
            "Kubernetes": 65,
            "CI/CD": 70
        }

        for skill, proficiency in other_skills.items():
            st.markdown(f"**{skill}**")
            st.progress(proficiency / 100)


# Projects section
def projects_section():
    st.markdown('<div class="section-header">Projects</div>', unsafe_allow_html=True)

    projects = [
        {
            "title": "Customer Churn Prediction System",
            "description": "Developed a machine learning model to predict customer churn for a telecom company, resulting in a 30% reduction in customer attrition. Implemented end-to-end pipeline from data preprocessing to model deployment.",
            "tech": ["Python", "Scikit-Learn", "XGBoost", "Flask", "AWS"],
            "link": "https://github.com/yourusername/churn-prediction"
        },
        {
            "title": "Sentiment Analysis for Product Reviews",
            "description": "Created an advanced NLP model to analyze product reviews sentiment across multiple e-commerce platforms. Built a dashboard to visualize trends and insights from over 1 million reviews.",
            "tech": ["Python", "BERT", "PyTorch", "Streamlit", "MongoDB"],
            "link": "https://github.com/yourusername/sentiment-analysis"
        },
        {
            "title": "Real-time Stock Portfolio Tracker",
            "description": "Designed and implemented a real-time dashboard to track stock portfolios, including performance metrics, risk analysis, and automated alerts based on predefined conditions.",
            "tech": ["Python", "Pandas", "Plotly", "Streamlit", "Flask", "REST APIs"],
            "link": "https://github.com/yourusername/stock-tracker"
        },
        {
            "title": "Medical Image Classification",
            "description": "Developed a deep learning model to classify medical images for early disease detection, achieving 94% accuracy. Implemented a user-friendly interface for medical professionals.",
            "tech": ["Python", "TensorFlow", "CNN", "OpenCV", "Docker", "Kubernetes"],
            "link": "https://github.com/yourusername/medical-image-classifier"
        }
    ]

    col1, col2 = st.columns(2)
    cols = [col1, col2]

    for i, project in enumerate(projects):
        with cols[i % 2]:
            with st.container():
                st.markdown(f"""
                <div class="project-card">
                    <h3>{project['title']}</h3>
                    <p>{project['description']}</p>
                    <p><b>Technologies:</b> {', '.join(project['tech'])}</p>
                    <a href="{project['link']}" target="_blank">View Project →</a>
                </div>
                """, unsafe_allow_html=True)


# Certifications section
def certifications_section():
    st.markdown('<div class="section-header">Certifications</div>', unsafe_allow_html=True)

    certifications = [
        {
            "name": "AWS Certified Machine Learning - Specialty",
            "issuer": "Amazon Web Services",
            "date": "Feb 2023",
            "credential_id": "AWS-ML-12345"
        },
        {
            "name": "TensorFlow Developer Certificate",
            "issuer": "Google",
            "date": "Oct 2022",
            "credential_id": "TF-DEV-67890"
        },
        {
            "name": "Microsoft Certified: Azure Data Scientist Associate",
            "issuer": "Microsoft",
            "date": "May 2022",
            "credential_id": "MSFT-DS-54321"
        },
        {
            "name": "Deep Learning Specialization",
            "issuer": "Coursera/DeepLearning.AI",
            "date": "Jan 2022",
            "credential_id": "DL-SPEC-98765"
        }
    ]

    col1, col2 = st.columns(2)
    cols = [col1, col2]

    for i, cert in enumerate(certifications):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="cert-box">
                <h3>{cert['name']}</h3>
                <p><b>Issuer:</b> {cert['issuer']}</p>
                <p><b>Date:</b> {cert['date']}</p>
                <p><b>Credential ID:</b> {cert['credential_id']}</p>
            </div>
            """, unsafe_allow_html=True)


# Main function to display all sections
def main():
    # Navigation tabs
    st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        font-size: 16px;
    }
    </style>""", unsafe_allow_html=True)

    tabs = st.tabs(["Summary", "Experience", "Education", "Skills", "Projects", "Certifications"])

    # Profile header is always visible at the top
    profile_header()

    # Display content based on selected tab
    with tabs[0]:
        summary_section()

    with tabs[1]:
        experience_section()

    with tabs[2]:
        education_section()

    with tabs[3]:
        skills_section()

    with tabs[4]:
        projects_section()

    with tabs[5]:
        certifications_section()

    # Footer
    st.markdown("---")
    st.markdown("© 2025 Your Name. All rights reserved.")


if __name__ == "__main__":
    main()




























