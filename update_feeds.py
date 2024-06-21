import xml.etree.ElementTree as ET
import pandas as pd
import tabulate
import feedparser
import shutil

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
                print_line()

                feed_name = feed.attrib['text']
                html_url = feed.attrib['htmlUrl']
                xmlUrl = feed.attrib['xmlUrl']
                
                # Parse html_url to get the favicon
                try:
                    feed_html = feedparser.parse(html_url)
                    meta = feed_html['feed']['meta']['content']
                    print("\nMeta: ",meta)
                    
                    favicon = "./icons/generic.svg"
                    
                    # input("\nPress Enter to continue...")
                except:
                    print("The Favicon wasnt on html_url>feed>meta>content")
                    favicon = "./icons/generic.svg"
                

                # Create an new Pandas Series
                series = pd.Series([
                    Category_name, 
                    subcategory_name, 
                    feed_name, 
                    html_url,
                    favicon,
                    xmlUrl], index=['Category', 'Subcategory', 'Feed', 'htmlUrl', 'favicon', 'xmlUrl'])
                
                # Add the Series to the DataFrame
                feeeds = pd.concat([feeeds, series.to_frame().T], ignore_index=True)
                
    cleared_feeds = feeeds
    
    #Remove htmlUrl and xmlUrl columns
    cleared_feeds = cleared_feeds.drop(['htmlUrl', 'xmlUrl'], axis=1)
    
    
    print(tabulate.tabulate(cleared_feeds, headers='keys', tablefmt='psql'))
    return feeeds

def fetch_feed(feeds):
    
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
            NewsFeed = feedparser.parse(row['xmlUrl'])
            
            # Print the attributes of NewsFeed
            print(NewsFeed.keys())
            input("Press Enter to continue...")
            
            print(f"{index+1}/{len(feeds)} [{category}] | Fetching {row['Feed']} | Number of RSS posts :{len(NewsFeed.entries)}")
                    
            # Iterate through each post
            for entry in NewsFeed.entries:
                
                # General Information
                entry_title = getattr(entry, 'title', None)
                entry_title_detail = getattr(entry, 'title_detail', None)
                subtitle = getattr(entry, 'subtitle', None)
                
                # General Information
                subtitle_detail = getattr(entry, 'subtitle_detail', None) 
                link = getattr(entry, 'link', None)
                links = getattr(entry, 'links', None)
                authors = getattr(entry, 'authors', None)
                author = getattr(entry, 'author', None)
                author_detail = getattr(entry, 'author_detail', None)
                published = getattr(entry, 'published', None)
                published_parsed = getattr(entry, 'published_parsed', None)
                tags = getattr(entry, 'tags', None)
                id = getattr(entry, 'id', None)
                summary = getattr(entry, 'summary', None)
                summary_detail = getattr(entry, 'summary_detail', None)
                content = getattr(entry, 'content', None)
                media_content = getattr(entry, 'media_content', None)
                wfw_commentrss = getattr(entry, 'wfw_commentrss', None)
                slash_comments = getattr(entry, 'slash_comments', None)
                updated = getattr(entry, 'updated', None)
                updated_parsed = getattr(entry, 'updated_parsed', None)
                media_thumbnail = getattr(entry, 'media_thumbnail', None)
                href = getattr(entry, 'href', None)
                thr_total = getattr(entry, 'thr_total', None)
                source = getattr(entry, 'source', None)
                guidislink = getattr(entry, 'guidislink', None)
                
                # Videos
                yt_videoid = getattr(entry, 'yt_videoid', None)
                yt_channelid = getattr(entry, 'yt_channelid', None)
                media_starrating = getattr(entry, 'media_starrating', None)
                media_statistics = getattr(entry, 'media_statistics', None)
                media_community = getattr(entry, 'media_community', None)
                
                # Podcasts
                itunes_title = getattr(entry, 'itunes_title', None)
                itunes_episodetype = getattr(entry, 'itunes_episodetype', None)
                image = getattr(entry, 'image', None)
                omny_clipid = getattr(entry, 'omny_clipid', None)
                itunes_duration = getattr(entry, 'itunes_duration', None)
                itunes_explicit = getattr(entry, 'itunes_explicit', None)
                acast_episodeid = getattr(entry, 'acast_episodeid', None)
                acast_showid = getattr(entry, 'acast_showid', None)
                acast_episodeurl = getattr(entry, 'acast_episodeurl', None)
                acast_settings = getattr(entry, 'acast_settings', None)
                itunes_season = getattr(entry, 'itunes_season', None)
                itunes_episode = getattr(entry, 'itunes_episode', None)
                podcast_season = getattr(entry, 'podcast_season', None)
                podcast_episode = getattr(entry, 'podcast_episode', None)
                podcast_episodetype = getattr(entry, 'podcast_episodetype', None)
                itunes_block = getattr(entry, 'itunes_block', None)
                googleplay_block = getattr(entry, 'googleplay_block', None)
                googleplay_description = getattr(entry, 'googleplay_description', None)
                googleplay_image = getattr(entry, 'googleplay_image', None)
                googleplay_explicit = getattr(entry, 'googleplay_explicit', None)
                podcast_transcript = getattr(entry, 'podcast_transcript', None)
                
                # Blogs
                media_player = getattr(entry, 'media_player', None)
                media_rating = getattr(entry, 'media_rating', None)
                rating = getattr(entry, 'rating', None)
                
                # News Information
                comments = getattr(entry, 'comments', None)
                media_credit = getattr(entry, 'media_credit', None)
                credit = getattr(entry, 'credit', None)
                discourse_topicpinned = getattr(entry, 'discourse_topicpinned', None)
                discourse_topicclosed = getattr(entry, 'discourse_topicclosed', None)
                discourse_topicarchived = getattr(entry, 'discourse_topicarchived', None)
                publisher = getattr(entry, 'publisher', None)
                publisher_detail = getattr(entry, 'publisher_detail', None)
                rights = getattr(entry, 'rights', None)
                rights_detail = getattr(entry, 'rights_detail', None)
                dc_type = getattr(entry, 'dc_type', None)
                
                series = pd.Series([
                    category,
                    subcategory,
                    feed,
                    entry_title,
                    entry_title_detail,
                    subtitle,
                    subtitle_detail,
                    link,
                    links,
                    authors,
                    author,
                    author_detail,
                    published,
                    published_parsed,
                    tags,
                    id,
                    summary,
                    summary_detail,
                    content,
                    media_content,
                    wfw_commentrss,
                    slash_comments,
                    updated,
                    updated_parsed,
                    media_thumbnail,
                    href,
                    thr_total,
                    source,
                    guidislink,
                    yt_videoid,
                    yt_channelid,
                    media_starrating,
                    media_statistics,
                    media_community,
                    itunes_title,
                    itunes_episodetype,
                    image,
                    omny_clipid,
                    itunes_duration,
                    itunes_explicit,
                    acast_episodeid,
                    acast_showid,
                    acast_episodeurl,
                    acast_settings,
                    itunes_season,
                    itunes_episode,
                    podcast_season,
                    podcast_episode,
                    podcast_episodetype,
                    itunes_block,
                    googleplay_block,
                    googleplay_description,
                    googleplay_image,
                    googleplay_explicit,
                    podcast_transcript,
                    media_player,
                    media_rating,
                    rating,
                    comments,
                    media_credit,
                    credit,
                    discourse_topicpinned,
                    discourse_topicclosed,
                    discourse_topicarchived,
                    publisher,
                    publisher_detail,
                    rights,
                    rights_detail,
                    dc_type
                ], index=[
                    'Category',
                    'Subcategory',
                    'Feed',
                    'Title',
                    'Title_detail',
                    'Subtitle',
                    'Subtitle_detail',
                    'Link',
                    'Links',
                    'Authors',
                    'Author',
                    'Author_detail',
                    'Published',
                    'Published_parsed',
                    'Tags',
                    'Id',
                    'Summary',
                    'Summary_detail',
                    'Content',
                    'Media_content',
                    'Wfw_commentrss',
                    'Slash_comments',
                    'Updated',
                    'Updated_parsed',
                    'Media_thumbnail',
                    'Href',
                    'Thr_total',
                    'Source',
                    'Guidislink',
                    'Yt_videoid',
                    'Yt_channelid',
                    'Media_starrating',
                    'Media_statistics',
                    'Media_community',
                    'Itunes_title',
                    'Itunes_episodetype',
                    'Image',
                    'Omny_clipid',
                    'Itunes_duration',
                    'Itunes_explicit',
                    'Acast_episodeid',
                    'Acast_showid',
                    'Acast_episodeurl',
                    'Acast_settings',
                    'Itunes_season',
                    'Itunes_episode',
                    'Podcast_season',
                    'Podcast_episode',
                    'Podcast_episodetype',
                    'Itunes_block',
                    'Googleplay_block',
                    'Googleplay_description',
                    'Googleplay_image',
                    'Googleplay_explicit',
                    'Podcast_transcript',
                    'Media_player',
                    'Media_rating',
                    'Rating',
                    'Comments',
                    'Media_credit',
                    'Credit',
                    'Discourse_topicpinned',
                    'Discourse_topicclosed',
                    'Discourse_topicarchived',
                    'Publisher',
                    'Publisher_detail',
                    'Rights',
                    'Rights_detail',
                    'Dc_type'
                ])
                
                news = pd.concat([news, series.to_frame().T], ignore_index=True)
                
                
        except Exception as e:
            print(f"Error fetching {row['Feed']}: {e}")
            
    return news
            
                
# ######################################################################################################################################
#  AUXILIARY FUNCTIONS
def print_line():
    # Get the width of the screen
    screen_width = shutil.get_terminal_size().columns
    # Print a separator
    print("#" * screen_width)

# ######################################################################################################################################
# MAIN LOOP


if __name__ == "__main__":

    # Example usage
    filename = 'All_Feeds.opml'
    
    feeds = open_opml(filename)
    
    news = fetch_feed(feeds)

    print("\nSalvando dados em Excell...")
    
    excel_writer = pd.ExcelWriter(f'Feeds.xlsx', engine='xlsxwriter')
    
    feeds.to_excel(excel_writer, sheet_name='Feeds', index=False)
    
    # Separate news by category and save each category to an excel file
    for category in news['Category'].unique():
        
        news_by_category = news.loc[news['Category'] == category]
        
        # Drop the category column
        news_by_category = news_by_category.drop('Category', axis=1)
        
        # Drop Collumns not beeing used right now
        news_by_category = news_by_category.drop([
            'Title_detail', 
            'Author_detail',
            'Wfw_commentrss',
            'Slash_comments',
            'Comments',
            'Links',
            'Authors',
            'Published',
            'Summary_detail',
            'Media_community',
            
            
            ], axis=1)
        
        
        # Remove EMpty columns
        news_by_category = news_by_category.dropna(axis=1, how='all')
        
        # Make collumns width automatic
        news_by_category = news_by_category.style.set_properties(**{'width': 'auto'})
        
        news_by_category.to_excel(excel_writer, sheet_name=category, index=False)
        
    excel_writer._save()




