#WPP to create a mobile class and declare the states mobiles as colour,price brand,series,version,features,storage,battery capacity,ram,processor create 10 objects and initialize using constructor print the details of the individual objects using function
class Mobile:
    def __init__(self, color, price, brand, series, version, features, storage, battery_capacity, ram, processor):
        self.color = color
        self.price = price
        self.brand = brand
        self.series = series
        self.version = version
        self.features = features
        self.storage = storage
        self.battery_capacity = battery_capacity
        self.ram = ram
        self.processor = processor

    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Series: {self.series}")
        print(f"Version: {self.version}")
        print(f"Color: {self.color}")
        print(f"Price: ${self.price}")
        print(f"Features: {self.features}")
        print(f"Storage: {self.storage} GB")
        print(f"Battery Capacity: {self.battery_capacity} mAh")
        print(f"RAM: {self.ram} GB")
        print(f"Processor: {self.processor}")
        print("-" * 30)

mobiles = [
    Mobile("Black", 699, "Apple", "iPhone", "14", "5G, Face ID", 128, 3095, 6, "A15 Bionic"),
    Mobile("White", 799, "Samsung", "Galaxy", "S22", "5G, AMOLED", 256, 3700, 8, "Exynos 2200"),
    Mobile("Blue", 499, "OnePlus", "Nord", "2", "5G, AMOLED", 128, 4500, 12, "Dimensity 1200"),
    Mobile("Red", 299, "Xiaomi", "Redmi", "Note 10", "4G, AMOLED", 64, 5000, 4, "Snapdragon 678"),
    Mobile("Green", 899, "Google", "Pixel", "6", "5G, OLED", 128, 4614, 8, "Google Tensor"),
    Mobile("Gray", 399, "Realme", "GT", "Master", "5G, AMOLED", 256, 4500, 8, "Snapdragon 778G"),
    Mobile("Pink", 599, "Vivo", "X", "70", "5G, AMOLED", 256, 4400, 12, "Dimensity 1200"),
    Mobile("Gold", 349, "Nokia", "G", "50", "5G, LCD", 128, 5000, 4, "Snapdragon 480"),
    Mobile("Silver", 799, "Sony", "Xperia", "1", "5G, OLED", 256, 4500, 12, "Snapdragon 888"),
    Mobile("Purple", 499, "Oppo", "Reno", "6", "5G, AMOLED", 128, 4500, 8, "Dimensity 900"),
]
for mobile in mobiles:
    mobile.display_details()
