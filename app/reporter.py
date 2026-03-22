import json
import os
from google import genai
from dotenv import load_dotenv

#Load gemini API key 
load_dotenv()
# Initialize LLM
client = genai.Client(api_key= os.environ["GEMINI_API_KEY"])


# Generate Human readable report using Gemini LLM
def generate_manager_report(dispatch_plan: dict) -> dict:
    """Takes mathematical output from MDP and generates prompt for LLM"""

    raw_data = json.dumps(dispatch_plan, indent=2)
    #1. Convert python dictionary into a clean JSON string
    prompt = f""" You are an expert Logistics Operation Manager, 
    I am giving you raw JSON output from our multi-agent dispatch agorithm.

    Your job is to read this data and write a short , professional, 2-3 sentence summary
    for the shift supervisor.
    - Mention which robots are active.
    - Highlight if there are any unassigned tasks (these are emergencies requiring human intervention).
    - Do not list every single task ID, just the big picture.
    
    RAW DATA:
    {raw_data}    
    """
    try:
        response = client.models.generate_content(
            model = 'gemini-2.5-flash',
            contents = prompt,
            )

        ai_summary = response.text
    
    except Exception as e:
        ai_summary = f"System Warning: MDP dispatch successful, but AI reporting is currently unavailablr. Error: {str(e)}"

    return{
        "llm_prompt_generated": prompt,
        "manager_summary": ai_summary
    }

