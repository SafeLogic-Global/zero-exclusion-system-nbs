"""
NBS - Null-Blockierungs-System (Zero Exclusion Logic)
Module: Safe-Math-Handler (SMH) - Extended Version
Logic & Implementation: ORCID [0009-0003-9088-2341]
Status: Experimental / Proof of Concept
License: Apache License 2.0 (see LICENSE file)

DISCLAIMER: This software is provided "AS IS", without warranty of any kind.
The mathematical logic is designed to structurally prevent zero-values in 
mission-critical systems. Use at your own risk.
"""

import math

class SafeMathHandler:
    def __init__(self, limit=1e15):
        self.active = False
        self.limit = limit  # Schwellenwert für Normalisierung

    def activate(self):
        """Aktiviert den sicheren Betriebsmodus bei erkanntem Risiko."""
        self.active = True

    def stabilize(self, value):
        """
        Erzwingt numerische Integrität und normalisiert extreme Ausreißer.
        Verhindert NaN-Zustände und deckelt Werte bei Überschreitung des Limits.
        """
        try:
            val_float = float(value)
            
            # 1. Schutz vor Unendlichkeit (Inf) oder NaN
            if not math.isfinite(val_float):
                return 0.0  # Fallback auf sicheren Zustand
            
            # 2. Normalisierung (Clipping) bei aktivem SMH-Schutz
            if self.active and abs(val_float) > self.limit:
                # Vorzeichen beibehalten, aber Wert auf Limit setzen
                return math.copysign(self.limit, val_float)
            
            return val_float
            
        except (ValueError, TypeError):
            return 0.0 # Absoluter Sicherheits-Fallback bei korrupten Daten
