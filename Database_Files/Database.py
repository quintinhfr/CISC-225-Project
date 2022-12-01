import os 
import sqlite3
import pywin32 

#Create & connect to database
db = sqlite3.connect("emails.db")
# Create empty tables
db.execute("""
CREATE TABLE IF NOT EXISTS "articles" (
"id" INTEGER,
"title" TEXT UNIQUE,
"publication" TEXT,
PRIMARY KEY("id" AUTOINCREMENT))
""")
db.execute("""
CREATE TABLE IF NOT EXISTS "links" (
"article_id"    INTEGER,
"link0" TEXT,
"link1" TEXT,
"link2" TEXT,
PRIMARY KEY("article_id"))
""")
db.execute("""
CREATE TABLE IF NOT EXISTS "platforms" (
"article_id"    INTEGER,
"platform0" TEXT,
"platform1" TEXT,
"platform2" TEXT,
PRIMARY KEY("article_id"))
""")
# Create an folder input dialog with tkinter
folder_path = os.path.normpath(askdirectory(title='Select Folder'))
# Initialise & populate list of emails
email_list = 
[file for file in os.listdir(folder_path) if file.endswith(".msg")]
# Connect to Outlook with MAPI
outlook = win32com.client.Dispatch("Outlook.Application")
                  .GetNamespace(“MAPI”)
# Iterate through every email
for i, _ in enumerate(email_list):
   # Create variable storing info from current email being parsed
   msg = outlook.OpenSharedItem(os.path.join(folder_path,
   email_list[i]))
   # Search email HTML for body text
   regex = re.search(r"<body([\s\S]*)</body>", msg.HTMLBody)
   body = regex.group()
# Search email body text for unique entries
pattern = r"li class=MsoListParagraph([\s\S]*?)</li>"
results = re.findall(pattern, body)
regex = re.search(r"[^<>]+(?=\(|sans-serif’>([\s\S]*?)</span>)", header)
# HTML unescape to get remove remaining HTML
title_pub = html.unescape(regex.group())
title = split_list[0].strip()
publication = split_list[1].strip()
# List of publications to check for
platform_list = ["Online", "Facebook", "Instagram", "Twitter", "LinkedIn", "Youtube"]
# Create empty list to store publications
platform = []
# Iterate and check for each item in my first list
for p in platform_list:
   if p in header:
      platform.append(p)
      # Find all links using regex
links = re.findall(r"<a href=\”([\s\S]*?)\”>", header)
# Insert title & pub by substituting values into each ? placeholder
db.execute("INSERT INTO articles (title, publication) 
VALUES (?, ?)", (title, publication))
# Get article id and copy to platforms & links tables
article_id = db.execute(“SELECT id FROM articles WHERE title = ?”, (title,))
for item in article_id:
   _id = item[0]
for i, _ in enumerate(platform):
   db.execute(f”UPDATE platforms SET platform{i} = ? WHERE    
   article_id = ?”, (platform[i], _id))
for i, _ in enumerate(links):
   db.execute(f”UPDATE links SET link{i} = ? WHERE article_id = ?”, 
   (links[i], _id))
# Commit changes
db.commit()




