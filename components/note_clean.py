from constant.column_name import NOTE


def clean_note(df):
  if NOTE not in df.columns:
    df[NOTE] = ''
  
  return df


