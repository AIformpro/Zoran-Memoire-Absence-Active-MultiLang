#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo bayésienne — Mémoire par Absence Active
Observation: pas de souvenir (not_mem) d'un événement supposé distinctif.
On met à jour P(no_event | not_mem).
"""
import argparse

def posterior_no_event(prior_event: float, m: float, f: float) -> float:
    """
    prior_event: P(H) — probabilité a priori que l'événement ait eu lieu
    m = P(mem | H) — probabilité de se souvenir si l'événement a eu lieu (haute)
    f = P(mem | ¬H) — faux positif de souvenir (basse)
    Retourne P(¬H | ¬mem)
    """
    pH = prior_event
    pNotH = 1 - pH
    p_notmem_given_H = 1 - m
    p_notmem_given_notH = 1 - f
    num = p_notmem_given_notH * pNotH
    den = p_notmem_given_H * pH + p_notmem_given_notH * pNotH
    if den == 0:
        return 1.0 if num > 0 else 0.0
    return num / den

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--prior", type=float, default=0.5, help="P(H) — a priori que l'événement a eu lieu")
    ap.add_argument("--m", type=float, default=0.95, help="P(mem | H) — souvenir si l'événement a eu lieu (haut)")
    ap.add_argument("--f", type=float, default=0.05, help="P(mem | ¬H) — faux positif (bas)")
    args = ap.parse_args()

    p_noevent = posterior_no_event(args.prior, args.m, args.f)
    print("=== Mémoire par Absence Active — Démo Bayésienne ===")
    print(f"P(H)            = {args.prior:.4f}  (événement a eu lieu)")
    print(f"P(mem | H)      = {args.m:.4f}")
    print(f"P(mem | ¬H)     = {args.f:.4f}")
    print("Observation     = ¬mem (pas de souvenir)")
    print(f"P(¬H | ¬mem)    = {p_noevent:.4f}  ← probabilité que l'événement n'ait pas eu lieu")

