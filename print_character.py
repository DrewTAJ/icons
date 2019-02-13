#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont

def print_character(character):
    img = Image.open("page-1.png")
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("Roboto/Roboto-Regular.ttf", size=28)

    d.text((250, 80), character["name"], fill="black", font=font) # Name
    d.text((650, 80), "N/A", fill="black", font=font) # Real Name 
    d.text((980, 80), "Drew Johnson", fill="black", font=font) # Player

    for index, power in enumerate(character["powers"]):
        draw_power(d, power["name"], power["level"], 230 + (50 * index), font)

    for index, specialty in enumerate(character["specialties"]):
        d.text((120, 600 + (50 * index)), specialty, fill="black", font=font)

    for index, item in enumerate(character["equipment"]):
        d.text((830, 600 + (50 * index)), item, fill="black", font=font)

    stats = [
        character["stats"]["prowess"],
        character["stats"]["coordination"],
        character["stats"]["strength"],
        character["stats"]["intellect"],
        character["stats"]["awareness"],
        character["stats"]["willpower"]
    ]

    stat_start_y = 192

    stat_font = ImageFont.truetype("Roboto/Roboto-Regular.ttf", size=38)

    draw_stats(d, stat_start_y, stats, stat_font)

    other_stats = [character["stamina"], character["determination"]]

    other_start_y = 442
    draw_stats(d, other_start_y, other_stats, stat_font)

    draw_qualities(d, character["qualities"], font)


    draw_notes(d, character["notes"], font)

    img_width, img_height = img.size

    d.rectangle([(0, img_height - 30), (200, img_height)], fill="white")
    
    img.show()

    return img

def get_multiline_text(text, max_width, text_font):
    split_text = text.split(" ")
    lines = []
    for index, line in enumerate(split_text):
        if index is 0:
            lines.append("- %s" % (line))
            continue
        width, height = text_font.getsize("%s %s" % (lines[len(lines) - 1], line))
        if width > max_width:
            lines.append(line)
        else:
            lines[len(lines) - 1] = "%s %s" % (lines[len(lines) - 1], line)
    return lines

def draw_power(d, power_name, power_points, y, power_font):
    d.text((500, y), power_name, fill="black", font=power_font) # Power Name
    d.text((900, y), str(power_points), fill="black", font=power_font) # Power Points

def draw_stats(d, start_y, stats, stat_font):
    new_start_y = start_y
    stat_container_height = 37
    spacing = 1
    for index, stat in enumerate(stats):
        if index > 0:
            new_start_y = new_start_y + stat_container_height + spacing
        draw_stat(d, stat, new_start_y, stat_container_height, stat_font)

def draw_stat(d, stat_number, y, stat_container_height, stat_font):
    width = 40
    start_x = 401
    font_width, font_height = stat_font.getsize(str(stat_number))
    d.rectangle([(start_x, y), (start_x + width, y + stat_container_height)], fill="white", outline=None)
    center_x = start_x + (width / 2) - (font_width / 2)
    d.text((center_x, y - 2), str(stat_number), fill="black", font=stat_font)

def draw_multiline_text(d, lines, start_x, start_y, line_spacing, line_font):
    line_y = start_y
    for line in lines:
        d.text((start_x, line_y), line, fill="black", font=line_font)
        line_y = line_y + line_spacing
    return line_y

def draw_section(d, texts, start_x, start_y, max_width, text_font):
    line_y = start_y
    for text in texts:
        lines = get_multiline_text(text, max_width, text_font)
        line_y = draw_multiline_text(d, lines, start_x, line_y, 28, text_font) + 8

def draw_qualities(d, qualities, quality_font):
    draw_section(d, qualities, 490, 600, 300, quality_font)

def draw_notes(d, notes, note_font):
    draw_section(d, notes, 120, 960, 650, note_font)

def main(character):
    return print_character(character)