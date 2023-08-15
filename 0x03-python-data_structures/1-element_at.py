#!/usr/bin/python3
# 1-element_at.py
# clifford karimi<Ckarimi676@gmail.com>

def element_at(my_list, idx):
    """Retrive an element from a list."""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
