import pandas as pd

# Manually parsed listings data
listings_data = [
    {"Address": "5358 Carolina Hwy, Denmark, SC 29042", "Price": 220000, "Beds": 7, "Baths": 9, "Sqft": 4187},
    {"Address": "302 West Rd, Greer, SC 29650", "Price": 213000, "Beds": 3, "Baths": 2, "Sqft": 1484},
    {"Address": "4293 Brandy Creek Ct #91, Clover, SC 29710", "Price": 199900, "Beds": 4, "Baths": 4, "Sqft": 3272},
    {"Address": "121 Spring Water Dr, Lexington, SC 29073", "Price": 209900, "Beds": 3, "Baths": 3, "Sqft": 1936},
    {"Address": "7 Stone Meadow Rd, Greenville, SC 29615", "Price": 215000, "Beds": 2, "Baths": 2, "Sqft": 1457},
    {"Address": "600 Norfolk St, Florence, SC 29506", "Price": 190000, "Beds": 3, "Baths": 2, "Sqft": 1409},
    {"Address": "587 Pine St, Warrenville, SC 29851", "Price": 240000, "Beds": 3, "Baths": 2, "Sqft": 1551},
    {"Address": "217 Pleasant Dr, Greer, SC 29651", "Price": 225000, "Beds": 3, "Baths": 2, "Sqft": 1266},
    {"Address": "718 Kingsbridge Rd, Columbia, SC 29210", "Price": 249000, "Beds": 4, "Baths": 3, "Sqft": 2424},
    {"Address": "204 Forest Ave, Anderson, SC 29625", "Price": 173000, "Beds": 3, "Baths": 3, "Sqft": 2017},
    {"Address": "1114 Lakeview Blvd, Hartsville, SC 29550", "Price": 215000, "Beds": 3, "Baths": 2, "Sqft": 1600},
    {"Address": "2983 Highway 418, Fountain Inn, SC 29644", "Price": 114900, "Beds": 3, "Baths": 3, "Sqft": 1750},
    {"Address": "476 Live Oak Church Rd., Loris, SC 29569", "Price": 235000, "Beds": 3, "Baths": 2, "Sqft": 1438},
    {"Address": "2410 High St, Columbia, SC 29203", "Price": 129000, "Beds": 3, "Baths": 1, "Sqft": 1302},
    {"Address": "190 Boys Home Rd, Pauline, SC 29374", "Price": 239900, "Beds": 4, "Baths": 3, "Sqft": 2459},
    {"Address": "160 Fairway Grn, Anderson, SC 29621", "Price": 179900, "Beds": 4, "Baths": 2, "Sqft": 1935},
    {"Address": "37 Vanderbilt Dr, Aiken, SC 29803", "Price": 235000, "Beds": 3, "Baths": 2, "Sqft": 1550},
    {"Address": "1368 E Old Marion Hwy, Florence, SC 29506", "Price": 199500, "Beds": 3, "Baths": 2, "Sqft": 1619},
    {"Address": "425 Brantley Dr, Hartsville, SC 29550", "Price": 240000, "Beds": 3, "Baths": 2, "Sqft": 2061},
    {"Address": "613 Cantey Pkwy, Camden, SC 29020", "Price": 185000, "Beds": 3, "Baths": 2, "Sqft": 1320},
    {"Address": "505 Forestbrook Dr., Myrtle Beach, SC 29579", "Price": 239500, "Beds": 4, "Baths": 2, "Sqft": 1569},
    {"Address": "102 Huntingridge Pl, Summerville, SC 29486", "Price": 185000, "Beds": 4, "Baths": 3, "Sqft": 1834},
    {"Address": "76 Proud Hope Ln, Due West, SC 29639", "Price": 75000, "Beds": 2, "Baths": 2, "Sqft": 1534},
    {"Address": "205 Woodlands W, Columbia, SC 29229", "Price": 225000, "Beds": 3, "Baths": 3, "Sqft": 2007},
    {"Address": "2730 Cultra Rd., Conway, SC 29526", "Price": 147900, "Beds": 2, "Baths": 1, "Sqft": 2548},
    {"Address": "924 Bridge St, Saint Matthews, SC 29135", "Price": 95000, "Beds": 3, "Baths": 2, "Sqft": 1615},
    {"Address": "300 E Myles Ln, Spartanburg, SC 29303", "Price": 220000, "Beds": 3, "Baths": 2, "Sqft": 1251},
    {"Address": "1600 Bolt Dr, Anderson, SC 29621", "Price": 225000, "Beds": 3, "Baths": 2, "Sqft": 1500},
    {"Address": "117 Dover Rd, Spartanburg, SC 29301", "Price": 250000, "Beds": 3, "Baths": 3, "Sqft": 2010},
    {"Address": "117 Whitehurst Way, Columbia, SC 29229", "Price": 185000, "Beds": 3, "Baths": 2, "Sqft": 1623},
    {"Address": "2109 Apple Valley Rd, Columbia, SC 29210", "Price": 195000, "Beds": 4, "Baths": 2, "Sqft": 1734},
    {"Address": "2816 Pisgah Rd, Florence, SC 29501", "Price": 225000, "Beds": 2, "Baths": 2, "Sqft": 1520},
    {"Address": "206 Gibert St, Union, SC 29379", "Price": 250000, "Beds": 4, "Baths": 3, "Sqft": 3583},
    {"Address": "93 Orchard Dr, Inman, SC 29349", "Price": 239900, "Beds": 3, "Baths": 2, "Sqft": 1835},
    {"Address": "1419 Hobart Dr, Florence, SC 29501", "Price": 235000, "Beds": 3, "Baths": 2, "Sqft": 1704},
    {"Address": "27031 Pocotaligo Rd, Yemassee, SC 29945", "Price": 240000, "Beds": 3, "Baths": 2, "Sqft": 1962},
    {"Address": "3205 W Bobo Newsom Hwy, Hartsville, SC 29550", "Price": 209900, "Beds": 3, "Baths": 2, "Sqft": 1580},
    {"Address": "117 Wrightson Ave, Spartanburg, SC 29306", "Price": 210000, "Beds": 3, "Baths": 2, "Sqft": 1646},
    {"Address": "8261 Truman Ave, Aiken, SC 29803", "Price": 185000, "Beds": 3, "Baths": 2, "Sqft": 1545},
    {"Address": "131 Whixley Ln, Columbia, SC 29223", "Price": 209900, "Beds": 3, "Baths": 2, "Sqft": 1266},
    {"Address": "320 Woodview Ave, Spartanburg, SC 29306", "Price": 150000, "Beds": 4, "Baths": 3, "Sqft": 2300},
]

# Creating DataFrame
df = pd.DataFrame(listings_data)

# Display the DataFrame
print(df)
