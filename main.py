from fastapi import FastAPI
import uvicorn

from starlette.middleware.cors import CORSMiddleware #cors middleware
from starlette.middleware.httpsredirect import (  # noqa  - https redirect
    HTTPSRedirectMiddleware as HTTPSRedirectMiddleware,
)
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from dotenv import load_dotenv

from patient_info.info_router import router as info_router


load_dotenv()


app = FastAPI()

# middleware
origins = [ 
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(info_router)



if __name__ == '__main__': 
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)