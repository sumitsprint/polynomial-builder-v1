# Polynomial Builder V1

Polynomial Builder V1 is a full-stack web application that takes 2D coordinates as input, determines the polynomial that passes through those points, displays the equation in mathematical notation, and plots the graph.


## What it does

- Accepts a set of 2D coordinates as input.
- Determines the degree of the polynomial using the finite differences method.
- Computes the polynomial coefficients using NumPy.
- Displays the polynomial equation in mathematical notation using KaTeX.
- Plots the polynomial graph interactively using Desmos.


## How it works

1. The user enters a set of 2D coordinates.
2. The backend validates that the x-values are equally spaced.
3. The polynomial degree is determined using the finite differences method.
4. NumPy's `polyfit` computes the polynomial coefficients.
5. The backend returns the coefficients to the frontend.
6. The frontend formats the polynomial using KaTeX and plots it interactively using Desmos.


## Tech Stack

### Frontend
- React
- Vite
- JavaScript
- KaTeX
- Desmos API

### Backend
- FastAPI
- Python
- NumPy

