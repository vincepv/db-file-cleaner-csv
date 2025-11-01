from constant.column_name import MOT_CLE


def keyword_bv(df):
    """
    Ajoute, lorsque présent, le contenu de la colonne "BV" dans la colonne
    "Mot clé" en préfixant la valeur par "BV".

    Paramètres:
        df (pd.DataFrame): Le DataFrame auquel ajouter le mot clé BV.

    Retourne:
        pd.DataFrame: Le DataFrame avec la colonne "Mot clé" mise à jour.
    """
    # check keyword col 
    if MOT_CLE not in df.columns:
        df[MOT_CLE] = ''

    df[MOT_CLE] = df[MOT_CLE].fillna("").astype(str).str.strip()

    # Recherche insensible à la casse de la colonne BV.
    bv_column = next(
        (col for col in df.columns if col.strip().lower() == "bv"),
        None,
    )

    if not bv_column:
        return df

    bv_values = (
        df[bv_column]
        .fillna("")
        .astype(str)
        .str.strip()
        .str.replace(r"\.0+$", "", regex=True)
    )
    has_bv_value = bv_values != ""

    if not has_bv_value.any():
        return df

    keywords_to_add = "BV " + bv_values[has_bv_value]
    check_existing_keywords = df.loc[has_bv_value, MOT_CLE].fillna("").astype(str).str.strip()

    # Ajoute le mot clé BV en le séparant avec une virgule si nécessaire.
    keyword_to_keep = check_existing_keywords.where(
        check_existing_keywords == "",
        check_existing_keywords + ",",
    )

    df.loc[has_bv_value, MOT_CLE] = (keyword_to_keep+ keywords_to_add).str.strip(", ").str.strip()

    return df
