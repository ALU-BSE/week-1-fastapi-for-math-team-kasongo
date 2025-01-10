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

    
    
    product = M @ B  
    
    result = np.add(product, B)  # Adding matrix B

    sigmondToResult = sigmond(result)
    
    # Return the result as a dictionary (FastAPI automatically converts to JSON)
    return {'with_numpy': sigmondToResult.tolist()}  # Convert NumPy array to list for JSON serialization

if __name__ == "__main__":
    uvicorn.run(app)
