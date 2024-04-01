# Libraries
from bs4 import BeautifulSoup
import pandas as pd
import requests

# Lists for Storing all attributes
Seat_Rating = []
Cabin_staff_service_Rating = []
Food_Beverages_Rating = []
Inflight_Rating = []
Ground_service_Rating = []
Wifi_connectivity_Rating = []
Value_Rating = []

Review_Date = []
Rating = []
Comment = []
Reviewer_Name = []
Reviewer_Country = []
Full_review = []
Verified = []

Aircraft = []
Travel_type = []
Seat_type = []
Route = []
Date_Flown = []
Recommended = []
Airline_Name = []

companies_links_name = []

def reviewer_details_extraction(review):
    try :
        review_Date = ''
        review_Date = review.find('meta', {'itemprop': 'datePublished'}).get('content')
      #  print(f'Review_Date {review_Date}')
        Review_Date.append(review_Date)

        rating = ''
        rating = review.find('span',{'itemprop':'ratingValue'})
        if rating:
            Rating.append(rating.text)
        else:
            Rating.append(None)

        comment = ''
        comment = review.find('h2').text[:].strip() # For Removing quotes back n forth
    #    print(f'Comment:{comment}')
        Comment.append(comment)

        reviewer_Name = ''
        reviewer_Name = review.find('span',{'itemprop':'name'}).text.strip()
       # print(f'Reviewer_Name:{reviewer_Name}')
        Reviewer_Name.append(reviewer_Name)

        # Reviewer Origin Country
        reviwer_Country = ''
        country_text = review.find('h3').text
        start,end = country_text.find('('),country_text.find(')')
        reviwer_Country = country_text[start+1:end].strip()
        #print(f'Reviwer_Country:{reviwer_Country}')
        Reviewer_Country.append(reviwer_Country)

        full_review = ''
        verified = ' '
        full_review = review.find('div',{'itemprop':'reviewBody'}).text
        st = full_review[:15]

        if full_review.startswith('Not'):
            verified = 'No'
            mark = full_review.find('|')+2
            full_review = full_review[mark:]
        else:
            if st.endswith('Verified'):
                verified = 'Yes'
                mark = full_review.find('|')+2
                full_review = full_review[mark:]
            else:
                verified = 'No'
        #print(f'full_review:{full_review}')
        #print(f'Verified:{verified}')
        Full_review.append(full_review.strip())
        Verified.append(verified)
    except:
        print('Error Occured')
        
        
        
def reviewer_ratings(review):
    aircraft  = None
    travel_type = None
    seat_type = None
    route = None
    date_flown = None
    recommended = None

    for row in review.find_all('tr'):
        header_tag = row.find('td', {'class': 'review-rating-header'})
        value_tag = row.find('td', {'class': 'review-value'})

        if header_tag.text.startswith('Aircraft'):
            aircraft = value_tag.text
        elif header_tag.text.startswith('Type'):
            travel_type = value_tag.text
        elif header_tag.text.endswith('Type'):
            seat_type = value_tag.text
        elif header_tag.text.startswith('Route'):
            route = value_tag.text
        elif header_tag.text.startswith('Date'):
            date_flown = value_tag.text
        elif header_tag.text.startswith('Recommended'):
            recommended = value_tag.text.upper()

    Aircraft.append(aircraft)
    Travel_type.append(travel_type)
    Seat_type.append(seat_type)
    Route.append(route)
    Date_Flown.append(date_flown)
    Recommended.append(recommended)
    
    
def reviewer_star_ratings(review):
    seat_rating = None
    cabin_staff_service_rating = None
    food_Beverages_rating = None
    inflight_rating = None
    ground_service_rating = None
    wifi_connectivity_rating = None
    value_rating = None

    for row in review.find_all('tr'):
        star_header_tag = row.find('td', {'class': 'review-rating-header'})
        star_rating = row.find('td', {'class': 'review-rating-stars'})

        if star_header_tag.text and star_rating:
            star = star_rating.find_all('span','star fill')

            if star_header_tag.text.endswith('Comfort'):
                seat_rating = len(star)

            elif star_header_tag.text.startswith('Cabin'):
                cabin_staff_service_rating = len(star)

            elif star_header_tag.text.startswith('Food'):
                food_Beverages_rating = len(star)

            elif star_header_tag.text.startswith('Inflight'):
                inflight_rating = len(star)

            elif star_header_tag.text.startswith('Ground'):
                ground_service_rating = len(star)

            elif star_header_tag.text.startswith('Wifi'):
                wifi_connectivity_rating = len(star)

            else:
                value_rating = len(star)

    Seat_Rating.append(seat_rating)
    Cabin_staff_service_Rating.append(cabin_staff_service_rating)
    Food_Beverages_Rating.append(food_Beverages_rating)
    Inflight_Rating.append(inflight_rating)
    Ground_service_Rating.append(ground_service_rating)
    Wifi_connectivity_Rating.append(wifi_connectivity_rating)
    Value_Rating.append(value_rating)
    
    


def review_extraction(airline_url,airline_name):
    number = 1
    condition = True
    while condition:
        url = airline_url+'/page/'+str(number)
        try:
            response = requests.get(url)
            if response.status_code == 200:

                main_soup = BeautifulSoup(response.content,'html')
                all_articles_ = main_soup.find_all('article', itemprop='review')
                for review in all_articles_:
                    reviewer_details_extraction(review)
                    reviewer_ratings(review)
                    reviewer_star_ratings(review)
                    Airline_Name.append(airline_name)


                if bool(all_articles_):
                    number+=1
                else:
                    condition =False
                    print(airline_name+'Completed')
        except:
            print('Unexpected Error Occured')
            
            
base_url = 'https://www.airlinequality.com/review-pages/a-z-airline-reviews/'
response = requests.get(base_url)
main_soup = BeautifulSoup(response.content,'html')
alphabets = main_soup.find_all('div',class_='a_z_col_group')
common_url = 'https://www.airlinequality.com/'
for i in alphabets:
    ul_element = i.find_all('ul', class_='items')
    for order_list in ul_element:
        for horizontal in order_list.find_all('li'):
            for airline in horizontal:
                airline_link = airline.get('href')
                airline_name = airline.text
                #review_extraction(airline_link,airline_name)
                #print(common_url+airline_link,airline_name)
                companies_links_name.append((common_url+airline_link,airline_name))
                
                
                
# Main Function
for i in companies_links_name:
  review_extraction(i[0],i[1])
  
  

# Cross checking
print(len(Review_Date),len(Rating),len(Comment),len(Reviewer_Name),len(Reviewer_Country),len(Full_review),len(Verified))
print(len(Aircraft),len(Travel_type),len(Seat_type),len(Route),len(Date_Flown),len(Recommended))
print(len(Seat_Rating),len(Cabin_staff_service_Rating),len(Food_Beverages_Rating),len(Inflight_Rating),len(Ground_service_Rating),len(Wifi_connectivity_Rating),len(Value_Rating))

# Dataframe Creation
data_p = {
        'Airline_Name': Airline_Name,
        'Review_Date': Review_Date,
        'Rating': Rating,
        'Comment':Comment,
        'Reviewer_Name':Reviewer_Name,
        'Reviewer_Country':Reviewer_Country,
        'Verified':Verified,
        'Seat_Rating':Seat_Rating,
        'Cabin_staff_service_Rating':Cabin_staff_service_Rating,
        'Food_Beverages_Rating':Food_Beverages_Rating,
        'Inflight_Rating':Inflight_Rating,
        'Ground_service_Rating':Ground_service_Rating,
        'Wifi_connectivity_Rating':Wifi_connectivity_Rating,
        'Value_Rating':Value_Rating,
        'Full_review':Full_review
       }

df = pd.DataFrame(data_p)

df.head()