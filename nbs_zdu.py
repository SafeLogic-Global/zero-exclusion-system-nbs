"""
NBS - Null-Blockierungs-System (Zero Exclusion Logic)
Module: Zero Detection Unit (ZDU)
Logic & Implementation: ORCID [0009-0003-9088-2341]
Status: Experimental / Proof of Concept
License: Apache License 2.0 (see LICENSE file)

DISCLAIMER: This software is provided "AS IS", without warranty of any kind.
The mathematical logic is designed to structurally prevent zero-values in 
mission-critical systems. Use at your own risk.
"""

class ZeroDetectionUnit:
    def __init__(self, epsilon=1e-12):
        self.epsilon = epsilon

    def is_zero(self, x):
        """Erkennt Null- oder Null-nahe Werte bevor sie Schaden anrichten."""
        return abs(x) <= self.epsilon
