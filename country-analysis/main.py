import pandas as pd
import json
import os
import sys
from pathlib import Path
import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="seaborn")

# Adding a project path to a Python system
project_path = Path(__file__).parent.parent
sys.path.append(str(project_path))

# Import modules 
from scripts.data_loading import load_and_clean_data
from scripts.basic_analysis import basic_analysis
from scripts.notes_analysis import analyze_notes
from scripts.advanced_analysis import advanced_analysis


def main():
    # Specify the file path 
    current_dir = Path(__file__).parent
    data_path = current_dir / 'data' / 'Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_19373.csv'
    

    # Verify the file exists
    if not data_path.exists():
        raise FileNotFoundError(f"Data file not found at: {data_path}")
    
    print(f"Loading data from: {data_path}")
    df = load_and_clean_data(str(data_path))
    
    # Step 2: Fundamental Analysis
    print("\nStep 2: Performing basic analysis...")
    basic_results = basic_analysis(df)

    # Step 3: Analyze the notes
    print("\nStep 3: Analyzing special notes...")
    notes_results = analyze_notes(df)
    
    # Step 4: Advanced Analysis
    print("\nStep 4: Performing advanced analysis...")
    advanced_results = advanced_analysis(df)
    
    # Save results
    final_results = {
        'basic_analysis': basic_results,
        'notes_analysis': notes_results,
        'advanced_analysis': advanced_results
    }
    
    results_path = os.path.join(project_path, 'output', 'reports', 'final_results.json')
    with open(results_path, 'w') as f:
        json.dump(final_results, f, indent=4)
    
    print("\nAll analyses completed successfully!")
    print(f"Total countries analyzed: {len(df)}")
    print(f"Visualizations saved to: {os.path.join(project_path, 'output', 'visualizations')}")
    print(f"Reports saved to: {os.path.join(project_path, 'output', 'reports')}")

if __name__ == "__main__":
    main()