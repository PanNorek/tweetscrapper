# tweetscrapper
A simple app for collecting tweets from Twitter API by given hashtags or account name

# Project Setup

<li>Create a virtual environment using <code> virtualenv venv </code>
<li>Activate the virtual environment by running <code> venv/bin/activate </code>
<li>On Windows use <code> venv\Scripts\activate.bat </code>
<li>Install the dependencies using <code> pip3 install -r requirements.txt </code>
<li>Run application using <code>python main.py </code>
<li>Run the test module using <code>python3 -m unittest</code>

# Usage
1. Login to your account on Twitter <a>https://twitter.com/login</a>
2. Create dev account <a>https://developer.twitter.com/en/portal/petition/essential/basic-info</a>
3. Create a new app and project.  <a>https://developer.twitter.com/en/portal/dashboard</a>
4. Copy all the keys from the app and paste them in the <code>api_keys.json</code> file (this version only needs the bearer token)
You can paste your keys in the <code>your_api_keys_sample.json</code> file and cut off 'your_' and '_sample' from the file name.
5. Change the <code>main.py</code> file to change the hashtahgs/account names and count.
5. Alternatively, you can manipulate the <code>config.json</code> file set the specified tweets you want to download.
6. Run the application using <code>python3 main.py </code>

You should see the tweets ids running in the console.
Sample photo: ![Screenshot4](/images/Screenshot1.png)

Sample csv file contents: ![Screenshot2](/images/Screenshot3.png)


# Updates

- [x] TrendLocator class is looking for top twitter trending topics in country you choose.
- [x] App could download tweets every n(15) minutes. 
- [x] App could be controlled by manipulating config.json file
- [ ] Upgrading api requests to be more stable
- [ ] Creating DataCollector class to store tweets in one csv file
