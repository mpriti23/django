import time
import psutil
import uvicorn
from cacheout import Cache
from fastapi import FastAPI, Path, Request, Header, Response, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
import json
from model.models import *
from utils.dbutil import mongodb_connection
from utils.utils import *

origins = ["*"]

app = FastAPI()


@app.post("/v1/api/addBook")
async def addBook(item:AddBook):
    m_item=item.dict()
    _id=get_random_id()
    m_item['_id']=_id
    mongodb_connection('book').insert_one(m_item)
    # mongodb_connection('bookdata').insert_one({'Id':item.Id,'name':item.name,'price':item.price})
    return {'msg' : 'successful'} 

@app.get("/v1/api/getBook")
async def getBook():
    listofitems = []
    for x in mongodb_connection('book').find():
        listofitems.append(x)
    return listofitems

@app.get("/v1/api/getBook/{price}")
async def getBook(price:int):
    x=mongodb_connection('book').find_one({'price':price})
    return x 


if __name__ == "__main__":
    print("starting server ")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
