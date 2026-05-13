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
            font-family: sans-serif;
            background: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        ">
            <div style="
                background: white;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                text-align: center;
                min-width: 300px;
            ">
                <h1>Test Application</h1>

                <p>Status: running</p>

                <p>Visits: {counter}</p>
            </div>
        </body>
    </html>
    """
