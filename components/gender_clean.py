from constant.column_name import SEXE

def gender_clean(df):
  if SEXE not in df.columns:
    df[SEXE] = '0'


  df[SEXE] = df[SEXE].astype(str)

  dic_female = {
    'Femme': '1',
    'femme': '1',
    'F': '1',
    'f': '1',
  }

  dic_male = {
    'Monsieur': '2',
    'M': '2',
    'm': '2',
    'Homme': '2',
    'homme': '2',
    'H': '2',
  }

  df[SEXE] = df[SEXE].replace(dic_female, regex=True)
  df[SEXE] = df[SEXE].replace(dic_male, regex=True)
  return df
  