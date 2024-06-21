# Web Scraping Projects 
This repository contains two web scraping projects using Playwright and Python.
## Projects Overview

1. **Google Maps Business Scraper**
2. **Booking.com Hotel Scraper**

3. ### 1. Google Maps Business Scraper
4. This script scrapes business information from Google Maps based on a search query. The data collected includes business name, address, website, and phone number. The results are saved in both Excel and CSV formats.
5. #### Dependencies

- Python 3.x
- Playwright
- Pandas
- Dataclasses
- #### to install
- pip install -r requirements.txt
-  playwright install chromium

-  ####to Run
-  python3 main.py -s=<what & where to search for> -t=<how many>
 #### Example
 python google_maps_scraper.py -s "dentist New York" -t 10
 
-  ###Booking.com Hotel Scraper
-  This is simple scraper that uses Playwright to extract data from Booking.com
#### to install
- pip install -r requirements.txt
-  playwright install chromium
-  ####to Run
-  python3 booking_com_scraper.py

 
