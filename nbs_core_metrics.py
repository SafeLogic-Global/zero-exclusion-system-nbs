"""
NBS - Null-Blockierungs-System (Zero Exclusion Logic)
Module: Core System & Error Metrics
Logic & Implementation: ORCID [0009-0003-9088-2341]
Status: Experimental / Proof of Concept
License: Apache License 2.0 (see LICENSE file)

DISCLAIMER: This software is provided "AS IS", without warranty of any kind.
"""

from nbs_zdu import ZeroDetectionUnit
from nbs_fap import FailureAnticipationPredictor
from nbs_zob import ZeroOverrideBlock
from nbs_smh import SafeModeHandler

def nbs_error_metric(result, reference):
    """
    Standardisierte, null-sichere Fehlermetrik.
    Liefert eine Qualitätskennzahl für Audit & Monitoring.
    """
    scale = max(abs(reference), 1e-12)
    return abs(result - reference) / scale

class NBSCoreSystem:
    def __init__(self):
        self.zdu = ZeroDetectionUnit()
        self.fap = FailureAnticipationPredictor()
        self.zob = ZeroOverrideBlock()
        self.smh = SafeModeHandler()

    def compute(self, op, a, b, reference=None):
        # 1. Zero detection
        is_zero_a = self.zdu.is_zero(a)
        is_zero_b = self.zdu.is_zero(b)
        
        # 2. Risikoabschätzung
        risk = self.fap.assess_risk(a, b, is_zero_a, is_zero_b)
        if risk > 0.8:
            self.smh.activate()
            
        # 3. Sichere Ausführung
        result = self.zob.execute(op, a, b)
        
        # 4. Stabilisierung
        result = self.smh.stabilize(result)
        
        # 5. Fehlermetrik (optional)
        error = None
        if reference is not None:
            error = nbs_error_metric(result, reference)
            
        return result, error

# Beispiel für die Anwendung
if __name__ == "__main__":
    nbs = NBSCoreSystem()
    # Kritische Operation: Division durch Null
    result, error = nbs.compute(op="div", a=100.0, b=0.0, reference=100.0)
    print(f"NBS Result: {result}")
    print(f"NBS Error metric: {error}")
