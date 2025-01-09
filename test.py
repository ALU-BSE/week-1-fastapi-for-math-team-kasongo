from fastapi import FastAPI
import uvicorn 
import numpy as np 

app = FastAPI()

# use the post decorator directly below this
'''
    Initialize M and B as np arrays
'''
@app.post('/calculate')
def f(x):
    M = np.zeros((5,5))
    B = np.ones((5,5))
    X = np.array(x['matrix'])
    product = np.array(M) @ np.array(B)
    result = np.add(product,np.array(B))
    return {'matrix_multiplication':result}


#def sec_f(y):
    # Non numpy function
 
#Implement the formula MX + B
#Have two function one using numpy and another not using numpy
#Return 

#initialize x as a 5 * 5 matrix

#Make a call to the function

#Recreate the function with the sigmoid Function

if __name__ == "__main__":
   uvicorn.run(app,host="127.0.0.1", port=8000)



