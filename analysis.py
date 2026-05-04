import pandas as pd

df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Revenue"] = df["Price"] * df["Quantity"]

print("="*50)
print("PEHLE 5 ROWS")
print("="*50)
print(df.head())

print("\n--- SALES INSIGHTS ---")
print(f"Total Revenue       : Rs.{df['Revenue'].sum():,.0f}")
print(f"Average Order Value : Rs.{df['Revenue'].mean():,.0f}")
print(f"Total Orders        : {df['OrderID'].count()}")

print("\n--- TOP 5 PRODUCTS (Quantity) ---")
print(df.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head())

print("\n--- MOST REVENUE PRODUCT ---")
print(df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(1))

print("\n--- REVENUE PER CITY ---")
city_rev = df.groupby("City")["Revenue"].sum().sort_values(ascending=False)
print(city_rev)
print(f"Best City: {city_rev.idxmax()}")

print("\n--- SALES PER DAY ---")
day_sales = df.groupby("Date")["Revenue"].sum()
print(day_sales)
print(f"Best Day: {day_sales.idxmax().date()}")

print("\n--- REVENUE BY CATEGORY ---")
print(df.groupby("Category")["Revenue"].sum())

print("\n--- QUANTITY BY CATEGORY ---")
print(df.groupby("Category")["Quantity"].sum())

print("\n--- PRICE > 10000 ---")
print(df[df["Price"] > 10000][["OrderID","Product","Price","City"]])

print("\n--- PATNA ORDERS ---")
print(df[df["City"] == "Patna"][["OrderID","Product","Revenue"]])

print("\n--- ELECTRONICS ORDERS ---")
print(df[df["Category"] == "Electronics"][["OrderID","Product","Price"]])

print("\n--- TOP 5 REVENUE ORDERS ---")
print(df.sort_values("Revenue", ascending=False).head(5)[["OrderID","Product","Revenue"]])

print("\nDone!")