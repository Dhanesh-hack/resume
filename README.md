# Dhanesh's Cybersecurity Portfolio

A cybersecurity-themed portfolio website showcasing skills, experience, and projects.

## Deployment Instructions

1. Create an account on [Render.com](https://render.com)
2. Click on "New +" and select "Web Service"
3. Connect your GitHub repository
4. Use the following settings:
   - Name: dhanesh-portfolio
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Click "Create Web Service"

The site will be automatically deployed and you'll get a URL like `https://dhanesh-portfolio.onrender.com`

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the development server:
```bash
python app.py
```

Visit `http://localhost:8000` in your browser. 