# 3D Print Scheduling using MILP

This project models a single-machine scheduling problem with precedence constraints using Mixed Integer Linear Programming (MILP).

Motivation:
While building a 4-axis CNC foam cutter, multiple parts needed to be printed on a single 3D printer.
Some parts depended on others, and one part required ~11 hours of printing.

The order of printing significantly affected the total build time.

Methods:
1. MILP Optimization (PuLP solver)
2. Random heuristic
3. Longest Processing Time heuristic

Optimal schedule:
6 → 2 → 1 → 3 → 4 → 5

Optimal Makespan:
23.7 hours

Tech Stack:
Python, PuLP, Operations Research

Run:
pip install -r requirements.txt
python src/milp_scheduler.py

Author: Jatin Moolchandani
