import streamlit as st
import pandas as pd

# Define the travel itineraries for the selected cities
itineraries = {
    "Mumbai": {
        "Adventure": {
            "₹50,000 and Below": """
### Day 1: Arrival and Adventure
- Check in at **Hotel New Aadya International** (₹2,500 per night).
- Visit **Sanjay Gandhi National Park** for trekking.
- Dinner at **Bademiya** (₹500 per person) for famous kebabs.

### Day 2: Beach Day
- Explore **Juhu Beach** and enjoy local street food like bhel puri (₹50 per plate).
- Visit **Versova Beach** for a relaxing evening.

### Day 3: Sightseeing
- Visit **Gateway of India** and **Elephanta Caves** (ferry ride).
- Dinner at **Trishna** (₹1,000 per person) for seafood delicacies.
""",
            "₹1,00,000 and Below": """
### Day 1: Arrival and Adventure
- Check in at **The Orchid Hotel** (₹9,000 per night).
- Visit **Elephanta Caves** (ferry ride).
- Dinner at **The Table** (₹2,000 per person) for contemporary dining.

### Day 2: Culture and Adventure
- Morning at **Marine Drive**.
- Evening at **Haji Ali Dargah**.

### Day 3: Sightseeing
- Visit **Gateway of India** and **Elephanta Caves**.
- Explore **Colaba Causeway** for shopping.
""",
            "₹2,00,000 and Below": """
### Day 1: Arrival and Luxury Adventure
- Check in at **Taj Mahal Palace** (₹24,000 per night).
- Private yacht tour of Mumbai.
- Fine dining at **Wasabi by Morimoto** (₹5,000 per person) for high-end Japanese cuisine.

### Day 2: Adventure and Relaxation
- Water sports at **Aksa Beach**.
- Evening at a luxury spa.

### Day 3: Sightseeing
- Visit **Gateway of India** and **Elephanta Caves**.
- Explore **Colaba Causeway** for shopping.
"""
        },
        "Sightseeing": {
            "₹50,000 and Below": """
### Day 1: Arrival and Sightseeing
- Check in at **Hotel New Aadya International** (₹2,500 per night).
- Visit **Gateway of India** and **Marine Drive**.
- Dinner at **Cafe Madras** (₹600).

### Day 2: Cultural Exploration
- Morning at **Chhatrapati Shivaji Maharaj Terminus**.
- Afternoon at **Prince of Wales Museum**.

### Day 3: Departure
- Explore **Colaba Causeway** for shopping.
- Check out and depart.
""",
            "₹1,00,000 and Below": """
### Day 1: Arrival and Sightseeing
- Check in at **The Orchid Hotel** (₹9,000 per night).
- Visit **Elephanta Caves** and **Gateway of India**.

### Day 2: Cultural Exploration
- Visit **Haji Ali Dargah** and **Marine Drive**.

### Day 3: Departure
- Explore **Colaba Causeway**.
- Check out and depart.
""",
            "₹2,00,000 and Below": """
### Day 1: Arrival and Luxury Sightseeing
- Check in at **Taj Mahal Palace** (₹24,000 per night).
- Private guided tour of **Gateway of India**.

### Day 2: Cultural Exploration
- Visit **Chhatrapati Shivaji Maharaj Vastu Sangrahalaya**.
- Evening at a luxury spa.

### Day 3: Departure
- Visit **Dharavi** for a guided tour.
- Check out and depart.
"""
        },
        "Fun": {
            "₹50,000 and Below": """
### Day 1: Arrival and Fun
- Check in at **Hotel New Aadya International** (₹2,500 per night).
- Visit local markets and street food stalls like **Bademiyan** (₹200 per plate) for kebabs.
- Dinner at **Cafe Mondegar** (₹500 per person) for local cuisine.

### Day 2: Explore Local Nightlife
- Morning at **Juhu Beach**.
- Evening at local pubs like **Aer** (₹1,000 per person) for drinks with a view.

### Day 3: Departure
- Explore **Colaba Causeway** for shopping.
- Check out and depart.
""",
            "₹1,00,000 and Below": """
### Day 1: Arrival and Fun
- Check in at **The Orchid Hotel** (₹9,000 per night).
- Visit **Essel World** amusement park.
- Dinner at **Masala Library** (₹3,000 per person) for modern Indian cuisine.

### Day 2: Explore Local Culture
- Evening at a local concert or event.

### Day 3: Departure
- Visit **Dharavi** for a guided tour.
- Check out and depart.
""",
            "₹2,00,000 and Below": """
### Day 1: Arrival and Luxury Fun
- Check in at **Taj Mahal Palace** (₹24,000 per night).
- Private guided tour of local attractions.

### Day 2: Adventure and Relaxation
- Visit **Aksa Beach** for water sports.
- Evening at a luxury spa.

### Day 3: Departure
- Explore **Colaba Causeway** for shopping.
- Check out and depart.
"""
        }
    },
    "Delhi": {
        "Adventure": {
            "₹50,000 and Below": """
### Day 1: Arrival and Adventure
- Check in at **Hotel Ajanta** (₹3,000 per night).
- Visit **Red Fort** and **Jama Masjid**.
- Dinner at **Karim's** (₹500 per person) for Mughlai cuisine.

### Day 2: Explore Nature
- Morning trek at **Tughlaqabad Fort**.
- Afternoon at **Sanjay Lake**.
""",
            "₹1,00,000 and Below": """
### Day 1: Arrival and Adventure
- Check in at **The Oberoi** (₹12,000 per night).
- Visit **Qutub Minar** and **Humayun's Tomb**.
- Dinner at **Bukhara** (₹2,000 per person) for North Indian cuisine.

### Day 2: Cultural Exploration
- Morning visit to **India Gate** and **Rashtrapati Bhavan**.
- Evening at **Connaught Place** for shopping.
"""
        },
        "Sightseeing": {
            "₹50,000 and Below": """
### Day 1: Arrival and Sightseeing
- Check in at **Hotel Ajanta** (₹3,000 per night).
- Visit **Red Fort** and **Jama Masjid**.
- Dinner at **Karim's** (₹500 per person) for Mughlai cuisine.

### Day 2: Cultural Exploration
- Morning at **Qutub Minar**.
- Afternoon at **Humayun's Tomb**.

### Day 3: Departure
- Visit **India Gate** and **Rashtrapati Bhavan**.
- Check out and depart.
""",
            "₹1,00,000 and Below": """
### Day 1: Arrival and Sightseeing
- Check in at **The Oberoi** (₹12,000 per night).
- Visit **Qutub Minar** and **Humayun's Tomb**.
- Dinner at **Bukhara** (₹2,000 per person) for North Indian cuisine.

### Day 2: Cultural Exploration
- Morning visit to **India Gate** and **Rashtrapati Bhavan**.
- Evening at **Connaught Place** for shopping.

### Day 3: Departure
- Visit **Red Fort** and **Jama Masjid**.
- Check out and depart.
"""
        }
    },
    "Kolkata": {
        "Adventure": {
            "₹50,000 and Below": """
### Day 1: Arrival and Adventure
- Check in at **Hotel Casa Fortuna** (₹3,500 per night).
- Visit **Howrah Bridge** and take a ferry ride on the Hooghly River.
- Dinner at **Bhojohori Manna** (₹600 per person) for biryani.

### Day 2: Nature and Culture
- Explore **Sundarbans National Park** (day trip).
- Evening at **Victoria Memorial**.
""",
            "₹1,00,000 and Below": """
### Day 1: Arrival and Adventure
- Check in at **Taj Bengal** (₹10,000 per night).
- Visit **Howrah Bridge** and take a ferry ride on the Hooghly River.
- Dinner at **Peter Cat** (₹1,200 per person) for continental cuisine.

### Day 2: Nature and Culture
- Explore **Sundarbans National Park** (day trip).
- Evening at **Victoria Memorial**.
"""
        },
        "Sightseeing": {
            "₹50,000 and Below": """
### Day 1: Arrival and Sightseeing
- Check in at **Hotel Casa Fortuna** (₹3,500 per night).
- Visit **Victoria Memorial** and **Indian Museum**.
- Dinner at **Bhojohori Manna** (₹600 per person) for biryani.

### Day 2: Cultural Exploration
- Morning at **Dakshineswar Kali Temple**.
- Afternoon at **Belur Math**.

### Day 3: Departure
- Explore **Park Street** for shopping.
- Check out and depart.
""",
            "₹1,00,000 and Below": """
### Day 1: Arrival and Sightseeing
- Check in at **Taj Bengal** (₹10,000 per night).
- Visit **Victoria Memorial** and **Indian Museum**.
- Dinner at **Peter Cat** (₹1,200 per person) for continental cuisine.

### Day 2: Cultural Exploration
- Morning at **Dakshineswar Kali Temple**.
- Afternoon at **Belur Math**.

### Day 3: Departure
- Explore **Park Street** for shopping.
- Check out and depart.
"""
        }
    },
    "Chennai": {
        "Adventure": {
            "₹50,000 and Below": """
### Day 1: Arrival and Adventure
- Check in at **Hotel Palmgrove** (₹3,000 per night).
- Visit **Mahabalipuram** for rock climbing.
- Dinner at **Murugan Idli Shop** (₹200 per person) for South Indian breakfast.

### Day 2: Beach Day
- Explore **Marina Beach** and enjoy local street food like pani puri (₹20 per plate).
- Dinner at **Dakshin** (₹1,000 per person) for authentic South Indian cuisine.
""",
            "₹1,00,000 and Below": """
### Day 1: Arrival and Adventure
- Check in at **ITC Grand Chola** (₹12,000 per night).
- Visit **Mahabalipuram** for surfing.
- Dinner at **Dakshin** (₹1,000 per person) for authentic South Indian cuisine.

### Day 2: Cultural Exploration
- Visit **Kapaleeshwarar Temple** and **Arignar Anna Zoological Park**.
- Dinner at **Anjappar** (₹500 per person) for Chettinad cuisine.
"""
        },
        "Sightseeing": {
            "₹50,000 and Below": """
### Day 1: Arrival and Sightseeing
- Check in at **Hotel Palmgrove** (₹3,000 per night).
- Visit **Marina Beach** and **Kapaleeshwarar Temple**.
- Dinner at **Murugan Idli Shop** (₹200 per person) for South Indian breakfast.

### Day 2: Cultural Exploration
- Morning at **Fort St. George** and **Government Museum**.
- Afternoon at **Parthasarathy Temple**.

### Day 3: Departure
- Explore **T Nagar** for shopping.
- Check out and depart.
""",
            "₹1,00,000 and Below": """
### Day 1: Arrival and Sightseeing
- Check in at **ITC Grand Chola** (₹12,000 per night).
- Visit **Kapaleeshwarar Temple** and **Fort St. George**.
- Dinner at **Dakshin** (₹1,000 per person) for authentic South Indian cuisine.

### Day 2: Cultural Exploration
- Visit **Government Museum** and **Parthasarathy Temple**.
- Afternoon at **Marina Beach**.

### Day 3: Departure
- Explore **T Nagar** for shopping.
- Check out and depart.
"""
        }
    }
}

# Streamlit app
st.set_page_config(page_title="Travel Itinerary", page_icon="✈️")

st.title("Detailed Travel Itinerary")

# Login functionality
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

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
    st.header("Welcome to the Itinerary Generator")

    # User preferences
    st.subheader("Your Default Preferences Based on History")
    st.write("Age: 30")
    st.write("Interests: Adventure, Sightseeing")
    st.write("Budget: ₹1,00,000 and Below")
    
    st.write("You can change your preferences below:")

    # User preferences input
    city = st.selectbox("Select a city:", list(itineraries.keys()))
    age = st.number_input("Age", min_value=18, max_value=100, value=30, step=1)
    interests = st.multiselect("Interests", ["Adventure", "Sightseeing", "Culture", "Food", "Shopping"], default=["Adventure", "Sightseeing"])
    budget = st.selectbox("Budget", ["₹50,000 and Below", "₹1,00,000 and Below", "₹2,00,000 and Below"], index=1)
    travel_date = st.date_input("Travel Date")

    # Previous trips
    st.subheader("Your Previous Trips")
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
        st.subheader("Suggested Itineraries")
        if "Adventure" in interests:
            st.write("Adventure Itinerary:")
            st.markdown(itineraries[city]["Adventure"][budget])
        if "Sightseeing" in interests:
            st.write("Sightseeing Itinerary:")
            st.markdown(itineraries[city]["Sightseeing"][budget])
        if "Fun" in interests:
            st.write("Fun Itinerary:")
            st.markdown(itineraries[city]["Fun"][budget])
    
        # Demo user DataFrame
        st.subheader("Connect with Fellow Travelers")
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
