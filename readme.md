<h1>
Upwork Selenium Bot
</h1>

<h3> This bot uses Selenium to make the get requests then passes the html file to the scraper which then scrapes all the data.<br>
The scraper then returns the results in a json like format of list, with each element of list being a dictionary. 
It looks something like this:


</h3>

<h2>Setting up the repo
</h2>
  
  <h3>Make sure you've installed everything from requirements.txt
  
  <ul>
  <li>
  To install, use a virtual environment and open the project directory in cmd and use<br>
 </li>
  <li>
  pip install -r requirements.txt
  </li>
  <li>
  After that, go to 'C:\Program Files (x86)\chromedriver.exe' and paste the chrome driver to setup the selenium driver
  </li>
  </h3>

<h2 style =  "text-align: center;">
How to use the bot
</h2>

<h3>
<ul>
<li>To use the bot, open the main.py file
</li>
<li>main.py file has two global variable bindings, the first one is query and the second one is num_pages. 
Write the keyword you want to search in the query and the number of pages should be an int.

Example:
If you want to search: Devops and scrpae 5 pages then write
query = 'Devops'
num_pages = 5

</li>


<li>
Run the main.py file in your ide and type main() in the interpreter, the bot will start scraping
</li>


<li>
  If you want to get all the details instead of just getting the name, url, title and position you can simply pass an additional argument <br>
  get_all_details = True<br>
  to the <br>
  get_freelance_details method of the scraper<br>
  
  So, instead of writing<br>
  freelancers +=scraper.get_freelance_details()
  <br>
  you can write 
  <br>
  freelancers +=scraper.get_freelance_details(get_all_details = True)
  <br>
   in the main.py module and the scraper will get all the details.
 </li>










