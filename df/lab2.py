import sqlite3
import pandas as pd
import kivy
import tkinter
import math
import matplotlib.pyplot as plt
from flask import Flask
import pygame
import panda3d
import numpy as np

# 1. sqlite3
try:
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE test (id INTEGER, name TEXT)")
    cursor.execute("INSERT INTO test VALUES (1, 'Max')")
    connection.commit()
    cursor.execute("SELECT * FROM test")
    print("SQLite3 результат:", cursor.fetchall())
except Exception as e:
    print("Помилка sqlite3:", e)

# 2. pandas
try:
    df = pd.DataFrame({"Name": ["Anna", "Ivan"], "Score": [95, 88]})
    print("Pandas DataFrame:\n", df)
except Exception as e:
    print("Помилка pandas:", e)

# 3. math
try:
    print("sin(0) =", math.sin(0))
    print("sqrt(16) =", math.sqrt(16))
except Exception as e:
    print("Помилка math:", e)

# 4. matplotlib
try:
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.title("Test plot")
    plt.savefig("plot.png")
    print("Графік збережено як plot.png")
except Exception as e:
    print("Помилка matplotlib:", e)

# 5. numpy
try:
    arr = np.array([1, 2, 3, 4])
    print("NumPy масив * 2:", arr * 2)
except Exception as e:
    print("Помилка numpy:", e)
