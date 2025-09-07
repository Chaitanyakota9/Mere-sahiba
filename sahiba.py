import time

def printlyrics():
    lines = [
        ("...", 1.5),
        ("...", 2.5),
        ("...", 1.5),
        ("...", 3),
        ("SAHIBA, too hee mera aaeena,", 4),
        ("haathon mein bhee mere, haan", 3),
        ("tera hee naseeb aathaa hai", 3.5),
        ("SAHIBA, neenden-vinden aayena", 3),
        ("raatein kaati jae naa", 3),
        ("tera hee khyaal din-rain aathaa hai", 4),
        ("SAHIBA, neenden-vinden aaye", 3),
        ("naa, raatein kaati jae naa", 2),
        ("tera hee khyaal din-rain aathaa hai", 5),
        ("...", 2),
        ("...", 2),
        ("...", 2),
        ("...", 2),
    ]
    
    for line, duration in lines:
        # Calculate delay per character to match the total duration
        char_delay = duration / len(line)
        
        # Type each letter one by one with proper timing
        for char in line:
            if char == "S" and line.startswith("SAHIBA"):
                # Handle SAHIBA word specially
                if line[:6] == "SAHIBA":
                    print("\033[97mSAHIBA\033[38;5;88m", end="", flush=True)
                    # Skip the rest of SAHIBA
                    remaining = line[6:]
                    for c in remaining:
                        print(f"\033[38;5;88m{c}\033[0m", end="", flush=True)
                        time.sleep(char_delay)
                    break
            else:
                print(f"\033[38;5;88m{char}\033[0m", end="", flush=True)
                time.sleep(char_delay)
        
        print()  # New line after each word

printlyrics()
         