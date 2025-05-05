import pandas as pd

def load_and_clean_data(filepath):
    """
    Load and preprocess the country metadata CSV file
    Args:
        filepath (str): Path to the CSV file
    Returns:
        pd.DataFrame: Cleaned dataframe
    """
    # Load the data with proper encoding
    df = pd.read_csv(filepath, encoding='utf-8-sig')
    
    # Clean column names
    df.columns = df.columns.str.strip()
    
    # Handle missing values
    df['Region'] = df['Region'].fillna('Global')
    df['IncomeGroup'] = df['IncomeGroup'].fillna('Not Specified')
    df['SpecialNotes'] = df['SpecialNotes'].fillna('No notes available')
    
    # Clean text data
    df['SpecialNotes'] = df['SpecialNotes'].str.replace('\n', ' ')
    df['SpecialNotes'] = df['SpecialNotes'].str.strip()
    
    # Filter out regional aggregates (optional)
    df = df[~df['Country Code'].isin(['ARB', 'CEB', 'CSS', 'EMU', 'EUU', 'HIC', 'HPC', 'IBD', 'IBT', 'IDA', 'IDB', 'IDX', 'LAC', 'LCN', 'LDC', 'LIC', 'LMC', 'LMY', 'LTE', 'MEA', 'MIC', 'MNA', 'NAC', 'OED', 'OSS', 'PRE', 'PSS', 'PST', 'SAS', 'SSA', 'SSF', 'SST', 'TEA', 'TEC', 'TLA', 'TMN', 'TSA', 'TSS', 'UMC', 'WLD'])]
    
    return df

if __name__ == "__main__":
    # Example usage
    df = load_and_clean_data('../data/Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_19373.csv')
    df.to_csv('../output/cleaned_data.csv', index=False)
    print("Data cleaned and saved successfully!")