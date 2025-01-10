from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import uvicorn

app = FastAPI()


class MatrixRequest(BaseModel):
    matrix: list[list[float]]  

@app.post('/calculate')
def calculate(x: MatrixRequest): 
    
    M = np.zeros((5, 5))  
    B = np.ones((5, 5)) 
    
    
    X = np.array(x.matrix)
    
    
    product = M @ B  
    
    result = np.add(product, B)  # Adding matrix B

    sigmondToResult = sigmond(result)
    
    # Return the result as a dictionary (FastAPI automatically converts to JSON)
    return {'with_numpy': sigmondToResult.tolist()}  # Convert NumPy array to list for JSON serialization

if __name__ == "__main__":
    uvicorn.run(app)
