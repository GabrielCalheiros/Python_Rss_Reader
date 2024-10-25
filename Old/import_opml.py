import xml.etree.ElementTree as ET
import pandas as pd
import tabulate
import feedparser
import shutil
import re
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import favicon

# ######################################################################################################################################
# RSS RELATED FUNCTIONS

def open_opml(filename):
    
    tree = ET.parse(filename)
    root = tree.getroot()
        
    head = root[0]
    title = head[0]
    lastModified = head[1]
    
    body = root[1]
    
    feeeds = pd.DataFrame()
    
    # Add each category in the body
    for category in body:
        
        # Print atribute of the category
        Category_name = category.attrib['text']
        
        print("Readig " + Category_name)
        
        # Iterate through each subcategory
        for subcategory in category:
            subcategory_name = subcategory.attrib['text']
            
            print("- Readig " + subcategory_name)
            
            # Iterate through each feed
            for feed in subcategory:
                # print_line()

                feed_name = feed.attrib['text']
                html_url = feed.attrib['htmlUrl']
                xmlUrl = feed.attrib['xmlUrl']

                # Create an new Pandas Series
                series = pd.Series([
                    Category_name, 
                    subcategory_name, 
                    feed_name, 
                    html_url,
                    xmlUrl], index=['Category', 'Subcategory', 'Feed', 'htmlUrl', 'xmlUrl'])
                
                # Add the Series to the DataFrame
                feeeds = pd.concat([feeeds, series.to_frame().T], ignore_index=True)
                
    cleared_feeds = feeeds
    
    #Remove htmlUrl and xmlUrl columns
    cleared_feeds = cleared_feeds.drop(['htmlUrl', 'xmlUrl'], axis=1)
    
    print(tabulate.tabulate(cleared_feeds, headers='keys', tablefmt='psql'))
    
    return feeeds

def fetch_feed(feeds):
    
    fetched_feeds = pd.DataFrame()
    category_keys = {}
    news = pd.DataFrame()
    
    # Iterate through each feed
    for index, row in feeds.iterrows():
        
        category = row['Category']
        subcategory = row['Subcategory']
        feed = row['Feed']
        
        if category not in category_keys:
            category_keys[category] = []

        try:
            # Parse the RSS feed
            NewsFeed = feedparser.parse(row['xmlUrl'])
            
            print(f"\n\n\n{index+1}/{len(feeds)} [{category}] | Fetching {row['Feed']} | Number of RSS posts :{len(NewsFeed.entries)} | URL: {row['xmlUrl']}")

        # ##################################################################################################################################################################
                        
            icons = favicon.get(row['htmlUrl'])
                        
            # Select the icon with the highest resolution
            if icons:
                largest_icon = max(icons, key=lambda icon: icon.width)
                print(f"Icon with highest resolution: {largest_icon.url} ({largest_icon.width}x{largest_icon.height})")
            else:
                print("No icons found, using generic icon.")
                largest_icon = "./icons/generic.svg"

                
        # ##################################################################################################################################################################

            # Create an new Pandas Series
            series = pd.Series([
                row['Category'], 
                row['Subcategory'], 
                row['Feed'],
                row['htmlUrl'],
                row['xmlUrl'],
                largest_icon,
                # favicon,
                ], index=['Category', 'Subcategory', 'Feed', 'htmlUrl', 'xmlUrl', 'Icon'])
            
            # Add the Series to the DataFrame
            fetched_feeds = pd.concat([fetched_feeds, series.to_frame().T], ignore_index=True)
        
        # ##################################################################################################################################################################
                            
      
        except Exception as e:
            print(f"Error fetching {row['Feed']}: {e}")
            
    return fetched_feeds
            
# ######################################################################################################################################
#  AUXILIARY FUNCTIONS

def print_line():
    # Get the width of the screen
    screen_width = shutil.get_terminal_size().columns
    # Print a separator
    print("#" * screen_width)

def get_favicon_from_domain(domain):
    # Try the common favicon location first
    try:
        response = requests.get(domain + 'favicon.ico', timeout=5)
        if response.status_code == 200:
            return domain + 'favicon.ico'
    except requests.RequestException:
        pass

    # Fallback: Parse HTML and look for <link rel="icon"> or <link rel="shortcut icon">
    try:
        response = requests.get(domain, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        icon_link = soup.find("link", rel="icon")
        if not icon_link:
            icon_link = soup.find("link", rel="shortcut icon")
        
        if icon_link and 'href' in icon_link.attrs:
            icon_url = icon_link['href']
            # Handle relative URLs
            if icon_url.startswith('/'):
                icon_url = domain + icon_url.lstrip('/')
            return icon_url
    except requests.RequestException:
        pass

    return "./icons/generic.svg"

# ######################################################################################################################################
# MAIN LOOP

if __name__ == "__main__":

    filename = "../Data/feeds.opml"
    
    feeds = open_opml(filename)
    
    feeds = fetch_feed(feeds)

    print("\nSalvando dados em Excell...")
    
    excel_writer = pd.ExcelWriter(f'../Data/feeds.xlsx', engine='xlsxwriter')
    
    feeds.to_excel(excel_writer, sheet_name='Feeds', index=False)
            
    excel_writer._save()
