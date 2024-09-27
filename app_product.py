from model import Session
from model.product import Product
from schemas.product import ProductDelSchema, ProductSchema, ProductViewSchema, apresenta_product, apresenta_products


def create_product(form: ProductSchema):
    """ Adiciona um novo produto

    Retorna uma representação do produto
    """

    try:
        session = Session()
        product = Product(
            form.title, form.size, form.price, form.description
        )
        session.add(product)
        session.commit()

        return apresenta_product(product), 200

    except ValueError as e:
        return {"message": str(e)}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar novo produto :/"
        return {"message": error_msg}, 400


def search_product(query: ProductDelSchema):
    """Busca no BD pelo Produto a partir de seu id
    """
    try:
        session = Session()
        product = session.query(Product).filter(Product.id == query.id).first()

        if not product:
            error_msg = "Produto não encontrado na base :/"
            return {"message": error_msg}, 404

        return apresenta_product(product), 200

    except Exception as e:
        error_msg = "Não foi possível consultar o Produto :/"
        return {"message": error_msg}, 400

def search_products():
    """Busca no BD pelos Produtos
    """
    try:
        session = Session()
        products = session.query(Product).all()

        return apresenta_products(products), 200

    except Exception as e:
        error_msg = "Não foi possível consultar os Produtos :/"
        return {"message": error_msg}, 400


def change_product(form: ProductViewSchema):
    """ Edita o Produto na base de dados
    """

    try:
        session = Session()
        product = session.query(Product).filter(
            Product.id == form.id).first()

        if not product:
            error_msg = "Produto não encontrado na base :/"
            return {"message": error_msg}, 404

        product.setProduct(form.title, form.size, form.price,
                            form.description)
        session.commit()

        return apresenta_product(product), 200

    except ValueError as e:
        return {"message": str(e)}, 409

    except Exception as e:
        error_msg = "Não foi possível editar o produto :/"
        return {"message": error_msg}, 400


def remove_product(form: ProductDelSchema):
    """Deleta o produto na base de dados
    """

    try:
        session = Session()
        product = session.query(Product).filter(
            Product.id == form.id).first()

        if not product:
            error_msg = "Produto não encontrado na base :/"
            return {"message": error_msg}, 404

        session.delete(product)
        session.commit()

        return {"message": "Produto removido!"}, 200

    except ValueError as e:
        return {"message": str(e)}, 409

    except Exception as e:
        error_msg = "Não foi possível remover o produto :/"
        return {"message": error_msg}, 400
