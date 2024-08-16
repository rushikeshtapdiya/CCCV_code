import streamlit as st
import pandas as pd

# Define the travel itineraries for the selected cities
itineraries = {
    "Mumbai": {
        "Adventure": {
            "Below ₹10,000": """
### Day 1: Arrival and Trekking in Sanjay Gandhi National Park
- Check in at **Hostel Stay** (₹2,000 per night).
- Explore **Sanjay Gandhi National Park** with a trek to **Kanheri Caves**.
- Dinner at **Shiv Sagar** (₹400 per person) for vegetarian cuisine.

### Day 2: Water Sports at Alibaug
- Day trip to **Alibaug** for jet skiing and parasailing.
- Packed lunch (₹300 per person).
- Return to Mumbai and relax at the hostel.

### Day 3: Beach Day at Aksa Beach and Departure
- Visit **Aksa Beach** for relaxation and beach games.
- Dinner at **Prithvi Cafe** (₹500 per person) for a relaxed atmosphere.
""",
            "₹10,000 - ₹50,000": """
### Day 1: Arrival and Adventure at Lonavala
- Check in at **The Dukes Retreat** (₹7,000 per night).
- Visit **Karla Caves** and **Bhaja Caves** for a light trek.
- Dinner at **Rama Krishna** (₹800 per person) for Indian cuisine.

### Day 2: Water Sports at Mandwa Beach
- Day trip to **Mandwa Beach** for jet skiing, kayaking, and banana boat rides.
- Lunch at **Boardwalk by Flamboyante** (₹1,500 per person).
- Return to Mumbai for the evening.

### Day 3: Adventure at EsselWorld and Water Kingdom
- Full day at **EsselWorld** and **Water Kingdom** for rides and water activities.
- Dinner at **Pizza By The Bay** (₹1,200 per person) by Marine Drive.
""",
            "₹50,000 - ₹1,00,000": """
### Day 1: Luxurious Arrival and Adventure at Matheran
- Check in at **Radisson Blu Resort & Spa Alibaug** (₹20,000 per night).
- Private guided trek in **Matheran** and exploration of **Panorama Point**.
- Dinner at **Bohemyan Blue** (₹2,500 per person) for Mediterranean cuisine.

### Day 2: Water Sports at Juhu Beach
- Experience paragliding, windsurfing, and kayaking at **Juhu Beach**.
- Lunch at **Olive Bar & Kitchen** (₹3,000 per person).
- Return to the resort for a spa session.

### Day 3: Private Yacht Cruise and Departure
- Private yacht cruise along the **Mumbai coastline**.
- Dinner at **Dome** (₹4,000 per person) at InterContinental Marine Drive for a rooftop dining experience.
""",
            "Above ₹1,00,000": """
### Day 1: Arrival and Luxury Adventure in Mumbai
- Check in at **The Taj Mahal Palace** (₹50,000 per night).
- Private helicopter ride over **Mumbai**.
- Dinner at **Masala Library** (₹5,000 per person) for molecular gastronomy.

### Day 2: Exclusive Water Sports and Yacht Experience
- Private speedboat to **Mandwa Beach** for exclusive water sports.
- Gourmet lunch at **Ziya** (₹7,000 per person) at The Oberoi.
- Return to Mumbai for a luxury yacht cruise.

### Day 3: Adventure and Departure
- Private scuba diving experience at **Tarkarli** (day trip by private jet).
- Dinner at **Wasabi by Morimoto** (₹8,000 per person) at The Taj Mahal Palace.
"""
        },
        "Sightseeing": {
            "Below ₹10,000": """
### Day 1: Arrival and City Sightseeing
- Check in at **Backpacker Panda Colaba** (₹2,500 per night).
- Visit **Gateway of India**, **Chhatrapati Shivaji Maharaj Terminus**, and **Marine Drive**.
- Dinner at **Bademiya** (₹500 per person) for street food.

### Day 2: South Mumbai Heritage Walk
- Guided walking tour of **Kala Ghoda**, **Prince of Wales Museum**, and **Flora Fountain**.
- Lunch at **Leopold Cafe** (₹800 per person).
- Visit **Haji Ali Dargah** and **Worli Sea Face**.

### Day 3: Elephanta Caves and Departure
- Ferry ride to **Elephanta Caves** with a guided tour.
- Dinner at **Cafe Mondegar** (₹600 per person) for a casual meal.
""",
            "₹10,000 - ₹50,000": """
### Day 1: Arrival and City Sightseeing
- Check in at **Fariyas Hotel Mumbai** (₹10,000 per night).
- Private guided tour of **Gateway of India**, **Colaba Causeway**, and **Marine Drive**.
- Dinner at **Indigo** (₹2,000 per person) for continental cuisine.

### Day 2: Cultural Exploration in South Mumbai
- Private tour of **Chhatrapati Shivaji Maharaj Terminus**, **Kala Ghoda**, and **Jehangir Art Gallery**.
- Lunch at **The Table** (₹2,500 per person).
- Visit **Haji Ali Dargah** and **Mahalaxmi Temple**.

### Day 3: Historical Sites and Departure
- Visit **Elephanta Caves** with a private guide.
- Dinner at **Trishna** (₹3,000 per person) for seafood specialties.
""",
            "₹50,000 - ₹1,00,000": """
### Day 1: Luxurious Arrival and City Sightseeing
- Check in at **The Oberoi Mumbai** (₹30,000 per night).
- Private chauffeured tour of **Gateway of India**, **Marine Drive**, and **Colaba**.
- Dinner at **Ziya** (₹5,000 per person) for Indian fine dining.

### Day 2: South Mumbai Heritage Tour
- Private tour of **Chhatrapati Shivaji Maharaj Terminus**, **Prince of Wales Museum**, and **Kala Ghoda**.
- Lunch at **The Table** (₹4,000 per person).
- Visit **Haji Ali Dargah** and **Worli Sea Face** with personal guide.

### Day 3: Exclusive Elephanta Caves Tour and Departure
- Private ferry to **Elephanta Caves** with a historian guide.
- Dinner at **The Tasting Room** (₹6,000 per person) for a curated experience.
""",
            "Above ₹1,00,000": """
### Day 1: Arrival and Royal Sightseeing in Mumbai
- Check in at **The St. Regis Mumbai** (₹60,000 per night).
- Exclusive helicopter tour of **Mumbai** with views of iconic landmarks.
- Dinner at **Yuuka** (₹7,000 per person) at The St. Regis for modern Japanese cuisine.

### Day 2: Private Heritage Tour
- Chauffeured tour of **Gateway of India**, **Chhatrapati Shivaji Maharaj Terminus**, and **Kala Ghoda** with historian.
- Lunch at **Wasabi by Morimoto** (₹8,000 per person) at The Taj Mahal Palace.
- Visit **Haji Ali Dargah** and **Mahalaxmi Temple** with exclusive access.

### Day 3: Luxury Elephanta Caves Tour and Departure
- Private yacht to **Elephanta Caves** with an art historian and luxury picnic.
- Dinner at **Masque** (₹10,000 per person) for a chef's tasting menu.
"""
        }
    },
    "Kashmir": {
        "Adventure": {
            "Below ₹10,000": """
### Day 1: Arrival in Srinagar and Trekking
- Check in at **Hotel Grand Habib** (₹3,000 per night).
- Trek to **Shankaracharya Temple** with panoramic views of **Dal Lake**.
- Dinner at **Krishna Vaishno Dhaba** (₹300 per person) for vegetarian cuisine.

### Day 2: Gulmarg Adventure
- Day trip to **Gulmarg** for skiing or a gondola ride.
- Packed lunch (₹300 per person).
- Return to Srinagar and relax at the hotel.

### Day 3: Pahalgam Excursion and Departure
- Day trip to **Pahalgam** for hiking and exploring **Betaab Valley**.
- Dinner at **Mughal Darbar** (₹500 per person) for Kashmiri Wazwan.
""",
            "₹10,000 - ₹50,000": """
### Day 1: Arrival in Srinagar and Shikara Ride
- Check in at **Houseboat Naaz Kashmir** (₹8,000 per night).
- Shikara ride on **Dal Lake** with a visit to **Mughal Gardens**.
- Dinner at **Ahdoos** (₹1,500 per person) for Kashmiri cuisine.

### Day 2: Gulmarg Adventure
- Day trip to **Gulmarg** for skiing and snowboarding with an instructor.
- Lunch at **Hotel Highlands Park** (₹2,000 per person).
- Return to Srinagar for the evening.

### Day 3: Pahalgam Adventure and Departure
- Day trip to **Pahalgam** for white-water rafting and horse riding.
- Dinner at **Shamyana Restaurant** (₹1,500 per person) for authentic Kashmiri dishes.
""",
            "₹50,000 - ₹1,00,000": """
### Day 1: Luxurious Arrival in Srinagar
- Check in at **The Lalit Grand Palace** (₹30,000 per night).
- Exclusive Shikara ride on **Dal Lake** with a private guide.
- Dinner at **The Chinar** (₹3,000 per person) at The Lalit for gourmet Kashmiri cuisine.

### Day 2: Exclusive Gulmarg Adventure
- Private helicopter ride to **Gulmarg** for skiing and snowboarding with a personal instructor.
- Lunch at **Khyber Himalayan Resort & Spa** (₹4,000 per person).
- Return to Srinagar for a relaxing evening.

### Day 3: Pahalgam Adventure and Departure
- Private guided trek in **Pahalgam**, including a visit to **Aru Valley**.
- Dinner at **Jade Dragon** (₹4,000 per person) at Vivanta Dal View for pan-Asian cuisine.
""",
            "Above ₹1,00,000": """
### Day 1: Arrival and Exclusive Adventure in Srinagar
- Check in at **Vivanta Dal View** (₹60,000 per night).
- Private Shikara ride on **Dal Lake** with personalized service and refreshments.
- Dinner at **Zabarwan Dining Room** (₹5,000 per person) at The Lalit Grand Palace.

### Day 2: Helicopter Adventure in Gulmarg
- Helicopter transfer to **Gulmarg** for private skiing and snowboarding lessons.
- Gourmet lunch at **Khyber Himalayan Resort & Spa** (₹6,000 per person).
- Return to Srinagar by helicopter for a spa session.

### Day 3: Exclusive Adventure in Pahalgam and Departure
- Private helicopter to **Pahalgam** for a customized hiking and fishing experience.
- Dinner at **Tuscany** (₹8,000 per person) at Vivanta Dal View for Italian fine dining.
"""
        },
        "Sightseeing": {
            "Below ₹10,000": """
### Day 1: Arrival in Srinagar and City Exploration
- Check in at **Hotel Sunshine** (₹2,500 per night).
- Visit **Mughal Gardens**: **Shalimar Bagh**, **Nishat Bagh**, and **Chashme Shahi**.
- Dinner at **Mughal Darbar** (₹500 per person) for traditional Kashmiri cuisine.

### Day 2: Day Trip to Sonamarg
- Visit **Sonamarg** to explore **Thajiwas Glacier** and scenic landscapes.
- Packed lunch (₹300 per person).
- Return to Srinagar and visit **Shankaracharya Temple**.

### Day 3: Old Srinagar City Tour and Departure
- Explore **Old Srinagar**: **Jamia Masjid**, **Shah-e-Hamdan Shrine**, and local markets.
- Dinner at **Krishna Vaishno Dhaba** (₹400 per person) for a casual meal.
""",
            "₹10,000 - ₹50,000": """
### Day 1: Arrival in Srinagar and Shikara Ride
- Check in at **Houseboat Pride of Kashmir** (₹10,000 per night).
- Shikara ride on **Dal Lake** and a visit to **Mughal Gardens**.
- Dinner at **Ahdoos** (₹2,000 per person) for Kashmiri Wazwan.

### Day 2: Full-Day Sonamarg Excursion
- Private car to **Sonamarg** for a guided tour of **Thajiwas Glacier**.
- Lunch at **Hotel Snowland** (₹1,500 per person).
- Return to Srinagar for the evening.

### Day 3: Cultural Tour in Srinagar and Departure
- Explore **Shankaracharya Temple**, **Hari Parbat**, and **Old Srinagar City**.
- Dinner at **Shamyana Restaurant** (₹1,500 per person) for a traditional feast.
""",
            "₹50,000 - ₹1,00,000": """
### Day 1: Luxurious Arrival in Srinagar
- Check in at **The Lalit Grand Palace** (₹30,000 per night).
- Exclusive Shikara ride on **Dal Lake** with a private guide.
- Dinner at **The Chinar** (₹3,000 per person) at The Lalit for gourmet Kashmiri cuisine.

### Day 2: Private Tour of Sonamarg
- Chauffeured drive to **Sonamarg** with a personal guide.
- Picnic lunch at **Thajiwas Glacier** (₹4,000 per person).
- Return to Srinagar and relax at the hotel.

### Day 3: Exclusive Srinagar Tour and Departure
- Private tour of **Mughal Gardens**, **Shankaracharya Temple**, and **Hari Parbat**.
- Dinner at **The Jade Dragon** (₹4,000 per person) for fine dining.
""",
            "Above ₹1,00,000": """
### Day 1: Arrival and Royal Sightseeing in Srinagar
- Check in at **Vivanta Dal View** (₹60,000 per night).
- Private Shikara ride on **Dal Lake** with gourmet refreshments.
- Dinner at **Tuscany** (₹5,000 per person) at Vivanta Dal View for Italian cuisine.

### Day 2: Helicopter Tour to Sonamarg
- Private helicopter tour to **Sonamarg** with a personal guide.
- Gourmet lunch at **Khyber Himalayan Resort** (₹6,000 per person).
- Return to Srinagar by helicopter for a luxury spa treatment.

### Day 3: Exclusive Cultural Tour in Srinagar and Departure
- Private guided tour of **Old Srinagar City**, **Shankaracharya Temple**, and **Hari Parbat**.
- Dinner at **Zabarwan Dining Room** (₹8,000 per person) at The Lalit Grand Palace.
"""
        }
    },
    "Kolkata": {
        "Adventure": {
            "Below ₹10,000": """
### Day 1: Arrival in Kolkata and Local Exploration
- Check in at **Hotel Broadway** (₹2,500 per night).
- Explore **Princep Ghat** and **Howrah Bridge**.
- Dinner at **Kewpie's** (₹500 per person) for traditional Bengali cuisine.

### Day 2: Day Trip to Sunderbans
- Take a day trip to **Sunderbans** for a boat safari.
- Packed lunch (₹300 per person).
- Return to Kolkata and relax at the hotel.

### Day 3: Eco Park Adventure
- Visit **Eco Park** for activities like cycling and water sports.
- Lunch at **The Astor Hotel** (₹800 per person).
- Departure from Kolkata in the evening.
""",
            "₹10,000 - ₹50,000": """
### Day 1: Arrival in Kolkata and Riverside Dinner
- Check in at **The Park Kolkata** (₹8,000 per night).
- Evening boat ride on **Hooghly River** with views of **Howrah Bridge**.
- Dinner at **The 8th Day Cafe & Bakery** (₹1,500 per person).

### Day 2: Day Trip to Sunderbans with Luxury Safari
- Private day trip to **Sunderbans** with a luxury boat safari.
- Lunch on the boat (₹1,500 per person).
- Return to Kolkata for a relaxed evening.

### Day 3: Visit to **Jorpokhir Math** and Departure
- Morning visit to **Jorpokhir Math** for scenic views and tranquility.
- Lunch at **Baan Thai** (₹2,000 per person).
- Departure from Kolkata.
""",
            "₹50,000 - ₹1,00,000": """
### Day 1: Luxurious Arrival in Kolkata
- Check in at **ITC Sonar Kolkata** (₹20,000 per night).
- Private guided tour of **Victoria Memorial** and **Indian Museum**.
- Dinner at **Dum Pukht** (₹3,000 per person) for gourmet dining.

### Day 2: Exclusive Sunderbans Experience
- Private helicopter tour to **Sunderbans** for a luxury safari.
- Gourmet lunch on the boat (₹4,000 per person).
- Return to Kolkata and enjoy a spa session at the hotel.

### Day 3: Exclusive Tour of Kolkata and Departure
- Private guided tour of **Kalighat Temple** and **Belur Math**.
- Lunch at **The Bengal Lounge** (₹4,000 per person).
- Departure from Kolkata.
""",
            "Above ₹1,00,000": """
### Day 1: Arrival and Royal Kolkata Experience
- Check in at **The Oberoi Grand** (₹60,000 per night).
- Private evening cruise on **Hooghly River** with gourmet refreshments.
- Dinner at **Baan Thai** (₹6,000 per person) for fine dining.

### Day 2: Exclusive Sunderbans Adventure
- Private luxury yacht to **Sunderbans** for an exclusive safari.
- Gourmet lunch on the yacht (₹8,000 per person).
- Return to Kolkata by private jet and enjoy a personal spa treatment.

### Day 3: Ultimate Kolkata Experience and Departure
- Private helicopter tour of **Kolkata** including **Howrah Bridge**, **Victoria Memorial**, and **Indian Museum**.
- Lunch at **Zen** (₹10,000 per person) for top-notch Asian cuisine.
- Departure from Kolkata.
"""
        },
        "Sightseeing": {
            "Below ₹10,000": """
### Day 1: Arrival in Kolkata and City Exploration
- Check in at **Hotel Cenin** (₹2,000 per night).
- Visit **Victoria Memorial**, **Indian Museum**, and **Howrah Bridge**.
- Dinner at **Oudh 1590** (₹500 per person) for Mughlai cuisine.

### Day 2: Day Trip to Sundarbans
- Day trip to **Sundarbans** for a scenic boat ride.
- Packed lunch (₹300 per person).
- Return to Kolkata and visit **Marble Palace**.

### Day 3: Old Kolkata Tour and Departure
- Explore **College Street**, **New Market**, and **Kalighat Temple**.
- Dinner at **Mocambo** (₹500 per person) for continental food.
""",
            "₹10,000 - ₹50,000": """
### Day 1: Arrival in Kolkata and Shikara Ride
- Check in at **The Peerless Inn** (₹6,000 per night).
- Shikara ride on **Rabindra Sarobar Lake** and visit **Victoria Memorial**.
- Dinner at **The Bohemian** (₹2,000 per person) for modern Bengali cuisine.

### Day 2: Full-Day Sightseeing
- Private car for a full-day tour including **Indian Museum**, **Kalighat Temple**, and **Belur Math**.
- Lunch at **The Bridge** (₹1,500 per person).
- Return to hotel for relaxation.

### Day 3: Cultural Tour and Departure
- Explore **South Park Street Cemetery** and **Jorasanko Thakur Bari**.
- Lunch at **Mughlai Restaurant** (₹1,500 per person).
- Departure from Kolkata.
""",
            "₹50,000 - ₹1,00,000": """
### Day 1: Luxurious Arrival in Kolkata
- Check in at **ITC Sonar** (₹30,000 per night).
- Exclusive guided tour of **Victoria Memorial** and **Indian Museum**.
- Dinner at **The Royal Bengal Room** (₹4,000 per person) for fine dining.

### Day 2: Private Tour and Luxury Shopping
- Private tour of **Kolkata** including **Marble Palace**, **Kalighat Temple**, and **South Park Street Cemetery**.
- Lunch at **The French Restaurant** (₹3,000 per person).
- Afternoon shopping at **Quest Mall** with a personal shopper.

### Day 3: Exclusive Cultural Experience and Departure
- Visit **Belur Math** and enjoy a private boat ride on **Hooghly River**.
- Lunch at **The Bengal Lounge** (₹5,000 per person).
- Departure from Kolkata.
""",
            "Above ₹1,00,000": """
### Day 1: Arrival and Elite Kolkata Experience
- Check in at **The Oberoi Grand** (₹60,000 per night).
- Private evening cruise on **Hooghly River** with gourmet refreshments.
- Dinner at **Baan Thai** (₹8,000 per person) for high-end dining.

### Day 2: Exclusive Sunderbans and Kolkata Tour
- Private helicopter tour to **Sunderbans** for a luxury safari.
- Gourmet lunch on the yacht (₹10,000 per person).
- Return to Kolkata and enjoy a spa session at the hotel.

### Day 3: Ultimate Kolkata Experience and Departure
- Private helicopter tour of **Kolkata** including **Victoria Memorial**, **Howrah Bridge**, and **Indian Museum**.
- Lunch at **Zen** (₹12,000 per person) for top-tier Asian cuisine.
- Departure from Kolkata.
"""
        }
    },
    "Delhi": {
        "Adventure": {
            "Below ₹10,000": """
### Day 1: Arrival in Delhi and Local Exploration
- Check in at **Hotel Godwin Deluxe** (₹3,000 per night).
- Explore **India Gate** and **Connaught Place**.
- Dinner at **Saravana Bhavan** (₹500 per person) for South Indian cuisine.

### Day 2: Adventure at Delhi’s Parks
- Visit **Adventure Island** in Rohini for amusement rides.
- Packed lunch (₹300 per person).
- Explore **Lodhi Gardens** and **Humayun's Tomb** in the evening.

### Day 3: Excursion to Aravalli Hills
- Day trip to **Sultanpur National Park** for bird watching.
- Dinner at **Rajinder Da Dhaba** (₹500 per person) for Punjabi cuisine.
""",
            "₹10,000 - ₹50,000": """
### Day 1: Arrival in Delhi and Cultural Exploration
- Check in at **The Leela Palace** (₹12,000 per night).
- Explore **Qutub Minar** and **Humayun's Tomb**.
- Dinner at **Bukhara** (₹2,000 per person) for fine dining.

### Day 2: Adventure and Shopping
- Visit **Kingdom of Dreams** for entertainment and shows.
- Lunch at **Hotel Westend** (₹1,500 per person).
- Explore **Hauz Khas Village** for nightlife and shopping.

### Day 3: Day Trip to Agra
- Private car to **Agra** to visit the **Taj Mahal** and **Agra Fort**.
- Lunch at **Peshawri** (₹2,500 per person).
- Return to Delhi for departure.
""",
            "₹50,000 - ₹1,00,000": """
### Day 1: Luxurious Arrival in Delhi
- Check in at **The Oberoi** (₹30,000 per night).
- Private guided tour of **Red Fort**, **Qutub Minar**, and **India Gate**.
- Dinner at **Mistral** (₹5,000 per person) for gourmet dining.

### Day 2: Exclusive Adventure and Luxury Shopping
- Private tour of **Kingdom of Dreams** and **Lotus Temple**.
- Lunch at **The Spice Route** (₹3,000 per person).
- Shopping at **Emporio Mall** with a personal shopper.

### Day 3: Exclusive Historical Tour and Departure
- Visit **Raj Ghat**, **Humayun’s Tomb**, and **Lodhi Gardens** with a private guide.
- Lunch at **Indian Accent** (₹6,000 per person).
- Departure from Delhi.
""",
            "Above ₹1,00,000": """
### Day 1: Arrival and Royal Delhi Experience
- Check in at **The Imperial** (₹60,000 per night).
- Private evening cruise on **Yamuna River** with gourmet refreshments.
- Dinner at **The Spice Route** (₹8,000 per person) for fine dining.

### Day 2: Exclusive Delhi and Agra Tour
- Private helicopter tour to **Agra** for a luxury visit to the **Taj Mahal** and **Agra Fort**.
- Gourmet lunch at **ITC Mughal** (₹10,000 per person).
- Return to Delhi by helicopter and enjoy a personal spa session.

### Day 3: Ultimate Delhi Experience and Departure
- Private guided tour of **Delhi** including **Red Fort**, **Raj Ghat**, and **Qutub Minar**.
- Lunch at **Tuscany** (₹12,000 per person) for Italian fine dining.
- Departure from Delhi.
"""
        },
        "Sightseeing": {
            "Below ₹10,000": """
### Day 1: Arrival in Delhi and City Tour
- Check in at **Hotel Pooja Palace** (₹2,500 per night).
- Visit **India Gate**, **Rashtrapati Bhavan**, and **Connaught Place**.
- Dinner at **The Big Chill** (₹500 per person) for continental cuisine.

### Day 2: Historical Sites
- Explore **Qutub Minar**, **Humayun's Tomb**, and **Lodhi Gardens**.
- Lunch at **Haldiram’s** (₹500 per person).
- Visit **Lotus Temple** in the evening.

### Day 3: Old Delhi Exploration and Departure
- Tour of **Red Fort**, **Jama Masjid**, and **Chandni Chowk**.
- Dinner at **Karim's** (₹500 per person) for Mughlai cuisine.
""",
            "₹10,000 - ₹50,000": """
### Day 1: Arrival in Delhi and Heritage Tour
- Check in at **Radisson Blu** (₹7,000 per night).
- Visit **Red Fort**, **Raj Ghat**, and **Jama Masjid**.
- Dinner at **Indian Accent** (₹2,000 per person) for modern Indian cuisine.

### Day 2: Cultural and Modern Delhi
- Explore **India Gate**, **Rashtrapati Bhavan**, and **Qutub Minar**.
- Lunch at **Olive Bar & Kitchen** (₹1,500 per person).
- Visit **Hauz Khas Village** for evening entertainment.

### Day 3: Shopping and Departure
- Visit **Akshardham Temple** and **Lotus Temple**.
- Lunch at **Bukhara** (₹2,000 per person).
- Departure from Delhi.
""",
            "₹50,000 - ₹1,00,000": """
### Day 1: Luxurious Arrival in Delhi
- Check in at **The Leela Palace** (₹30,000 per night).
- Private guided tour of **Red Fort**, **Qutub Minar**, and **India Gate**.
- Dinner at **Mistral** (₹4,000 per person) for gourmet cuisine.

### Day 2: Exclusive Delhi Tour
- Private tour of **Humayun's Tomb**, **Lotus Temple**, and **Raj Ghat**.
- Lunch at **The Spice Route** (₹2,500 per person).
- Evening at **Kingdom of Dreams** for a spectacular show.

### Day 3: Ultimate Delhi Experience and Departure
- Explore **Delhi** with a private guide including **Hauz Khas Village** and **Lodhi Gardens**.
- Lunch at **Indian Accent** (₹4,000 per person).
- Departure from Delhi.
""",
            "Above ₹1,00,000": """
### Day 1: Arrival and Elite Delhi Experience
- Check in at **The Oberoi** (₹60,000 per night).
- Private evening cruise on **Yamuna River** with gourmet refreshments.
- Dinner at **Tuscany** (₹10,000 per person) for high-end Italian dining.

### Day 2: Exclusive Delhi and Agra Tour
- Private helicopter tour to **Agra** to visit **Taj Mahal** and **Agra Fort**.
- Gourmet lunch at **ITC Mughal** (₹12,000 per person).
- Return to Delhi by helicopter and enjoy a spa session.

### Day 3: Ultimate Delhi Experience and Departure
- Private guided tour of **Delhi** including **Red Fort**, **Qutub Minar**, and **Humayun's Tomb**.
- Lunch at **Zen** (₹15,000 per person) for fine dining.
- Departure from Delhi.
"""
        }
    },
    "Varanasi": {
        "Adventure": {
            "Below ₹10,000": """
### Day 1: Arrival in Varanasi and River Adventure
- Check in at **Hotel Ganges Grand** (₹3,000 per night).
- Evening boat ride on the **Ganges River** to witness the **Ganga Aarti**.
- Dinner at **Keshari Restaurant** (₹500 per person) for traditional Indian cuisine.

### Day 2: Explore Ghats and Temples
- Morning boat ride from **Assi Ghat** to **Dashashwamedh Ghat**.
- Explore **Kashi Vishwanath Temple** and **Durga Temple**.
- Packed lunch (₹300 per person).
- Visit **Banaras Hindu University** and **Bharat Kala Bhavan Museum**.

### Day 3: Sarnath Excursion and Departure
- Day trip to **Sarnath** for an adventurous exploration of ancient ruins and stupas.
- Dinner at **Baati Chokha** (₹500 per person) for a taste of local cuisine.
""",
            "₹10,000 - ₹50,000": """
### Day 1: Arrival in Varanasi and Cultural Exploration
- Check in at **BrijRama Palace** (₹10,000 per night).
- Private evening boat ride on the **Ganges River** to witness the **Ganga Aarti**.
- Dinner at **The Palate** (₹1,500 per person) for fine dining with a view of the Ganges.

### Day 2: Adventure on the Ganges
- Early morning private boat ride from **Assi Ghat** with a guided tour of the **Ghats**.
- Visit **Kashi Vishwanath Temple** and **Tulsi Manas Temple**.
- Lunch at **Brown Bread Bakery** (₹1,000 per person) for organic and healthy cuisine.
- Evening exploration of **Ramnagar Fort**.

### Day 3: Sarnath and Silk Weaving Experience
- Private tour to **Sarnath** with a guided exploration of stupas and the museum.
- Visit a local silk weaving workshop to see the making of **Banarasi Silk**.
- Dinner at **Pizzeria Vaatika Café** (₹1,500 per person) for Italian cuisine with a view of the Ganges.
""",
            "₹50,000 - ₹1,00,000": """
### Day 1: Luxurious Arrival in Varanasi
- Check in at **Taj Nadesar Palace** (₹30,000 per night).
- Exclusive evening boat ride on the **Ganges River** with a private guide for the **Ganga Aarti**.
- Dinner at **Dolphin Restaurant** (₹2,500 per person) for a fine dining experience on the riverbank.

### Day 2: Exclusive Ganges Adventure and Exploration
- Private sunrise boat ride with a luxury breakfast on the boat.
- Guided tour of **Kashi Vishwanath Temple**, **Sankat Mochan Temple**, and **Durga Temple**.
- Lunch at **Varuna Restaurant** (₹2,000 per person) for authentic Indian cuisine.
- Evening visit to **Ramnagar Fort** with a private guide.

### Day 3: Private Tour of Sarnath and Departure
- Exclusive helicopter tour to **Sarnath** with a guided exploration of the archaeological sites.
- Visit a luxury silk emporium to experience the weaving of **Banarasi Silk**.
- Dinner at **The Great Kabab Factory** (₹3,500 per person) for a gourmet experience.
""",
            "Above ₹1,00,000": """
### Day 1: Royal Arrival in Varanasi
- Check in at **Taj Nadesar Palace** (₹60,000 per night).
- Exclusive evening boat ride on the **Ganges River** with a personalized **Ganga Aarti** ceremony.
- Dinner at **Taj Ganges** (₹5,000 per person) for an exquisite dining experience with royal service.

### Day 2: Helicopter and River Adventure
- Private helicopter tour over **Varanasi** for aerial views of the **Ghats** and **Temples**.
- Luxurious breakfast on the boat during a private sunrise Ganges cruise.
- Private guided tour of **Kashi Vishwanath Temple**, **Ramnagar Fort**, and **Sarnath**.
- Lunch at **Varuna Restaurant** (₹5,000 per person) for a fine dining experience.
- Evening visit to an exclusive silk weaving house with a private demonstration.

### Day 3: Cultural Immersion and Departure
- Private cultural tour including visits to **local artisan workshops**, **Banaras Hindu University**, and **Bharat Kala Bhavan Museum**.
- Dinner at **The Palate** (₹8,000 per person) for a grand farewell meal.
- Departure from Varanasi.
"""
        },
        "Sightseeing": {
            "Below ₹10,000": """
### Day 1: Arrival in Varanasi and Ghats Exploration
- Check in at **Hotel Buddha** (₹2,500 per night).
- Explore **Dashashwamedh Ghat** and **Assi Ghat**.
- Dinner at **Keshari Restaurant** (₹500 per person) for local flavors.

### Day 2: Temples and Museums
- Visit **Kashi Vishwanath Temple**, **Tulsi Manas Temple**, and **Durga Temple**.
- Lunch at **Shree Cafe** (₹400 per person).
- Explore **Banaras Hindu University** and **Bharat Kala Bhavan Museum**.
- Evening visit to **Ramnagar Fort**.

### Day 3: Sarnath and Old City Tour
- Day trip to **Sarnath** for a guided tour of the stupas and archaeological sites.
- Lunch at **Baati Chokha** (₹500 per person) for traditional food.
- Explore the **Old City** and visit local markets before departure.
""",
            "₹10,000 - ₹50,000": """
### Day 1: Arrival in Varanasi and Heritage Walk
- Check in at **BrjiRama Palace** (₹10,000 per night).
- Evening heritage walk along the **Ghats** and through the **Old City**.
- Dinner at **The Palate** (₹1,500 per person) with a view of the Ganges.

### Day 2: Comprehensive Temple and Cultural Tour
- Visit **Kashi Vishwanath Temple**, **Sankat Mochan Temple**, and **Durga Temple**.
- Lunch at **Brown Bread Bakery** (₹1,000 per person) for organic food.
- Visit **Banaras Hindu University** and **Bharat Kala Bhavan Museum**.
- Evening boat ride on the **Ganges River** for the **Ganga Aarti**.

### Day 3: Sarnath and Ramnagar Fort
- Private tour to **Sarnath** with a visit to the **Sarnath Museum**.
- Lunch at **Dolphin Restaurant** (₹1,500 per person) for riverside dining.
- Explore **Ramnagar Fort** in the afternoon.
- Departure from Varanasi.
""",
            "₹50,000 - ₹1,00,000": """
### Day 1: Luxurious Arrival in Varanasi
- Check in at **Taj Nadesar Palace** (₹30,000 per night).
- Private evening boat ride on the **Ganges River** with a guide for the **Ganga Aarti**.
- Dinner at **Dolphin Restaurant** (₹2,500 per person) for fine dining.

### Day 2: Exclusive Cultural and Temple Tour
- Private guided tour of **Kashi Vishwanath Temple**, **Tulsi Manas Temple**, and **Durga Temple**.
- Lunch at **The Great Kabab Factory** (₹3,000 per person) for gourmet Indian cuisine.
- Visit **Banaras Hindu University** and **Bharat Kala Bhavan Museum**.
- Evening exploration of **Ramnagar Fort**.

### Day 3: Sarnath and Old City Tour
- Private tour to **Sarnath** with a visit to the **Sarnath Museum** and nearby ruins.
- Lunch at **Varuna Restaurant** (₹3,000 per person) for a fine dining experience.
- Explore the **Old City** and visit local artisan workshops before departure.
""",
            "Above ₹1,00,000": """
### Day 1: Royal Arrival in Varanasi
- Check in at **Taj Nadesar Palace** (₹60,000 per night).
- Private guided evening boat ride on the **Ganges River** with an exclusive **Ganga Aarti** ceremony.
- Dinner at **Taj Ganges** (₹5,000 per person) for an exquisite dining experience.

### Day 2: Helicopter Tour and Cultural Immersion
- Private helicopter tour over **Varanasi** for aerial views of the **Ghats** and **Temples**.
- Luxurious breakfast on the boat during a private sunrise Ganges cruise.
- Private guided tour of **Kashi Vishwanath Temple**, **Ramnagar Fort**, and **Sarnath**.
- Lunch at **Varuna Restaurant** (₹5,000 per person) for a fine dining experience.
- Evening visit to an exclusive silk weaving house with a private demonstration.

### Day 3: Exclusive Old City and Cultural Tour
- Private cultural tour including visits to **local artisan workshops**, **Banaras Hindu University**, and **Bharat Kala Bhavan Museum**.
- Dinner at **The Palate** (₹8,000 per person) for a grand farewell meal.
- Departure from Varanasi.
"""
        }
    },
    "Rishikesh": {
        "Adventure": {
            "Below ₹10,000": """
### Day 1: Arrival in Rishikesh and Local Exploration
- Check in at **Shiv Shakti Hostel** (₹1,500 per night).
- Explore **Laxman Jhula** and **Ram Jhula**.
- Dinner at **Chotiwala Restaurant** (₹300 per person) for local cuisine.

### Day 2: River Rafting Adventure
- Early morning river rafting on the **Ganges River** (₹1,000 per person).
- Packed lunch (₹300 per person).
- Evening visit to **Triveni Ghat** for the **Ganga Aarti**.

### Day 3: Trekking and Departure
- Half-day trek to **Neer Garh Waterfall** (₹500 per person).
- Return to Rishikesh and departure.
""",
            "₹10,000 - ₹50,000": """
### Day 1: Arrival in Rishikesh and Ashram Visit
- Check in at **Ganga Kinare - A Riverside Boutique Hotel** (₹6,000 per night).
- Visit **Parmarth Niketan Ashram** and **Sivananda Ashram**.
- Dinner at **The Sitting Elephant** (₹1,000 per person) for a riverside dining experience.

### Day 2: Rafting and Bungee Jumping Adventure
- River rafting on the **Ganges River** with a professional guide (₹2,000 per person).
- Bungee jumping at **Jumpin Heights** (₹3,500 per person).
- Lunch at **Free Spirit Café** (₹800 per person).
- Evening relaxation at the hotel.

### Day 3: Yoga, Trekking, and Departure
- Morning yoga session at the hotel (₹1,000 per person).
- Trek to **Patna Waterfall** and explore the surrounding nature (₹1,000 per person).
- Return to Rishikesh and departure.
""",
            "₹50,000 - ₹1,00,000": """
### Day 1: Luxurious Arrival in Rishikesh
- Check in at **Ananda in the Himalayas** (₹30,000 per night).
- Personalized yoga and meditation session at the resort.
- Dinner at **The Pavilion** (₹2,500 per person) for fine dining with a Himalayan view.

### Day 2: Exclusive Rafting and Adventure
- Private river rafting experience on the **Ganges River** (₹5,000 per person).
- Bungee jumping at **Jumpin Heights** with personalized service (₹3,500 per person).
- Lunch at **60’s Café Delmar/Beatles Café** (₹2,000 per person).
- Spa treatment at **Ananda Spa** in the evening.

### Day 3: Private Trekking and Departure
- Exclusive guided trek to **Kunjapuri Temple** for sunrise (₹5,000 per person).
- Return to the resort for a late breakfast and relaxation.
- Departure from Rishikesh.
""",
            "Above ₹1,00,000": """
### Day 1: Arrival and Ultra-Luxury in Rishikesh
- Check in at **Ananda in the Himalayas** (₹60,000 per night).
- Private yoga and wellness consultation followed by personalized sessions.
- Dinner at **Tree Top Deck** (₹5,000 per person) for an exclusive dining experience amidst nature.

### Day 2: Helicopter Adventure and Exclusive Rafting
- Helicopter transfer to the **Ganges River** for a private rafting adventure (₹10,000 per person).
- Gourmet picnic lunch by the river (₹5,000 per person).
- Afternoon helicopter tour of **Rishikesh** and the surrounding Himalayas.
- Return to the resort for an evening spa session.

### Day 3: Private Cultural and Nature Tour
- Private guided tour of **Rishikesh**, including visits to **ashrams**, **temples**, and **local artisan workshops**.
- Lunch at **The Pavilion** (₹5,000 per person) for a gourmet experience.
- Exclusive guided trek or nature walk in the Himalayas.
- Departure from Rishikesh.
"""
        },
        "Sightseeing": {
            "Below ₹10,000": """
### Day 1: Arrival in Rishikesh and Ghat Exploration
- Check in at **Divine Ganga Cottage** (₹2,500 per night).
- Explore **Laxman Jhula** and **Ram Jhula**.
- Dinner at **Chotiwala Restaurant** (₹300 per person) for local flavors.

### Day 2: Temple and Ashram Tour
- Visit **Parmarth Niketan Ashram** and **Sivananda Ashram**.
- Lunch at **The Ganga View Café** (₹400 per person).
- Explore **Triveni Ghat** and attend the **Ganga Aarti** in the evening.

### Day 3: Waterfall Visit and Departure
- Morning visit to **Neer Garh Waterfall** for a short trek and nature experience.
- Return to Rishikesh and explore local markets before departure.
""",
            "₹10,000 - ₹50,000": """
### Day 1: Arrival in Rishikesh and Riverside Walk
- Check in at **Ganga Kinare - A Riverside Boutique Hotel** (₹6,000 per night).
- Evening walk along the **Ganges River** and explore **Rishikesh Market**.
- Dinner at **The Sitting Elephant** (₹1,000 per person) for a riverside dining experience.

### Day 2: Ashram and Temple Tour
- Visit **Parmarth Niketan Ashram**, **Sivananda Ashram**, and **Neelkanth Mahadev Temple**.
- Lunch at **Pure Soul Café** (₹1,000 per person) for a healthy and organic meal.
- Attend the **Ganga Aarti** at **Triveni Ghat** in the evening.

### Day 3: Scenic Excursion and Departure
- Morning visit to **Kunjapuri Temple** for sunrise views.
- Lunch at **Free Spirit Café** (₹800 per person).
- Explore the **Beatles Ashram** (Chaurasi Kutia) before departure.
""",
            "₹50,000 - ₹1,00,000": """
### Day 1: Luxurious Arrival in Rishikesh
- Check in at **Ananda in the Himalayas** (₹30,000 per night).
- Evening yoga and meditation session at the resort.
- Dinner at **The Pavilion** (₹2,500 per person) for fine dining with a Himalayan view.

### Day 2: Private Sightseeing and Wellness Experience
- Private guided tour of **Rishikesh**, including **Laxman Jhula**, **Ram Jhula**, and **Parmarth Niketan**.
- Lunch at **60’s Café Delmar/Beatles Café** (₹2,000 per person).
- Afternoon visit to **Neelkanth Mahadev Temple** with a private guide.
- Evening spa and wellness session at **Ananda Spa**.

### Day 3: Exclusive Cultural and Nature Exploration
- Private sunrise trek to **Kunjapuri Temple** (₹5,000 per person).
- Return to the resort for breakfast and relaxation.
- Guided visit to the **Beatles Ashram** (Chaurasi Kutia).
- Departure from Rishikesh.
""",
            "Above ₹1,00,000": """
### Day 1: Arrival and Ultra-Luxury Stay in Rishikesh
- Check in at **Ananda in the Himalayas** (₹60,000 per night).
- Private wellness consultation and personalized yoga sessions.
- Dinner at **Tree Top Deck** (₹5,000 per person) for a unique dining experience amidst nature.

### Day 2: Helicopter Sightseeing and Cultural Immersion
- Helicopter tour of **Rishikesh** and the **Himalayas** for breathtaking views (₹10,000 per person).
- Private guided tour of **ashrams** and **temples** including **Parmarth Niketan** and **Sivananda Ashram**.
- Lunch at **The Pavilion** (₹5,000 per person) for a gourmet meal.
- Evening exclusive Ganga Aarti experience at **Triveni Ghat**.

### Day 3: Private Trekking and Departure
- Guided sunrise trek to **Kunjapuri Temple** with luxurious breakfast upon return.
- Private visit to **Neelkanth Mahadev Temple** and **Beatles Ashram**.
- Departure from Rishikesh.
"""
        }
    },
    "Munnar": {
        "Adventure": {
            "Below ₹10,000": """
### Day 1: Arrival in Munnar and Short Trek
- Check in at **Zina Cottages** (₹2,500 per night).
- Short trek to **Pothamedu Viewpoint** for panoramic views of the tea plantations.
- Dinner at **Rapsy Restaurant** (₹300 per person) for traditional Kerala cuisine.

### Day 2: Anamudi Peak Trekking
- Early morning trek to **Anamudi Peak**, the highest peak in South India (₹1,000 per person).
- Packed lunch (₹300 per person).
- Return to Munnar and relax at the hotel.

### Day 3: Attukal Waterfalls and Departure
- Visit **Attukal Waterfalls** for a short trek and explore the surrounding nature.
- Departure from Munnar.
""",
            "₹10,000 - ₹50,000": """
### Day 1: Arrival in Munnar and Plantation Walk
- Check in at **Tea County Munnar** (₹6,000 per night).
- Guided walk through **Kolukkumalai Tea Estate**, the highest tea plantation in the world (₹1,500 per person).
- Dinner at **Saravana Bhavan** (₹800 per person) for authentic South Indian cuisine.

### Day 2: Adventure at Chokramudi Peak
- Early morning trek to **Chokramudi Peak** with stunning views of the surrounding hills and valleys (₹2,000 per person).
- Lunch at **Sandal Breeze Hotel** (₹1,200 per person).
- Evening relaxation at the hotel or a stroll through the town.

### Day 3: Mountain Biking and Departure
- Morning mountain biking adventure through the **tea plantations** (₹2,000 per person).
- Return to the hotel for breakfast and relaxation.
- Departure from Munnar.
""",
            "₹50,000 - ₹1,00,000": """
### Day 1: Luxurious Arrival in Munnar
- Check in at **Windermere Estate** (₹20,000 per night).
- Private guided tour of **Kolukkumalai Tea Estate** with tea tasting (₹5,000 per person).
- Dinner at **The Silver Tips** (₹3,000 per person) for a fusion dining experience.

### Day 2: Private Trekking and Wildlife Safari
- Exclusive trekking experience to **Meesapulimala** with a private guide (₹10,000 per person).
- Gourmet picnic lunch in the hills (₹3,000 per person).
- Evening wildlife safari in **Eravikulam National Park** (₹5,000 per person).
- Return to the hotel for relaxation and a spa session.

### Day 3: Scenic Exploration and Departure
- Morning visit to **Top Station** for breathtaking views and a guided nature walk (₹5,000 per person).
- Return to the hotel for breakfast and leisure.
- Departure from Munnar.
""",
            "Above ₹1,00,000": """
### Day 1: Ultra-Luxury Arrival in Munnar
- Check in at **SpiceTree Munnar** (₹40,000 per night).
- Exclusive private tour of **Kolukkumalai Tea Estate** with helicopter transfer (₹15,000 per person).
- Dinner at **T&U Leisure Hotel** (₹5,000 per person) for gourmet Kerala cuisine.

### Day 2: Helicopter Trekking and Wildlife Adventure
- Helicopter ride to **Meesapulimala** for a private trekking experience (₹20,000 per person).
- Gourmet picnic lunch with a view of the valleys (₹5,000 per person).
- Private wildlife safari in **Eravikulam National Park** with a naturalist guide (₹10,000 per person).
- Return to the hotel for a luxury spa treatment.

### Day 3: Exclusive Scenic Tour and Departure
- Private helicopter tour of **Top Station** and the surrounding areas (₹20,000 per person).
- Return to the hotel for a lavish breakfast.
- Departure from Munnar.
"""
        },
        "Sightseeing": {
            "Below ₹10,000": """
### Day 1: Arrival in Munnar and Local Exploration
- Check in at **Green View Munnar** (₹2,000 per night).
- Explore **Munnar Tea Museum** and learn about the history of tea production.
- Dinner at **Rapsy Restaurant** (₹300 per person) for local cuisine.

### Day 2: Scenic Sightseeing Tour
- Visit **Mattupetty Dam**, **Echo Point**, and **Kundala Lake** for a day of scenic exploration.
- Packed lunch by the lake (₹300 per person).
- Return to Munnar for an evening stroll in the town.

### Day 3: Eravikulam National Park and Departure
- Morning visit to **Eravikulam National Park** to see the endangered **Nilgiri Tahr** and enjoy the lush landscapes.
- Return to the hotel for breakfast.
- Departure from Munnar.
""",
            "₹10,000 - ₹50,000": """
### Day 1: Arrival in Munnar and Tea Garden Visit
- Check in at **Tea Valley Resort** (₹8,000 per night).
- Visit **Kolukkumalai Tea Estate** for a guided tour and tea tasting experience (₹1,500 per person).
- Dinner at **Saravana Bhavan** (₹800 per person) for a traditional meal.

### Day 2: Full-Day Sightseeing Tour
- Visit **Mattupetty Dam**, **Echo Point**, **Kundala Lake**, and **Top Station**.
- Lunch at **Sandal Breeze Hotel** (₹1,200 per person).
- Explore **Munnar Tea Museum** in the evening.
- Return to the hotel for dinner and relaxation.

### Day 3: Scenic Exploration and Departure
- Early morning visit to **Eravikulam National Park** for a wildlife experience.
- Return to the hotel for breakfast.
- Departure from Munnar.
""",
            "₹50,000 - ₹1,00,000": """
### Day 1: Luxurious Arrival in Munnar
- Check in at **SpiceTree Munnar** (₹20,000 per night).
- Private guided tour of **Kolukkumalai Tea Estate** with a tea masterclass (₹5,000 per person).
- Dinner at **The Silver Tips** (₹3,000 per person) for a fine dining experience.

### Day 2: Private Sightseeing and Cultural Tour
- Chauffeured tour of **Mattupetty Dam**, **Echo Point**, and **Kundala Lake**.
- Gourmet picnic lunch at **Top Station** (₹3,000 per person).
- Visit **Munnar Tea Museum** for a private tour.
- Return to the hotel for a spa session and evening relaxation.

### Day 3: Exclusive Wildlife and Departure
- Private visit to **Eravikulam National Park** with a personal naturalist guide (₹5,000 per person).
- Return to the hotel for a leisurely breakfast.
- Departure from Munnar.
""",
            "Above ₹1,00,000": """
### Day 1: Ultra-Luxury Arrival in Munnar
- Check in at **SpiceTree Munnar** (₹40,000 per night).
- Helicopter transfer to **Kolukkumalai Tea Estate** for a private tour and tasting (₹15,000 per person).
- Dinner at **T&U Leisure Hotel** (₹5,000 per person) for a gourmet Kerala feast.

### Day 2: Helicopter Sightseeing and Cultural Immersion
- Private helicopter tour of **Munnar** including **Mattupetty Dam**, **Echo Point**, and **Top Station** (₹20,000 per person).
- Exclusive cultural experience with a visit to a local village and tea factory.
- Return to the hotel for a luxury spa treatment.
- Dinner at **Tree House Restaurant** (₹5,000 per person) for a unique dining experience.

### Day 3: Private Wildlife and Departure
- Helicopter transfer to **Eravikulam National Park** for a private safari with a naturalist guide (₹10,000 per person).
- Return to the hotel for a lavish breakfast.
- Departure from Munnar.
"""
        }
    },
    "Bangalore": {
        "Adventure": {
            "Below ₹10,000": """
### Day 1: Arrival in Bangalore and Nandi Hills Trek
- Check in at **Treebo Trend Hotel** (₹2,500 per night).
- Early morning drive to **Nandi Hills** for a sunrise trek.
- Breakfast at a local café (₹300 per person).
- Evening visit to **Cubbon Park** for a walk or cycling.
- Dinner at **Vidyarthi Bhavan** (₹300 per person) for traditional South Indian cuisine.

### Day 2: Savandurga Trek and Adventure Activities
- Early morning trek to **Savandurga**, one of Asia's largest monolith hills (₹1,000 per person for guide).
- Packed lunch (₹300 per person).
- Afternoon adventure activities at **XtremeZone** (₹1,500 per person) for zip-lining and kayaking.
- Return to Bangalore and relax at the hotel.

### Day 3: Cycling and Departure
- Morning cycling tour of **Bangalore Palace** and **Ulsoor Lake** (₹1,000 per person).
- Breakfast at **Koshy’s** (₹400 per person).
- Departure from Bangalore.
""",
            "₹10,000 - ₹50,000": """
### Day 1: Arrival in Bangalore and Rock Climbing at Ramanagara
- Check in at **The Chancery Pavilion** (₹7,000 per night).
- Drive to **Ramanagara** for a rock climbing session (₹3,000 per person).
- Lunch at **Namma Ooru** (₹1,000 per person).
- Evening stroll at **Lalbagh Botanical Garden**.
- Dinner at **Karavalli** (₹2,000 per person) for coastal cuisine.

### Day 2: Adventure at Bannerghatta and Microlight Flying
- Morning safari and adventure activities at **Bannerghatta National Park** (₹2,000 per person).
- Packed lunch (₹500 per person).
- Experience microlight flying at **Jakkur Aerodrome** (₹5,000 per person).
- Return to the hotel for relaxation and dinner at **Ebony** (₹2,000 per person).

### Day 3: Biking Tour and Departure
- Morning biking tour of **Nandi Hills** with a guide (₹3,000 per person).
- Return to Bangalore for breakfast at **MTR** (₹800 per person).
- Departure from Bangalore.
""",
            "₹50,000 - ₹1,00,000": """
### Day 1: Luxurious Arrival in Bangalore and Adventure at Ramanagara
- Check in at **The Oberoi** (₹25,000 per night).
- Private guided rock climbing session at **Ramanagara** (₹10,000 per person).
- Gourmet lunch at **JW Kitchen** (₹3,000 per person).
- Evening visit to **Lalbagh Botanical Garden** for a private guided tour.
- Dinner at **The Lantern** (₹4,000 per person) at The Ritz-Carlton for a fine dining experience.

### Day 2: Exclusive Wildlife Safari and Helicopter Tour
- Private morning safari at **Bannerghatta National Park** with a naturalist guide (₹15,000 per person).
- Lunch at **Grasshopper** (₹3,000 per person).
- Exclusive helicopter tour of Bangalore and nearby attractions (₹20,000 per person).
- Return to the hotel for a spa session and relaxation.
- Dinner at **The Royal Afghan** (₹4,000 per person) at ITC Windsor for North-West Frontier cuisine.

### Day 3: Personalized Adventure and Departure
- Personalized adventure experience, choosing between a private cycling tour of **Nandi Hills** or a microlight flying experience.
- Gourmet breakfast at the hotel.
- Departure from Bangalore.
""",
            "Above ₹1,00,000": """
### Day 1: Ultra-Luxury Arrival in Bangalore and Exclusive Rock Climbing
- Check in at **The Ritz-Carlton** (₹60,000 per night).
- Private helicopter transfer to **Ramanagara** for a customized rock climbing experience with a professional guide (₹25,000 per person).
- Gourmet lunch at **Toscano** (₹5,000 per person).
- Evening private tour of **Lalbagh Botanical Garden** with a horticulturist.
- Dinner at **Alba** (₹6,000 per person) at JW Marriott for Italian fine dining.

### Day 2: Helicopter Safari and Luxury Adventure
- Helicopter transfer to **Bannerghatta National Park** for an exclusive wildlife safari with a personal guide (₹50,000 per person).
- Picnic lunch arranged by **Leela Palace** (₹10,000 per person).
- Helicopter tour of Bangalore and nearby hills.
- Return to the hotel for a luxury spa session and relaxation.
- Dinner at **The Lantern** (₹8,000 per person) for an exquisite culinary experience.

### Day 3: Exclusive Personalized Adventure and Departure
- Personalized adventure experience with options for a private biking tour, microlight flying, or a hot air balloon ride.
- Gourmet breakfast at **The Ritz-Carlton**.
- Departure from Bangalore.
"""
        },
        "Sightseeing": {
            "Below ₹10,000": """
### Day 1: Arrival in Bangalore and City Highlights
- Check in at **Treebo Trend Hotel** (₹2,500 per night).
- Visit **Cubbon Park** and **Bangalore Palace**.
- Lunch at **Vidyarthi Bhavan** (₹300 per person).
- Explore **Lalbagh Botanical Garden** in the evening.
- Dinner at **Rameshwaram Café** (₹500 per person) for South Indian specialties.

### Day 2: Full-Day Sightseeing Tour
- Morning visit to **ISKCON Temple** and **Bull Temple**.
- Lunch at **Mavalli Tiffin Room (MTR)** (₹600 per person).
- Explore **Tipu Sultan’s Summer Palace** and **Visvesvaraya Industrial and Technological Museum**.
- Evening visit to **Commercial Street** for shopping.
- Dinner at **Konark Vegetarian Restaurant** (₹800 per person).

### Day 3: Historical Tour and Departure
- Morning visit to **Nandi Hills** for a historical tour and sunrise view.
- Return to Bangalore for breakfast at **Koshy’s** (₹500 per person).
- Departure from Bangalore.
""",
            "₹10,000 - ₹50,000": """
### Day 1: Arrival in Bangalore and Cultural Exploration
- Check in at **The Chancery Pavilion** (₹7,000 per night).
- Visit **Bangalore Palace** and **Vidhana Soudha**.
- Lunch at **Mavalli Tiffin Room (MTR)** (₹800 per person).
- Explore **Lalbagh Botanical Garden** with a private guide.
- Dinner at **Karavalli** (₹2,000 per person) for coastal cuisine.

### Day 2: Full-Day Sightseeing and Shopping
- Morning visit to **ISKCON Temple** and **Bull Temple**.
- Lunch at **Ebony** (₹1,500 per person) for a rooftop dining experience.
- Explore **Tipu Sultan’s Summer Palace** and **Ulsoor Lake**.
- Evening shopping at **Commercial Street**.
- Dinner at **The Only Place** (₹1,500 per person) for continental cuisine.

### Day 3: Historical and Cultural Tour and Departure
- Morning visit to **Nandi Hills** for a historical tour with a guide.
- Return to Bangalore for breakfast at **Koshy’s** (₹800 per person).
- Departure from Bangalore.
""",
            "₹50,000 - ₹1,00,000": """
### Day 1: Luxurious Arrival in Bangalore and Private City Tour
- Check in at **The Oberoi** (₹25,000 per night).
- Private guided tour of **Bangalore Palace**, **Vidhana Soudha**, and **Cubbon Park**.
- Lunch at **Rim Naam** (₹3,000 per person) at The Oberoi for an exquisite dining experience.
- Evening visit to **Lalbagh Botanical Garden** with a private horticulturist guide.
- Dinner at **The Lantern** (₹4,000 per person) at The Ritz-Carlton for fine dining.

### Day 2: Exclusive Sightseeing and Cultural Immersion
- Morning visit to **ISKCON Temple** and **Bull Temple** with a private guide.
- Lunch at **The Royal Afghan** (₹4,000 per person) at ITC Windsor.
- Private tour of **Tipu Sultan’s Summer Palace** and **Visvesvaraya Industrial and Technological Museum**.
- Evening shopping at **UB City Mall** with a personal shopper.
- Dinner at **Alba** (₹4,000 per person) at JW Marriott.

### Day 3: Historical Exploration and Departure
- Private guided tour to **Nandi Hills** for a historical experience.
- Return to Bangalore for breakfast at **The Oberoi**.
- Departure from Bangalore.
""",
            "Above ₹1,00,000": """
### Day 1: Ultra-Luxury Arrival in Bangalore and Exclusive Sightseeing
- Check in at **The Ritz-Carlton** (₹60,000 per night).
- Private helicopter tour of **Bangalore Palace**, **Vidhana Soudha**, and **Cubbon Park** (₹25,000 per person).
- Gourmet lunch at **Toscano** (₹5,000 per person).
- Evening exclusive tour of **Lalbagh Botanical Garden** with a horticulturist.
- Dinner at **Alba** (₹8,000 per person) at JW Marriott for an Italian fine dining experience.

### Day 2: Personalized Cultural and Shopping Experience
- Personalized private tour of **ISKCON Temple** and **Bull Temple**.
- Lunch at **The Lantern** (₹6,000 per person) at The Ritz-Carlton.
- Private guided visit to **Tipu Sultan’s Summer Palace** and **Visvesvaraya Industrial and Technological Museum**.
- Evening shopping at **UB City Mall** with a personal shopper and stylist.
- Dinner at **The Lantern** (₹8,000 per person).

### Day 3: Exclusive Historical Tour and Departure
- Private helicopter transfer to **Nandi Hills** for a personalized historical tour (₹30,000 per person).
- Return to Bangalore for a gourmet breakfast at **The Ritz-Carlton**.
- Departure from Bangalore.
"""
        }
    },
    "Shimla": {
        "Adventure": {
            "Below ₹10,000": """
### Day 1: Arrival in Shimla and Kufri Adventure
- Check in at **Hotel Willow Banks** (₹3,000 per night).
- Visit **Kufri** for adventure activities like horse riding and tobogganing (₹500 per person).
- Lunch at a local dhaba (₹400 per person).
- Evening walk on **Mall Road** and **The Ridge**.
- Dinner at **Ashiana & Goofa** (₹500 per person) for North Indian cuisine.

### Day 2: Jakhu Temple Trek and Mashobra Exploration
- Early morning trek to **Jakhu Temple** for panoramic views of Shimla.
- Breakfast at **Indian Coffee House** (₹200 per person).
- Day trip to **Mashobra** for zip-lining and rappelling (₹1,500 per person).
- Packed lunch (₹300 per person).
- Return to Shimla and relax at the hotel.
- Dinner at **Himani Sweets** (₹500 per person).

### Day 3: Tattapani Adventure and Departure
- Early morning drive to **Tattapani** for white-water rafting (₹2,000 per person).
- Visit the hot springs before returning to Shimla.
- Departure from Shimla.
""",
            "₹10,000 - ₹50,000": """
### Day 1: Arrival in Shimla and Kufri Adventure
- Check in at **Radisson Hotel Shimla** (₹8,000 per night).
- Private car to **Kufri** for skiing and horse riding (₹2,000 per person).
- Lunch at **Café Simla Times** (₹1,500 per person).
- Evening stroll on **Mall Road** and **The Ridge**.
- Dinner at **Eighteen71 Cookhouse & Bar** (₹2,000 per person) for multi-cuisine options.

### Day 2: Jakhu Temple Trek and Chail Adventure
- Morning trek to **Jakhu Temple** with a guide.
- Breakfast at **Wake & Bake Café** (₹800 per person).
- Day trip to **Chail** for trekking and exploring the **Chail Palace**.
- Packed lunch (₹1,000 per person).
- Return to Shimla and relax at the hotel.
- Dinner at **The Restaurant** (₹2,500 per person) at The Oberoi Cecil.

### Day 3: Tattapani Adventure and Departure
- Drive to **Tattapani** for white-water rafting and paragliding (₹3,000 per person).
- Visit the hot springs before returning to Shimla.
- Departure from Shimla.
""",
            "₹50,000 - ₹1,00,000": """
### Day 1: Luxurious Arrival in Shimla and Kufri Adventure
- Check in at **Wildflower Hall, An Oberoi Resort** (₹25,000 per night).
- Chauffeured drive to **Kufri** for skiing and yak rides (₹5,000 per person).
- Gourmet lunch at **The Restaurant** at Wildflower Hall (₹3,000 per person).
- Evening private tour of **Mall Road** and **The Ridge**.
- Dinner at **The Oberoi Cecil** (₹4,000 per person) for a fine dining experience.

### Day 2: Exclusive Trekking and Chail Adventure
- Private guided trek to **Jakhu Temple**.
- Breakfast at **Wake & Bake Café** (₹1,000 per person).
- Day trip to **Chail** with a personal guide for hiking and visiting **Chail Palace**.
- Packed gourmet lunch (₹2,000 per person).
- Return to the resort for a spa session.
- Dinner at **Café Sol** (₹3,000 per person) for Continental cuisine.

### Day 3: Private Adventure at Tattapani and Departure
- Chauffeured drive to **Tattapani** for exclusive white-water rafting and paragliding (₹8,000 per person).
- Visit the hot springs before returning to Shimla.
- Departure from Shimla.
""",
            "Above ₹1,00,000": """
### Day 1: Ultra-Luxury Arrival in Shimla and Exclusive Kufri Adventure
- Check in at **Wildflower Hall, An Oberoi Resort** (₹60,000 per night).
- Private helicopter transfer to **Kufri** for an exclusive skiing experience with a personal instructor (₹20,000 per person).
- Gourmet lunch at **The Restaurant** at Wildflower Hall (₹5,000 per person).
- Private guided evening tour of **Mall Road** and **The Ridge**.
- Dinner at **The Oberoi Cecil** (₹6,000 per person) for a luxurious dining experience.

### Day 2: Helicopter Tour and Chail Adventure
- Private helicopter tour of **Jakhu Temple** and **Chail**.
- Gourmet breakfast at **Wildflower Hall**.
- Exclusive hiking experience in **Chail** with a personal guide and gourmet picnic lunch (₹10,000 per person).
- Return to the resort for a personalized spa session.
- Dinner at **Café Sol** (₹6,000 per person) for an upscale dining experience.

### Day 3: Exclusive Tattapani Adventure and Departure
- Helicopter transfer to **Tattapani** for a luxury white-water rafting and paragliding experience (₹15,000 per person).
- Visit the hot springs with a private guide before returning to Shimla.
- Departure from Shimla.
"""
        },
        "Sightseeing": {
            "Below ₹10,000": """
### Day 1: Arrival in Shimla and Mall Road Exploration
- Check in at **Hotel Willow Banks** (₹3,000 per night).
- Explore **Mall Road**, **The Ridge**, and **Christ Church**.
- Lunch at **Himani Sweets** (₹400 per person).
- Visit **Lakkar Bazaar** for local handicrafts shopping.
- Dinner at **Ashiana & Goofa** (₹500 per person) for North Indian cuisine.

### Day 2: Kufri and Shimla Heritage Walk
- Morning visit to **Kufri** for sightseeing and horse riding (₹1,000 per person).
- Breakfast at a local café (₹300 per person).
- Return to Shimla for a heritage walk, including **Viceregal Lodge** and **Gorton Castle**.
- Packed lunch (₹400 per person).
- Evening visit to **Jakhu Temple**.
- Dinner at **Seventh Heaven** (₹800 per person).

### Day 3: Mashobra and Departure
- Day trip to **Mashobra** for nature walks and scenic views.
- Breakfast at **Wake & Bake Café** (₹400 per person).
- Return to Shimla and visit **The Mall** for a last-minute stroll.
- Departure from Shimla.
""",
            "₹10,000 - ₹50,000": """
### Day 1: Arrival in Shimla and Heritage Walk
- Check in at **Radisson Hotel Shimla** (₹8,000 per night).
- Explore **Mall Road**, **The Ridge**, and **Christ Church**.
- Lunch at **Café Simla Times** (₹1,500 per person).
- Visit **Viceregal Lodge** and **Gaiety Theatre**.
- Dinner at **Eighteen71 Cookhouse & Bar** (₹2,000 per person) for multi-cuisine options.

### Day 2: Full-Day Kufri and Naldehra Sightseeing
- Morning visit to **Kufri** for sightseeing and horse riding (₹2,000 per person).
- Breakfast at **Wake & Bake Café** (₹800 per person).
- Drive to **Naldehra** for a visit to the golf course and nature walks.
- Lunch at **The Restaurant** (₹2,000 per person) at The Oberoi Cecil.
- Return to Shimla for an evening at leisure.
- Dinner at **The Oberoi Cecil** (₹2,500 per person) for a fine dining experience.

### Day 3: Mashobra and Departure
- Day trip to **Mashobra** with a private guide for a nature walk and picnic (₹2,500 per person).
- Breakfast at **Café Sol** (₹1,000 per person).
- Return to Shimla and departure.
""",
            "₹50,000 - ₹1,00,000": """
### Day 1: Luxurious Arrival in Shimla and Private City Tour
- Check in at **Wildflower Hall, An Oberoi Resort** (₹25,000 per night).
- Private guided tour of **Mall Road**, **The Ridge**, and **Christ Church**.
- Lunch at **The Restaurant** at Wildflower Hall (₹3,000 per person).
- Visit **Viceregal Lodge** with a private historian guide.
- Dinner at **The Oberoi Cecil** (₹4,000 per person) for a fine dining experience.

### Day 2: Exclusive Kufri and Naldehra Sightseeing
- Private car to **Kufri** for a sightseeing tour and yak ride (₹5,000 per person).
- Gourmet breakfast at **The Restaurant** (₹1,500 per person).
- Drive to **Naldehra** for a private tour of the golf course and scenic areas.
- Gourmet lunch at **The Restaurant** (₹3,000 per person) at The Oberoi Cecil.
- Return to Shimla for a relaxing evening at the resort.
- Dinner at **Café Sol** (₹3,000 per person) for an upscale dining experience.

### Day 3: Exclusive Mashobra Tour and Departure
- Chauffeured drive to **Mashobra** with a private guide for an exclusive nature walk and gourmet picnic lunch (₹8,000 per person).
- Return to Shimla for a final evening at the resort.
- Departure from Shimla.
""",
            "Above ₹1,00,000": """
### Day 1: Ultra-Luxury Arrival in Shimla and Private Tour
- Check in at **Wildflower Hall, An Oberoi Resort** (₹60,000 per night).
- Private guided tour of **Mall Road**, **The Ridge**, and **Christ Church** with a historian guide.
- Gourmet lunch at **The Restaurant** at Wildflower Hall (₹5,000 per person).
- Exclusive tour of **Viceregal Lodge** and **Gaiety Theatre**.
- Dinner at **The Oberoi Cecil** (₹6,000 per person) for a luxurious dining experience.

### Day 2: Helicopter Tour of Kufri and Naldehra
- Private helicopter tour to **Kufri** for an exclusive sightseeing experience (₹20,000 per person).
- Gourmet breakfast at **Wildflower Hall**.
- Helicopter transfer to **Naldehra** for a private tour of the golf course and scenic areas with a personal guide.
- Gourmet picnic lunch at Naldehra (₹10,000 per person).
- Return to Shimla by helicopter and enjoy a spa session.
- Dinner at **Café Sol** (₹6,000 per person) for an upscale dining experience.

### Day 3: Exclusive Mashobra Tour and Departure
- Helicopter transfer to **Mashobra** for an exclusive nature walk and gourmet picnic lunch (₹15,000 per person).
- Return to Shimla for a final evening at the resort.
- Departure from Shimla.
"""
        }
    }
}



# Streamlit app
st.set_page_config(page_title="Travel Itinerary", page_icon="✈️")


# Display the logo at the top of the page
logo_url = 'https://path_to_your_logo/logo.png'  # Replace with your logo URL
st.image("travelmate_logo_transparent-removebg-preview.png", use_column_width=True)
st.title("Personalized Travel Solutions")

# Login functionality
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.logged_in = True
if not st.session_state.logged_in:
    st.header("Login")
    username = st.text_input("Username", "")
    password = st.text_input("Password", "", type="password")

    if st.button("Login"):
        if username == "user" and password == "pass":
            st.success("Login successful!")
            st.session_state.logged_in = True
        else:
            st.error("Invalid username or password.")
else:
    # Logged-in users can access the itinerary
    st.header("Welcome to the Itinerary Generator",divider = True )

    # User preferences
    st.subheader("Your Default Preferences Based on History",divider=True)
    st.write("Age: 25")
    st.write("Interests: Adventure, Sightseeing")
    st.write("Budget: ₹10,000 - ₹50,000")
    
    st.write("You can change your preferences below:")

    # User preferences input
    city = st.selectbox("Select a city:", list(itineraries.keys()))
    age = st.number_input("Age", min_value=18, max_value=100, value=25, step=1)
    interests = st.multiselect("Interests", ["Adventure", "Sightseeing", "Culture", "Food", "Shopping"], default=["Adventure", "Sightseeing"])
    budget = st.selectbox("Budget", ["Below ₹10,000", "₹10,000 - ₹50,000", "₹50,000 - ₹1,00,000","Above ₹1,00,000"], index=1)
    travel_date = st.date_input("Travel Date")

    # Previous trips
    st.subheader("Your Previous Trips",divider=True)
    previous_trips = {
        "Destination": ["Goa", "Rajasthan", "Kerala", "Ladakh"],
        "Trip Type": ["Adventure", "Sightseeing", "Culture", "Adventure"],
        "Year": [2019, 2020, 2021, 2022]
    }
    trips_df = pd.DataFrame(previous_trips)
    st.dataframe(trips_df)

    # Update preferences button
    
    if st.button("Suggested Itineraries based on Updated Preferences"):

    # Suggest itineraries based on preferences
        st.subheader("Suggested Itineraries",divider=True)
        if "Adventure" in interests:
            st.subheader("Adventure Itinerary:", divider =True)
            st.markdown(itineraries[city]["Adventure"][budget])
        if "Sightseeing" in interests:
            st.subheader("Sightseeing Itinerary:",divider = True)
            st.markdown(itineraries[city]["Sightseeing"][budget])
        if "Fun" in interests:
            st.subheader("Fun Itinerary:")
            st.markdown(itineraries[city]["Fun"][budget])
    
        # Demo user DataFrame
        st.subheader("Connect with Fellow Travelers", divider = True)
        demo_users = {
            "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
            "Number of Trips": [5, 3, 10, 7, 2],
            "Rating": [4.5, 4.0, 4.8, 4.2, 4.6],
            "Chat": ["Chat", "Chat", "Chat", "Chat", "Chat"]
        }
        user_df = pd.DataFrame(demo_users)
        
        # Adding stars to ratings
        user_df['Star Rating'] = user_df['Rating'].apply(lambda x: '⭐' * int(x) + '☆' * (5 - int(x)))
    
        # Display the DataFrame with chat options
        st.dataframe(user_df)
    
        # Add chat buttons for each user
        for user in user_df['Name']:
            if st.button(f"Chat with {user}"):
                st.success(f"Starting chat with {user}...")

    # Logout button
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.success("You have been logged out.")
