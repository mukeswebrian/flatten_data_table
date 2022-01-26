import pandas as pd
import json

def flatten(df, col_dim, row_dim, value_dim):
    entries = []
    for col in df.columns:
        print(f'parsing column {col} ...')
        for row in df.index:
            entry = {
                col_dim: col,
                row_dim: row,
                value_dim: df[col].loc[row]
            }
            entries.append(entry)

    return pd.DataFrame(entries)

if __name__=='__main__':
    config = json.load(open('flatten_config.json', 'r'))
    df = pd.read_excel(config['file_name'], index_col=0)

    df_flat = flatten(df=df,  
                      col_dim=config['column_dimension'],
                      row_dim=config['row_dimension'],   
                      value_dim=config['value_dimension']
              )

    output_name = config['file_name'].split('.')[0] + '_flat.xlsx'

    df_flat.to_excel(output_name)
