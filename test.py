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

  

    sigmondToResult = sigmond(result)
    
    # Return the result as a dictionary (FastAPI automatically converts to JSON)
    return {'with_numpy': sigmondToResult.tolist()}  # Convert NumPy array to list for JSON serialization

if __name__ == "__main__":
    uvicorn.run(app)
