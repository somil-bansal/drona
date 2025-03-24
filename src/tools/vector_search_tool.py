import logging
from typing import Annotated

from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

from tools.decorators import log_io

logger = logging.getLogger(__name__)

# select relevant index, filter based on whatever criteria, retrieve results, multimodal

@tool
@log_io
def vector_search_tool(
        url: Annotated[str, "The url to crawl."],
) -> HumanMessage:
    """Use this to crawl a url and get a readable content in markdown format."""
    try:
        crawler = Crawler()

    except BaseException as e:
        error_msg = f"Failed to crawl. Error: {repr(e)}"
        logger.error(error_msg)
        return error_msg
