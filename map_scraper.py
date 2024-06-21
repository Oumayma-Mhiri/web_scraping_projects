from playwright.sync_api import sync_playwright
from dataclasses import dataclass, asdict, field
import pandas as pd
import argparse


@dataclass
class Business:
    name: str = None
    address: str = None
    website: str = None
    phone_number: str = None
   


@dataclass
class BusinessList:
    business_list: list[Business] = field(default_factory=list)

    def dataframe(self):
        return pd.json_normalize(
            (asdict(business) for business in self.business_list), sep="_"
        )

    def save_to_excel(self, filename):
        self.dataframe().to_excel(f'{filename}.xlsx', index=False)

    def save_to_csv(self, filename):
        self.dataframe().to_csv(f'{filename}.csv', index=False)


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.google.com/maps')
       

        page.locator('//input[@id="searchboxinput"]').fill(search_for)
      

        page.keyboard.press('Enter')

        #scrolling
        page.hover('//a[@class="hfpxzc"][1]')

        while True:
             page.mouse.wheel(0,1000)
             if page.locator('//a[@class="hfpxzc"]').count()>= total:
                  listings=page.locator('//a[@class="hfpxzc"]').all()[:total]
                  print(f'Total Scraped: {len(listings)}')
                  break
             else:
                  print(f'Currently Scraped:', page.locator('//a[@class="hfpxzc"]').count())

         

        listings = page.locator('//a[@class="hfpxzc"]').all()
        print(f"Found {len(listings)} listings")

        business_list = BusinessList()
        for i, listing in enumerate(listings):
            try:
                listing.click()
                

                name_attribute = 'aria-label'

                address_xpath = '//button[@data-item-id="address"]//div[contains(@class, "fontBodyMedium")]'
                website_xpath = '//a[@data-item-id="authority"]//div[contains(@class, "fontBodyMedium")]'
                phone_number_xpath = '//button[contains(@data-item-id, "phone:tel:")]//div[contains(@class, "fontBodyMedium")]'
               
            
               
                
                business = Business()


                if len(listing.get_attribute(name_attribute))>=1:

                      business.name = listing.get_attribute(name_attribute)
                else:
                    business.name=""     


                if page.locator(address_xpath).count()>0:
                      business.address = page.locator(address_xpath).inner_text()
                else:
                      business.address=""

                if page.locator(website_xpath).count()>0:
                      business.website = page.locator(website_xpath).inner_text()
                else:
                      business.website=""
                
                if page.locator(phone_number_xpath).count()>0:
                      business.phone_number = page.locator(phone_number_xpath).inner_text()
                else:
                       business.phone_number=""

                

                
                
                
                
                
                
                
                
                
                
                
                print(f"Scraped {i+1}/{total}: {business}")

                business_list.business_list.append(business)
                page.go_back()
                page.wait_for_timeout(5000)
            except Exception as e:
                print(f"Error scraping listing {i+1}: {e}")
              

        
        try:
            business_list.save_to_excel('google_maps_data')
            business_list.save_to_csv('google_maps_data')
            print("Data saved successfully.")
        except Exception as e:
            print(f"Error saving data: {e}")

        browser.close()



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--search", type=str)
   
    parser.add_argument("-t", "--total", type=int)

    args = parser.parse_args()
    
    if args.search:
         search_for=args.search
    else:
         search_for='dentist new york'

    if args.total:
         total=args.total
    else:
         total= 10
  
    main()