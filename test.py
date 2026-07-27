from monday_api import get_deals, get_workorders

print("=" * 60)
print("READING DEALS")
print("=" * 60)

deals = get_deals()

print(deals.head())

print()

print("Rows :", len(deals))
print("Columns :", len(deals.columns))

print()

print(deals.columns.tolist())

print("\n")

print("=" * 60)
print("READING WORK ORDERS")
print("=" * 60)

work = get_workorders()

print(work.head())

print()

print("Rows :", len(work))
print("Columns :", len(work.columns))

print()

print(work.columns.tolist())

print("\n")

print("=" * 60)
print("REVENUE TEST")
print("=" * 60)

column = "Amount in Rupees (Incl of GST) (Masked)"

if column in work.columns:

    print()

    print(work[column].head())

    print()

    print("Datatype :", work[column].dtype)

    print()

    print("Total Revenue")

    print(work[column].sum())

else:

    print("Revenue column not found.")