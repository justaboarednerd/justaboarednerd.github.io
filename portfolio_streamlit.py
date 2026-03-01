"""
Portfolio Website avec Streamlit
Alternative moderne et interactive au HTML statique
"""

import streamlit as st
import base64
from pathlib import Path

# Configuration de la page
st.set_page_config(
    page_title="Hamza Bendaoud | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Custom
st.markdown("""
    <style>
    .main {
        padding: 0rem 0rem;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
    }
    h1 {
        color: #1A1A2E;
        font-size: 3rem;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    h2 {
        color: #0F3460;
        border-bottom: 3px solid #E94560;
        padding-bottom: 0.5rem;
    }
    .tagline {
        text-align: center;
        font-size: 1.3rem;
        color: #6C757D;
        margin-bottom: 2rem;
    }
    .project-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #E94560;
    }
    .stat-card {
        background: linear-gradient(135deg, #0F3460, #E94560);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
    }
    .stat-number {
        font-size: 2.5rem;
        font-weight: bold;
    }
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    .skill-badge {
        background: #F8F9FA;
        color: #0F3460;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        display: inline-block;
        margin: 0.2rem;
    }
    .contact-link {
        display: inline-block;
        padding: 0.5rem 1rem;
        background: #E94560;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        margin: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("## 📍 Navigation")
    page = st.radio(
        "",
        ["🏠 Home", "👤 About", "💼 Projects", "🛠️ Skills", "💼 Experience", "📬 Contact"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### 📄 Quick Links")
    st.markdown("[📥 Download Resume](#)")
    st.markdown("[💼 LinkedIn](https://www.linkedin.com/in/hamza-bendaoud/)")
    st.markdown("[💻 GitHub](https://github.com/hamzabendaoud)")
    
    st.markdown("---")
    st.markdown("### 📊 Stats")
    st.metric("Projects", "6+")
    st.metric("Experience", "3+ years")
    st.metric("Technologies", "20+")

# ============================================
# HOME PAGE
# ============================================
if page == "🏠 Home":
    # Hero Section
    st.markdown("<h1>Hamza Bendaoud</h1>", unsafe_allow_html=True)
    st.markdown("<p class='tagline'>Software Engineer | Distributed Systems & Machine Learning</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/hamza-bendaoud/)")
        st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/hamzabendaoud)")
    
    st.markdown("---")
    
    # Quick Stats
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">3+</div>
            <div class="stat-label">Years Experience</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">6+</div>
            <div class="stat-label">Major Projects</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">100K+</div>
            <div class="stat-label">Data Points Processed</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Featured Projects Preview
    st.markdown("## ⭐ Featured Projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 Buyer Index Optimizer")
        st.markdown("""
        ML-powered campaign optimization engine processing **1M+ events/day**, 
        achieving **85% prediction accuracy** and **32% ROAS improvement**.
        """)
        st.markdown("**Tech:** Python • XGBoost • PySpark • FastAPI • Streamlit")
        st.button("View Project →", key="buyer_index")
    
    with col2:
        st.markdown("### 🤖 AI-Powered RAG System")
        st.markdown("""
        Production-ready RAG system handling **1000+ daily queries** with **95% satisfaction**, 
        achieving **200ms average response time**.
        """)
        st.markdown("**Tech:** LangChain • FastAPI • Pinecone • Redis • PostgreSQL")
        st.button("View Project →", key="rag_system")

# ============================================
# ABOUT PAGE
# ============================================
elif page == "👤 About":
    st.markdown("## About Me")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        Hi! I'm **Hamza Bendaoud**, a Software Engineer from **École Centrale** with a passion for 
        building scalable distributed systems and deploying machine learning models in production.
        
        I've worked at:
        - **Safran Aircraft Engines** - Building performance data systems
        - **ONCF (Moroccan Railways)** - ML pipelines for predictive maintenance
        - **Royal Air Maroc** - Workforce management platforms
        
        My experience spans backend engineering, ML systems, data pipelines, and cloud infrastructure. 
        I love solving complex technical challenges and shipping products that scale.
        
        ### 🏆 Achievements
        - **Regional Representative**, Mathematical Olympiad
        - **Member**, MathsMaroc (National Math Olympiad preparation)
        - **GPA**: 4.15/5 (MIT Scale)
        
        ### 🎯 What I'm Looking For
        I'm currently seeking opportunities in:
        - Software Engineering (Backend/Distributed Systems)
        - ML Engineering (Production ML Systems)
        - Data Engineering (Pipelines, Spark, Kafka)
        
        Particularly interested in **FAANG** and high-growth tech companies.
        """)
    
    with col2:
        st.info("""
        **📍 Location**  
        Melun, France
        
        **🎓 Education**  
        École Centrale Supélec  
        École Centrale Casablanca  
        ESSEC Business School
        
        **💬 Languages**  
        • French (Fluent - C1)  
        • English (Fluent - C1)  
        • Arabic (Native)
        
        **📧 Contact**  
        hamza.bendaoud@student-cs.fr
        """)

# ============================================
# PROJECTS PAGE
# ============================================
elif page == "💼 Projects":
    st.markdown("## Technical Projects")
    
    # Project 1
    st.markdown("""
    <div class="project-card">
        <h3>🎯 Buyer Index: Campaign Performance Optimizer</h3>
        <p>
            ML-powered decision support engine for commerce media optimization processing 
            <strong>1M+ events/day</strong>, achieving <strong>85% buyer intent prediction accuracy</strong> 
            and <strong>32% ROAS improvement</strong> through dynamic budget allocation.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Key Features:**")
        st.markdown("• Multi-scenario addressability")
        st.markdown("• Real-time scoring (<100ms)")
        st.markdown("• Budget optimization (Linear Programming)")
    with col2:
        st.markdown("**Impact:**")
        st.markdown("• 32% ROAS improvement")
        st.markdown("• 85% prediction accuracy")
        st.markdown("• 1M+ events/day processing")
    with col3:
        st.markdown("**Technologies:**")
        st.markdown("• Python • XGBoost • PySpark")
        st.markdown("• FastAPI • Streamlit • PostgreSQL")
        st.markdown("• Docker • Linear Programming")
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("🔗 Live Demo", key="buyer_demo")
    with col2:
        st.button("💻 View Code", key="buyer_code")
    
    st.markdown("---")
    
    # Project 2
    st.markdown("""
    <div class="project-card">
        <h3>🤖 AI-Powered Virtual Customer Teleadvisor (LLM & RAG)</h3>
        <p>
            Production-ready Retrieval-Augmented Generation system handling <strong>1000+ daily queries</strong> 
            with <strong>95% user satisfaction</strong>, achieving <strong>200ms average response time</strong> 
            through async endpoints and Redis caching.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Key Features:**")
        st.markdown("• Hybrid search (vector + keyword)")
        st.markdown("• A/B-tested prompt engineering")
        st.markdown("• Real-time monitoring")
    with col2:
        st.markdown("**Impact:**")
        st.markdown("• 95% user satisfaction")
        st.markdown("• 200ms avg response time")
        st.markdown("• 1000+ daily queries")
    with col3:
        st.markdown("**Technologies:**")
        st.markdown("• LangChain • FastAPI • Pinecone")
        st.markdown("• Elasticsearch • Redis • PostgreSQL")
        st.markdown("• Prometheus • Grafana • Docker")
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("🔗 Live Demo", key="rag_demo")
    with col2:
        st.button("💻 View Code", key="rag_code")
    
    st.markdown("---")
    
    # Project 3
    st.markdown("""
    <div class="project-card">
        <h3>🕶️ AI-Powered Augmented Reality Smart Glasses</h3>
        <p>
            End-to-end multimodal AI platform integrating computer vision, NLP, and speech processing 
            with <strong>real-time performance (<100ms latency)</strong> using WebRTC streaming and 
            optimized neural networks.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Key Features:**")
        st.markdown("• Multimodal AI (CV + NLP + Speech)")
        st.markdown("• Real-time AR rendering")
        st.markdown("• Edge computing")
    with col2:
        st.markdown("**Impact:**")
        st.markdown("• <100ms latency")
        st.markdown("• 100+ concurrent users")
        st.markdown("• Auto-scaling infrastructure")
    with col3:
        st.markdown("**Technologies:**")
        st.markdown("• TensorFlow • Flask • WebRTC")
        st.markdown("• React • AWS • YOLO")
        st.markdown("• GPT • Whisper • Edge Computing")
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("🔗 Demo Video", key="ar_demo")
    with col2:
        st.button("💻 View Code", key="ar_code")

# ============================================
# SKILLS PAGE
# ============================================
elif page == "🛠️ Skills":
    st.markdown("## Technical Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💻 Languages")
        skills = ["Python", "Java", "C#", "SQL", "JavaScript", "C++", "Bash"]
        st.markdown(" ".join([f'<span class="skill-badge">{s}</span>' for s in skills]), unsafe_allow_html=True)
        
        st.markdown("### 🔧 Backend & APIs")
        skills = ["FastAPI", "Flask", "Django", "REST APIs", "GraphQL", "Microservices", "gRPC"]
        st.markdown(" ".join([f'<span class="skill-badge">{s}</span>' for s in skills]), unsafe_allow_html=True)
        
        st.markdown("### 🧠 ML/AI")
        skills = ["TensorFlow", "PyTorch", "Scikit-learn", "Hugging Face", "LangChain", "RAG", "YOLO", "GPT"]
        st.markdown(" ".join([f'<span class="skill-badge">{s}</span>' for s in skills]), unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📊 Data Engineering")
        skills = ["Apache Spark", "Kafka", "Pandas", "NumPy", "ETL Pipelines", "Stream Processing"]
        st.markdown(" ".join([f'<span class="skill-badge">{s}</span>' for s in skills]), unsafe_allow_html=True)
        
        st.markdown("### ☁️ Cloud & DevOps")
        skills = ["AWS", "Docker", "Kubernetes", "CI/CD", "Terraform", "GitHub Actions"]
        st.markdown(" ".join([f'<span class="skill-badge">{s}</span>' for s in skills]), unsafe_allow_html=True)
        
        st.markdown("### 🗄️ Databases")
        skills = ["PostgreSQL", "MongoDB", "Redis", "Elasticsearch", "Pinecone", "MySQL"]
        st.markdown(" ".join([f'<span class="skill-badge">{s}</span>' for s in skills]), unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 📈 Proficiency Levels")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Expert**")
        st.progress(0.95)
        st.caption("Python • FastAPI • PostgreSQL • Docker")
        
        st.markdown("**Advanced**")
        st.progress(0.85)
        st.caption("TensorFlow • AWS • Spark • Kafka")
    
    with col2:
        st.markdown("**Proficient**")
        st.progress(0.75)
        st.caption("PyTorch • Kubernetes • React • MongoDB")
        
        st.markdown("**Intermediate**")
        st.progress(0.60)
        st.caption("Java • C# • GraphQL • Terraform")

# ============================================
# EXPERIENCE PAGE
# ============================================
elif page == "💼 Experience":
    st.markdown("## Professional Experience")
    
    # Safran
    st.markdown("### Software Engineer Intern")
    st.markdown("**Safran Aircraft Engines** | *Jun 2024 - Dec 2024* | France")
    st.markdown("""
    - Architected automated Python pipelines processing **100K+ simulation data points**, 
      reducing manual processing time by **85%**
    - Built scalable RESTful APIs serving **50+ concurrent users** with **sub-200ms p95 latency**
    - Deployed CI/CD pipelines with Docker and **95% code coverage**, reducing deployment time 
      from hours to **minutes**
    """)
    
    with st.expander("🔍 View Details"):
        st.markdown("""
        **Key Achievements:**
        - 3x throughput improvement through parallel execution
        - 60% dashboard load time improvement via caching
        - Zero-downtime releases with containerization
        
        **Technologies:**
        Python • FastAPI • PostgreSQL • Docker • Multiprocessing • Async I/O
        """)
    
    st.markdown("---")
    
    # ONCF
    st.markdown("### Backend Engineer & ML Systems Intern")
    st.markdown("**Office National des Chemins de Fer (ONCF)** | *Apr 2023 - Aug 2023* | Morocco")
    st.markdown("""
    - Engineered end-to-end ML pipeline processing real-time sensor data from **200+ locomotives**
    - Developed FastAPI backend handling **10K+ requests/day** with **99.9% uptime**
    - Achieved **5x performance improvement** on critical analytical workloads
    """)
    
    with st.expander("🔍 View Details"):
        st.markdown("""
        **Key Achievements:**
        - 70% training time reduction through distributed computing
        - 45% reduction in data quality issues
        - Real-time monitoring and alerting system
        
        **Technologies:**
        Apache Spark • Kafka • FastAPI • PostgreSQL • Ray • Python
        """)
    
    st.markdown("---")
    
    # RAM
    st.markdown("### Full-Stack Developer Intern")
    st.markdown("**Royal Air Maroc** | *Jul 2022 - Sep 2022* | Morocco")
    st.markdown("""
    - Built workforce management platform serving **500+ users**
    - Reduced manual report generation time by **80%** through automation
    - Achieved **90%+ test coverage** with comprehensive testing suite
    """)
    
    with st.expander("🔍 View Details"):
        st.markdown("""
        **Key Achievements:**
        - RBAC and rate limiting implementation
        - Automated reporting with scheduled jobs
        - Production bug reduction through testing
        
        **Technologies:**
        Django • PostgreSQL • React • REST APIs • Python
        """)

# ============================================
# CONTACT PAGE
# ============================================
elif page == "📬 Contact":
    st.markdown("## Get In Touch")
    
    col1, col2 = st.columns([2,1])
    
    with col1:
        st.markdown("""
        I'm currently **actively looking** for opportunities in:
        - **Software Engineering** (Backend, Distributed Systems)
        - **ML Engineering** (Production ML Systems)
        - **Data Engineering** (Pipelines, Spark, Kafka)
        
        Particularly interested in **FAANG** and high-growth tech companies.
        
        Whether you want to discuss a project, a job opportunity, or just say hi, 
        feel free to reach out!
        """)
        
        st.markdown("### 📧 Email")
        st.markdown("[hamza.bendaoud@student-cs.fr](mailto:hamza.bendaoud@student-cs.fr)")
        st.markdown("[hamouzy11@gmail.com](mailto:hamouzy11@gmail.com)")
        
        st.markdown("### 💼 LinkedIn")
        st.markdown("[linkedin.com/in/hamza-bendaoud](https://www.linkedin.com/in/hamza-bendaoud/)")
        
        st.markdown("### 💻 GitHub")
        st.markdown("[github.com/hamzabendaoud](https://github.com/hamzabendaoud)")
        
        st.markdown("### 📱 Phone")
        st.markdown("+33 7 52 75 30 82")
    
    with col2:
        st.info("""
        **📍 Location**  
        Melun, France
        
        **🌍 Open to**  
        • Remote work  
        • Hybrid  
        • Relocation
        
        **📅 Availability**  
        Immediately
        
        **💼 Work Authorization**  
        EU/France
        """)
        
        st.success("""
        **📥 Download Resume**  
        [PDF Version](#)
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #6C757D; padding: 2rem;'>
    <p>© 2025 Hamza Bendaoud | Built with Streamlit & Python</p>
    <p>⭐ Open to opportunities | 🚀 Always learning</p>
</div>
""", unsafe_allow_html=True)
