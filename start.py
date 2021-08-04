from typing import Optional

from fastapi import FastAPI, File, UploadFile
from detect import my_fun

from typing import List
import io
from starlette.responses import Response
from PIL import Image
from io import BytesIO
import os
import shutil

app = FastAPI()
    
@app.post("/LogoNet")
async def logo_yolov5(files: List[UploadFile] = File(...)):
    dir = 'data/uploads'
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.makedirs(dir)
    i=1
    for file in files:
        file_bytes = file.file.read()
        image = Image.open(io.BytesIO(file_bytes))
        name = f"data/uploads/{i}_{file.filename}"
        image.save(name)
        image.filename = name
        i+=1
    s = my_fun()

    return Response(s, media_type="text/html")