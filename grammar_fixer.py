import os
import sys
import google.generativeai as genai

def fix_grammar(text):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        # If not in env, try to read from a local .env file or config for easier user setup
        # But for now, let's stick to env var or hardcoded placeholder check
        return "Error: GEMINI_API_KEY not found. Please set it in the script or environment."

    genai.configure(api_key=api_key)
    
    # Use a valid model from the available list
    model = genai.GenerativeModel('gemini-flash-latest')
    
    prompt = f"""
    Act as a professional editor. 
    Correct the grammar, spelling, and punctuation of the following text.
    Keep the original meaning and tone.
    Do NOT add any introductory or concluding remarks.
    Return ONLY the corrected text.

    Input Text:
    {text}
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error calling Gemini API: {str(e)}"

if __name__ == "__main__":
    # Support both arguments and stdin
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])
    else:
        input_text = sys.stdin.read()

    if not input_text or not input_text.strip():
        # If no input, just exit
        sys.exit(0)

    corrected = fix_grammar(input_text)
    print(corrected, end="")
