"""Test functions for module factorial"""
# MCS 260 Fall 2021 Lecture 2**5
# Meant to be run with pytest, not as a script

import factorial

def test_fact_0():
    "test fact(0)==1"
    assert factorial.fact(0)==1

def test_fact_iterative_0():
    "test fact_iterative(0)==1"
    assert factorial.fact_iterative(0)==1

known_factorials = {
    1: 1,
    2: 2,
    3: 6,
    4: 24,
    10: 3628800
}

def test_fact_behavior():
    "test several return values of fact()"
    for k in known_factorials:
        assert factorial.fact(k) == known_factorials[k]

def test_fact_iterative_behavior():
    "test several return values of fact_iterative()"
    for k in known_factorials:
        assert factorial.fact_iterative(k) == known_factorials[k]

def test_fact_recursive_iterative_comparison():
    "test that fact() and fact_iterative() return same values"
    for n in range(900):
        assert factorial.fact(n) == factorial.fact_iterative(n)
