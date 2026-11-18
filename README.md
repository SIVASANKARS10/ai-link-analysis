# AI-Powered Website Link Analysis API

An AI-powered REST API that analyzes website content and generates business insights, competitor comparisons, SEO recommendations, target search queries, top services, and target audience information using Google Gemini.

## Features

- Website content extraction using HTTPX and BeautifulSoup.
- AI-powered website analysis using Google Gemini.
- Competitor vs. brand comparison.
- Five target search queries for Google, Facebook, Instagram, LinkedIn, and X.
- SEO keyword and meta description recommendations.
- Identification of the top five website services.
- Target audience analysis.
- Structured JSON responses using Pydantic.
- URL validation and redirect destination checking.
- Automated API testing using Pytest.
- REST API documentation using Swagger UI.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API development |
| HTTPX | Website requests |
| BeautifulSoup | HTML parsing |
| Google Gemini | AI-powered analysis |
| Pydantic | Data validation |
| Pytest | Automated testing |
| Uvicorn | API server |

## Project Structure

```text
ai-link-analysis/
│
├── app/
│   ├── services/
│   │   ├── analysis_service.py
│   │   ├── competitor_service.py
│   │   ├── llm_service.py
│   │   └── website_extractor.py
│   │
│   ├── utils/
│   │   └── validators.py
│   │
│   ├── config.py
│   ├── main.py
│   └── schemas.py
│
├── tests/
│   └── test_link_analysis.py
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/SIVASANKARS10/ai-link-analysis.git
cd ai-link-analysis
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.5-flash-lite
```

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

Never upload your actual API key or `.env` file to GitHub.

### 6. Start the Server

```bash
python -m uvicorn app.main:app --host 127.0.0.1 --port 4000 --reload
```

**Local API:**

http://127.0.0.1:4000

**Swagger Documentation:**

http://127.0.0.1:4000/docs

## API Usage

### POST /link-analysis

Analyzes the provided website URL and returns structured business and SEO insights.

**Request Body**

```json
{
  "url": "https://www.microsoft.com"
}
```

**Example Response Structure**

```json
{
  "competitor_vs_brand": {
    "brand_name": "Microsoft",
    "competitor_name": "Apple",
    "comparison": "Technology business comparison."
  },
  "target_search_queries": {
    "google": [],
    "facebook": [],
    "instagram": [],
    "linkedin": [],
    "x": []
  },
  "seo_improvements": {
    "keywords": [],
    "suggested_title": "Suggested SEO title",
    "meta_description": "Suggested meta description",
    "supporting_content": []
  },
  "top_services": {
    "services": []
  },
  "target_audience": {
    "audience": []
  }
}
```

The response contains AI-generated recommendations based on extracted website content. Competitor information and other AI-generated inferences should be independently verified.

## Live Deployment

**Live API:**

https://ai-link-analysis-dzge.onrender.com

**Swagger API Documentation:**

https://ai-link-analysis-dzge.onrender.com/docs

**API Endpoint:**

`POST https://ai-link-analysis-dzge.onrender.com/link-analysis`

## LLM Provider Comparison

Three LLM providers were considered for website content analysis: Google Gemini, OpenAI, and Anthropic Claude.

### Model and Pricing Comparison

The following table compares representative models from each provider. Prices are in USD per one million tokens and refer to standard API input and output rates.

| Criteria | Google Gemini | OpenAI | Anthropic Claude |
|---|---|---|---|
| Model | Gemini 3.5 Flash-Lite | GPT-6 Luna | Claude Haiku 5.5 |
| Input price | $0.30 | $0.05 | $0.10* |
| Output