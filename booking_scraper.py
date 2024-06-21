from playwright.sync_api import sync_playwright
import pandas as pd

def main():
    with sync_playwright() as p:
        checkin_date='2024-06-25'
        checkout_date='2024-06-29'

        page_url = f'https://www.booking.com/searchresults.en-us.html?checkin={checkin_date}&checkout={checkout_date}&selected_currency=USD&ss=Paris&ssne=Paris&ssne_untouched=Paris&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_type=city&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
         

        browser= p.chromium.launch(headless=False)
        page=browser.new_page()
        
        page.goto(page_url,timeout=60000)

        hotels = page.locator('//div[@data-testid="property-card"]').all()
        print(f'There are: {len(hotels)} hotels.')

        hotels_list=[]
        for hotel in hotels:
            hotel_dict={}
            hotel_dict['hotel'] = hotel.locator('//div[@data-testid="title"]').inner_text()
            hotel_dict['price'] = hotel.locator('//span[@data-testid="price-and-discounted-price"]').inner_text()
            hotel_dict['score'] = hotel.locator('//div[@data-testid="review-score"]/div[1]').inner_text()
            hotel_dict['avg review'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[1]').inner_text()
            hotel_dict['reviews count'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[2]').inner_text()
            hotel_dict['Type']=hotel.locator('//div[@class="b5ab47188a"]/h4').inner_text()
            hotel_dict['distance to center']=hotel.locator('//div[@class="b290e5dfa6 bca66f8f42"]//span[@data-testid="distance"]').inner_text()
            hotels_list.append(hotel_dict)
           
           
           
        df=pd.DataFrame(hotels_list)
        df.to_excel('hotels_list.xlsx',index=False)
        df.to_csv('hotels_list.csv', index=False) 






        browser.close()









if __name__ == '__main__':
   main()