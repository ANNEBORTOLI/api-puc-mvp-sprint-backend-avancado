from flask import redirect

from flask_openapi3 import OpenAPI, Info, Tag

from flask_cors import CORS

from app_product import change_product, create_product, remove_product, search_product
from schemas.error import ErrorSchema
from schemas.product import ProductDelSchema, ProductDelViewSchema, ProductSchema, ProductViewSchema

info = Info(title="API de Produtos - PiKombucha", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo as tags do OpenAPI
home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
product_tag = Tag(
    name="Product", description="Operações relacionadas a produtos")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# Rotas referentes a endereço


@app.post('/product', tags=[product_tag],
          responses={"200": ProductViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_product(form: ProductSchema):
    """Adiciona um novo produto na base de dados
    """
    return create_product(form)


@app.put('/product', tags=[product_tag],
         responses={"200": ProductViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def edit_product(form: ProductSchema):
    """Edita o produto na base de dados
    """
    return change_product(form)


@app.get('/product', tags=[product_tag],
         responses={"200": ProductViewSchema, "404": ErrorSchema})
def get_product():
    """Busca no BD pelo produto 
    """
    return search_product()


@app.delete('/product', tags=[product_tag],
            responses={"200": ProductDelViewSchema, "404": ErrorSchema})
def del_product(form: ProductDelSchema):
    """Deleta o produto na base de dados
    """
    return remove_product(form)
