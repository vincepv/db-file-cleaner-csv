from constant.column_name import CATEGORIE, PRENOM, NOM, PAYS, ADRESSE, CP, VILLE, EMAIL, MOBILE, SEXE, DATE_NAISSANCE, MOT_CLE

def rename_column(df):
    """
    Renomme les colonnes spécifiques d'un DataFrame pandas.

    Paramètres:
    df (pd.DataFrame): Le DataFrame dont les colonnes doivent être renommées.

    Retourne:
    pd.DataFrame: Le DataFrame avec les colonnes renommées.
    """
 

    # Dictionnaire de renommage
    column_to_rename = {
        'Category': CATEGORIE,
        'First Name': PRENOM,
        'first name': PRENOM,
        'firstname': PRENOM,
        'First Name': PRENOM,
        'first name': PRENOM,
        'firstname': PRENOM,
        'prénom': PRENOM,
        'prenom': PRENOM,
        'PRENOM': PRENOM,
        'Prénom': PRENOM,
        'Nom': NOM,
        'nom': NOM,
        'NOM': NOM,
        'Last Name': NOM,
        'last name': NOM,
        'lastname': NOM,
        'Country': PAYS,
        'country': PAYS,
        'Pays': PAYS,
        'pays': PAYS,
        'PAYS': PAYS,
        'Street Address': ADRESSE,
        'adresse': ADRESSE,
        'Adr': ADRESSE,
        'cp': CP,
        'CP': CP,
        'code postal': CP,
        'CODE POSTAL': CP,
        'Zip': CP,
        'City': VILLE,
        'Commune': VILLE,
        'ville': VILLE,
        'Email': EMAIL,
        'email': EMAIL,
        'mail': EMAIL,
        'MAIL': EMAIL,
        'Gender': SEXE,
        'gender': SEXE,
        'SEXE': SEXE,
        'Sexe': SEXE,
        'sexe': SEXE,
        'Date of Birth': DATE_NAISSANCE,
        'DATE DE NAISSANCE': DATE_NAISSANCE,
        'date': DATE_NAISSANCE,
        'Date': DATE_NAISSANCE,
        'Keywords': MOT_CLE,
        'MOBILE': MOBILE,
        'mobile': MOBILE,
        'Phone': MOBILE,
        'phone': MOBILE,
        'telephone': MOBILE,
        'Telephone': MOBILE,
        'tel': MOBILE,
    }

    

    # Renommer les colonnes
    df_renamed_column = df.rename(columns=column_to_rename)

    return df_renamed_column

