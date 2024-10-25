import feedparser
import pandas as pd
import tabulate
import utils
import xml.etree.ElementTree as ET
import pandas as pd

# Feed Parser ##############################################################################################################

def fetch_rss_feed(feed_url):
    # Parse the RSS feed
    NewsFeed = feedparser.parse(feed_url)
    
    # List to store entry data as dictionaries
    entries_data = []
    
    for entry in NewsFeed.entries:
        # Consolidated fields as per your specifications
        title = getattr(entry, 'title', None)
        
        
        subtitle = (
            getattr(entry, 'title_detail', None) or 
            getattr(entry, 'subtitle', None) or 
            getattr(entry, 'subtitle_detail', None) or 
            getattr(entry, 'itunes_title', None)
        )
        
        link = (
            getattr(entry, 'link', None) or 
            getattr(entry, 'links', None) or 
            getattr(entry, 'href', None) or 
            getattr(entry, 'source', None) or 
            getattr(entry, 'guidislink', None) or 
            getattr(entry, 'acast_episodeurl', None) or 
            getattr(entry, 'podcast_episode', None)
        )
        
        author = getattr(entry, 'author', None) or (entry.authors[0]['name'] if hasattr(entry, 'authors') and entry.authors else None)
        published = getattr(entry, 'published', None) or getattr(entry, 'published_parsed', None)
        tags = [tag['term'] for tag in entry.tags] if hasattr(entry, 'tags') else None
        summary = getattr(entry, 'summary', None) or getattr(entry, 'summary_detail', None)
        
        content = (
            getattr(entry, 'content', None) or 
            getattr(entry, 'content_detail', None) or 
            getattr(entry, 'media_content', None)
        )
        
        comments = (
            getattr(entry, 'comments', None) or 
            getattr(entry, 'wfw_commentrss', None) or 
            getattr(entry, 'slash_comments', None)
        )
        
        image = (
            getattr(entry, 'media_thumbnail', None) or 
            getattr(entry, 'image', None) or 
            getattr(entry, 'googleplay_image', None)
        )
        
        rating = (
            getattr(entry, 'media_starrating', None) or 
            getattr(entry, 'media_rating', None) or 
            getattr(entry, 'rating', None)
        )
        
        statistics = getattr(entry, 'media_statistics', None)
        duration = getattr(entry, 'itunes_duration', None)
        
        description = (
            getattr(entry, 'googleplay_description', None) or 
            getattr(entry, 'description', None)
        )
        
        publisher = (
            getattr(entry, 'publisher', None) or 
            getattr(entry, 'publisher_detail', None)
        )
        
        # Append entry data to the list
        entries_data.append({
            'Title': title,
            'Subtitle': subtitle,
            'Link': link,
            'Author': author,
            'Published': published,
            'Tags': tags,
            'Summary': summary,
            'Content': content,
            'Comments': comments,
            'Image': image,
            'Rating': rating,
            'Statistics': statistics,
            'Duration': duration,
            'Description': description,
            'Publisher': publisher,
        })
        
        utils.print_line()
        print(f"Title: {title}")
        print(f"\nSubtitle: {subtitle}")
        print(f"\nLink: {link}")
        print(f"\nAuthor: {author}")
        print(f"\nPublished: {published}")
        print(f"\nTags: {tags}")
        print(f"\nSummary: {summary}")
        print(f"\nContent: {content}")
        print(f"\nComments: {comments}")
        print(f"\nImage: {image}")
        print(f"\nRating: {rating}")
        print(f"\nStatistics: {statistics}")
        print(f"\nDuration: {duration}")
        print(f"\nDescription: {description}")
        print(f"\nPublisher: {publisher}")
    
    # Convert the list of dictionaries to a DataFrame
    entries_df = pd.DataFrame(entries_data)
    return entries_df

def parse_opml_to_df(opml_file_path):
    """
    Parses an OPML file into a Pandas DataFrame with feed information.
    
    Args:
        opml_file_path (str): Path to the OPML file.
        
    Returns:
        pd.DataFrame: DataFrame with columns ['Category', 'Subcategory', 'Feed', 'htmlUrl', 'xmlUrl'].
    """
    # Parse the OPML file
    tree = ET.parse(opml_file_path)
    root = tree.getroot()
    
    # Initialize an empty DataFrame
    feeds_df = pd.DataFrame(columns=['Category', 'Subcategory', 'Feed', 'htmlUrl', 'xmlUrl'])
    
    # Iterate through each category and subcategory
    for category in root.findall('.//outline[@text]'):
        category_name = category.attrib['text']
        
        for subcategory in category.findall('.//outline[@text]'):
            subcategory_name = subcategory.attrib['text']
            
            # Iterate through each feed under the subcategory
            for feed in subcategory.findall('.//outline[@xmlUrl]'):
                feed_name = feed.attrib.get('text', 'Unknown Feed')
                html_url = feed.attrib.get('htmlUrl', '')
                xml_url = feed.attrib.get('xmlUrl', '')

                # Append feed information to the DataFrame
                feed_info = pd.DataFrame([{
                    'Category': category_name,
                    'Subcategory': subcategory_name,
                    'Feed': feed_name,
                    'htmlUrl': html_url,
                    'xmlUrl': xml_url
                }])
                feeds_df = pd.concat([feeds_df, feed_info], ignore_index=True)
    
    print(tabulate.tabulate(feeds_df, headers='keys', tablefmt='psql'))
    return feeds_df

# Testing ##############################################################################################################

def main ():
    parse_opml_to_df('./opml_test.opml')
    # fetch_rss_feed('https://anchor.fm/s/2b00eb34/podcast/rss')

if __name__ == "__main__":
    main()
    