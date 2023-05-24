# Some "Fictitious Website" Scraper

This project is a web scraper designed to extract information from the "Some fictitious website". It gathers data on expert organizations and their email addresses from the website's registries.

## Features

- Fetches HTML content from the "Some fictitious website".
- Extracts expert organizations' information, including name and URL.
- Retrieves email addresses associated with each expert organization.
- Validates and cleans the data using Pydantic models.
- Writes the extracted data to CSV or XLSX file.

## Installation

1. _Clone the repository:_

   ```bash
   git clone https://github.com/tserediani/fictitious_website_scraper.git
   ```

2. _Change into the project directory:_
   ```bash
   cd fictitious_website_scraper
   ```
3. _Create a virtual environment (optional but recommended):_
   ```bash
   python -m venv env
   ```
4. _Activate the virtual environment:_
   _For Windows:_
   ```bash
   env\Scripts\activate
   ```
   _For Unix or Linux:_
   ```bash
   source env/bin/activate
   ```
5. _Install the dependencies:_
   ```bash
   pip install -r requirements.txt
   ```

# Usage

1. _Modify the necessary constants and configurations in constants.py to match your requirements._
2. _Run the main script:_
   ```bash
    python main.py
   ```
   The script will start scraping the "Some fictitious website" and extract expert organizations' data, including their email addresses. The data will be written to CSV files in the output/ directory.

# Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

# License

This project is licensed under the MIT License.
