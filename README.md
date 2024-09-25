# Python Rss Reader

![image](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![image](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![image](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

## 🚀 About

This project aims to take an OPML file, fetch all the feeds and store them in an excel file, and generate a website with all the feeds. The idea is that after built, you should put the update feed script in the cron job.

## 📝 How to Build

### Getting Started

## 📚 Documentation 

### Project Structure:

<pre>

    ├───Assets
    │   ├───css
    │   │   ├───adminlte.min.css
    │   │   ├───bootstrap.min.css
    │   │   └───dataTables.dataTables.min.css
    │   ├───images
    │   │   └───feed_icons
    │   └───js
    │       ├───adminlte.min.js
    │       ├───bootstrap.bundle.min.js
    │       ├───dataTables.min.js
    │       └───jquery-3.6.0.min.js
    ├───Data
    |   ├───feeds.opml [Initial File to import the RSS Feeds]
    |   └───feeds.xlsx [Sckaped Feeds, with icons, informations, etc.] 
    ├───Scripts
    |   ├───update_feeds.py
    |   └───update_frontend.py
    |
    └───Templates
        ├───header.html
        ├───navbar.html
        └───index_template.html

</pre>
