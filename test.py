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
    
    return {'without_num_py': list(result)}  # Convert NumPy array to list 

if __name__ == "__main__":
    uvicorn.run(app)
