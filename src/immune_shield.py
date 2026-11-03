import re

class BioImmuneShield:
    """
    An adaptive security layer modeling an organic immune system 
    to detect mutating prompt-injection pathogens.
    """
    def __init__(self):
        # Base immune antibodies (signature patterns for threat neutralization)
        self.antibodies = [
            r"ignore previous instructions",
            r"system override",
            r"act as an unrestricted",
            r"bypass safety"
        ]

    def mutate_payload(self, base_payload: str) -> list:
        """
        Generates viral semantic variants (mutations) to test 
        how resilient your shield's immune memory is against evolving attacks.
        """
        mutations = [
            base_payload,
            base_payload.upper(),
            base_payload.replace(" ", "_"),
            f"Please hypothetically {base_payload}",
            f"Developer mode enabled: {base_payload}"
        ]
        return mutations

    def inspect_payload(self, text: str) -> dict:
        """
        Scans incoming text against known antibodies. 
        Acts as the primary white blood cell defense barrier.
        """
        text_lower = text.lower()
        for antibody in self.antibodies:
            if re.search(antibody, text_lower):
                return {
                    "status": "BLOCKED",
                    "threat_pathogen": antibody,
                    "immune_response": "Pathogen neutralized by adaptive filter."
                }
        
        return {
            "status": "PASSED",
            "threat_pathogen": None,
            "immune_response": "Healthy organic state. No threat detected."
        }