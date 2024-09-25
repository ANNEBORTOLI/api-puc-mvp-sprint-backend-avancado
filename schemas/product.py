from pydantic import BaseModel, validator

from model.product import Product

class ProductViewSchema(BaseModel):
    """ Define como um Produto será retornado.
    """
    id: int = 1
    title: str = "kombucha Pitanga"
    size: str = "350 ml"
    price: str = 18.00
    description: str = "Kombucha é uma bebida milenar de origem chinesa conhecida como o “chá da imortalidade” e é obtida a partir da fermentação natural da infusão do chá minimamente adoçado realizada por bactérias e leveduras benéficas para a saúde."


class ProductDelSchema(BaseModel):
    """ Define como os parâmetros para remover um produto.
    """
    id: int = 1

    @validator('id', pre=True, always=True)
    def valida_id(cls, valor):
        if not valor or valor == "":
            valor = 0
        return valor


class ProductDelViewSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str


class ProductSchema(BaseModel):
    """ Define como um produto a ser inserido/editado deve ser representado
    """
    id: int = 1
    title: str = "kombucha Alfazema"
    size: str = "350 ml"
    price: str = 18.00
    description: str = "Kombucha é uma bebida milenar de origem chinesa conhecida como o “chá da imortalidade” e é obtida a partir da fermentação natural da infusão do chá minimamente adoçado realizada por bactérias e leveduras benéficas para a saúde."

    @validator('id', pre=True, always=True)
    def valida_id(cls, valor):
        if not valor or valor == "":
            valor = 0
        return valor


def apresenta_product(product: Product):
    """ Retorna uma representação do Produto seguindo o schema definido em
        ProductViewSchema.
    """
    return {
        "id": product.id,
        "title": product.title,
        "size": product.size,
        "price": product.price,
        "description": product.description
    }
