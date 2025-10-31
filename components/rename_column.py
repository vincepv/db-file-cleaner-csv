from constant.column_name import CATEGORIE, PRENOM, NOM, NOM_NAISSANCE,PAYS, ADRESSE, CP, VILLE, EMAIL, MOBILE, SEXE, DATE_NAISSANCE, MOT_CLE

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
        'category': CATEGORIE,
        'catégorie': CATEGORIE,
        'Categorie': CATEGORIE,
        'Catégorie': CATEGORIE,
        'Category': CATEGORIE,
        
        'First Name': PRENOM,
        'first name': PRENOM,
        'firstname': PRENOM,
        'First Name': PRENOM,
        'first name': PRENOM,
        'firstname': PRENOM,
        'prénoms': PRENOM,
        'Prénoms': PRENOM,
        'PRENOMS': PRENOM,
        'prénom': PRENOM,
        'prenom': PRENOM,
        'PRENOM': PRENOM,
        'Prénom': PRENOM,

        
        'Nom Usage': NOM,
        'nom usage': NOM,
        'NOM USAGE': NOM,
        'Last Name': NOM,
        'last name': NOM,
        'lastname': NOM,

        'nom de naissance': NOM_NAISSANCE,
        'Nom de naissance': NOM_NAISSANCE,
        'NOM DE NAISSANCE': NOM_NAISSANCE,
        'nom naissance': NOM_NAISSANCE,
        'Nom Naissance': NOM_NAISSANCE,
        'NOM NAISSANCE': NOM_NAISSANCE,
        'Birth Name': NOM_NAISSANCE,
        'birth name': NOM_NAISSANCE,
        'Birthname': NOM_NAISSANCE,
        'birthname': NOM_NAISSANCE,

        
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
        'Country': PAYS,
        'country': PAYS,
        'Pays': PAYS,
        'pays': PAYS,
        'PAYS': PAYS,
        
        'Email': EMAIL,
        'email': EMAIL,
        'mail': EMAIL,
        'MAIL': EMAIL,
        
        'civilité': SEXE,
        'Civilité': SEXE,
        'CIVILITÉ': SEXE,
        'CIVILITE': SEXE,
        'civilite': SEXE,
        'genre': SEXE,
        'Genre': SEXE,
        'Gender': SEXE,
        'gender': SEXE,
        'SEXE': SEXE,
        'Sexe': SEXE,
        'sexe': SEXE,
        
        'Date of Birth': DATE_NAISSANCE,
        'Date de naissance': DATE_NAISSANCE,
        'date de naissance': DATE_NAISSANCE,
        'DATE DE NAISSANCE': DATE_NAISSANCE,
        'date': DATE_NAISSANCE,
        'Date': DATE_NAISSANCE,
        'Date naissance': DATE_NAISSANCE,
        'Date Naissance': DATE_NAISSANCE,
        'DATE NAISSANCE': DATE_NAISSANCE,
        
        'Keywords': MOT_CLE,
        'keywords': MOT_CLE,
        'Mots clés': MOT_CLE,
        'mots clés': MOT_CLE,
        'Mots cles': MOT_CLE,
        'mots cles': MOT_CLE,
        'MOT CLE': MOT_CLE,
        'mot cle': MOT_CLE,
        'Mot clé': MOT_CLE,
        'mot clé': MOT_CLE,
        
        
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

