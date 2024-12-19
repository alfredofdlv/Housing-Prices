import numpy as np
def assign_station(month): 
    if month in [12,1,2]: 
        return 'Winter'
    elif month in [3,4,5]:
        return 'Spring'
    elif month in [6,7,8]:
        return 'Summer'
    elif month in [9,10,11]:
        return 'Autumn'
def treat_date_cols(df_original,dc,nc,cc):
    '''

    Parameters
    -----------------
    df : pandas.DataFrame 
      Dataframe with all the data.

    Returns 
    ----------------

    df_2 : pandas.DataFrame

    '''
    df=df_original
    #We save the latest date of the dataset for future calculations 
    latest_date=max(df['YearRemodAdd'])

    for col in dc: 
        if col  in nc: 
            nc.remove(col)          # We remove from the numerical columns list each one of the date columns. As we are not going to treat them as numerical.

        else: 
            print(f"Column '{col}' not found in numeric_cols.")
        if col == 'MoSold': 
            df['Station_Sold']=df[col].apply(assign_station)
            df['Station_Sold']=df['Station_Sold'].astype('category')
            cc.append('Station_Sold')
            df[col]=df[col].astype('category')
            cc.append(col)

        if col == 'YearBuilt': 
            # We calculate Anitquity of the House by subsctracting from the latest date possible the date of the house.
            df['House_Age']=latest_date-df[col]
        if col == 'YearRemodAdd':
            # We calculate number of years since last remodelation
            df['Year_Remod']=latest_date-df[col] 
            # We create a categoric feature to see if the House has been remodeled
            df['WasRemod']  =(df['YearBuilt'] != df['YearRemodAdd']).astype(int)
        if col == 'GarageYrBlt' : 
            df['Garage_Age'] = np.where(
                                df[col].isna(),           
                                    -1,                                 
                                    latest_date - df[col]     
                                        )
            df['HasGarage'] = df[col].notnull().astype(int)
        if col =='YrSold' : 
            df[col]=df[col].astype('category')
            cc.append(col)
            # df=df.drop(columns=col)
    print(type(df))
    return df,dc,nc,cc
            