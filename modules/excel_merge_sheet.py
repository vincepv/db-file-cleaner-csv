import streamlit as st

from components.excel_merge_sheet import merge_excel_sheet


def excel_merge_sheet():
    uploaded_file = st.file_uploader(
        "Choisissez un fichier Excel", type=["xls", "xlsx"], key="excel_merge_sheet"
    )

    if uploaded_file is None:
        return

    try:
        merged_df = merge_excel_sheet(uploaded_file)
    except Exception as error:
        st.error(f"Impossible de fusionner les feuilles de calcul : {error}")
        return

    if merged_df.empty:
        st.warning("Le classeur ne contient aucune donnée exploitable.")
        return

    st.write("Aperçu du fichier fusionné :")
    st.dataframe(merged_df.head())

    csv_content = merged_df.to_csv(index=False)

    st.download_button(
        label="Télécharger le CSV fusionné",
        data=csv_content,
        file_name="fichier_fusionne.csv",
        mime="text/csv",
    )
