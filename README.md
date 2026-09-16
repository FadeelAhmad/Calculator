# Full-Stack Scientific Calculator

A modern, interactive web-based scientific calculator built with a Python backend and an HTML/JS/CSS frontend. It supports basic arithmetic, scientific operations, and graphing capabilities.

## Features

* **Basic Arithmetic**: Addition, subtraction, multiplication, and division.
* **Scientific Operations**: Square root, sine, cosine, tangent, logarithms, and powers.
* **Graphing Engine**: Enter an algebraic function (e.g., `sin(x)` or `x**2`) and instantly visualize it on an interactive graph.
* **Modern UI**: A sleek, dark-mode calculator interface.
* **Secure Evaluation**: The backend safely evaluates mathematical expressions.

## Tech Stack

* **Backend**: Python, [FastAPI](https://fastapi.tiangolo.com/), Uvicorn, NumPy
* **Frontend**: HTML5, CSS3, Vanilla JavaScript
* **Graphing Library**: [Chart.js](https://www.chartjs.org/)

## Installation and Setup

To run this project locally, follow these steps:

### 1. Start the Backend Server

Open a terminal in the root of the project directory and install the Python dependencies:

```bash
cd backend
pip install -r requirements.txt
```

Run the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

The backend API will start running on `http://127.0.0.1:8000`.

### 2. Launch the Frontend

Once the backend is running, you can simply open the `frontend/index.html` file in any modern web browser to interact with the calculator.

## Usage

1. **Calculate**: Use the on-screen buttons to build an expression on the display, then press `=` to calculate the result.
2. **Graph**: In the graph section, enter a valid mathematical function in terms of `x` (for example, `x**3 - 2*x`) and click **Graph**. The backend will generate the plot points and render the curve on the canvas.
