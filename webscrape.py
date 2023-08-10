import requests
import re
from bs4 import BeautifulSoup, NavigableString, Tag

#gets courses, units, and prereqs for each course required for a major from UC Davis website
def getDegreeReqs(URL, output_file):
    with open(output_file, "w") as f: 
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        
        #get Degree Requirements Table 
        tbody = soup.tbody  

        #get rows from table
        trs = tbody.contents

        #loop through each table row
        for tr in trs:
            if isinstance(tr, NavigableString): #skip NavigableStrings
                continue
            if isinstance(tr, Tag):
                for td in tr.contents: #Go through data in each row
                    link = td.a 
                    if link is None:
                        continue
                    else:
                        f.write(link.string + "  ")
                        prereq_url_ending = link.get('href')
                        prereq_url = "https://catalog.ucdavis.edu" + prereq_url_ending #full URL to course website containing prereq info
                        new_page = requests.get(prereq_url)
                        new_soup = BeautifulSoup(new_page.content, "html.parser")
                        prereqs = new_soup.find('p', attrs={"class": "text courseblockdetail detail-prerequisite"}) #find prereq info
                        units = new_soup.find(string=re.compile("^\([0-9]{1}\s[units]*\)$")) #number of units
                        f.write(units + "   ")
                        if prereqs is None:
                            f.write("Prerequisite(s): None\n\n")
                        else:
                            f.write(prereqs.text + "\n\n")

if __name__ == "__main__":
    ASE_URL = "https://catalog.ucdavis.edu/departments-programs-degrees/mechanical-aerospace-engineering/aerospace-science-engineering-bs/#requirementstext"
    getDegreeReqs(ASE_URL, "ASE_deg_reqs.txt")



        