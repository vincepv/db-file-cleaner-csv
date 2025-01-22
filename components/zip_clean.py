from constant.column_name import CP



def clean_zip(df):
  if CP not in df:
    df.insert(loc=0, column=CP,value = '')
    return df

  df[CP] = df[CP].astype(str)
  # remove ending .0  with regex
  df[CP] = df[CP].str.replace(r'\.0$', '')
  df[CP] = df[CP].str.replace(' ', '')
  return df
