"""
NBS - Null-Blockierungs-System (Zero Exclusion Logic)
Module: Central Control Unit & ZOFI-Metric (Core)
Logic & Implementation: ORCID [0009-0003-9088-2341]
Status: Experimental / Proof of Concept
Version: 1.0
License: Apache License 2.0 (see LICENSE file)

DISCLAIMER: This software is provided "AS IS", without warranty of any kind.
The mathematical logic is designed to structurally prevent zero-values in 
mission-critical systems. Use at your own risk.
"""

from nbs_zdu import ZeroDetectionUnit
from nbs_fap import FallbackArithmeticProtocol
from nbs_zob import ZeroOperationBlocker
from nbs_smh import SafeMathHandler

def zofi_metric(nbs_result, classical_reference):
    """Berechnet den Zero-Operation Fault Index (ZOFI)."""
    # Verhindert Division durch Null bei der Metrik-Berechnung selbst
    scale = max(abs(classical_reference), 1e-12)
    return abs(nbs_result - classical_reference) / scale

class NBSCoreSystem:
    def __init__(self, safe_limit=1e15):
        """
        Initialisiert das NBS mit den vier Kern-Modulen.
        :param safe_limit: Maximal zulässiger Wert, bevor der SMH eingreift.
        """
        self.zdu = ZeroDetectionUnit()
        self.fap = FallbackArithmeticProtocol()
        self.zob = ZeroOperationBlocker()
        # Der SMH erhält hier sein Limit für die Normalisierung
        self.smh = SafeMathHandler(limit=safe_limit)

    def compute(self, op, a, b):
        """Führt eine Operation nach den NBS-Axiomen aus."""
        # 1. Erkennung & Risiko-Check
        is_zero_a = self.zdu.is_zero(a)
        is_zero_b = self.zdu.is_zero(b)
        risk = self.fap.assess_risk(a, b, is_zero_a, is_zero_b)
        
        # SMH aktivieren, wenn Risiko hoch ist (> 0.8)
        if risk > 0.8:
            self.smh.activate()
            
        # 2. Ausführung der NBS-Logik (ZOB nutzt die Axiome aus dem Whitepaper)
        result = self.zob.execute(op, a, b)
        
        # 3. Stabilisierung (Inklusive Limit-Prüfung und NaN-Schutz)
        result = self.smh.stabilize(result)
        
        # 4. Klassische Vergleichswerte für ZOFI-Berechnung
        if op == "mul": 
            classical = 0.0 # Standard: x * 0 = 0
        elif op == "div": 
            classical = 0.0 # Standard: Crash (hier als 0 simuliert)
        else: 
            classical = result
            
        zofi = zofi_metric(result, classical)
        return result, zofi

if __name__ == "__main__":
    # Test mit niedrigem Limit, um die Normalisierung zu provozieren
    system = NBSCoreSystem(safe_limit=1000.0)
    
    print("--- NBS Stabilitäts-Test ---")
    
    # Test 1: Axiom-Check (42 * 0 = 42)
    val, z = system.compute("mul", 42.0, 0.0)
    print(f"Multiplikation (42 * 0): {val} | ZOFI: {z}")
    
    # Test 2: Normalisierungs-Check (5000 / 0 -> Deckelung auf 1000)
    val_high, z_high = system.compute("div", 5000.0, 0.0) 
    print(f"Normalisierung (5000 / 0 -> Limit): {val_high} | ZOFI: {z_high}")
