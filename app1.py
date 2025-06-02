import streamlit as st
import requests

# Function to fetch user data from LeetScan API
def fetch_user_data(username):
    url = f"https://leetscan.vercel.app/{username}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

# Function to display user profile information safely
def display_user_profile(data):
    if not data:
        st.error("No data found for this user.")
        return

    st.header(f"LeetCode Profile: {data.get('username', 'N/A')}")
    st.write(f"Total Problems Solved: {data.get('totalSolved', 'N/A')}")
    st.write(f"Total Submissions: {data.get('totalSubmissions', 'N/A')}")
    #st.write(f"Acceptance Rate: {data.get('acceptanceRate', 'N/A')}%")

    st.subheader("Problems Solved by Difficulty")
    st.write(f"Easy: {data.get('easySolved', 'N/A')}")
    st.write(f"Medium: {data.get('mediumSolved', 'N/A')}")
    st.write(f"Hard: {data.get('hardSolved', 'N/A')}")

    contest = data.get('contestRanking')
    if contest:
        st.write(f"Global Contest Rank: {contest.get('globalRanking', 'N/A')}")
    else:
        st.write("Global Contest Rank: Not available")

# Streamlit interface
def main():
    st.title("📊 LeetCode User Profile Analyzer")
    username = st.text_input("Enter LeetCode Username")

    if username:
        user_data = fetch_user_data(username)
        if user_data:
            display_user_profile(user_data)
        else:
            st.error("Could not retrieve data. Please check the username or try again later.")

if __name__ == "__main__":
    main()
