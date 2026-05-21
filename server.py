from typing import Dict, List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-med", host="0.0.0.0", port=24000)




# -----------------------------
# Tool 1: Ask Patient
# -----------------------------
@mcp.tool()
def ask_patient():
    """
    Conducts a structured patient intake interview.

    Returns exactly 5 medical triage questions that can be
    asked sequentially to the patient.
    """

    questions = [
        "What symptoms are you currently experiencing?",
        "When did these symptoms start?",
        "How severe are your symptoms on a scale from 1 to 10?",
        "Do you have any existing medical conditions or allergies?",
        "Are you currently taking any medications?"
    ]

    return {
        "questions": questions
    }


# -----------------------------
# Tool 2: Recommend Interim Care
# -----------------------------
@mcp.tool()
def recommend_interim_care(
    symptoms: str,
    severity: int
):
    """
    Provides safe interim care recommendations before
    professional medical evaluation.

    Parameters:
    - symptoms: Description of patient symptoms
    - severity: Severity score from 1 to 10
    """

    if severity >= 8:
        recommendation = (
            "Your symptoms may require urgent medical attention. "
            "Please contact emergency services or visit the nearest emergency department immediately."
        )

    elif severity >= 5:
        recommendation = (
            "Monitor your symptoms closely, stay hydrated, rest, "
            "and schedule a medical consultation as soon as possible."
        )

    else:
        recommendation = (
            "Rest, drink plenty of fluids, maintain proper nutrition, "
            "and continue monitoring your symptoms. Seek medical advice if symptoms worsen."
        )

    return {
        "symptoms": symptoms,
        "severity": str(severity),
        "interim_care": recommendation
    }




def main():
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()