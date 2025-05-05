import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def basic_analysis(df):
    """
    Perform basic statistical analysis and visualizations
    Args:
        df (pd.DataFrame): Cleaned dataframe
    """
    # Set style for plots
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    # 1. Income Group Distribution
    income_dist = df['IncomeGroup'].value_counts()
    plt.figure(figsize=(12, 6))
    income_plot = sns.barplot(x=income_dist.index, y=income_dist.values, palette="viridis")
    plt.title('Distribution of Countries by Income Group', fontsize=14)
    plt.xlabel('Income Group', fontsize=12)
    plt.ylabel('Number of Countries', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('../output/visualizations/income_distribution.png')
    plt.close()
    
    # 2. Region Distribution
    region_dist = df['Region'].value_counts()
    plt.figure(figsize=(14, 6))
    region_plot = sns.barplot(x=region_dist.index, y=region_dist.values, palette="magma")
    plt.title('Distribution of Countries by Region', fontsize=14)
    plt.xlabel('Region', fontsize=12)
    plt.ylabel('Number of Countries', fontsize=12)
    plt.xticks(rotation=75, ha='right')
    plt.tight_layout()
    plt.savefig('../output/visualizations/region_distribution.png')
    plt.close()
    
    # 3. Income Group by Region
    plt.figure(figsize=(14, 8))
    cross_tab = pd.crosstab(df['Region'], df['IncomeGroup'])
    heatmap = sns.heatmap(cross_tab, annot=True, fmt='d', cmap='YlOrBr', linewidths=.5)
    plt.title('Income Group Distribution by Region', fontsize=14)
    plt.xlabel('Income Group', fontsize=12)
    plt.ylabel('Region', fontsize=12)
    plt.tight_layout()
    plt.savefig('../output/visualizations/income_by_region.png')
    plt.close()
    
    return {
        'income_distribution': income_dist.to_dict(),
        'region_distribution': region_dist.to_dict()
    }

if __name__ == "__main__":
    df = pd.read_csv('../output/cleaned_data.csv')
    results = basic_analysis(df)
    print("Basic analysis completed and visualizations saved!")