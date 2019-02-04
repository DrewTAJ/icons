#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import smtplib
import os
from email.mime.Text import MIMEText
import grilly
# from PyPDF2 import PdfFileMerger

font = ImageFont.truetype("Roboto/Roboto-Regular.ttf", size=28)

def print_character(character):
    img = Image.open("page-1.png")
    d = ImageDraw.Draw(img)
    d.text((250, 80), character["name"], fill="black", font=font) # Name
    d.text((650, 80), "N/A", fill="black", font=font) # Real Name 
    d.text((980, 80), "Drew Johnson", fill="black", font=font) # Player

    for index, power in enumerate(character["powers"]):
        draw_power(d, power["name"], power["level"], 230 + (50 * index))

    for index, specialty in enumerate(character["specialties"]):
        d.text((120, 600 + (50 * index)), specialty, fill="black", font=font)

    for index, quality in enumerate(character["qualities"]):
        d.text((490, 600 + (50 * index)), quality, fill="black", font=font)

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

    send_email("sample.pdf")

    img.show()
    # img.save("file.pdf", "PDF")

def draw_power(d, power_name, power_points, y):
    d.text((500, y), power_name, fill="black", font=font) # Power Name
    d.text((900, y), str(power_points), fill="black", font=font) # Power Points

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

def draw_notes(d, notes):
    print ""

def send_email(file_name):
    from_email = "drew.t.a.johnson@gmail.com"
    to_email = "jamieson.smith@gmail.com"
    message = "This is a message"

def main():
    test_character = grilly.getCharacter()
    print_character(test_character)

# def save_character_sheet():
#     dir_name = "characters/"
#     if not os.path.exists(dir_name):
#         os.makedirs(dir_name)

#     file_name = "character.pdf"

#     merger = PdfFileMerger()
    
main()