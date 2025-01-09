from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import uvicorn

app = FastAPI()

# Define a Pydantic model for the request body (5x5 matrix)
class MatrixRequest(BaseModel):
    matrix: list[list[float]]  # A list of lists, each containing floats (5x5 matrix)

@app.post('/calculate')
def calculate(x: MatrixRequest):  # Accept matrix as the body input
    # Initialize M and B as numpy arrays
    M = np.zeros((5, 5))  # Zero matrix
    B = np.ones((5, 5))    # Ones matrix
    
    # Convert the input matrix to a NumPy array
    X = np.array(x.matrix)
    
    # Perform matrix multiplication: M * B
    product = M @ B  # Matrix multiplication
    
    # Add matrix B to the product
    result = np.add(product, B)  # Adding matrix B
    
    # Return the result as a dictionary (FastAPI automatically converts to JSON)
    return {'matrix_multiplication': result.tolist()}  # Convert NumPy array to list for JSON serialization

# Run the application using Uvicorn in development mode
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
