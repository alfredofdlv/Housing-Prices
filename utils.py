
def assign_station(month): 
    if month in [12,1,2]: 
        return 'Winter'
    elif month in [3,4,5]:
        return 'Spring'
    elif month in [6,7,8]:
        return 'Summer'
    elif month in [9,10,11]:
        return 'Autumn'
def treat_date_cols(df,dc,nc):
    '''

    Parameters
    -----------------
    df : pandas.DataFrame 
      Dataframe with all the data.

    Returns 
    ----------------

    df_2 : pandas.DataFrame

    '''

    for col in dc: 
        nc.remove(col)
        latest_date=max(df['YearRemodAdd'])
        if col == 'MoSold': 
            # df['Station_Sold']=df[col].apply(assign_station)
            # df['Station_Sold']=df['Station_Sold'].astype('category')
            df[col]=df[col].astype('category')
        if col == 'YearBuilt': 
            df['House_Age']=latest_date-df[col]
            df=df.drop(columns=col)
        if col == 'YearRemodAdd':
            df['Year_Remod']=latest_date-df[col]
            df=df.drop(columns=col)