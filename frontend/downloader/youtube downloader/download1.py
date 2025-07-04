import os
import re
import csv
import requests
import yt_dlp
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC
from tqdm import tqdm

SONG_DIR = "songs"
IMAGE_DIR = "cover_images"
CSV_PATH = "metadata.csv"

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', '', name)

def ensure_dirs():
    os.makedirs(SONG_DIR, exist_ok=True)
    os.makedirs(IMAGE_DIR, exist_ok=True)

def download_and_tag(link):
    try:
        ydl_opts_info = {
            'quiet': True,
            'skip_download': True,
            'format': 'bestaudio/best',
        }

        with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
            info = ydl.extract_info(link, download=False)

        # Metadata
        title = sanitize_filename(info.get('title', 'Unknown Title'))
        artist = sanitize_filename(info.get('artist') or info.get('uploader') or 'Unknown Artist')
        album = sanitize_filename(info.get('album') or 'YouTube')
        thumbnail_url = info.get('thumbnail')

        # Final paths
        filename_base = f"{title} - {artist}"
        song_path = os.path.join(SONG_DIR, filename_base + ".mp3")
        image_path = os.path.join(IMAGE_DIR, filename_base + ".jpg")

        # yt_dlp download
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(SONG_DIR, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': r"C:\Users\palya\Downloads\Compressed\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin",  # Update if different
            'quiet': True,
            'progress_hooks': [progress_hook],
        }

        print(f"\n🎵 Downloading: {title}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        # Rename downloaded file
        downloaded_file = find_latest_file(SONG_DIR, '.mp3')
        if not downloaded_file:
            print(f"❌ No MP3 file found for: {title}")
            return
        os.rename(downloaded_file, song_path)

        # Metadata tagging
        audio = EasyID3(song_path)
        audio['title'] = title
        audio['artist'] = artist
        audio['album'] = album
        audio.save()

        # Save cover image
        if thumbnail_url:
            save_cover_image(thumbnail_url, image_path)
            embed_cover_image(song_path, image_path)

        # Save metadata to CSV
        save_to_csv([title, artist, album, link, song_path, image_path])

        print(f"✅ Done: {filename_base}")

    except Exception as e:
        print(f"❌ Failed to download {link}: {e}")

def save_cover_image(thumbnail_url, image_path):
    try:
        img_data = requests.get(thumbnail_url).content
        with open(image_path, 'wb') as f:
            f.write(img_data)
        print(f"🖼️ Cover image saved to: {image_path}")
    except Exception as e:
        print(f"⚠️ Failed to save cover image: {e}")

def embed_cover_image(mp3_path, image_path):
    try:
        with open(image_path, 'rb') as img:
            img_data = img.read()
        audio = ID3(mp3_path)
        audio.add(APIC(
            encoding=3,
            mime='image/jpeg',
            type=3,
            desc='Cover',
            data=img_data
        ))
        audio.save()
    except Exception as e:
        print(f"⚠️ Failed to embed cover: {e}")

def save_to_csv(row):
    file_exists = os.path.isfile(CSV_PATH)
    with open(CSV_PATH, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Title', 'Artist', 'Album', 'YouTube Link', 'MP3 Path', 'Image Path'])
        writer.writerow(row)

def progress_hook(d):
    if d['status'] == 'downloading':
        p = d.get('_percent_str', '0.0%').strip()
        print(f"\r⏳ Downloading... {p}", end='', flush=True)
    elif d['status'] == 'finished':
        print("\r📥 Download complete. Converting...")

def find_latest_file(folder, ext):
    files = [f for f in os.listdir(folder) if f.endswith(ext)]
    files.sort(key=lambda x: os.path.getctime(os.path.join(folder, x)), reverse=True)
    return os.path.join(folder, files[0]) if files else None

def main():
    ensure_dirs()
    if not os.path.exists("links.txt"):
        print("❌ 'links.txt' file not found.")
        return
    with open("links.txt", 'r', encoding='utf-8') as f:
        links = [line.strip() for line in f if line.strip()]
    for link in links:
        download_and_tag(link)

if __name__ == "__main__":
    main()
