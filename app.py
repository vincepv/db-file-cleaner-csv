import streamlit as st

from modules.clean_regular_file import clean_regular_file
from modules.athena_clean import athena_clean
from modules.excel_merge_sheet import excel_merge_sheet

st.title("DigitaleBox: nettoyage de fichiers CSV")
st.write(
    "Uploader fichier CSV : encodage utf8, délimiteur virgule. "
)

st.divider()
st.header("Script nettoyage CSV")
st.write ("Le CSV doit contenir les colonnes suivantes : prenom , nom usage, nom naissance  ,date de naissance ,mobile ,email,Adresse,code postal")
clean_regular_file()

st.divider()
st.header("Script fusioner des feuilles Excel en 1 fichier CSV")
excel_merge_sheet()

st.divider()
st.header("Script Athena")
st.write ("Le CSV doit contenir les colonnes suivantes : Prénom, Nom de naissance, Date de naissance,Email, Mobile, Numéro de rue, Nom de rue, Mots clés, Code postal")
athena_clean()