from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def start_page():
    return 'hi there'

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
