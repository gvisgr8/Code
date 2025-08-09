# Python Calculator

A simple web-based calculator application built with Python and Flask.

## Features

*   Basic arithmetic operations: addition, subtraction, multiplication, and division.
*   A clean, user-friendly interface.
*   A RESTful API for performing calculations.

## Getting Started

### Prerequisites

*   Python 3.6 or later
*   pip

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd python/Calculator
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the web application, execute the following command:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5001`.

## Running the Tests

To run the tests, use the following command:

```bash
pytest
```

## API Documentation

The application provides a single API endpoint for performing calculations.

### `POST /calculate`

This endpoint performs a calculation based on the provided JSON payload.

**Request Body:**

```json
{
  "operation": "add",
  "a": 5,
  "b": 3
}
```

*   `operation` (string): The operation to perform. Can be `add`, `subtract`, `multiply`, or `divide`.
*   `a` (number): The first number.
*   `b` (number): The second number.

**Success Response:**

*   **Code:** 200 OK
*   **Content:**
    ```json
    {
      "result": 8
    }
    ```

**Error Response:**

*   **Code:** 400 Bad Request
*   **Content:**
    ```json
    {
      "error": "Cannot divide by zero."
    }
    ```
