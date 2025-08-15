SHOWS = [
    " Avatar: the last airbender", 
    "Ben 10",
    "Arthur",
    " Spongebob Squarepants",
    "Kim possible",
    "Jimmy Neutron",
    "Phineas and Ferb",
    "The Proud Family "
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.title().strip())
    
    print(', '.join(cleaned_shows))

main()