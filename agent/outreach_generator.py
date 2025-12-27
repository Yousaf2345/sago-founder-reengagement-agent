class OutreachGenerator:
    def generate(self, context, signals):
        founder = context["founder_context"]

        return f"""
Hi {founder['founder_name']},

Saw the recent Seed round — congrats on the progress. When we last spoke in {founder['last_meeting']}, traction was the main open question.

Would love to reconnect and hear how things have evolved.

Best,
[Investor Name]
"""
