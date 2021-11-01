"""Fichier d'installation de notre script salut.py."""

from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "salut",
    version = "0.1",
    description = "Ce programme vous dit bonjour",
    executables = [Executable("mainWindowMain.py")],
    executables = [Executable("ProductWidgetMain.py")],
    executables = [Executable("pysql.py")],
)