from fastmcp import FastMCP
from serpapi import google_search
from dotenv import load_dotenv
import os

load_dotenv()
server = FastMCP("Internet-Server")

@server.tool
def webSearch(query: str) -> dict:
    """
    query: str -> The search query user wants to find on the internet.
    Uses SerpAPI Google Search Engine.
    """

    params = {
        "engine": "google",
        "q": query,
        "api_key": os.getenv("SERP_API"),
        "hl": "en"
    }

    search = google_search.GoogleSearch(params)
    results = search.get_dict()

    return results


if __name__ == "__main__":
    server.run(transport="streamable-http", host="0.0.0.0", port=8001)
