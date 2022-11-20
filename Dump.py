import os, sys
try:
    __import__("Dump").file_menu()
except Exception as e:
    exit(str(e))
