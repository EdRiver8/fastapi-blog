from typing import List, Optional
from fastapi import APIRouter, Form, Header, Cookie
from fastapi.responses import Response, HTMLResponse, PlainTextResponse
from custom_log import log

# Tags permite agrupar en el swagger
router = APIRouter(prefix="/product", tags=["product"])

products = ["watch", "cameras", "phone"]


@router.post("/new")
def create_product(name: str = Form(...)):
    products.append(name)
    return products


# respuesta en archivo plano
@router.get("/all")
def get_all_products():
    log("MyAPI", "Call to get all products")
    # return products
    data = " ".join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="test_cookie_value")
    return response


@router.get("/withheader")
def get_products(
    response: Response,
    custom_header: Optional[List[str]] = Header(None),
    test_cookie: Optional[str] = Cookie(None),
):
    if custom_header:
        response.headers["custom_response_headers"] = ", ".join(custom_header)
    return {"data": products, "custom_header": custom_header, "my_cookie": test_cookie}


# respuesta en html
@router.get(
    "/{id}",
    responses={
        200: {
            "content": {"text/html": {"example": "<div>Product</div>"}},
            "description": "Returns the HTML fron an object",
        },
        400: {
            "content": {"text/plain": {"example": "Product Not Exists"}},
            "description": "A Clear Text Error Message",
        },
    },
)
def get_product_by_id(id: int):
    if id >= len(products):
        out = "Product Not Exists"
        return PlainTextResponse(status_code=404, content=out, media_type="text/plain")
    else:
        product = products[id]
        out = f"""
        <head>
        <style>
        .product{{
            width: 100px;
            height: 30px;
            border: 2px inset green;
            background-color: lightblue;
            text-align: center;
        }}
        </style>
        <div class="product">{product}</div>
        """
        return HTMLResponse(content=out, media_type="text/html")
