from fastapi.middleware.cors import CORSMiddleware

origins = [
    "https://nimble-melomakarona-1d767c.netlify.app",
    "http://localhost:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
