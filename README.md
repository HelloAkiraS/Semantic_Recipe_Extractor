# Semantic Recipe Extractor 🍳🤖

> A semantic information extractor for Brazilian Portuguese recipes using Natural Language Processing (NLP) and Python.

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python)
![spaCy](https://img.shields.io/badge/NLP-spaCy-green?style=flat&logo=spacy)
![Status](https://img.shields.io/badge/Status-MVP%20Completed-success)

## 📋 About the Project

The **Semantic Recipe Extractor** is a backend tool designed to transform unstructured recipe texts (natural language, slang, abbreviations) into structured data (JSON).

The system leverages the power of the **spaCy** library for morphosyntactic analysis and **Regular Expressions (Regex)** for text normalization, allowing for the automated identification of ingredients, actions (preparation steps), and measurements.

This project was built using a **Rule-Based Architecture**, focusing on deterministic accuracy and creating datasets for future Machine Learning models.

## 🚀 Key Features

- **Text Normalization:** Cleans slang, standardizes abbreviations (e.g., "col" -> "colher", "add" -> "adicionar"), and handles punctuation via a robust dictionary system.
- **Ingredient Extraction:** Identifies edible nouns (`NOUN`) while intelligently filtering out kitchen utensils (e.g., ensuring "pan" is not listed as an ingredient).
- **Action Extraction (Lemmatization):** Converts conjugated verbs (e.g., "pique", "mexendo") into their infinitive forms (e.g., "picar", "mexer"), standardizing the preparation steps via **Attribute Rulers**.
- **Measurement Separation:** Automatically distinguishes between ingredients and units of measurement (e.g., separating "cup" from "flour").
- **JSON Output:** Generates a clean JSON object ready for API or Front-end consumption.

## 🛠️ Tech Stack

* **Python 3.12+**
* **spaCy** (Model: `pt_core_news_md`): Used for POS Tagging (Part-of-Speech) and Lemmatization.
* **Re (Regex):** Used for string normalization and "blinding" dictionary keys to prevent errors.
* **Collections (Counter):** Used for optimizing and counting unique items.

## 📦 Installation & Setup

*Note: consider using a Python Virtual Environment (venv).*

1.  **Clone the repository:**

    git clone [https://github.com/HelloAkiraS/Semantic_Recipe_Extractor.git](https://github.com/HelloAkiraS/Semantic_Recipe_Extractor.git)
    cd Cemantic_Recipe_Extractor

2.  **Install dependencies:**

    python -m pip install -r requirements.txt

3.  **Download the Portuguese language model:**

    python -m spacy download pt_core_news_md

## 💻 Usage

The `main.py` file contains the `SemanticRecipeExtractor` class. You can import it into your project or run the file directly to test it.

    from main import SemanticRecipeExtractor

    # Example input (Brazilian Portuguese Raw Text)
    raw_text = """
    Bora fazer aquele frango! 
    Pega 1 kg de peito de frango e joga na panela. 
    Add 2 colheres de shoyu e deixa refogar.
    """

    extractor = SemanticRecipeExtractor()
    print(extractor.get_json(raw_text))

**Expected Output (JSON):**

    {
        "Ingredients": ["frango", "peito", "shoyu"],
        "Actions": ["pegar", "jogar", "adicionar", "deixar", "refogar"],
        "Measures": ["kg", "colheres"]
    }

## 🧠 Project Architecture

The system operates as an **ETL Pipeline** (Extract, Transform, Load):

1.  **Input:** Receives raw text.
2.  **Normalizer:** Applies Regex and "Blinded" Dictionaries (anti-KeyError) to expand abbreviations and correct spelling before NLP processing.
3.  **spaCy NLP:** Converts clean text into a `Doc` object, applying grammatical tags (POS Tags) and custom Attribute Rulers (to fix tricky verbs like "pique").
4.  **Extractors:**
    * *Ingredients:* Filters `NOUN` (Nouns), excluding utensils and measurements.
    * *Actions:* Filters `VERB` (Verbos) and converts them to `Lemma` (Infinitive).
    * *Measures:* Filters units based on a control list.
5.  **Output:** Returns the structure in JSON format.

## 📂 File Structure

* `main.py`: Contains the `SemanticRecipeExtractor` class and orchestration logic.
* `material.py`: Knowledge base (Slang dictionaries, lists of Utensils, Measurements, and Non-culinary verbs).

## 🔮 Future Roadmap

This project is currently an MVP (Minimum Viable Product). Future improvements include:
- [ ] Implementing **Named Entity Recognition (NER)** specifically trained for culinary terms.
- [ ] Using **Word Embeddings** to generalize unknown ingredients via semantic similarity.
- [ ] Extracting numerical quantities linked to specific ingredients (Dependency Parsing).

## 👨‍💻 Author

**HelloAkiraS**

Internet's Systems Student at **Fatec Rubens Lara**.

---
*Project developed for educational purposes in Natural Language Processing and Software Engineering.*
