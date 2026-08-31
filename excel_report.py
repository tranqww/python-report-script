# чтение CSV, сборка Excel-отчёта (openpyxl)
import csv

from openpyxl import Workbook


def read_stories(csv_path):
    with open (csv_path, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

def build_excel_report(stories, output_path):
    wb = Workbook()
    ws = wb.active
    if ws is not None:
        ws.title = "HN Stories"
        ws.append(["title", "url", "score"])
    for story in stories: 
        if ws is not None:
            ws.append([story["title"], story["url"], int(story["score"])]) 
    wb.save(output_path)
