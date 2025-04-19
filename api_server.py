from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "SC2TTS Server is running!"}

@app.post("/tts")
async def tts(text: str = "Halo Jos!", speaker: str = "default"):
    # Buat dummy file untuk testing
    with open("output.wav", "wb") as f:
        f.write(b"DUMMY AUDIO")
    return FileResponse("output.wav", media_type="audio/wav", filename="output.wav")
