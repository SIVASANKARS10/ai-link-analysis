
from app.services.website_extractor import extract_website_content
from app.services.llm_service import analyze_with_gemini


async def perform_link_analysis(url: str) -> dict:
    # Step 1: Extract website content
    website_data = await extract_website_content(url)

    # Step 2: Analyze extracted content using Gemini
    analysis_result = await analyze_with_gemini(website_data)

    # Step 3: Return complete analysis
    return analysis_result
