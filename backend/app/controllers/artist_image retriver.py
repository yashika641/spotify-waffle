import wikipedia
import requests
import csv
import os
from tqdm import tqdm
from PIL import Image
from io import BytesIO

# Constants
IMAGE_DIR = "artist_images"
CSV_PATH = "artists.csv"

# Create directories
os.makedirs(IMAGE_DIR, exist_ok=True)

# List of (artist_name, country)
artists_data = [
    # --- Mostly Indian artists ---
    ("Arijit Singh", "India"), ("Neha Kakkar", "India"), ("Shreya Ghoshal", "India"),
    ("Armaan Malik", "India"), ("Dhvani Bhanushali", "India"), ("Badshah (rapper)", "India"),
    ("Jubin Nautiyal", "India"), ("Jonita Gandhi", "India"), ("King (rapper)", "India"),
    ("MC Stan", "India"), ("Raftaar", "India"), ("Tulsi Kumar", "India"),
    ("Prateek Kuhad", "India"), ("Anuv Jain", "India"), ("Stebin Ben", "India"),
    ("Sachet Tandon", "India"), ("Sidhu Moose Wala", "India"), ("Diljit Dosanjh", "India"),
    ("Asees Kaur", "India"), ("Palak Muchhal", "India"), ("B Praak", "India"),
    ("Sanam Puri", "India"), ("Lisa Mishra", "India"), ("Tony Kakkar", "India"),
    # --- International artists ---
    ("Taylor Swift", "USA"), ("Ariana Grande", "USA"), ("Ed Sheeran", "UK"),
    ("Billie Eilish", "USA"), ("BTS", "South Korea"), ("BLACKPINK", "South Korea"),
    ("The Weeknd", "Canada"), ("Olivia Rodrigo", "USA"), ("Dua Lipa", "UK"),
    ("Justin Bieber", "Canada"), ("Harry Styles", "UK"), ("Camila Cabello", "USA"),("Shilpa Rao", "India"),
    ("Sona Mohapatra", "India"),
    ("Vishal Mishra", "India"),
    ("Rekha Bhardwaj", "India"),
    ("Papon", "India"),
    ("Kaushiki Chakraborty", "India"),
    ("Anuv Jain", "India"),
    ("Divine (rapper)", "India"),
    ("Ankur Tewari", "India"),
    ("Raghav Meattle", "India"),
    ("Kamlesh Barot", "India"),
    ("Raja Kumari", "India"),
    ("Dee MC", "India"),
    ("Taba Chake", "India"),
    ("When Chai Met Toast", "India"),
    ("The Local Train", "India"),
    ("Parekh & Singh", "India"),
    ("Ananya Birla", "India"),
    ("KSHMR", "India-USA"),
    ("Kavya Trehan", "India"),

    # USA
    ("SZA", "USA"),
    ("Halsey", "USA"),
    ("Khalid", "USA"),
    ("Tyler, the Creator", "USA"),
    ("Lil Nas X", "USA"),
    ("Jack Harlow", "USA"),
    ("HER", "USA"),
    ("Megan Thee Stallion", "USA"),
    ("21 Savage", "USA"),
    ("Giveon", "USA"),

    # UK & Europe
    ("Raye", "UK"),
    ("Jessie J", "UK"),
    ("Stormzy", "UK"),
    ("Lewis Capaldi", "UK"),
    ("Anne-Marie", "UK"),
    ("Rina Sawayama", "UK"),
    ("Måneskin", "Italy"),
    ("Zaz", "France"),
    ("Stromae", "Belgium"),

    # Korea & Asia
    ("Taeyeon", "South Korea"),
    ("IU (singer)", "South Korea"),
    ("Baekhyun", "South Korea"),
    ("Jay Chou", "Taiwan"),
    ("Joji", "Japan-Australia"),
    ("Rich Brian", "Indonesia"),
    ("NIKI", "Indonesia"),

    # Latin America & Others
    ("Karol G", "Colombia"),
    ("Maluma", "Colombia"),
    ("J Balvin", "Colombia"),
    ("Bad Bunny", "Puerto Rico"),
    ("TINI", "Argentina"),("Siddharth Slathia", "India"),
    ("Shashaa Tirupati", "India"),
    ("Ash King", "India"),
    ("Akhil Sachdeva", "India"),
    ("Raghav Chaitanya", "India"),
    ("Sireesha Bhagavatula", "India"),
    ("Vipin Aneja", "India"),
    ("Arjun Kanungo", "India"),
    ("Pritam Chakraborty", "India"),
    ("Mithoon", "India"),
    ("Ankit Tiwari", "India"),
    ("Mohit Chauhan", "India"),
    ("Rochak Kohli", "India"),
    ("Navraj Hans", "India"),
    ("Sukhwinder Singh", "India"),
    ("Sunidhi Chauhan", "India"),
    ("Bhavatharini", "India"),
    ("Anirudh Ravichander", "India"),
    ("Yuvan Shankar Raja", "India"),
    ("Sid Sriram", "India"),
    ("GV Prakash", "India"),
    ("Shankar Mahadevan", "India"),
    ("Hariharan", "India"),
    ("Sanjith Hegde", "India"),
    ("Shalmali Kholgade", "India"),
    ("Haricharan", "India"),
    ("Meiyang Chang", "India"),
    ("Sreerama Chandra", "India"),
    ("Rahat Fateh Ali Khan", "India"),
    ("Jonita Dutta", "India"),

    # --- USA / North America ---
    ("Tate McRae", "Canada"),
    ("Beabadoobee", "Philippines-UK"),
    ("Bryson Tiller", "USA"),
    ("Lana Del Rey", "USA"),
    ("Saweetie", "USA"),
    ("Ty Dolla Sign", "USA"),
    ("Alec Benjamin", "USA"),
    ("Clairo", "USA"),
    ("Phoebe Bridgers", "USA"),
    ("Sabrina Carpenter", "USA"),
    ("Fousheé", "USA"),
    ("Lauv", "USA"),
    ("Jon Bellion", "USA"),
    ("Noah Kahan", "USA"),

    # --- UK & Europe ---
    ("Tom Odell", "UK"),
    ("Sam Fender", "UK"),
    ("Celeste (singer)", "UK"),
    ("Birdy", "UK"),
    ("Freya Ridings", "UK"),
    ("Benjamin Clementine", "UK"),
    ("Tove Lo", "Sweden"),
    ("Zara Larsson", "Sweden"),
    ("Agnes Obel", "Denmark"),
    ("ROSALÍA", "Spain"),
    ("Alvaro Soler", "Spain"),

    # --- Korea & Asia ---
    ("Hwasa", "South Korea"),
    ("Chungha", "South Korea"),
    ("Jisoo", "South Korea"),
    ("Jackson Wang", "Hong Kong"),
    ("Eric Nam", "South Korea-USA"),
    ("Agnez Mo", "Indonesia"),
    ("Kenshi Yonezu", "Japan"),
    ("YOASOBI", "Japan"),
    ("Namie Amuro", "Japan"),

    # --- Latin America / World ---
    ("Lali Espósito", "Argentina"),
    ("Sebastián Yatra", "Colombia"),
    ("Becky G", "USA-Mexico"),
    ("Cazzu", "Argentina"),
    ("Danna Paola", "Mexico"),
    ("Myke Towers", "Puerto Rico"),
    ("Rauw Alejandro", "Puerto Rico"),
    ("Manuel Turizo", "Colombia"),
    ("Ludmilla", "Brazil"),
    ("Pabllo Vittar", "Brazil"),
    ("Anitta", "Brazil")
]

# Store results
results = []

print("Fetching artists and validating image quality...\n")
for name, country in tqdm(artists_data):
    try:
        page = wikipedia.page(name, auto_suggest=False)
        summary = wikipedia.summary(name, auto_suggest=False)

        # Try to find a suitable image
        image_url = None
        for img in page.images:
            if any(img.lower().endswith(ext) for ext in [".jpg", ".jpeg", ".png"]):
                # Skip logos, flags, vector, icons
                if any(x in img.lower() for x in ["logo", "icon", "symbol", "flag", "svg", "map", "signature"]):
                    continue

                # Try downloading and verifying the image
                try:
                    resp = requests.get(img, timeout=10)
                    image = Image.open(BytesIO(resp.content))
                    image.verify()  # validate image
                    image = Image.open(BytesIO(resp.content))  # reopen to get size
                    if image.width < 100 or image.height < 100:
                        continue  # reject tiny images
                    image_url = img
                    break  # found good image
                except:
                    continue  # try next

        if image_url:
            # Save image
            response = requests.get(image_url, timeout=10)
            file_name = name.replace(" ", "_").replace("/", "_") + ".jpg"
            img_path = os.path.join(IMAGE_DIR, file_name)
            with open(img_path, "wb") as f:
                f.write(response.content)

            # Save result
            results.append({
                "name": name,
                "bio": summary[:500].replace("\n", " "),
                "image_path": img_path,
                "country": country
            })

    except Exception as e:
        continue  # skip errors silently

# Save to CSV
with open(CSV_PATH, mode="w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "bio", "image_path", "country"])
    writer.writeheader()
    writer.writerows(results)

print(f"\n✅ DONE! {len(results)} valid artists saved to '{CSV_PATH}' with good images in '{IMAGE_DIR}/'")
