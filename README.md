# Python Rss Reader

![image](https://img.shields.io/badge/RSS-FFA500?style=for-the-badge&logo=rss&logoColor=white)
![image](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![image](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![image](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

## 🚀 About

This is a simple python rss feed reader built with the flask framework. This is a project for my personal use, and the original though is for this to be only used in local networks, not served externally (no login required or authentication system is used).

## 📝 How to Build

### How to import the rss feed into your app:

Using an OPML, the structure of the OPML must be the following:

<pre>
    Outline 1 [Category]
    .
    ├── Outline 1 [Category]
    │   ├── Outline 1.1 [Sub-Category]
    │   │   ├── Outline 1.1.1 [Feed]
    │   |   └── Outline 1.1.2 [Feed]
    │   ├── Outline 1.2 [Sub-Category]
    │   |   ├── Outline 1.2.1 [Feed]
    │   |   └── Outline 1.2.2 [Feed]
    |   |   └── Outline 1.2.3 [Feed]
    │   └── Outline 1.1 [Sub-Category]
    ├── Outline 2 [Category]
    |   ├── Outline 2.1 [Sub-Category]
    |   │   └── Outline 2.1.1 [Feed]
    |   └── Outline 2.1 [Sub-Category]
    |   ├── Outline 2.2 [Sub-Category]
    |   └── Outline 2.3 [Sub-Category]
</pre>

The first outline is the main category, the second the sub-category and the last the feed. If the category or sub-category does not exist, it will be created, and the standart view will be used for it. You can change the standart view in the index page. 

## 📚 Documentation 

### Project Structure:

<pre>

    .
    ├── .env
    ├── README.md
    ├── requirements.txt
    ├── database.sql
    ├── config.py
    ├── run.py
    └── app
        ├── tmp
        │   └── [TEMPORARY FILES]
        ├── __init__.py
        ├── models.py
        ├── routes.py 
        ├── feeds_fetcher.py
        ├── static
        │   ├── css
        │   │   ├───adminlte.min.css
        │   │   ├───bootstrap.min.css
        │   │   └───dataTables.dataTables.min.css
        │   ├── js
        │   |   ├───adminlte.min.js
        │   |   ├───bootstrap.bundle.min.js
        │   |   ├───dataTables.min.js
        │   |   └───jquery-3.6.0.min.js
        │   └── images
        │       ├───[IMAGES]
        |       ├── feed_icons
        |       └── [FEED_ICONS]
        └── templates
            ├── index.html
            ├── category_view.html
            ├── subcategory_view.html
            ├── single_feed_view.html
            └── components
                ├── header.html
              ├── navbar.html
                └── [MINOR COMPONENTS]
</pre>

### Project Routes:

**Served Pages:**

- /index
- /category_view?category=[id_category]
- /subcategory_view?subcategory=[id_subcategory]
- /feed_view?feed=[id_feed]
  
**Actions:**

- /import_opml
- /update_feeds
- /add_feed
- /remove_feed
- 
Todo list notes:
[] Unify published and published_parsed
[] Unify content and media_content
[] Unify wfw_commentrss and slash_comments
[] Unify image and media_thumbnail and googleplay_image
[] Unify itunes_explicit and googleplay_explicit

