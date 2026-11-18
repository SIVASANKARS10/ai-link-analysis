
# AI-Powered Website Link Analysis API

An AI-powered REST API that analyzes website content and generates business insights, competitor comparisons, SEO recommendations, target search queries, services, and target audience information.

## Features

- Website content extraction using HTTPX and BeautifulSoup.
- AI-powered website analysis using Google Gemini.
- Competitor vs brand comparison.
- Five search queries for Google, Facebook, Instagram, LinkedIn, and X.
- SEO keyword and meta description recommendations.
- Identification of top website services.
- Target audience analysis.
- Structured JSON responses using Pydantic.
- URL validation and redirect checking.
- Automated API testing using Pytest.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API development |
| HTTPX | Website requests |
| BeautifulSoup | HTML parsing |
| Google Gemini | AI analysis |
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

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ai-link-analysis
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.5-flash-lite
```

Get your API key from Google AI Studio:

https://aistudio.google.com/

Never upload your actual API key or `.env` file to GitHub.

### 6. Start the server

```bash
python -m uvicorn app.main:app --host 127.0.0.1 --port 4000 --reload
```

API base URL:

```text
http://127.0.0.1:4000
```

Swagger documentation:

```text
http://127.0.0.1:4000/docs
```

## API Usage

### POST /link-analysis

Analyzes the provided website URL.

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

The response contains AI-generated recommendations based on the extracted website content. Competitor information and other inferences should be independently verified.

## Testing

Run automated tests:

```bash
python -m pytest -v
```

Current test coverage includes:

- Home endpoint.
- Successful link analysis response.
- Invalid URL validation.
- Analysis failure handling.

## Security and Limitations

- Validates website URLs before fetching.
- Checks redirect destinations.
- Uses request timeouts.
- Limits downloaded website content to 2 MB.
- Keeps API credentials in environment variables.
- Some websites may block automated requests or return HTTP 403.
- AI-generated analysis may contain inaccuracies and should be verified.
- URL validation should be reviewed and strengthened before public production deployment.

## Future Improvements

- Support additional LLM providers.
- Implement verified competitor research.
- Improve SEO keyword research.
- Add deployment and monitoring.
- Improve SSRF protection and automated security testing.

## Author

Siva Sankar S

GitHub: https://github.com/SIVASANKARS10

LinkedIn: https://www.linkedin.com/in/siva-sankar-s-312356300
```
