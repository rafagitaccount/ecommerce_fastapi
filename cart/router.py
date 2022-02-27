from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

import db
from user.schema import User
from . import services
from . import schema
from auth.jwt import get_current_user


router = APIRouter(
    tags=["Cart"],
    prefix='/cart'
)


@router.get('/add', status_code=status.HTTP_201_CREATED)
async def add_product_to_cart(product_id: int,
                              database: Session = Depends(db.get_db),
                              current_user: User = Depends(get_current_user)):
    result = await services.add_to_cart(product_id, current_user, database)
    return result


@router.get('/', response_model=schema.ShowCart)
async def get_all_cart_items(database: Session = Depends(db.get_db),
                             current_user: User = Depends(get_current_user)):
    result = await services.get_all_items(database, current_user)
    return result


@router.delete('/{cart_item_id}', status_code=status.HTTP_204_NO_CONTENT,
               response_class=Response)
async def remove_cart_item_by_id(cart_item_id: int,
                                 database: Session = Depends(db.get_db),
                                 current_user: User = Depends(get_current_user)):
    await services.remove_cart_item(cart_item_id, current_user, database)
