#!/usr/bin/env python3
import sys

print("<!DOCTYPE html>")
print("<html lang='en'>")
print("<head><meta charset='UTF-8'><title>Final Exam - Wataru Okada</title></head>")
print("<body>")

party_items = [
    ("0: Cake", 20), ("1: Balloons", 21), ("2: Music System", 10), ("3: Lights", 5),
    ("4: Catering Service", 8), ("5: DJ", 3), ("6: Photo Booth", 15), ("7: Tables", 7),
    ("8: Chairs", 12), ("9: Drinks", 6), ("10: Party Hats", 9), ("11: Streamers", 18),
    ("12: Invitation Cards", 4), ("13: Party Games", 2), ("14: Cleaning Service", 11)
]

try:
    if len(sys.argv) < 2:
        raise ValueError("No items passed.")

    if not sys.argv[1].startswith("items="):
        raise ValueError("Invalid argument format. Expected 'items=...'")

    raw_input = sys.argv[1].split("=")[1]
    indices = []
    for i in raw_input.split(","):
        try:
            index = int(i.strip())
            if 0 <= index < len(party_items):
                indices.append(index)
            else:
                raise ValueError(f"Index {index} out of range.")
        except ValueError:
            raise ValueError(f"Invalid index: {i}")

    selected_names = [party_items[i][0] for i in indices]
    selected_values = [party_items[i][1] for i in indices]

    print("<p><strong>Selected Items:</strong> " + ", ".join(selected_names) + "</p>")

    base_code = selected_values[0] if selected_values else 0
    and_steps = str(selected_values[0]) if selected_values else "N/A"
    for val in selected_values[1:]:        
        base_code &= val        
        and_steps += f" & {val}"

    print(f"<p><strong>Base Party Code:</strong> {and_steps} = {base_code}</p>")

    final_code = base_code
    if base_code == 0:
        final_code += 5
        message = "Epic Party Incoming!"
        print(f"<p><strong>Adjusted Party Code:</strong> 0 + 5 = {final_code}</p>")
    elif base_code > 5:
        final_code -= 2
        message = "Let's keep it classy!"
        print(f"<p><strong>Adjusted Party Code:</strong> {base_code} - 2 = {final_code}</p>")
    else:
        message = "Chill vibes only!"
        print(f"<p><strong>Adjusted Party Code:</strong> {final_code}</p>")

    print(f"<p><strong>Final Party Code:</strong> {final_code}</p>")
    print(f"<p><strong>Message:</strong> {message}</p>")

except Exception as e:
    print(f"<p><strong>Error:</strong> {e}</p>")

print("</body></html>")
