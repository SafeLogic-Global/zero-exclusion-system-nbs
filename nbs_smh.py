"""
NBS - Null-Blockierungs-System (Zero Exclusion Logic)
Module: Safe-Math-Handler (SMH) - Extended Version
"""

import math

class SafeMathHandler:
    def __init__(self, limit=1e15):
        self.active = False
        self.limit = limit  # Schwellenwert für Normalisierung

    def activate(self):
        self.active = True

    def stabilize(self, value):
        """
        Erzwingt numerische Integrität und normalisiert extreme Ausreißer.
        """
        try:
            val_float = float(value)
            
            # 1. Schutz vor Unendlichkeit (Inf) oder NaN
            if not math.isfinite(val_float):
                return 0.0  # Fallback auf sicheren Null-Zustand
            
            # 2. Normalisierung bei aktivierter SMH-Logik
            # Wenn der Wert das Limit sprengt, wird er auf das Limit gedeckelt
            if self.active and abs(val_float) > self.limit:
                # Vorzeichen beibehalten, aber Wert auf Limit setzen
                return math.copysign(self.limit, val_float)
            
            return val_float
            
        except (ValueError, TypeError):
            return 0.0 # Absoluter Sicherheits-Fallback
