# 🎯 Portfolio Website - Deployment Guide

## 🚀 Option 1: GitHub Pages (RECOMMANDÉ - 5 minutes)

### **Étape 1 : Setup GitHub Repo**
```bash
# Crée un repo spécial avec ton username
# Le repo DOIT s'appeler: hamzabendaoud.github.io (remplace par ton username)

git init
git add .
git commit -m "Initial portfolio commit"
git remote add origin https://github.com/hamzabendaoud/hamzabendaoud.github.io.git
git push -u origin main
```

### **Étape 2 : Activer GitHub Pages**
1. Va sur ton repo GitHub
2. Settings → Pages
3. Source: "Deploy from a branch"
4. Branch: "main" → Folder: "/ (root)"
5. Save

### **Étape 3 : Accéder**
Ton site sera live à : **https://hamzabendaoud.github.io**

✅ **C'est tout !** Ton portfolio est en ligne !

---

## 🌐 Option 2: Custom Domain (Optionnel mais Pro)

Si tu veux un domaine custom comme `hamzabendaoud.com` :

### **Acheter un Domaine** (~$10/an)
- **Namecheap** : https://www.namecheap.com
- **Google Domains** : https://domains.google
- **OVH** : https://www.ovh.com

### **Configurer DNS**
1. Dans ton registrar, ajoute ces DNS records:
```
Type: A
Host: @
Value: 185.199.108.153

Type: A
Host: @
Value: 185.199.109.153

Type: A
Host: @
Value: 185.199.110.153

Type: A
Host: @
Value: 185.199.111.153

Type: CNAME
Host: www
Value: hamzabendaoud.github.io
```

2. Dans ton repo GitHub, crée un fichier `CNAME`:
```
hamzabendaoud.com
```

3. Dans Settings → Pages, configure le custom domain

⏱️ Attendre 24-48h pour propagation DNS

---

## 📝 Personnalisation

### **Ajouter Tes Projets**

Dans `index.html`, section `<!-- Projects Section -->`, duplique ce bloc :

```html
<div class="project-card">
    <div class="project-image">
        <i class="fas fa-chart-line"></i> <!-- Change l'icône -->
    </div>
    <div class="project-content">
        <h3 class="project-title">Ton Projet</h3>
        <p class="project-description">
            Description de ton projet avec métriques quantifiables
        </p>
        <div class="project-tags">
            <span class="tag">Python</span>
            <span class="tag">FastAPI</span>
            <!-- Ajoute tes technologies -->
        </div>
        <div class="project-links">
            <a href="lien-demo"><i class="fas fa-external-link-alt"></i> Live Demo</a>
            <a href="lien-github"><i class="fab fa-github"></i> Code</a>
        </div>
    </div>
</div>
```

### **Icônes Disponibles** (Font Awesome)
- `fa-chart-line` - Analytics
- `fa-robot` - AI/ML
- `fa-glasses` - AR/VR
- `fa-traffic-light` - Traffic
- `fa-video` - Computer Vision
- `fa-database` - Database
- `fa-cloud` - Cloud
- Plus sur : https://fontawesome.com/icons

### **Changer les Couleurs**

Dans `index.html`, section `<style>`, modifie :

```css
:root {
    --primary: #1A1A2E;     /* Couleur principale */
    --secondary: #0F3460;   /* Couleur secondaire */
    --accent: #E94560;      /* Couleur d'accent */
    --light: #F8F9FA;       /* Background clair */
}
```

---

## 📸 Ajouter des Screenshots

1. Crée un dossier `images/` dans ton repo
2. Ajoute tes screenshots : `project1.png`, `project2.png`, etc.
3. Remplace la `project-image` div par:

```html
<div class="project-image">
    <img src="images/project1.png" alt="Project Screenshot" style="width: 100%; height: 100%; object-fit: cover;">
</div>
```

---

## 🔗 Ajouter des Liens Externes

### **Pour chaque projet, ajoute :**

1. **Live Demo** : Lien Streamlit Cloud, Vercel, etc.
2. **Code** : Lien GitHub du repo
3. **Blog Post** (optionnel) : Article Medium/Dev.to
4. **Case Study** (optionnel) : PDF avec détails techniques

### **Exemple :**
```html
<div class="project-links">
    <a href="https://buyer-index.streamlit.app"><i class="fas fa-external-link-alt"></i> Live Demo</a>
    <a href="https://github.com/hamzabendaoud/buyer-index"><i class="fab fa-github"></i> Code</a>
    <a href="blog-post.html"><i class="fas fa-book"></i> Case Study</a>
</div>
```

---

## 📊 Analytics (Optionnel)

Ajoute Google Analytics pour tracker les visites :

1. Crée un compte : https://analytics.google.com
2. Obtiens ton tracking ID : `G-XXXXXXXXXX`
3. Ajoute dans `<head>` de index.html :

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

---

## ✅ Checklist Avant de Publier

- [ ] Toutes les infos personnelles à jour (email, LinkedIn, etc.)
- [ ] Tous les projets ajoutés avec descriptions
- [ ] Liens GitHub fonctionnent
- [ ] PDF du resume uploadé
- [ ] Screenshots de projets ajoutés (optionnel)
- [ ] Testé sur mobile (responsive design)
- [ ] Vérifié les typos
- [ ] Analytics configuré (optionnel)

---

## 🎨 Personnalisations Avancées (Optionnel)

### **Ajouter une Section Blog**
Crée `blog.html` pour partager tes articles techniques

### **Ajouter une Section Certifications**
Montre tes certifications AWS, Google Cloud, etc.

### **Mode Sombre**
Ajoute un toggle pour dark mode

### **Animations**
Ajoute des animations scroll (AOS library)

---

## 🚀 Déploiement Rapide

```bash
# 1. Clone ou crée le repo
git clone https://github.com/hamzabendaoud/hamzabendaoud.github.io.git
cd hamzabendaoud.github.io

# 2. Copie le fichier index.html
cp path/to/index.html .

# 3. Personnalise
# Edit index.html avec tes infos

# 4. Upload ton CV
# Copie Hamza_Bendaoud_Resume.pdf dans le repo

# 5. Commit & Push
git add .
git commit -m "Portfolio website v1.0"
git push origin main

# 6. Visite ton site
# https://hamzabendaoud.github.io
```

---

## 📱 Test Responsive

Teste sur différents devices :
- Desktop (Chrome DevTools)
- Mobile (iPhone, Android)
- Tablet (iPad)

---

## 🆘 Troubleshooting

### **Le site ne s'affiche pas**
- Attends 2-3 minutes après le push
- Vérifie Settings → Pages → Branch est bien "main"
- Vérifie que le fichier s'appelle `index.html` (pas Index.html)

### **Les images ne s'affichent pas**
- Vérifie les chemins relatifs : `images/photo.png`
- Commit et push les images

### **Le CSS ne marche pas**
- Le CSS est inline dans index.html, donc pas de fichier externe
- Si tu veux séparer : crée `styles.css` et link avec `<link rel="stylesheet" href="styles.css">`

---

## 💡 Pro Tips

1. **SEO** : Ajoute des meta tags dans `<head>`
2. **Performance** : Optimise les images (WebP format)
3. **Accessibilité** : Ajoute des attributs `alt` sur les images
4. **Social Sharing** : Ajoute Open Graph tags pour LinkedIn/Twitter

---

## 🎯 Update Régulier

Mets à jour ton portfolio :
- **Après chaque nouveau projet**
- **Après chaque nouvelle expérience**
- **Tous les 3 mois minimum**

Un portfolio à jour = signal que tu es actif et passionné !

---

**Ton portfolio sera live à : https://hamzabendaoud.github.io** 🚀

Bonne chance avec tes applications FAANG ! 🎯
