from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

counter = 0

@app.get("/", response_class=HTMLResponse)
def home():
    global counter
    counter += 1

    return f"""
    <html>
        <body style="
            margin:0;
            display:flex;
            justify-content:center;
            align-items:center;
            height:100vh;
            font-family:sans-serif;
            background:white;
        ">
            <h1>visits: {counter}</h1>
        </body>
    </html>
    """
