import pandas as pd
import matplotlib.pyplot as plt


csv_df = pd.read_csv('data.csv')          
excel_df = pd.read_excel('data.xlsx')     
json_df = pd.read_json('data.json')        


csv_df.dropna(inplace=True)
excel_df.dropna(inplace=True)
json_df.dropna(inplace=True)


csv_df.reset_index(drop=True, inplace=True)
excel_df.reset_index(drop=True, inplace=True)
json_df.reset_index(drop=True, inplace=True)


merged_df = pd.concat([csv_df, excel_df, json_df], ignore_index=True)


print("Summary Statistics:")
print(merged_df.describe(include='all'))


if 'lotsize' in merged_df.columns and 'tradedlots' in merged_df.columns:
    plt.figure(figsize=(10, 5))
    plt.bar(merged_df.index, merged_df['lotsize'], label='Lotsize')
    plt.bar(merged_df.index, merged_df['tradedlots'], label='Traded Lots', alpha=0.7)
    plt.title('Lotsize vs Traded Lots')
    plt.xlabel('Row Index')
    plt.ylabel('Values')
    plt.legend()
    plt.tight_layout()
    plt.show()
else:
    print("Columns 'lotsize' and 'tradedlots' not found for plotting.")
