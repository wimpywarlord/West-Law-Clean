import pandas as pd

def parse_date(date_str):
    # Try parsing with abbreviated month format
    try:
        return pd.to_datetime(date_str, format='%b. %d, %Y')
    except ValueError:
        pass
    
    # Try parsing with full month format
    try:
        return pd.to_datetime(date_str, format='%B %d, %Y')
    except ValueError:
        pass
    
    # If parsing fails, return NaT (Not a Time)
    return pd.NaT

def calculate_date_difference(csv_file_path, date_column1, date_column2, output_csv_file):
    df = pd.read_csv(csv_file_path)

    # Convert date strings to datetime objects using custom parsing function
    df[date_column1] = df[date_column1].apply(parse_date)
    df[date_column2] = df[date_column2].apply(parse_date)

    # Calculate the difference between dates
    df['date_difference'] = (df[date_column2] - df[date_column1]).dt.days

    # Export DataFrame to CSV
    df.to_csv(output_csv_file, index=False)

# Example usage:
csv_file_path = './output.csv'
date_column1 = 'PRIMARY CASE DATE'
date_column2 = 'TREATED CASE DATE'
output_csv_file = 'FinalOutputWithAge.csv'

calculate_date_difference(csv_file_path, date_column1, date_column2, output_csv_file)
