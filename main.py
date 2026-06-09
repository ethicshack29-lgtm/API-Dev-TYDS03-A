from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return{"hello":"Dear"}
    
@app.get("/view")
def view():
    students=[
        {
            "Id":1,
            "Name":"Aditya",
            "Age":19,
            "Course":"BscDS"
        },
        {
            "Id":2,
            "Name":"Aman",
            "Age":21,
            "Course":"BscIT"
        }
    ]
    return students