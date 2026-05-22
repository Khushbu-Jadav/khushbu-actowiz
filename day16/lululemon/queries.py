database_query = """
CREATE DATABASE IF NOT EXISTS lululemon_db
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
);
"""

insert_product_query = """
INSERT IGNORE INTO lululemon_products(
  product_id,product_name, product_url,product_price, product_category, product_size, image_url, description
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
