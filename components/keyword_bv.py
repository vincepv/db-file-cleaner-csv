import streamlit as st
import pandas as pd

from constant.column_name import MOT_CLE


def keyword_bv(df):    
  """
    Ajoute une colonne 'Mots clés' avec la valeur du BV à chaque ligne du DataFrame.

    Paramètres:
    df (pd.DataFrame): Le DataFrame auquel ajouter la colonne.

    Retourne:
    pd.DataFrame: Le DataFrame avec la nouvelle colonne 'Mots clés'.
    """
  if MOT_CLE not in df.columns:
    df[MOT_CLE] = ''
    
  
  df[MOT_CLE] = df[MOT_CLE].fillna("").astype(str).str.strip()

  # il faut regarder la colonne df['BV] 
  # si elle existe, on prend la valeur 
  # on ajoute la valeur : 'BV ' + valeur de la colonne BV
  # on assinge à la colonne MOT_CLE
  if "BV" in df.columns:
    df["BV"] = df["BV"].fillna("").astype(str).str.strip()

    df[MOT_CLE] = df.apply(
      lambda row: 
        f"BV {row['BV']}".strip() 
        if row['BV'] != "" 
        else row[MOT_CLE], 
      axis=1)


  return df