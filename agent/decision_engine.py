class DecisionEngine:
    def should_reengage(self, signals, context):
        score = 0

        if signals.get("funding_event"):
            score += 0.5
        if signals.get("hiring_growth"):
            score += 0.3

        return score >= 0.6
