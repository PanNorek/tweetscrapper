import requests
import re
from bs4 import BeautifulSoup
class TrendLocator:
    """
    A class which stores the data of today's top twitter trending topics in country you are looking for
    """
    def __init__(self, country:str="Poland", top_count:int=10)->None:
        self.country = country
        self.top_count = top_count

    def get_country(self)->str:
        return self.country

    def get_trends(self,count:int=None)->list:
        """
        Returns a list of trending hahtags in the country you are looking for
        """
        url = "https://twitter-trends.iamrohit.in/"
        url += str(self.country.lower())


        response = requests.get(url)

        soup = BeautifulSoup(response.content, "lxml")
        trends = [soup.find("a", id=f"hashtags-{i}").text for i in range(1, self.top_count+1)]
        trends = [re.sub(r'#', '', trend) for trend in trends]
        trends = [re.sub(r'\s+', '%20', trend) for trend in trends]

        
        return trends
        
    