from constant.column_name import PRENOM

def firstname_clean(df):
  if PRENOM not in df.columns:
    df[PRENOM] = 'Inconnu'

  df[PRENOM] = df[PRENOM].str.extract(r'^(\S+)')

  return df