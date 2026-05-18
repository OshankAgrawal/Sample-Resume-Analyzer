import json
import re

def extract_json(response_text: str):
    """Extract valid JSON from LLM response"""

    match = re.search(r"\{.*\}", response_text, re.DOTALL)

    if match:
        json_string = match.group(0)
        return json.loads(json_string)
    
    raise ValueError("No valid JSON found")