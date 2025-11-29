import os 
from dotenv import load_dotenv
load_dotenv()

DOCUMENT_FOLDER = "./documents"
ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY", "")