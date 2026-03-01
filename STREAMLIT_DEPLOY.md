# 🎨 Portfolio Streamlit - Deployment Guide

## 🚀 Option Streamlit Cloud (GRATUIT - 10 minutes)

### **Pourquoi Streamlit ?**
✅ **Gratuit** et hosting inclus  
✅ **Tu connais déjà Streamlit**  
✅ **Interactif** et moderne  
✅ **Perfect pour Data/ML projects**  
✅ **Auto-update** quand tu push sur GitHub  

---

## 📋 Étapes de Déploiement

### **Étape 1 : Préparer le Repo GitHub**

```bash
# Crée un nouveau repo
git init
git add .
git commit -m "Initial portfolio commit"
git remote add origin https://github.com/hamzabendaoud/portfolio-streamlit.git
git push -u origin main
```

### **Étape 2 : Structure du Repo**

Ton repo doit contenir :
```
portfolio-streamlit/
├── portfolio_streamlit.py    # L'app principale
├── requirements.txt           # Dépendances
└── README.md                  # Documentation
```

### **Étape 3 : Créer requirements.txt**

```txt
streamlit==1.30.0
```

### **Étape 4 : Déployer sur Streamlit Cloud**

1. Va sur **https://share.streamlit.io/**
2. Connecte-toi avec ton GitHub
3. Clique "New app"
4. Sélectionne :
   - **Repository** : hamzabendaoud/portfolio-streamlit
   - **Branch** : main
   - **Main file path** : portfolio_streamlit.py
5. Clique "Deploy!"

⏱️ **Déploiement : 2-3 minutes**

### **Étape 5 : Accéder**

Ton portfolio sera live à :
**https://hamzabendaoud-portfolio.streamlit.app**

✅ **C'est tout !**

---

## 🎨 Personnalisation

### **Ajouter Tes Projets**

Dans `portfolio_streamlit.py`, section Projects, duplique ce bloc :

```python
st.markdown("""
<div class="project-card">
    <h3>🎯 Ton Projet</h3>
    <p>
        Description avec <strong>métriques quantifiables</strong>
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**Key Features:**")
    st.markdown("• Feature 1")
    st.markdown("• Feature 2")
with col2:
    st.markdown("**Impact:**")
    st.markdown("• Impact 1")
    st.markdown("• Impact 2")
with col3:
    st.markdown("**Technologies:**")
    st.markdown("• Tech 1 • Tech 2")
    st.markdown("• Tech 3 • Tech 4")

col1, col2 = st.columns(2)
with col1:
    st.button("🔗 Live Demo", key="project_demo")
with col2:
    st.button("💻 View Code", key="project_code")
```

### **Changer les Couleurs**

Dans `portfolio_streamlit.py`, section CSS :

```python
:root {
    --primary: #1A1A2E;     # Couleur principale
    --secondary: #0F3460;   # Couleur secondaire
    --accent: #E94560;      # Couleur d'accent
}
```

### **Ajouter des Images**

1. Crée un dossier `images/` dans ton repo
2. Upload tes images
3. Dans le code :

```python
from PIL import Image

image = Image.open('images/project1.png')
st.image(image, caption='Mon Projet')
```

---

## 🔗 Connecter les Liens Externes

### **Boutons avec URLs**

Pour les liens Live Demo, GitHub, etc. :

```python
# Méthode 1 : Markdown link
st.markdown("[🔗 Live Demo](https://your-demo-url.com)")

# Méthode 2 : st.link_button (Streamlit 1.30+)
st.link_button("🔗 Live Demo", "https://your-demo-url.com")

# Méthode 3 : Button + redirect
if st.button("🔗 Live Demo"):
    st.markdown("[Open Demo](https://your-demo-url.com)")
```

### **Download Resume**

Pour permettre le téléchargement de ton CV :

```python
with open("Hamza_Bendaoud_Resume.pdf", "rb") as file:
    btn = st.download_button(
        label="📥 Download Resume",
        data=file,
        file_name="Hamza_Bendaoud_Resume.pdf",
        mime="application/pdf"
    )
```

---

## 📊 Analytics (Optionnel)

Ajoute Google Analytics :

```python
# Dans portfolio_streamlit.py, au début
import streamlit.components.v1 as components

# Google Analytics
components.html("""
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
""", height=0)
```

---

## 🎯 Avantages Streamlit vs HTML

| Aspect | Streamlit | HTML/GitHub Pages |
|--------|-----------|-------------------|
| **Setup Time** | 10 min ⚡ | 30 min |
| **Interactivité** | ✅ Natif | ❌ Limité |
| **Updates** | Auto sur push ✅ | Manuel |
| **Python** | ✅ Natif | ❌ N/A |
| **Widgets** | ✅ Built-in | ❌ Custom code |
| **ML Demos** | ✅ Perfect | ❌ Difficile |
| **SEO** | ❌ Limité | ✅ Excellent |
| **Custom Domain** | ❌ Payant | ✅ Gratuit |

**Recommandation** :
- **Streamlit** si tu veux montrer des démos ML interactives
- **HTML** si tu veux un site plus "corporate" avec SEO

---

## 🚀 Features Avancées Streamlit

### **Ajouter des Démos Interactives**

```python
# Demo d'un modèle ML
st.markdown("### 🧪 Try the Model")

user_input = st.text_input("Enter text:")
if st.button("Predict"):
    # Simulate model prediction
    prediction = "Positive" if len(user_input) > 10 else "Negative"
    st.success(f"Prediction: {prediction}")
```

### **Visualisations Interactives**

```python
import plotly.express as px

# Performance chart
data = {
    'Project': ['Buyer Index', 'RAG System', 'AR Glasses'],
    'Impact': [32, 95, 100]
}
fig = px.bar(data, x='Project', y='Impact', title='Project Impact (%)')
st.plotly_chart(fig, use_container_width=True)
```

### **Contact Form Intégré**

```python
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    
    submitted = st.form_submit_button("Send Message")
    if submitted:
        # Envoyer email via API (ex: SendGrid, Mailgun)
        st.success("Message sent! I'll get back to you soon.")
```

---

## 📱 Mobile Responsive

Streamlit est automatiquement responsive ! Teste sur :
- Mobile (iPhone, Android)
- Tablet (iPad)
- Desktop

Aucun code supplémentaire nécessaire ✅

---

## 🔄 Updates Automatiques

**Le gros avantage de Streamlit Cloud** :

1. Tu modifies `portfolio_streamlit.py` localement
2. Tu push sur GitHub
3. **Streamlit Cloud update automatiquement** ton site !

```bash
# Workflow typique
git add .
git commit -m "Added new project"
git push origin main
# Attends 30 secondes → Site updated ✅
```

---

## 💡 Pro Tips

### **1. Cache pour Performance**

```python
@st.cache_data
def load_data():
    # Load heavy data once
    return expensive_computation()
```

### **2. Secrets Management**

Pour API keys, etc. :

1. Dans Streamlit Cloud → Settings → Secrets
2. Ajoute :
```toml
api_key = "your-secret-key"
```
3. Dans le code :
```python
api_key = st.secrets["api_key"]
```

### **3. Custom Domain (Payant)**

Si tu veux `portfolio.hamzabendaoud.com` :
- Upgrade to Streamlit Cloud Pro ($20/month)
- Configure custom domain

---

## 🆘 Troubleshooting

### **L'app ne démarre pas**
- Vérifie `requirements.txt`
- Vérifie les imports
- Check les logs dans Streamlit Cloud

### **CSS ne s'applique pas**
- Le CSS est dans `st.markdown()` avec `unsafe_allow_html=True`
- Vérifie la syntaxe CSS

### **Lenteur de l'app**
- Utilise `@st.cache_data`
- Optimise les images
- Réduis les calculs lourds

---

## 📊 Comparaison des 2 Options

### **Option 1 : HTML (GitHub Pages)**
✅ SEO excellent  
✅ Custom domain gratuit  
✅ Plus "professionnel"  
❌ Moins interactif  
❌ Pas de démos ML faciles  

**Best for** : Portfolio général, visibilité Google

### **Option 2 : Streamlit Cloud**
✅ Démos ML interactives  
✅ Setup ultra-rapide  
✅ Updates auto  
❌ SEO limité  
❌ Custom domain payant  

**Best for** : Portfolio Data Science/ML avec démos

---

## 🎯 Ma Recommandation

**Fais LES DEUX !** 🚀

1. **HTML sur GitHub Pages** : `hamzabendaoud.github.io`
   - Pour SEO et visibilité professionnelle
   - Lien dans CV et LinkedIn
   
2. **Streamlit** : `hamzabendaoud-portfolio.streamlit.app`
   - Pour démos ML interactives
   - Lien dans sections "Projects"

**Stratégie** :
- Portfolio HTML = Point d'entrée principal
- Streamlit apps = Démos spécifiques de projets

---

## ✅ Checklist Déploiement

- [ ] Repo GitHub créé
- [ ] `portfolio_streamlit.py` uploadé
- [ ] `requirements.txt` créé
- [ ] App déployée sur Streamlit Cloud
- [ ] URL testée
- [ ] Mobile responsive vérifié
- [ ] Liens externes fonctionnent
- [ ] CV téléchargeable ajouté
- [ ] Analytics configuré (optionnel)

---

## 🚀 Commandes Rapides

```bash
# Setup
git clone https://github.com/hamzabendaoud/portfolio-streamlit.git
cd portfolio-streamlit

# Test local
streamlit run portfolio_streamlit.py

# Deploy
git add .
git commit -m "Portfolio v1.0"
git push origin main

# Visit
# https://hamzabendaoud-portfolio.streamlit.app
```

---

**Ton portfolio Streamlit sera live en 10 minutes !** 🎉

**URL finale** : https://hamzabendaoud-portfolio.streamlit.app

Bonne chance ! 🚀
