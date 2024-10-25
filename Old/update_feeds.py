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

def fetch_rss_feed(dataframe_feeds):
    
    news = pd.DataFrame()
    
    number_of_iterations = len(dataframe_feeds)

    # Iterate through each feed
    for index, row in dataframe_feeds.iterrows():
        
        url = row['xmlUrl']
        
        # Parse the RSS feed
        print(f"[{index+1}/{number_of_iterations}] Fetching {row['Feed']}")
        
        NewsFeed = feedparser.parse(url)
        
        # Iterate through each post
        for entry in NewsFeed.entries:
            
            category = row['Category']
            subcategory = row['Subcategory']
            feed = row['Feed']
            
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
                category, subcategory, feed, entry_title, entry_title_detail, subtitle, subtitle_detail,
                link, links, authors, author, author_detail, published, published_parsed,
                tags, id, summary, summary_detail, content, media_content, wfw_commentrss,
                slash_comments, updated, updated_parsed, media_thumbnail, href, thr_total, source,
                guidislink, yt_videoid, yt_channelid, media_starrating, media_statistics, media_community,
                itunes_title, itunes_episodetype, image, omny_clipid, itunes_duration, itunes_explicit,
                acast_episodeid, acast_showid, acast_episodeurl, acast_settings, itunes_season, itunes_episode,
                podcast_season, podcast_episode, podcast_episodetype, itunes_block, googleplay_block, googleplay_description,
                googleplay_image, googleplay_explicit, podcast_transcript, media_player, media_rating, rating, comments,
                media_credit, credit, discourse_topicpinned, discourse_topicclosed, discourse_topicarchived, publisher,
                publisher_detail, rights, rights_detail, dc_type
            ], index=[
                'Category', 'Subcategory', 'Feed', 'Title', 'Title_detail', 'Subtitle', 'Subtitle_detail', 
                'Link', 'Links', 'Authors', 'Author', 'Author_detail', 'Published', 'Published_parsed', 
                'Tags', 'Id', 'Summary', 'Summary_detail', 'Content', 'Media_content', 'Wfw_commentrss', 
                'Slash_comments', 'Updated', 'Updated_parsed', 'Media_thumbnail', 'Href', 'Thr_total', 'Source', 
                'Guidislink', 'Yt_videoid', 'Yt_channelid', 'Media_starrating', 'Media_statistics', 'Media_community', 
                'Itunes_title', 'Itunes_episodetype', 'Image', 'Omny_clipid', 'Itunes_duration', 'Itunes_explicit', 
                'Acast_episodeid', 'Acast_showid', 'Acast_episodeurl', 'Acast_settings', 'Itunes_season', 'Itunes_episode', 
                'Podcast_season', 'Podcast_episode', 'Podcast_episodetype', 'Itunes_block', 'Googleplay_block', 'Googleplay_description', 
                'Googleplay_image', 'Googleplay_explicit', 'Podcast_transcript', 'Media_player', 'Media_rating', 'Rating', 'Comments', 
                'Media_credit', 'Credit', 'Discourse_topicpinned', 'Discourse_topicclosed', 'Discourse_topicarchived', 'Publisher', 
                'Publisher_detail', 'Rights', 'Rights_detail', 'Dc_type'
            ])
            
            news = pd.concat([news, series.to_frame().T], ignore_index=True)
            
    return news

def fetch_all_youtube_videos(channel_url):
    # Instancia o objeto do canal do YouTube
    channel = Channel(channel_url)
    
    print(f'Fetching videos from channel: {channel.channel_name}')
    
    # Lista para armazenar os vídeos
    videos = []
    
    # Itera sobre todos os vídeos do canal
    for video in channel.videos:
        videos.append({
            "title": video.title,
            "url": video.watch_url,
            "views": video.views,
            "publish_date": video.publish_date
        })
        print(f'Video: {video.title} ({video.publish_date})')
    
    return videos

# ######################################################################################################################################
#  AUXILIARY FUNCTIONS

def append_new_entries(existing_df, new_entries):
    
    # Use 'Title' and 'Feed' columns to find new entries
    combined_df = pd.merge(new_entries, existing_df, on=['Title', 'Feed'], how='left', indicator=True)
    
    # Filter rows that are only in new_entries ('_merge' == 'left_only')
    new_rows = combined_df[combined_df['_merge'] == 'left_only'].drop('_merge', axis=1)
    
    return new_rows

def print_line():
    # Get the width of the screen
    screen_width = shutil.get_terminal_size().columns
    # Print a separator
    print("#" * screen_width)

# ######################################################################################################################################
# MAIN LOOP

if __name__ == "__main__":

    # Convert the file to an dataframe
    feeds = pd.read_excel("../Data/feeds.xlsx")
        
    # Get the news
    news = fetch_rss_feed(feeds)
    
    # Read the existing entries.xlsx file
    try:
        existing_entries = pd.read_excel("../Data/entries.xlsx", sheet_name=None)
    except FileNotFoundError:
        existing_entries = {}
    
    # Save the news to an excel file
    excel_writer = pd.ExcelWriter(f'../Data/entries.xlsx', engine='xlsxwriter')

    # Separate news by category and save each category to an excel file
    for category in news['Category'].unique():
        
        news_by_category = news.loc[news['Category'] == category]
        
        # Drop the category column
        news_by_category = news_by_category.drop('Category', axis=1)
        
        # Drop Columns not being used right now
        news_by_category = news_by_category.drop([
            'Author_detail', 'Wfw_commentrss', 'Slash_comments', 'Comments',
            'Links', 'Authors', 'Published', 'Media_community', 'Updated'
        ], axis=1)
        
        # Remove Empty columns
        news_by_category = news_by_category.dropna(axis=1, how='all')
        
        # Check if the category already exists in the existing entries
        if category in existing_entries:
            existing_df = existing_entries[category]
        else:
            existing_df = pd.DataFrame()  # Empty DataFrame for new categories

        # Append new entries
        new_entries = append_new_entries(existing_df, news_by_category)
        
        # Concatenate new entries with the existing data for this category
        combined_data = pd.concat([existing_df, new_entries], ignore_index=True)

        # Save the updated category data to the excel file
        combined_data.to_excel(excel_writer, sheet_name=category, index=False)
        
    # Save the Excel file
    excel_writer._save()
