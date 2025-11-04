from extract import extract_from_s3
from transform import clean_sales_data
from load import load_to_postgres

def main():
    print("🚀 Starting ETL process...")
    df = extract_from_s3()
    if df.empty:
        print("⚠️ No data found in S3. Exiting ETL.")
        return
    transformed_df = clean_sales_data(df)
    load_to_postgres(transformed_df)
    print("🎯 ETL completed successfully!")

if __name__ == "__main__":
    main()
