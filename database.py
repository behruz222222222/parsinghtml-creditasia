import psycopg2

def insert_category(category_name, category_link):
    with psycopg2.connect(
        database="asia_db",
        port=5432,
        user="postgres",
        host="localhost",
        password=123456
    ) as database:
        cursor = database.cursor()

        cursor.execute("""
        INSERT INTO category(category_title, category_link)
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING;
        """, (category_name, category_link))

        database.commit()


def insert_product(category_id, title, link, price, image, description):
    with psycopg2.connect(
            database="asia_db",
            port=5432,
            user="postgres",
            host="localhost",
            password=123456
    ) as database:
        cursor = database.cursor()
        cursor.execute("""
        INSERT INTO product(category_id, product_title, product_link, product_price,
                            product_image, product_description)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (category_id, title, link, price, image, description))

        database.commit()


def get_category_id(category_title):
    with psycopg2.connect(
            database="asia_db",
            port=5432,
            user="postgres",
            host="localhost",
            password=123456
    ) as database:
        cursor = database.cursor()

        cursor.execute("""
        SELECT category_id FROM category WHERE category_title = (%s)
        """, (category_title, ))

        category_id = cursor.fetchone()[0]

        return category_id

def insert_characteristics(product_id, characteristics: dict):
    with psycopg2.connect(
            database="asia_db",
            port=5432,
            user="postgres",
            host="localhost",
            password=123456
    ) as database:
        cursor = database.cursor()

        for key, value in characteristics.items():
            cursor.execute(f"""
                INSERT INTO characteristic(product_id,
                                           characteristic_title,
                                           characteristic_info)
                VALUES (%s, %s, %s);
            """, (product_id, key, value))
            database.commit()


def get_product_id(product_title):
    with psycopg2.connect(
            database="asia_db",
            port=5432,
            user="postgres",
            host="localhost",
            password=123456
    ) as database:
        cursor = database.cursor()

        cursor.execute("""
        SELECT product_id FROM product WHERE product_title = (%s);
        """, (product_title, ))

        product_id = cursor.fetchone()[0]

        return product_id

