import pandas as pd

def clean_general_movie_df(df):
    """
    Cleans movie_general_df through multiple actions:
        1. Removes duplicates if available
        2. Drops NaN if available on these columns: 'original_title', 'runtime_minutes', 'genres'
 
    Args:
        Value: movie_general_df

    Returns:
        Cleaned movie_general_df dataframe 
    """
    # Check for duplicates
    has_duplicates = df.duplicated().any()

    if has_duplicates:
        # Drop duplicates
        df = df.drop_duplicates()
        print("Duplicates detected and dropped.")
    else:
        print("No duplicates found.")

    # Rest of your cleaning logic
    df = df.dropna(subset=['original_title', 'runtime_minutes', 'genres'])

    return df
    

def clean_imdb_df(df):
    """
    Cleans IMDB dataset through multiple actions:
        1. Removes duplicates if available
        2. Drops NaN if available on these columns: 'averagerating', 'numvotes', 'primary_title'
        3. Filter out any 'numvotes' =< 500
        4. Removes every person that is dead so death_year is different than NaN
        5. Dropping column 'category' 

    Args:
        Value: All the IMDB defined dataframes

    Returns:
        Cleaned IMDB dataframes with movies having at least 500 votes and only alive actors, actresses, directors or writers.
    """
    # Check for duplicates
    has_duplicates = df.duplicated().any()

    if has_duplicates:
        # Drop duplicates
        df = df.drop_duplicates()
        print("Duplicates detected and dropped.")
    else:
        print("No duplicates found.")

    # Rest of your cleaning logic
    df = df.dropna(subset=['averagerating', 'numvotes', 'primary_title', 'genres'])
    df = df[df['numvotes'] >= 500]

    #Filter out rows where death_year is non NaN (to keep alive people)
    df = df[df['death_year'].isna()]

    return df





def convert_obj_to_int(value):
    """
    Converts a string with dollar signs and commas to an integer.

    Args:
        Value: The string value to convert.

    Returns:
        The integer value (or NaN if conversion fails).
    """
    value = str(value)  # Confirm value is a string in case we have NaN
    value = value.replace('$', '').replace(',', '')  # Remove comma after second replace
    try:
        return pd.to_numeric(value, errors='coerce', dtype='int64') #Convert value to int, coerce used to add NaN if conversion fails
    except:
        return pd.to_numeric(value, errors='coerce') 





def clean_tn_movies_df(df):
    """
    Cleans The Number dataset through multiple actions:
        1. Removes NaN lines based on the columns 'production_budget', 'domestic_gross', 'worldwide_gross'
        2. Converts the values in columns 'production_budget', 'domestic_gross', 'worldwide_gross' into integers.
        3. Converts the column release_date into datetime.

    Args:
        Value: The Number dataframe

    Returns:
        Cleaned The Number dataframe with the columns in the correct data type
    """

    df = df.dropna(subset=['production_budget','domestic_gross','worldwide_gross'])
    df['production_budget'] = df['production_budget'].apply(convert_obj_to_int)
    df['domestic_gross'] = df['domestic_gross'].apply(convert_obj_to_int)
    df['worldwide_gross'] = df['worldwide_gross'].apply(convert_obj_to_int)
    df['release_date'] = pd.to_datetime(df['release_date'])
    return df




def extract_main_genre(df, column_name, new_column):
    """
    Extracts the first word from the 'genre' column in a DataFrame and create a new column 'main_genre'
    Replace the values the new column 'main'genre' from 'Music' to 'Musical' that per investigation is the same genre.

    Args:
        df: The DataFrame to process.
        column_name: The name of the column containing the strings.
        new_column: Name for the new column where i will be adding the value extracted

    Returns:
        The DataFrame with a new column containing the first words.
    """

    # Create a new column to store the first word from column_name
    df[new_column] = df[column_name].str.split(',', expand=False).str[0].str.strip()
    df[new_column] = df[new_column].str.replace('Music', 'Musical')
    df[new_column] = df[new_column].str.replace('Musicalal', 'Musical')

    return df


def compare_columns_within_dataframes(df1, df2, df3, df4, column1, column2):
  """
  Compares two specified columns within each of four DataFrames and prints the results.

  Args:
    df1, df2, df3, df4: The four DataFrames to compare.
    column1: The name of the first column to compare.
    column2: The name of the second column to compare.
  """

  dataframes = [df1, df2, df3, df4]

  for i, df in enumerate(dataframes):
    if df[column1].equals(df[column2]):
      print(f"DataFrame {i+1} has the same values in columns '{column1}' and '{column2}'.")
    else:
      print(f"DataFrame {i+1} has different values in columns '{column1}' and '{column2}'.")


def clean_columns(df, columns_to_remove, column_name_mapping):
    """
    Cleans a DataFrame by removing unnecessary columns and changing the name of other columns.

    Args:
        df: The DataFrame to clean.
        columns_to_remove: A list of column names to remove.
    
    Returns:
        The cleaned DataFrame.
    """
    df = df.drop(columns_to_remove, axis=1)
    df = df.rename(columns=column_name_mapping)

    return df

def create_roi_columns(df):
    """
    Create two new columns for the domestic and worldwide ROI

    Args:
        df: The DataFrame to process.

    Returns:
        The DataFrame with a new column containing the first words.
    """

    # Create a new columns with domestic and worldwide ROI
    df['domestic_roi'] = (df['domestic_gross'] - df['production_budget'])/df['production_budget']
    df['international_roi']= (df['worldwide_gross'] - df['production_budget'])/df['production_budget']

    return df

def final_clean_columns(df):
    """
    Final DataFrame clean up by removing unnecessary columns.

    Args:
        df: The DataFrame to clean.
    
    Returns:
        The cleaned DataFrame.
    """
    df = df.drop(['production_budget', 'domestic_gross', 'worldwide_gross'], axis=1)

    return df

def clean_studio_column(df):
    df['studio']  = df['studio'].str.replace(' ', '').str.replace('.', '')
    df['studio'] = df['studio'].str.replace('WB(NL)', 'WB')
    df['studio'] = df['studio'].str.replace('FoxS', 'Fox')
    df['studio'] = df['studio'].str.replace('Blue Fox', 'Fox')
    df['studio'] = df['studio'].str.replace('LG/S', 'LGF')
    return df

def filter_df_by_values(df, column_name, values_to_drop):
  """
  Filters a DataFrame to exclude rows where a specified column contains any of the given values.

  Args:
    df: The DataFrame to filter.
    column_name: The name of the column to check.
    values_to_drop: A list of values to exclude.

  Returns:
    A new DataFrame containing the rows that do not match any of the values in `values_to_drop`.
  """

  # Create a boolean mask for rows to keep
  mask = ~df[column_name].isin(values_to_drop)

  # Filter the DataFrame using boolean indexing
  filtered_df = df[mask]

  return filtered_df

def filter_df_by_slection(df, column_to_filter, values):
    """Filters a DataFrame by the values input.

    Args:
        df: The DataFrame to filter.
        column_to_filter: column to use to filter
        values: A list of values to filter by

    Returns:
        A Series containing the value counts of the main genre for the filtered DataFrame.
    """

    df_filtered = df[df[column_to_filter].isin(values)]
    return df_filtered['main_genre'].value_counts()