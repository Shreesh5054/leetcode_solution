import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
 pr=(products["low_fats"]=="Y")&(products["recyclable"]=="Y")    
 return products.loc[pr,["product_id"]]