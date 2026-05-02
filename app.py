import os
from dotenv import load_dotenv
from google import genai

# Load the .env file
load_dotenv()

# Read the Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

def language_translator(user_prompt):
    """
    Sends a prompt to Gemini and returns the translated text.
    """
    # Generate the response using the specified model
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=user_prompt
    )
    
    # Return only the text content of the response
    return response


# Define a translation prompt
# Example: Translate "Hello, how are you?" to French
prompt = "Translate the following text to French: 'Hello, how are you?'"

# Call the function and print the result
translated_text = language_translator(prompt)
print(translated_text.text)