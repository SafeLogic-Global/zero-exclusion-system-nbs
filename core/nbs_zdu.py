"""
NBS - Null-Blockierungs-System (Zero Exclusion Logic)
Module: Zero-Detection-Unit (ZDU)
Logic & Implementation: ORCID [0009-0003-9088-2341]
Status: Experimental / Proof of Concept
License: Apache License 2.0
"""

class ZeroDetectionUnit:
    def __init__(self, epsilon=1e-12):
        self.epsilon = epsilon

    def is_zero(self, x):
        """
        Deterministische Identifikation von Operationen mit Null-Zustand.
        Erkennt Null- oder nullnahe Werte, bevor sie numerisch wirksam werden.
        """
        return abs(x) <= self.epsilon
