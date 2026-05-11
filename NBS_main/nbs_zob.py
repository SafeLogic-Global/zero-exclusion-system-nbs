"""
NBS - Null-Blockierungs-System (Zero Exclusion Logic)
Module: Zero-Operation-Blocker (ZOB)
Logic & Implementation: ORCID [0009-0003-9088-2341]
Status: Experimental / Proof of Concept
License: Apache License 2.0 (see LICENSE file)

DISCLAIMER: This software is provided "AS IS", without warranty of any kind.
The mathematical logic is designed to structurally prevent zero-values in 
mission-critical systems. Use at your own risk.
"""

class ZeroOperationBlocker:
    def __init__(self, substitute=1e-12):
        self.substitute = substitute

    def execute(self, op, a, b):
        """
        Setzt die NBS-Axiome (v1.0) deterministisch um.
        Ziel: Nicht-Operation bei Null-Beteiligung.
        """
        if op == "div":
            # Axiom 1.3: a : 0 = a
            if abs(b) <= self.substitute:
                return a  # Blockierung: Wert bleibt unverändert
            return a / b
        
        if op == "mul":
            # Axiom 1.2: a * 0 = a und 0 * a = a
            if abs(b) <= self.substitute:
                return a
            if abs(a) <= self.substitute:
                return b
            return a * b
            
        if op == "add":
            # Axiom 1.1: a + 0 = a
            return a + b
            
        if op == "sub":
            # Axiom 1.1: a - 0 = a
            return a - b
            
        raise ValueError(f"NBS-ZOB Error: Unknown operation '{op}'")
