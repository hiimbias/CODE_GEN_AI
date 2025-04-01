import re
import json

def clean_and_parse_output(raw_output):
    """Clean and parse the raw output into JSON format"""
    try:
        # Remove any markdown code blocks
        cleaned = re.sub(r'```.*?\n', '', str(raw_output))
        # Remove assistant prefix if present
        cleaned = cleaned.replace("assistant:", "").strip()
        # Try to find JSON part in the output
        json_match = re.search(r'\{.*\}', cleaned, re.DOTALL)
        if json_match:
            json_str = json_match.group(0)
            # Handle potential trailing commas
            json_str = re.sub(r',\s*}', '}', json_str)
            json_str = re.sub(r',\s*]', ']', json_str)
            return json.loads(json_str)
        return None
    except Exception as e:
        print(f"Error parsing output: {e}")
        return None