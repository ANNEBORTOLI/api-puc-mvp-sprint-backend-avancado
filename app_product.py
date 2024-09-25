from model import Session
from model.product import Product
from schemas.product import ProductDelSchema, ProductSchema, apresenta_product


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


def search_product(form: ProductDelSchema):
    """Busca no BD pelo Produto
    """
    try:
        session = Session()
        product = session.query(Product).filter_by(id = form.id)

        if not product:
            error_msg = "Produto não encontrado na base :/"
            return {"message": error_msg}, 404

        return apresenta_product(product), 200

    except Exception as e:
        error_msg = "Não foi possível consultar o Produto :/"
        return {"message": error_msg}, 400


def change_product(form: ProductSchema):
    """ Edita o Produto na base de dados
    """

    try:
        product_id = form.id
        session = Session()
        product = session.query(Product).filter(
            product.id == product_id)

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
        product_id = form.id
        session = Session()
        product = session.query(Product).filter(
            product.id == product_id)

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
