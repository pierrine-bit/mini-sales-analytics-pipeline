def load_data(df, output_path):
    """Write a DataFrame to a CSV file."""
    df.to_csv(output_path, index=False)
