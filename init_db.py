import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

# Plants table
cur.execute("""
CREATE TABLE IF NOT EXISTS plants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    name TEXT,
    price INTEGER,
    image TEXT,
    description TEXT
)
""")

# USERS TABLE
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

# BOOKINGS TABLE (with date + time)
cur.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plant_name TEXT,
    user_name TEXT,
    phone TEXT,
    address TEXT,
    quantity INTEGER,
    total_price INTEGER,
    date TEXT,
    time TEXT
)
""")

# Sample plants
plants = [
    ("fruit",
 "Mango",
 300,
 "mango.jpg",
 "Mango is a tropical fruit plant widely grown in India. Scientific Name: Mangifera indica. "
 "Climate: Tropical. Sunlight: Full sunlight. Watering: Moderate. "
 "Soil: Loamy soil. Growth Time: 3–5 years. "
 "Uses: Fruit, juice, pickle. Lifespan: 40–60 years."
)
,
    ("fruit",
 "Apple",
 250,
 "apple.jpg",
 "Apple is a popular temperate fruit plant. Scientific Name: Malus domestica. "
 "Climate: Cool & temperate. Sunlight: Full sun. Watering: Moderate. "
 "Soil: Well-drained loamy soil. Growth Time: 3–4 years. "
 "Uses: Fresh fruit, juice. Lifespan: 30–40 years."
)
,
    ("fruit",
 "Banana",
 150,
 "banana.jpg",
 "Banana is a fast-growing tropical plant. Scientific Name: Musa. "
 "Climate: Warm & humid. Sunlight: Full sun. Watering: Frequent. "
 "Soil: Fertile soil. Growth Time: 10–12 months. "
 "Uses: Fruit, cooking. Lifespan: 2–3 years."
)
,
    ("fruit",
 "Orange",
 200,
 "orange.jpg",
 "Orange is a citrus fruit plant. Scientific Name: Citrus sinensis. "
 "Climate: Subtropical. Sunlight: Full sun. Watering: Moderate. "
 "Soil: Well-drained soil. Growth Time: 3–4 years. "
 "Uses: Fruit, juice. Lifespan: 30–50 years."
)
,
    ("fruit",
 "Guava",
 180,
 "guava.jpg",
 "Guava is an easy-to-grow fruit plant. Scientific Name: Psidium guajava. "
 "Climate: Tropical & subtropical. Sunlight: Full sun. Watering: Moderate. "
 "Soil: Sandy loam. Growth Time: 2–3 years. "
 "Uses: Fruit, juice. Lifespan: 30–40 years."
)
,

    ("flower",
 "Rose",
 120,
 "rose.jpg",
 "Rose is a beautiful flowering plant. Scientific Name: Rosa. "
 "Climate: Mild. Sunlight: Full sun. Watering: Regular. "
 "Soil: Fertile soil. Growth Time: 2–3 months. "
 "Uses: Decoration, perfume. Lifespan: 5–7 years."
)
,
    ("flower",
 "Jasmine",
 100,
 "jasmine.jpg",
 "Jasmine is a fragrant flowering plant. Scientific Name: Jasminum. "
 "Climate: Tropical. Sunlight: Full sun. Watering: Moderate. "
 "Soil: Well-drained soil. Growth Time: 4–6 months. "
 "Uses: Perfume, decoration. Lifespan: 10–15 years."
)
,
   ("flower",
 "Hibiscus",
 140,
 "hibiscus.jpg",
 "Hibiscus is a bright and beautiful flowering plant commonly grown in Indian gardens. "
 "Scientific Name: Hibiscus rosa-sinensis. "
 "Climate: Tropical & warm. Sunlight: Full sun. "
 "Watering: Moderate, keep soil moist but not waterlogged. "
 "Soil: Well-drained fertile soil. Growth Time: 2–3 months. "
 "Uses: Religious पूजा, decoration, hair care. "
 "Lifespan: 5–10 years."
)
,
    ("flower",
 "Lily",
 160,
 "lily.jpg",
 "Lily is an ornamental flowering plant. Scientific Name: Lilium. "
 "Climate: Mild. Sunlight: Partial to full sun. Watering: Moderate. "
 "Soil: Fertile soil. Growth Time: 2–3 months. "
 "Uses: Decoration. Lifespan: Perennial."
)
,
    ("flower",
 "Sunflower",
 140,
 "sunflower.jpg",
 "Sunflower is a bright flowering plant. Scientific Name: Helianthus annuus. "
 "Climate: Warm. Sunlight: Full sun. Watering: Moderate. "
 "Soil: Well-drained soil. Growth Time: 2–3 months. "
 "Uses: Decoration, seeds. Lifespan: 1 year."
)
,

    ("show",
 "Bonsai",
 800,
 "bonsai.jpg",
 "Bonsai is a decorative miniature tree. "
 "Climate: Indoor/Outdoor. Sunlight: Partial. Watering: Regular. "
 "Soil: Bonsai soil mix. Growth Time: Long-term. "
 "Uses: Decoration. Lifespan: 20–50 years."
)
,
    ("show",
 "Palm",
 600,
 "palm.jpg",
 "Palm is a decorative indoor and outdoor plant. "
 "Climate: Tropical. Sunlight: Partial to full sun. Watering: Moderate. "
 "Soil: Sandy soil. Growth Time: Slow. "
 "Uses: Decoration. Lifespan: 40–60 years."
)
,
    ("show",
 "Maple",
 700,
 "maple.jpg",
 "Maple is a decorative tree known for colorful leaves. "
 "Scientific Name: Acer. Climate: Temperate. "
 "Sunlight: Full sun. Watering: Moderate. "
 "Soil: Well-drained soil. Lifespan: 80–100 years."
)
,
    ("show",
 "Oak",
 750,
 "oak.jpg",
 "Oak is a strong hardwood tree. Scientific Name: Quercus. "
 "Climate: Temperate. Sunlight: Full sun. Watering: Moderate. "
 "Soil: Loamy soil. Growth Time: Slow. "
 "Uses: Shade, wood. Lifespan: 200+ years."
)
,
    ("show",
 "Pine",
 650,
 "pine.jpg",
 "Pine is an evergreen tree. Scientific Name: Pinus. "
 "Climate: Cool. Sunlight: Full sun. Watering: Moderate. "
 "Soil: Sandy soil. Growth Time: Slow. "
 "Uses: Decoration, wood. Lifespan: 100+ years."
)

]

cur.executemany(
    "INSERT INTO plants (category, name, price, image, description) VALUES (?,?,?,?,?)",
    plants
)

conn.commit()
conn.close()

print("Database initialized successfully")
