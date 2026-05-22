database_query = """
CREATE DATABASE IF NOT EXISTS fashion_db
"""

bonker_product_query = """
CREATE TABLE IF NOT EXISTS bonkers_products (
    product_id VARCHAR(255) PRIMARY KEY,
    product_name TEXT,
    product_url TEXT,
    product_price VARCHAR(50),
    product_category VARCHAR(255),
    product_size TEXT,
    image_url LONGTEXT,
    description TEXT
)
"""

only_product_query = """
CREATE TABLE IF NOT EXISTS only_products (
    product_id VARCHAR(255) PRIMARY KEY,
    product_name TEXT,
    product_url TEXT,
    product_price VARCHAR(50),
    product_category VARCHAR(255),
    product_size TEXT,
    image_url LONGTEXT,
    description TEXT
)
"""

lululemon_product_query = """
CREATE TABLE IF NOT EXISTS lululemon_products (
    product_id VARCHAR(255) PRIMARY KEY,
    product_name TEXT,
    product_url TEXT,
    product_price VARCHAR(50),
    product_category VARCHAR(255),
    product_size TEXT,
    image_url LONGTEXT,
    description TEXT
)
"""

bonkers_insert_query = """
INSERT IGNORE INTO bonkers_products(
    product_id,
    product_name,
    product_url,
    product_category,
    product_price,
    product_size,
    image_url,
    description
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

only_insert_query = """
INSERT IGNORE INTO only_products(
    product_id,
    product_name,
    product_url,
    product_category,
    product_price,
    product_size,
    image_url,
    description
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

lululemon_insert_query = """
INSERT IGNORE INTO lululemon_products(
    product_id,
    product_name,
    product_url,
    product_category,
    product_price,
    product_size,
    image_url,
    description
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""