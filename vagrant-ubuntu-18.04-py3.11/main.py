from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    """
    A base route to return API uptime
    """
    return {"message": "Hello world from this virtualbox that is run by Vagrant!!"}