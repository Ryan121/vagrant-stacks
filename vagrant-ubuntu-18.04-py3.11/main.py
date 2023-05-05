from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    """
    A base route to return API uptime
    """
    return {"message": "Hello world from this virtualbox that is run by Vagrant!!"}


@app.get("/extra")
def extra():
    return {"message": "A second endpoint to show test API functionality"}
