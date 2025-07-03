import uvicorn
from fastapi import FastAPI, UploadFile, File
import io
import aiohttp

app = FastAPI()

@app.post("/moderate")
async def upload_img(file: UploadFile = File(...)):
    contents = await file.read()
    file_io = io.BytesIO(contents)
    file_io.seek(0)

    url = 'https://nsfw-categorize.it/api/upload'

    data = aiohttp.FormData()
    data.add_field("image", file_io)

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as responce:
            result = await responce.json()
            print("Ответ:", result)
            if result["data"]["nsfw"] and result["data"]["confidence"] >= 70:
                return {"status": "REJECTED", "reason": "NSFW content"}
            else:
                return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:app",
                host='0.0.0.0',
                port=8000,
                reload=True,
                workers=1)
