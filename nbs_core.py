"""
NBS - Null-Blockierungs-System (Zero Exclusion Logic)
Zentrale Steuerungseinheit & ZOFI-Metrik
"""

from nbs_zdu import ZeroDetectionUnit
from nbs_fap import FallbackArithmeticProtocol
from nbs_zob import ZeroOperationBlocker
from nbs_smh import SafeMathHandler

def zofi_metric(nbs_result, classical_reference):
    """Berechnet den Zero-Operation Fault Index (ZOFI)."""
    scale = max(abs(classical_reference), 1e-12)
    return abs(nbs_result - classical_reference) / scale

class NBSCoreSystem:
    def __init__(self):
        # Hier werden deine einzelnen Module geladen
        self.zdu = ZeroDetectionUnit()
        self.fap = FallbackArithmeticProtocol()
        self.zob = ZeroOperationBlocker()
        self.smh = SafeMathHandler()

    def compute(self, op, a, b):
        """Führt eine Operation nach den NBS-Axiomen aus."""
        # 1. Erkennung & Risiko-Check
        is_zero_a = self.zdu.is_zero(a)
        is_zero_b = self.zdu.is_zero(b)
        risk = self.fap.assess_risk(a, b, is_zero_a, is_zero_b)
        
        if risk > 0.8:
            self.smh.activate()
            
        # 2. Ausführung der NBS-Logik (ZOB nutzt deine neuen Axiome)
        result = self.zob.execute(op, a, b)
        result = self.smh.stabilize(result)
        
        # 3. Klassische Vergleichswerte für ZOFI-Berechnung
        # (Was würde die Standard-Mathematik tun?)
        if op == "mul": 
            classical = 0.0 # Standard: x * 0 = 0
        elif op == "div": 
            classical = 0.0 # Standard: Crash (hier als 0 simuliert)
        else: 
            classical = result
            
        zofi = zofi_metric(result, classical)
        return result, zofi

# Kurzer Selbsttest
if __name__ == "__main__":
    system = NBSCoreSystem()
    
    # Test: Multiplikation (Axiom 1.2: a * 0 = a)
    val, z = system.compute("mul", 42.0, 0.0)
    print(f"NBS-Multiplikation (42 * 0): {val} | ZOFI: {z}")
    
    # Test: Division (Axiom 1.3: a / 0 = a)
    val, z = system.compute("div", 100.0, 0.0)
    print(f"NBS-Division (100 / 0): {val} | ZOFI: {z}")
