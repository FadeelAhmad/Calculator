from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import math

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class EvaluateRequest(BaseModel):
    expression: str

class GraphRequest(BaseModel):
    equation: str
    x_min: float = -10.0
    x_max: float = 10.0

@app.post("/calculate")
def calculate(req: EvaluateRequest):
    try:
        allowed_names = {
            "sin": math.sin, "cos": math.cos, "tan": math.tan,
            "asin": math.asin, "acos": math.acos, "atan": math.atan,
            "sqrt": math.sqrt, "log": math.log, "log10": math.log10,
            "pi": math.pi, "e": math.e, "abs": abs
        }
        code = compile(req.expression, "<string>", "eval")
        for name in code.co_names:
            if name not in allowed_names:
                raise NameError(f"Use of '{name}' is not allowed")
                
        result = eval(code, {"__builtins__": {}}, allowed_names)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/graph")
def graph(req: GraphRequest):
    try:
        x_vals = np.linspace(req.x_min, req.x_max, 200)
        y_vals = []
        
        allowed_names = {
            "sin": math.sin, "cos": math.cos, "tan": math.tan,
            "asin": math.asin, "acos": math.acos, "atan": math.atan,
            "sqrt": math.sqrt, "log": math.log, "log10": math.log10, "pi": math.pi,
            "e": math.e, "abs": abs
        }
        
        code = compile(req.equation, "<string>", "eval")
        for name in code.co_names:
            if name not in allowed_names and name != "x":
                raise NameError(f"Use of '{name}' is not allowed")
                
        for x in x_vals:
            local_vars = {"x": float(x)}
            try:
                y = eval(code, {"__builtins__": {}}, {**allowed_names, **local_vars})
                y_vals.append(y)
            except ValueError:
                # Handle math domain errors (like sqrt of negative number)
                y_vals.append(None)
            
        return {"x": x_vals.tolist(), "y": y_vals}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
