from fastapi import File, UploadFile, FastAPI
from typing import List
import os

app = FastAPI()

@app.post("/upload")
def upload(files: List[UploadFile] = File(...)):
    for file in files:
        try:
            contents = file.file.read()
            with open(f'files/{file.filename}', 'wb') as f:
                f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            file.file.close()
            os.remove(f'files/{file.filename}')
    return {"message": f"Successfuly uploaded {[file.filename for file in files]}"} 