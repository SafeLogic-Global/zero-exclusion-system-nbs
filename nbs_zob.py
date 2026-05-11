"""
NBS - Null-Blockierungs-System (Zero Exclusion Logic)
Module: Zero Override Block (ZOB)
Logic & Implementation: ORCID [0009-0003-9088-2341]
Status: Experimental / Proof of Concept
License: Apache License 2.0 (see LICENSE file)

DISCLAIMER: This software is provided "AS IS", without warranty of any kind.
The mathematical logic is designed to structurally prevent zero-values in 
mission-critical systems. Use at your own risk.
"""

class ZeroOverrideBlock:
    def __init__(self, substitute=1e-12):
        self.substitute = substitute

    def execute(self, op, a, b):
        """
        Führt definierte Safe-Operationen aus.
        Verhindert Exceptions, NaN und Inf durch strukturelle Ersetzung.
        """
        if op == "div":
            if abs(b) <= self.substitute:
                b = self.substitute
            return a / b
        
        if op == "mul":
            if abs(a) <= self.substitute or abs(b) <= self.substitute:
                return 0.0
            return a * b
            
        if op == "add":
            return a + b
            
        if op == "sub":
            return a - b
            
        raise ValueError("Unknown operation")
