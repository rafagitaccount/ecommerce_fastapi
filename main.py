from fastapi import FastAPI
from user import router as user_router
from products import router as product_router
from cart import router as cart_router
from orders import router as order_router

app = FastAPI(title="EcommerceApp",
              docs_url="/private_docs",
              version="0.0.1")


app.include_router(user_router.router)
app.include_router(product_router.router)
app.include_router(cart_router.router)
app.include_router(order_router.router)
