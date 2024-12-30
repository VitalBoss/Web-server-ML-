import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from api.v1.api_route import router

app = FastAPI(

)


class StatusResponse(BaseModel):
    status: str

    model_config = ConfigDict(
        json_schema_extra={"examples": [{"status": "App healthy"}]}
    )
@app.get("/")
async def root():
    # Реализуйте метод получения информации о статусе сервиса.
    return StatusResponse(status="App healthy")

app.include_router(router)


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
