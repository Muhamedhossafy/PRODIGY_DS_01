import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re

def analyze_notes(df):
    """
    Analyze special notes content in the dataset
    Args:
        df (pd.DataFrame): Cleaned dataframe
    Returns:
        dict: Analysis results
    """
    results = {}
    
    # 1. Word Cloud of Special Notes
    text = ' '.join(note for note in df['SpecialNotes'] if note != 'No notes available')
    wordcloud = WordCloud(width=800, height=400, 
                         background_color='white',
                         stopwords=['country', 'data', 'world', 'bank']).generate(text)
    
    plt.figure(figsize=(15, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Most Common Terms in Country Special Notes', fontsize=14)
    plt.savefig('../output/visualizations/notes_wordcloud.png')
    plt.close()
    
    # 2. Categorize notes
    def categorize_note(note):
        note = note.lower()
        if 'exchange rate' in note or 'conversion factor' in note:
            return 'Exchange Rate'
        elif 'fiscal year' in note or 'calendar year' in note:
            return 'Fiscal Period'
        elif 'currency' in note or 'banknote' in note or 'denomination' in note:
            return 'Currency Change'
        elif 'conflict' in note or 'fragil' in note:
            return 'Conflict/Fragility'
        elif 'population' in note or 'census' in note:
            return 'Population Data'
        elif note == 'no notes available':
            return 'No Notes'
        else:
            return 'Other'
    
    df['NoteCategory'] = df['SpecialNotes'].apply(categorize_note)
    note_categories = df['NoteCategory'].value_counts()
    
    # 3. Plot note categories
    plt.figure(figsize=(12, 6))
    note_plot = sns.barplot(x=note_categories.index, y=note_categories.values, palette="rocket")
    plt.title('Categories of Special Notes', fontsize=14)
    plt.xlabel('Note Category', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('../output/visualizations/note_categories.png')
    plt.close()
    
    # 4. Extract years mentioned in notes
    def extract_years(text):
        return re.findall(r'(19[0-9]{2}|20[0-2][0-9])', text)
    
    df['YearsMentioned'] = df['SpecialNotes'].apply(extract_years)
    year_counts = {}
    for years in df['YearsMentioned']:
        for year in years:
            year_counts[year] = year_counts.get(year, 0) + 1
    
    results['note_categories'] = note_categories.to_dict()
    results['year_mentions'] = year_counts
    
    return results

if __name__ == "__main__":
    df = pd.read_csv('../output/cleaned_data.csv')
    results = analyze_notes(df)
    print("Notes analysis completed!")