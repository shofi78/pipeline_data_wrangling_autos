import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import normalize
from helper.constant import NEW_COLUMN_NAME


def feature_engineering(df):
    # Rename column name format from camelCase to snakecase
      df.rename(columns=NEW_COLUMN_NAME, inplace=True)
    
    # Change to datetime format
    cars_data[["ad_created", "date_crawled", "last_seen"]] = cars_data[["ad_created", "date_crawled", "last_seen"]].apply(pd.to_datetime)
    
    # Change value type of price & odomoter column to integer
    cars_data[['price', 'odometer']] = cars_data[['price', 'odometer']].replace('[^\d]+', '', regex=True).astype('int64')
    
    # Drop some column drop that are inbalace & the information doesn't match
    cars_data.drop(columns=['num_of_pictures'], axis=1, inplace=True)
    cars_data.drop(columns=['name', 'postal_code'], axis=1, inplace=True)
    cars_data.drop(columns=['seller','offer_type'], axis=1, inplace=True)
    
    # Filter data without outlier (in this task, we use range 500 - 40000)
    cars_data = (cars_data.loc[(cars_data['price'] >= 500) & (cars_data['price'] <= 40000)])
    
    # Fill in missing value, if object fill with mode, and if numeric fill with median
     for col in cars_data:
        if cars_data[col].dtypes == 'object':
            cars_data[col] = cars_data[col].fillna(cars_data[col].mode()[0])
        else:
            cars_data[col] = cars_data[col].fillna(cars_data[col].median())
      
    
    ## NORMALIZATION PROCESS (numeric)
    # Make a df copy to do normalization process
    cars_transformed = cars_data.copy()
    cars_transformed  = cars_transformed .reset_index(drop=True)
    
    # Normalize numeric column except price columns
    numeric_cols = cars_transformed .select_dtypes(include='int64')
    data_numeric = numeric_cols.loc[:, numeric_cols.columns != 'price']
    data_normal = pd.DataFrame(normalize(X=data_numeric, norm="l2", axis=1), columns=data_numeric.columns)
    
    # Join the column normalization with others
    cars_transformed.loc[:, ['registration_year', 'power_ps', 'odometer',
               'registration_month']] = data_normal
    
    
    ## ENCODING PROCESS (categorical)
    # LABEL-ENCODING for ordinal column (based on price there are grade between values)
    encode_fuel_type = {'benzin':1,'lpg':2, 'diesel':3, 
                    'cng':4, 'hybrid':5, 'elektro':6, 'andere':7}
    cars_transformed['fuel_type'] = cars_transformed['fuel_type'].map(encode_fuel_type)

    #GET DUMMIES for nominal columns
    cars_transformed = pd.get_dummies(cars_transformed, columns=['abtest','vehicle_type', 
                                                                 'gearbox', 'model','brand','unrepaired_damage'])
    cars_transformed
    
    
    return cars_transformed
    
    
    
    