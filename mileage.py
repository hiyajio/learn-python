print("How many kilometers did you run today?")
kms = float(input())
miles = round(kms/1.60934, 2)
print(f"Ok, your {kms} km run is equal to {miles} mi!")