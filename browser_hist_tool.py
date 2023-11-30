import os
import sqlite3
from collections import Counter
import matplotlib.pyplot as plt

def get_chrome_history():
    # Chrome history database path
    # Find You Path this path is for Windows 
    # C:\\Users\\Akash\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History
    history_db_path = "Your Path"

    # Connect to the database
    connection = sqlite3.connect(history_db_path)
    cursor = connection.cursor()

    # Query to select browsing history
    query = "SELECT * FROM urls ORDER BY last_visit_time DESC"

    # Execute the query
    cursor.execute(query)

    # Fetch all the results
    history_data = cursor.fetchall()

    # Close the connection
    connection.close()

    return history_data

def analyze_history(histData):
    # Extract URLs, titles and Visit_Counts
    
    urls=[entry[1] for entry in histData]
    titles=[entry[2] for entry in histData]
    visit_cnts=[entry[3] for entry in histData]

    # Count the occurrences of each URL and Title
    most_visited_counter=Counter(titles)
    most_visited_url_counter=Counter(urls)

    # Display top visited websites
    
    print("Top Visited Websites: ")
    print("**************************")
    for title,count in most_visited_counter.most_common(15):
        print(f"{title}: {count} visits")
    print("**************************")
    print("**************************")

    print("Top 10 Urls: ")
    print("**************************")
    for links,count in most_visited_url_counter.most_common(15):
        print(f"{links}: {count} visits")
        print("")
    print("**************************")
    print("**************************")
    
    # Create a histogram of visited websites
    plt.hist(titles,bins=20,edgecolor='black')
    plt.xlabel('Websites')
    plt.ylabel('Number of Visits')
    plt.title('Visited Websites as per Number of Counts')
    plt.show()


if __name__ == "__main__":
    # Extract Chrome browsing history
    chrome_history = get_chrome_history()

    # Analyze the history data
    analyze_history(chrome_history)
