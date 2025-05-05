import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def advanced_analysis(df):
    """
    Perform advanced analysis on the country data
    Args:
        df (pd.DataFrame): Cleaned dataframe with note categories
    Returns:
        dict: Advanced analysis results
    """
    results = {}
    
    # 1. Countries with dual/multiple exchange rates
    dual_exchange = df[df['SpecialNotes'].str.contains('multiple or dual exchange rate', case=False)]
    dual_exchange = dual_exchange[['Country Code', 'TableName', 'Region', 'IncomeGroup']]
    dual_exchange.to_csv('../output/reports/dual_exchange_countries.csv', index=False)
    
    # 2. Fiscal year countries
    fiscal_year = df[df['NoteCategory'] == 'Fiscal Period']
    fiscal_year = fiscal_year[['Country Code', 'TableName', 'Region', 'IncomeGroup']]
    fiscal_year.to_csv('../output/reports/fiscal_year_countries.csv', index=False)
    
    # 3. Currency change countries
    currency_change = df[df['NoteCategory'] == 'Currency Change']
    currency_change = currency_change[['Country Code', 'TableName', 'Region', 'IncomeGroup']]
    currency_change.to_csv('../output/reports/currency_change_countries.csv', index=False)
    
    # 4. Analysis by region and income group
    analysis_by_region = df.groupby(['Region', 'IncomeGroup']).size().unstack()
    analysis_by_region.to_csv('../output/reports/region_income_analysis.csv')
    
    # 5. Special notes length analysis
    df['NoteLength'] = df['SpecialNotes'].apply(lambda x: len(str(x)))
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='IncomeGroup', y='NoteLength', data=df, palette="Set3")
    plt.title('Special Notes Length by Income Group', fontsize=14)
    plt.xlabel('Income Group', fontsize=12)
    plt.ylabel('Note Length (characters)', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('../output/visualizations/note_length_by_income.png')
    plt.close()
    
    results['dual_exchange_count'] = len(dual_exchange)
    results['fiscal_year_count'] = len(fiscal_year)
    results['currency_change_count'] = len(currency_change)
    
    return results

if __name__ == "__main__":
    df = pd.read_csv('../output/cleaned_data.csv')
    results = advanced_analysis(df)
    print("Advanced analysis completed and reports generated!")