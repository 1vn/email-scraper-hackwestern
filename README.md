# email-scraper-hackwestern
Email scraping script to aid in Bus Coordinating for Hack Western written in Python 3 made purely for overengineering purposes.

Regex to identify email obtained here: http://www.regular-expressions.info/email.html

This is a script meant to be used by Hack Western Bus organizers to parse the emails from the bus list given.
Currently, it produces a new text file in the file directory of all the emails on the bus list separated by a ",\n". This is 
so that you can copy and paste all the emails into the "receipients" field of the email you want to send directly (hence the comma). 

This build is very crude, here's how you use it:

MAKE SURE YOU HAVE PYTHON 3 INSTALLED

1. Clone the repo
2. Place your bus list in the same directory as email_scraper.py
3. On line 2, change "toronto_bus_list" to the name of the bus_list.txt you received. 
4. Open up your favorite shell
5. Navigate to the directory of the repo.
6. Run the command: python email_scraper.py
7. Copy and paste the contents of the file produced, email_list.txt, into the receipients field of the email you want to send.
8. Write the contents of the email and press send.

At the moment I am open to any suggestions/pull requests to improve the script's user-friendliness or efficiency. 
