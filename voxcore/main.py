from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/status")
def get_status():
    return {"status": "ok", "service": "voxcore"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 15001))
    uvicorn.run(app, host="0.0.0.0", port=port)
