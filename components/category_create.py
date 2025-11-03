from constant.column_name import CATEGORIE

def category_create(df):
    if CATEGORIE not in df.columns:
        df[CATEGORIE] = '2'
    
    return df