"""Lectura común de las tablas del laboratorio."""

from pathlib import Path

import pandas as pd


INPUT_DIRECTORY = Path(__file__).resolve().parents[1] / "files" / "input"


def read_table(name):
    """Lee una tabla TSV por su nombre."""
    return pd.read_csv(INPUT_DIRECTORY / name, sep="\t")
