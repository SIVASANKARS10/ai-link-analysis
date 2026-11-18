
import json
import asyncio

from google import genai
from google.genai import types

from app.config import GEMINI_API_KEY, GEMINI_MODEL
from app.schemas import LinkAnalysisResponse


client = genai.Client(api_key=GEMINI_API_KEY)


async def analyze_with_gemini(website_data: dict) -> dict:

    prompt = f"""
You are a professional business intelligence, competitor research,
digital marketing and SEO analyst.

Your task is to analyze the actual business represented by the
website content provided below.

WEBSITE INFORMATION:

URL: {website_data['url']}
Title: {website_data['title']}
Meta Description: {website_data['meta_description']}
Headings: {website_data['headings']}
Content: {website_data['content']}


ANALYSIS REQUIREMENTS:

1. COMPETITOR VS BRAND

- Identify the actual company or brand name.
- Identify one relevant competitor in the same industry.
- Do not select unrelated companies.
- If the website content does not provide enough information
  to identify a competitor, use "Unknown".
- Explain the comparison using available evidence.
- Clearly distinguish confirmed information from reasonable inference.


2. TARGET SEARCH QUERIES

Generate exactly 5 relevant search queries for each platform:

- Google
- Facebook
- Instagram
- LinkedIn
- X

Requirements:
- Queries must relate to the actual company's products,
  services, industry and target customers.
- Avoid generic queries such as "official website".
- Avoid repeating the same query with minor wording changes.
- Make queries realistic and useful for digital marketing.


3. SEO IMPROVEMENTS

Provide:

- Relevant SEO keywords.
- An attractive and SEO-friendly page title.
- A natural meta description.
- Supporting content ideas.

Requirements:
- Focus on actual products, services and industry.
- Avoid irrelevant navigation text.
- Do not invent search volumes or keyword rankings.
- Make recommendations useful for search engine visibility.


4. TOP 5 SERVICES

- Identify up to 5 actual products or services offered by the company.
- Use the website content as evidence.
- Ignore navigation labels, menus, buttons, login messages,
  cookie notices and automated verification text.
- Never classify website navigation or homepage elements as services.
- If fewer than 5 genuine services are identifiable,
  return only those identifiable services.
- If no services are identifiable, return an empty list.


5. TARGET AUDIENCE

Identify the most likely customer groups based on:
- Products and services.
- Industry.
- Business model.
- Website content.

Avoid generic audiences such as "everyone" or "general public".
Do not assume demographic details without evidence.


IMPORTANT RULES:

- Use the actual website content as the primary source.
- Do not invent company facts, services or competitors.
- Do not treat navigation text as business information.
- Separate reasonable inferences from confirmed facts.
- Do not invent statistics, prices, rankings or search volumes.
- If information is unavailable, clearly indicate that.
- Return only valid JSON matching the provided response schema.
"""

    for attempt in range(3):
        try:
            response = await client.aio.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=LinkAnalysisResponse,
                    temperature=0.2
                )
            )

            if not response.text:
                raise ValueError("Gemini returned an empty response")

            result = json.loads(response.text)

            validated_result = LinkAnalysisResponse.model_validate(result)

            return validated_result.model_dump()

        except Exception as error:
            error_message = str(error)

            if "503" in error_message or "UNAVAILABLE" in error_message:
                if attempt < 2:
                    print(
                        f"Gemini busy. Retry attempt {attempt + 1}/2"
                    )
                    await asyncio.sleep(3 * (attempt + 1))
                    continue

            raise
