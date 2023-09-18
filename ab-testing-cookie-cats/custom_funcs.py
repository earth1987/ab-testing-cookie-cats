"""Custom code that gets used across more than notebook"""
import pandas as pd

def summarise_data(df, column):
    """Outputs the value count for a given column in a dataframe."""
    summary = pd.DataFrame(
        dict(count=df[column].value_counts(),
             perc=round(df[column].value_counts(normalize=True)*100,1)
            )
    )
    summary.loc['All'] = [df[column].value_counts().sum(), 
                          df[column].value_counts(normalize=True).sum()*100]

    return summary