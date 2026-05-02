# Language_Translator
A streamlined language translation tool powered by the **Google Gemini 2.0 Flash** model. This project demonstrates how to integrate Large Language Models (LLMs) into a Python application for high-accuracy, context-aware translations.


## 🚀 Features
* **AI-Powered Translation:** Uses Google's generative AI to handle nuances, idioms, and context better than traditional rule-based translators.
* **Secure Configuration:** Utilizes environment variables (`.env`) to keep API keys safe and out of version control.
* **Lightweight & Fast:** Optimized using the `google-genai` SDK and the `gemini-2.0-flash` model for near-instant responses.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **AI Model:** Google Gemini 2.0 Flash
* **Libraries:** 
    * `google-genai`: The official SDK for Gemini API interaction.
    * `python-dotenv`: For managing sensitive environment variables.


## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone [https://github.com/JyotsnaGuntha/Language_Translator.git](https://github.com/JyotsnaGuntha/Language_Translator.git)
cd Language_Translator
```

### 2. Install Dependencies
```bash
pip install python-dotenv google-genai
```
### 3. To run the translator, execute the script using Python:
```bash
python app.py
```