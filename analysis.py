import pandas as pd
import numpy as np

customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv")

# eksik yasları ortalama ile doldur
customers["age"] = customers["age"].fillna(customers["age"].mean())

# orders + products birleştir
df = orders.merge(products, on="product_id")

print("\nOrders + Products birleşmiş hali:")
print(df)

# toplam satış hesapla
df["total_sales"] = df["price"] * df["quantity"]

# customers tablosunu da ekle 
df = df.merge(customers, on="customer_id")

print("\nToplam satış eklenmiş tablo:")
print(df)

# kategori bazlı satış
category_sales = df.groupby("category")["total_sales"].sum()

print("\nKategoriye göre toplam satış:")
print(category_sales)

# şehir bazlı satış
city_sales = df.groupby("city")["total_sales"].sum()

print("\nŞehre göre toplam satış:")
print(city_sales)

#yas gruplarınba göre satıs
def age_group(age):
    if age < 30:
        return "Genç"
    else:
        return "Yetişkin"

df["age_group"] = df["age"].apply(age_group)

print("\nYaş kategorileri:")
print(df[["name","age","age_group"]])

#concat 
new_orders = pd.DataFrame({
    "order_id":[7],
    "customer_id":[2],
    "product_id":[103],
    "quantity":[2],
    "date":["2024-02-01"]
})

orders = pd.concat([orders, new_orders])

print("\nYeni sipariş eklendi:")
print(orders)

#en cok kazandıran ürün
best_products = df.groupby("product_name")["total_sales"].sum().sort_values(ascending=False)

print("\nEn çok kazandıran ürünler:")
print(best_products)

#en cok harcama yapan müşteri
best_customers = df.groupby("name")["total_sales"].sum().sort_values(ascending=False)

print("\nEn değerli müşteriler:")
print(best_customers)

#excele yazdırma
df.to_excel("analysis.xlsx")
