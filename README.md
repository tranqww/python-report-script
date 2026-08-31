# CSV to Excel Report Mailer

A command-line tool that converts a CSV file into a formatted Excel report and, optionally, emails it as an attachment.

## Features

- Reads any CSV with `title`, `url`, and `score` columns
- Converts it into a clean Excel report (`.xlsx`) via `openpyxl`
- Optionally sends the report by email as an attachment
- Fully configurable from the command line — no code editing needed to change input/output files or the recipient

## Tech stack

- Python
- `argparse` — command-line interface
- `openpyxl` — Excel file generation
- `smtplib` / `email.message` — sending email with attachments

## Project structure

main.py # CLI entry point (argparse), wires everything together
excel_report.py # Reads the CSV, builds the Excel report
mailer.py # Sends the report by email
requirements.txt


## Setup

1. Clone the repository and move into it:
```bash
   git clone <repo-url>
   cd csv-excel-email
```

2. Create and activate a virtual environment:
```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. (Only needed if you want email sending) Create a `.env` file:

EMAIL_ADDRESS=your-gmail-address@gmail.com
EMAIL_PASSWORD=your-16-character-app-password

   Gmail requires a Google Account **App Password** for this (not your regular password) — generate one at `myaccount.google.com/apppasswords` after enabling 2-Step Verification.

## Usage

```bash
python main.py
```
Reads `hh_stories.csv` (default), writes `report.xlsx` (default).

```bash
python main.py --input other.csv --output custom_report.xlsx
```
Use a different input or output file.

```bash
python main.py --email someone@example.com
```
Also sends the resulting report to the given address.

```bash
python main.py --help
```
Shows all available options.

## License

MIT — see [LICENSE](LICENSE).