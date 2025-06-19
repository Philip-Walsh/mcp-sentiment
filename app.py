# Hugging face spaces needs an app.py file to build the space. So the name of the python file has to be app.py

import json
import gradio as gr
from textblob import TextBlob


# The sentiment_analysis function takes a text input and returns a dictionary 🤗
# It uses TextBlob to analyze the sentiment
# The docstring is crucial as it helps Gradio generate the MCP tool schema
# Type hints (str and dict) help define the input/output schema


def sentiment_analysis(text: str) -> str:
    """
    Analyze the sentiment of the given text.

    Args:
        text (str): The text to analyze

    Returns:
        str: A JSON string containing polarity, subjectivity, and assessment
    """
    blob = TextBlob(text)
    sentiment = blob.sentiment

    result = {
        "polarity": round(sentiment.polarity, 2),  # -1 (negative) to 1 (positive) # type: ignore
        "subjectivity": round(sentiment.subjectivity, 2),  # 0 (objective) to 1 (subjective) # type: ignore
        "assessment": "positive" if sentiment.polarity > 0 else "negative" if sentiment.polarity < 0 else "neutral" # type: ignore
    }

    return json.dumps(result)

# Create the Gradio interface
# r.Interface creates both the web UI and MCP server
# The function is exposed as an MCP tool automatically
# Input and output components define the tool’s schema
# The JSON output component ensures proper serialization
demo = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(placeholder="Enter text to analyze..."),
    outputs=gr.Textbox(),  # Changed from gr.JSON() to gr.Textbox()
    title="Text Sentiment Analysis",
    description="Analyze the sentiment of text using TextBlob"
)

# Launch the interface and MCP server
if __name__ == "__main__":
    demo.launch(mcp_server=True)

# Setting mcp_server=True enables the MCP server
# The server will be available at http://localhost:7860/gradio_api/mcp/sse
# You can also enable it using the environment variable:
# Copied
# export GRADIO_MCP_SERVER=True