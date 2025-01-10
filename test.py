from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import uvicorn

app = FastAPI()


class MatrixRequest(BaseModel):
    matrix: list[list[float]]  

@app.post('/calculate')
def calculate(x: MatrixRequest): 
    
    #Pre definning matrices M and B using list comprehension
    
    M = [[0 for _ in range(5)] for _ in range(5)]
    B = [[1 for _ in range(5)] for _ in range(5)] 

    X = np.array(x.matrix)

    # Performing calculations with NumPy method
    np_result = np.array(M) @ np.array(B) 
    np_result = np.add(np_result, B)

    # Manual calculations without NumPy
    product = [[0 for _ in range(5)] for _ in range(5)] 
    for i in range(5):
        for j in range(5):
            for k in range(5):
                product[i][j] += M[i][k] * X[k][j]

    manual_result = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
           manual_result[i][j] = product[i][j] + B[i][j]

  
    # Function to perform sigmoid output
    def sigmoid(x):
       return 1 / (1 + np.exp(-x))

    # Apply the sigmoid function to np_result (NumPy result)
    sigmoid_output = sigmoid(np_result)    
    
    # Return the results
    return {
        'with_num_py': np_result.tolist(), 
        'without_num_py': manual_result,
        'sigmoid_output': sigmoid_output.tolist() 
    }
   
    # Deployed Api : https://week-1-fastapi-for-math-team-kasongo.onrender.com/calculate


if __name__ == "__main__":
    uvicorn.run(app)
