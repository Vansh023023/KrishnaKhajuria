from fastapi import FastAPI
from database.ia_filterdb import get_search_results

app = FastAPI()

@app.get("/api/search")
async def search(q: str):
    files, _, _ = await get_search_results(q, 0, 10)

    result = []

    for file in files:
        result.append({
            "name": file.file_name,
            "size": file.file_size,
            "file_id": file.file_id
        })

    return result
