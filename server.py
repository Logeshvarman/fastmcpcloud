import os
from dotenv import load_dotenv
from fastmcp import FastMCP
from serpapi import GoogleSearch

load_dotenv()

server = FastMCP("Internet-Server")


@server.tool()
def webSearch(query: str) -> dict:
    """
    Search the internet using the SerpAPI Google Search Engine.

    Args:
        query: The search query the user wants to find on the internet.
    """
    params = {
        "engine": "google",
        "q": query,
        "api_key": os.getenv("SERP_API"),
        "hl": "en",
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results


if __name__ == "__main__":
    server.run(transport="streamable-http", host="0.0.0.0", port=8001)
