from fastapi import(
    FastAPI
)

from routers import(
    tweets, users, auth
)

app = FastAPI()

app.include_router(tweets.tweets)
app.include_router(users.users)
app.include_router(auth.auth)