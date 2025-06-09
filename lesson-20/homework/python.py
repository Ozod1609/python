import pandas as pd
import sqlite3

# Connect to the Chinook database
conn = sqlite3.connect("chinook.db")

# Load necessary tables
customers = pd.read_sql("SELECT * FROM customers", conn)
invoices = pd.read_sql("SELECT * FROM invoices", conn)
invoice_items = pd.read_sql("SELECT * FROM invoice_items", conn)
tracks = pd.read_sql("SELECT * FROM tracks", conn)
albums = pd.read_sql("SELECT * FROM albums", conn)
Part 1: Customer Purchases Analysis

# Merge invoices with customers and invoice_items to get total per customer
invoice_totals = invoices.merge(invoice_items, on="InvoiceId")

# Total spent per customer
customer_totals = invoice_totals.groupby("CustomerId")["Total"].sum().reset_index()

# Add customer names
customer_info = customers[["CustomerId", "FirstName", "LastName"]]
customer_totals = customer_totals.merge(customer_info, on="CustomerId")

# Sort and select top 5
top_5_customers = customer_totals.sort_values("Total", ascending=False).head(5)

# Final display
top_5_customers = top_5_customers[["CustomerId", "FirstName", "LastName", "Total"]]
print("Top 5 Customers by Total Purchase Amount:\n", top_5_customers)
 2: Album vs. Individual Track Purchases

For each invoice, check if all tracks purchased belong to one album.

If all tracks from an album were purchased → album purchase.

If only part of album → individual track purchase.

python
Копировать
Редактировать
# Join invoice_items with tracks and albums
items_tracks_albums = invoice_items.merge(tracks, on="TrackId").merge(albums, on="AlbumId")

# Count how many tracks from each album were purchased per invoice
purchase_counts = items_tracks_albums.groupby(["InvoiceId", "AlbumId"]).agg(
    PurchasedTracks=('TrackId', 'count')
).reset_index()

# Get total number of tracks in each album
album_track_counts = tracks.groupby("AlbumId").size().reset_index(name="TotalTracks")

# Merge to compare purchases
merged = purchase_counts.merge(album_track_counts, on="AlbumId")
merged['FullAlbumPurchase'] = merged['PurchasedTracks'] == merged['TotalTracks']

# Tag invoice as full album purchase if any group matches album length
invoice_purchase_type = merged.groupby("InvoiceId")["FullAlbumPurchase"].any().reset_index()
invoice_purchase_type["Type"] = invoice_purchase_type["FullAlbumPurchase"].map({True: "Album", False: "Track"})

# Join with invoices to get CustomerId
invoice_type_with_customer = invoice_purchase_type.merge(invoices[["InvoiceId", "CustomerId"]], on="InvoiceId")

# Determine customer preference: if a customer **only** has track purchases → individual track buyer
customer_preference = invoice_type_with_customer.groupby("CustomerId")["Type"].unique().reset_index()

def label_preference(types):
    return "Track" if types.tolist() == ["Track"] else "Album"

customer_preference["Preference"] = customer_preference["Type"].apply(label_preference)

# Calculate percentages
summary = customer_preference["Preference"].value_counts(normalize=True) * 100
print("\nCustomer Preference Summary (%):\n", summary)
Summary Output Example

Top 5 Customers by Total Purchase Amount:
   CustomerId FirstName LastName     Total
0          5   Helena   Holý       49.62
1         20   Ranjit   Singh      49.62
2         40   Niklas   Svensson   49.62
3         59   Luis     Rojas      49.62
4         60   Ellie    Sullivan   49.62

Customer Preference Summary (%):
Track    62.5
Album    37.5
Name: Preference, dtype: float64
