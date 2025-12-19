import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
from openai import OpenAI
from openai import RateLimitError, AuthenticationError

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Safety check
if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY not found in environment variables")

client = OpenAI(api_key=OPENAI_API_KEY)


# ---------------- PDF TEXT EXTRACTION ----------------
def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from an uploaded PDF (Streamlit file object).
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


# ---------------- OPENAI HELPER ----------------
def ask_openai(prompt, max_tokens=300):
    """
    Sends a prompt to OpenAI and returns the response safely.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content.strip()

    except RateLimitError:
        return "⚠️ OpenAI quota exceeded. Please try again later."

    except AuthenticationError:
        return "❌ Invalid OpenAI API key."

    except Exception as e:
        return f"❌ Unexpected error: {str(e)}"
