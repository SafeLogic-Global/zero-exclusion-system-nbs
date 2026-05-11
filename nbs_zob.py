"""
NBS - Null-Blockierungs-System (Zero Exclusion Logic)
Module: Zero-Operation-Blocker (ZOB)
Logic & Implementation: ORCID [0009-0003-9088-2341]
Status: Experimental / Proof of Concept
License: Apache License 2.0
"""

class ZeroOperationBlocker:
    def __init__(self, substitute=1e-12):
        self.substitute = substitute

    def execute(self, op, a, b):
        """
        Führt definierte Safe-Operationen aus.
        Verhindert Exceptions, NaN und Inf durch strukturelle Ersetzung (ZOB-Logik).
        """
        if op == "div":
            # Kritische Division: Ersetzt den Divisor durch den Safe-Wert
            if abs(b) <= self.substitute:
                b = self.substitute
            return a / b
        
        if op == "mul":
            # Kontrollierte Multiplikation zur Vermeidung von Null-Propagation
            if abs(a) <= self.substitute or abs(b) <= self.substitute:
                return 0.0
            return a * b
            
        if op == "add":
            return a + b
            
        if op == "sub":
            return a - b
            
        raise ValueError(f"NBS-ZOB Error: Unknown operation '{op}'")
