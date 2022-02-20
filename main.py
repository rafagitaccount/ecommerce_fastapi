from fastapi import FastAPI
from user import router as user_router
from products import router as product_router

app = FastAPI(title="EcommerceApp", version="0.0.1")


app.include_router(user_router.router)
app.include_router(product_router.router)
