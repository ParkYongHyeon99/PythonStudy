from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from router.test1 import router


app = FastAPI()

#CORS설정
origins = [
    'http://localhost:63342'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,    #["*"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class PhoneList(BaseModel):
    name: str = ''
    phone: str = ''


@app.get('/')
def root():
    return {"hello": "world"}

@app.get('/test')
def test(a:int, b:int):
    c = a + b
    return c

@app.get('/submit_data',
         response_model=PhoneList)
def print_name_num(
        name:str,
        phone:str
) ->PhoneList:
    return PhoneList(
        name=name,
        phone=phone
    )

app.include_router(router, tags=['test'])


# uvicorn main:app --reload

