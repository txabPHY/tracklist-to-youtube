import re
import urllib.parse

def generate_youtube_links(text):
    # Use a more sophisticated regex that can capture:
    # (1) Simple artist-song pairs.
    # (2) Timestamped entries.
    # (3) Entries possibly prefixed by track numbers in parentheses.
    # This regex captures lines that might start with optional timestamps or track numbers, followed by the artist and song.
    pattern = r'(?:\d+:\d+|\(\d+\))?\s*([^\n-]+?)\s*-\s*([^\n\(]+)'
    matches = re.findall(pattern, text)

    # Generate YouTube search links for each valid match
    youtube_links = []
    for artist, song_name in matches:
        artist = artist.strip()
        song_name = song_name.strip()
        # Clean song name to remove trailing special characters like remix info in parentheses
        song_name = re.sub(r'\s*\([^)]*\)', '', song_name).strip()
        query = f"{artist} {song_name}"
        url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
        youtube_links.append((artist, song_name, url))

    return youtube_links

# Input your text here. This example contains a mix of formats:
input_text = """

Petrichor - unknown
Dance Dance Maniac - Zed Bias
Paul Du Lac - Jump Source
Infinity Plus One - Syclops
Pearson Sound - Verraco
King Doudou - Photonz
Pocz & Pacheko - DHS
Brumby Kapell - Americana
We're There (ft. Chunky) - Jil / Tlo Carb6n
DISTURBER - Ganzfeld Cookie
The Edge Of Dread - Pink Sarah Nyc Is Back
Gqomge Ondo - NLL561908703
Ponte las Pilas - Urgency
Feverdream - Always fwd
Zarbak - Intergalactic Dub

"""

links = generate_youtube_links(input_text)

# Print the links
for artist, song_name, url in links:
    print(f"Artist: {artist}, Song: {song_name}, YouTube Search: {url}")
