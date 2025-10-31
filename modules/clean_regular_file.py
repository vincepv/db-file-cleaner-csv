import streamlit as st
import pandas as pd

from components.rename_column import rename_column
from components.mobile_clean import mobile_clean
from components.clean_character import clean_character
from components.category_create import category_create
from components.clean_country import clean_country
from components.split_file import split_file
from components.address_clean import address_clean
from components.date_clean import date_clean
from components.firstname_clean import firstname_clean
from components.email_clean import email_clean
from components.zip_clean import clean_zip
from components.gender_clean import gender_clean
from components.clean_country import clean_country
from components.keyword_bv import keyword_bv

def clean_regular_file():
  uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv", key="clean_regular_file")



  if uploaded_file is not None:
      # guard close
      try :
        df = pd.read_csv(uploaded_file)
      except Exception as e:
        st.error(f"Utilisez un CSV séparateur , format: utf8 {e}")
        return
      
      if df.empty:
        st.error("Le fichier est vide. Veuillez télécharger un fichier CSV valide.")
        return
      
      # preview of the file
      st.write("Voici un aperçu du fichier chargé :")
      st.dataframe(df.head())
      

      # Main business logic
      
      if st.button("Nettoyer le fichier"):

          # cleaning logic
          df = clean_character(df)
          df = rename_column(df)

          # business logic
          df = firstname_clean(df)
          df = date_clean(df)
          df = gender_clean(df)
          
          df = address_clean(df)
          df = clean_country(df)
          df = clean_country(df)
          
          df = mobile_clean(df)
          df = email_clean(df)
          
          df = category_create(df)
          df = clean_zip(df)

          df = keyword_bv(df)

          # preview of the cleaned file
          # for dev only
          st.dataframe(df.head())

          # add keywords : add LE2024, BV 1

          split_file(df)
        
      