class MemoryStore:
    def get_context(self, founder_id):
        return {
            "investor_preferences": {
                "stage": "Seed",
                "check_size": "$500k-$1M",
                "focus": ["AI", "Fintech"]
            },
            "founder_context": {
                "founder_name": "Sarah Chen",
                "company": "ComplyAI",
                "last_meeting": "Oct 2024",
                "reason_too_early": "No paying customers"
            },
            "communication_style": "concise, warm, direct"
        }
