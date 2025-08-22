from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def root():
    # Read the HTML file and return it
    html_file = Path("static/index.html")
    if html_file.exists():
        return html_file.read_text()
    else:
        return """
        <html>
            <body>
                <h1>Static files not found</h1>
                <p>Please ensure static/index.html exists</p>
            </body>
        </html>
        """