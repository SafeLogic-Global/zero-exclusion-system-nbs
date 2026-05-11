"""
NBS - Null-Blockierungs-System (Zero Exclusion Logic)
Module: Core System & ZOFI (Zero-Operation Fault Index)
Logic & Implementation: ORCID [0009-0003-9088-2341]
Status: Experimental / Proof of Concept
License: Apache License 2.0
"""

from nbs_zdu import ZeroDetectionUnit
from nbs_fap import FallbackArithmeticProtocol # Umbenannt von Predictor
from nbs_zob import ZeroOperationBlocker      # Umbenannt von Override
from nbs_smh import SafeMathHandler           # Umbenannt von Mode

def zofi_metric(result, reference):
    """
    ZOFI - Zero-Operation Fault Index
    Liefert eine standardisierte Qualitätskennzahl.
    """
    scale = max(abs(reference), 1e-12)
    return abs(result - reference) / scale

class NBSCoreSystem:
    def __init__(self):
        self.zdu = ZeroDetectionUnit()
        self.fap = FallbackArithmeticProtocol()
        self.zob = ZeroOperationBlocker()
        self.smh = SafeMathHandler()

    def compute(self, op, a, b, reference=None):
        # 1. Zero detection (ZDU)
        is_zero_a = self.zdu.is_zero(a)
        is_zero_b = self.zdu.is_zero(b)
        
        # 2. Entscheidungs-Protokoll (FAP)
        risk = self.fap.assess_risk(a, b, is_zero_a, is_zero_b)
        if risk > 0.8:
            # 3. Safe Mode Aktivierung (SMH)
            self.smh.activate()
            
        # 4. Sichere Ausführung (ZOB)
        result = self.zob.execute(op, a, b)
        
        # 5. Stabilisierung (SMH)
        result = self.smh.stabilize(result)
        
        # 6. ZOFI Fehlermetrik (Optional)
        zofi_index = None
        if reference is not None:
            zofi_index = zofi_metric(result, reference)
            
        return result, zofi_index

# Beispiel für die Anwendung
if __name__ == "__main__":
    nbs = NBSCoreSystem()
    # Kritische Operation: Division durch Null
    result, zofi = nbs.compute(op="div", a=100.0, b=0.0, reference=100.0)
    print(f"NBS Result: {result}")
    print(f"ZOFI Index: {zofi}")
