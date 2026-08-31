# argparse, точка входа
import argparse

from excel_report import build_excel_report, read_stories
from mailer import send_report

parser = argparse.ArgumentParser(description="Convert a CSV report to Excel, optionally email it")
parser.add_argument("--input", "-i", default="hh_stories.csv", help="Path to input CSV file")
parser.add_argument("--output", "-u", default="report.xlsx", help="Path to output Excel file")
parser.add_argument("--email", "-e", help="Email address to send the report to (optional)")
args = parser.parse_args()

stories = read_stories(args.input)
build_excel_report(stories, args.output)
if args.email is not None:
    send_report(args.email, args.output)