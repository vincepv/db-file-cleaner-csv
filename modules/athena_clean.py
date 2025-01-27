import streamlit as st
import pandas as pd

from components.split_file import split_file

def athena_clean():

  uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv", key="athena_clean")

  if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, low_memory=False)

    st.write("Voici un aperçu du fichier chargé :")
    st.dataframe(df.head())
      
      
    if st.button("Nettoyer le fichier"):

      # PREPARE DATA

      # select columns based on column_key, get line where cells are empty
      column_key = [ 'Email', 'Mobile', 'Numéro de rue', 'Nom de rue']
      df_empty_key = df.loc[df[column_key].isnull().all(axis=1)]

      # prepare data for merge
      df = df.dropna(subset=column_key, how='all')

      # MERGE DATA

      # merge df et df_empty_key on ['Prénom', 'Nom de naissance', 'Date de naissance']
      df_merged = pd.merge(df, df_empty_key, on=['Prénom', 'Nom de naissance', 'Date de naissance'], how='left', indicator=True, validate='m:m')

      # fusionne le contenu de Mots clés_y dans Mots clés_x
      df_merged['Mots clés_x'] = df_merged['Mots clés_x'].fillna('') + ',' + df_merged['Mots clés_y'].fillna('')

      # CLEAN COLUMN

      # remove column ending with name _y
      df_merged = df_merged[df_merged.columns.drop(list(df_merged.filter(regex='_y')))]

      # rename column ending with name _x
      df_merged = df_merged.rename(columns=lambda x: x.replace('_x', ''))

      # clean ending .0 in column Mobile and Code postal
      df_merged['Mobile'] = df_merged['Mobile'].astype(str).str.replace('\.0$', '', regex=True)
      df_merged['Mobile'] = df_merged['Mobile'].str.replace('nan', '')
      df_merged['Code postal'] = df_merged['Code postal'].astype(str).str.replace('\.0$', '', regex=True)

      split_file(df_merged)