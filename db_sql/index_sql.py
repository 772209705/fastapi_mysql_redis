from models.product_model import ProductModel
from mydbs import db_method as db


from utils.tools import to_update_sql_type_param


# 查询产品列表
def query_product_list():
    query_sql = "SELECT * FROM product"
    return db.query_sql(query_sql)


# 新增产品
def save_new_product_db(product: ProductModel):
    save_sql = """
               INSERT INTO 
                    product (images, title, url, env, sort_key, create_time) 
               VALUES 
                    ('{}','{}','{}','{}','{}','{}')
               """.format(product.images, product.title, product.url, product.env, product.sort_key, product.create_time)

    return db.save_sql(save_sql)


# 更新产品信息
def update_product_db(product: ProductModel):
    data = to_update_sql_type_param(product)

    update_sql = """
                UPDATE product
                SET {}
                WHERE id = {}
    """.format(data, product.id)

    return db.update_sql(update_sql)


def delete_product_db(product_id: int):
    delete_sql = """
            DELETE FROM product
            WHERE id = {}
    """.format(product_id)

    return db.delete_sql(delete_sql)





