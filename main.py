from fastapi import FastAPI

app = FastAPI(title='Sample Docs', description='This is private docs',
              version='1.0') # docs_url=None


@app.get("/")
async def root():
    return {"message": "Hello PyCharm"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
