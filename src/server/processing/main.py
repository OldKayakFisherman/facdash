import datetime

from fastapi import FastAPI
from data import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/processing_queue")
async def processing_queue():
    records = get_processing_queue()
    print(datetime.datetime.now())
    return records


@app.get("/workflow_record/{report_id}")
async def workflow_record(report_id):
    record = get_workflow_record(report_id)
    print(datetime.datetime.now())
    print(record)
    return record

@app.get("/einsearch/{ein}")
async def ein_search(ein):
    records = get_ein_search(ein)
    print(datetime.datetime.now())
    print(records)
    return records



