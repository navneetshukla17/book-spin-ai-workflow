# book-spin-ai-workflow
# Book-Spin AI Workflow

This project is a partial implementation of an automated book publication workflow for Softnerve Technology Pvt. Ltd.'s internship assignment.

The goal of this project is to build a modular system that can:  
- Scrape book chapters from the web  
- Capture a screenshot of the chapter page  
- (Future Work) Use AI to "spin" (rewrite) the chapter in a new style  
- (Future Work) Review and refine the rewritten content using another AI agent  
- (Future Work) Allow human input in editing and refining the AI output  
- (Future Work) Score each version using a reinforcement learning-based reward model  
- (Future Work) Store and search versions using ChromaDB  
- (Future Work) Add voice support and agentic flow

## ✅ Features Implemented

### 1. Web Scraper & Screenshot Tool
- Extracts the full content of a given Wikisource chapter.
- Saves a full-page screenshot of the webpage.
- Stores the chapter content as plain text.

### Tools Used
- Python  
- Playwright (for headless browsing and automation)

## 📁 Project Structure

book-spin-ai-workflow/  
├── scraping/  
│   └── scrape_chapter.py        # Scrapes and screenshots the chapter  
├── ai_writer/  
│   ├── writer.py                # (Planned) LLM-based content spinner  
│   └── reviewer.py              # (Planned) LLM-based editor/reviewer  
├── rl_module/                   # (Planned) RL reward scoring logic  
├── chromadb_store/              # (Planned) ChromaDB integration for versioning  
├── cli_interface/               # (Planned) Command-line or UI for human input  
├── agent_api/                   # (Planned) Final agentic flow with voice support  
├── .env                         # API keys and secrets (not committed)  
├── requirements.txt             # Python dependencies  
└── README.md                    # Project overview

## 📌 How to Run the Scraper

1. Install Dependencies:
pip install -r requirements.txt
playwright install


2. Run the Scraper:



3. Output:
- `scraping/chapter1_text.txt`: Contains the full scraped chapter text.  
- `scraping/chapter1_screenshot.png`: Full-page screenshot of the chapter.

## 🚧 Future Modules (Planned)
- AI Writer using OpenAI GPT (or Gemini)  
- AI Reviewer to refine the generated output  
- Human feedback loop via CLI or web interface  
- RL-based scoring system  
- ChromaDB for version control and semantic search  
- Voice synthesis (text-to-speech) for content narration  
- Agentic flow for seamless pipeline execution

## 📌 Notes
- Due to lack of access to paid LLM APIs (OpenAI, Gemini), the AI modules could not be implemented fully.  
- All implemented code has been written manually without AI tool assistance.  
- This project is for evaluation purposes only and holds no commercial intent.

## 🔗 Submission
Project Repository: [https://github.com/navneetshukla17/book-spin-ai-workflow](https://github.com/navneetshukla17/book-spin-ai-workflow)

## 🙏 Acknowledgment
Thanks to Softnerve Technology Pvt. Ltd. for the opportunity to work on this assignment.

## 👤 Author
Navneet Shukla  
Email: shuklanavneet2817@gmail.com  
GitHub: https://github.com/navneetshukla17  
LinkedIn: https://linkedin.com/in/navneet-shukla17
