
import httpx
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from app.utils.validators import validate_url


async def extract_website_content(url: str) -> dict:
    if not validate_url(url):
        raise ValueError("Invalid or unsafe website URL")

    timeout = httpx.Timeout(15.0)

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/130.0.0.0 Safari/537.36"
        ),
        "Accept": (
            "text/html,application/xhtml+xml,"
            "application/xml;q=0.9,*/*;q=0.8"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive"
    }

    async with httpx.AsyncClient(
        timeout=timeout,
        follow_redirects=False,
        headers=headers
    ) as client:

        current_url = url

        for _ in range(5):
            if not validate_url(current_url):
                raise ValueError("Unsafe redirect URL")

            async with client.stream("GET", current_url) as response:

                if response.status_code in (301, 302, 303, 307, 308):
                    location = response.headers.get("location")

                    if not location:
                        raise ValueError("Invalid website redirect")

                    current_url = urljoin(current_url, location)
                    continue

                response.raise_for_status()

                content_type = response.headers.get(
                    "content-type", ""
                ).lower()

                if "text/html" not in content_type:
                    raise ValueError("Website does not return HTML")

                content = bytearray()

                async for chunk in response.aiter_bytes():
                    content.extend(chunk)

                    if len(content) > 2_000_000:
                        raise ValueError("Website content is too large")

                html = bytes(content)
                break

        else:
            raise ValueError("Too many website redirects")

    soup = BeautifulSoup(html, "html.parser")

    for element in soup([
        "script", "style", "nav", "footer",
        "header", "form", "noscript"
    ]):
        element.decompose()

    title = soup.title.get_text(strip=True) if soup.title else ""

    meta_tag = soup.find("meta", attrs={"name": "description"})

    meta_description = (
        meta_tag.get("content", "")
        if meta_tag else ""
    )

    headings = [
        heading.get_text(" ", strip=True)
        for heading in soup.find_all(["h1", "h2"])
    ]

    text_content = soup.get_text(" ", strip=True)

    return {
        "url": current_url,
        "title": title,
        "meta_description": meta_description,
        "headings": headings[:30],
        "content": text_content[:12000]
    }
