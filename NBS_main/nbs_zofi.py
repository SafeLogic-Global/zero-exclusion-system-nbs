"""
NBS - Null-Blockierungs-System (Zero Exclusion Logic)
Module: Zero-Operation Fault Index (ZOFI)
Logic & Implementation: ORCID [0009-0003-9088-2341]
"""

def zofi_metric(nbs_result, classical_reference):
    """
    Berechnet den Zero-Operation Fault Index (ZOFI).
    Quantifiziert die Abweichung der NBS-Logik zur klassischen Arithmetik.
    """
    # Verhindert Division durch Null bei der Metrik-Berechnung selbst
    scale = max(abs(classical_reference), 1e-12)
    return abs(nbs_result - classical_reference) / scale
