#!/usr/bin/python3
"""
    Module contains matrix_mul function
    Returns: list
    Tests contained in tests/100-matrix_mul.txt
"""


def matrix_mul(m_a: list, m_b: list):
    """
        Function multiplies two matrices
    """
    params = {"m_a": m_a, "m_b": m_b}
    _validateParamsAsNotNull(params)
    _validateParamsAsList(params)
    _validateParamsAsListofLists(params)
    _validateParamsElemAsIntOrFloat(params)
    _validateParamsAsRectangle(params)
    _validateParamsCantBeMultiplied(params)


def _validateParamsAsList(params: dict):
    for key, value in params.items():
        if not isinstance(value, list):
            raise TypeError(key + " must be a list")


def _validateParamsAsListofLists(params: dict):
    for key, value in params.items():
        if any(not isinstance(row, list) for row in value):
            raise TypeError(key + " must be a list of lists")


def _validateParamsAsNotNull(params: dict):
    for key, value in params.items():
        if len(value) == 0 or any(len(row) == 0 for row in value):
            raise ValueError(key + " can't be empty")


def _validateParamsElemAsIntOrFloat(params: dict):
    for key, value in params.items():
        if any(not isinstance(elem, (int, float))
               for row in value for elem in row):
            raise TypeError(key + " should contain only integers or floats")


def _validateParamsAsRectangle(params: dict):
    for key, value in params.items():
        if len(set([len(row) for row in value])) > 1:
            raise TypeError("each row of " + key + " must be of the same size")


def _validateParamsCantBeMultiplied(params: dict):
    if len(params["m_a"][0]) != len(params["m_b"]):
        raise ValueError("m_a and m_b can't be multiplied")
