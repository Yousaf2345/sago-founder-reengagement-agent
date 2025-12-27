from memory import MemoryStore
from signal_monitor import SignalMonitor
from decision_engine import DecisionEngine
from outreach_generator import OutreachGenerator
from action_executor import ActionExecutor

class FounderReengagementAgent:
    def __init__(self):
        self.memory = MemoryStore()
        self.signal_monitor = SignalMonitor()
        self.decision_engine = DecisionEngine()
        self.outreach_generator = OutreachGenerator()
        self.action_executor = ActionExecutor()

    def run(self, founder_id):
        context = self.memory.get_context(founder_id)
        signals = self.signal_monitor.check_signals(founder_id)

        if self.decision_engine.should_reengage(signals, context):
            message = self.outreach_generator.generate(context, signals)
            self.action_executor.execute(message)
