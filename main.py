from fastapi import FastAPI,HTTPException,status
from Modelos import LinearRegression
#from Schemas import IrisSchema
import pickle 

app = FastAPI()

@app.get("/",status_code=status.HTTP_200_OK)

async def root():
    #return{"message": "Hello World2"}
    num1=100
    num2=3
    respuesta= num1**num2
    return{"message": f"Esta es la respuesta {respuesta} holaaaaa"}


@app.get("/saludog10")
def saludar():
    """
    cuando llamo a este endpoint se hace un proceso interno
    """
    print('Hola soy una funcion')
    return{"message":"holis g10"}

@app.post("/predict/dtc", status_code= status.HTTP_200_OK)
async def predict_flower():#data:IrisSchema):
    """
    Esta funcion nos predecirá si es una setosa, virginica o versicolor
    """
    ModPredict= pickle.load(open("Modelos/model_dtc.pkl",'rb'))
    #prediccion=model_dtc.predict(data)
    return{"message":"holis not working code"}

#@app.post("/payment")
#def saludar(request: Request):
#    print('Hola soy una funcion')

#    id=request['id']
#    email= request['customer_details']['email']






