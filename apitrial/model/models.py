import time
from typing import Optional, List

from pydantic import BaseModel


class AddBook(BaseModel):
    Id: int
    name: str
    price: int



# class UpdateSubCategoryModel(BaseModel):
#     Id: int
#     subCategoryName: str
#     categoryId: int
