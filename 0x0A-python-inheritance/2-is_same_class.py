#!/usr/bin/python3
"""Defines a class-checking function."""


def is_kind_of_class(obj, a_class):
"""return true if obj is the exact class a_class, otherwise false"""
    return isinstance(obj, a_class)
