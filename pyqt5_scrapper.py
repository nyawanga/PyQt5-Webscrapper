import sys
import re
import PyQt5.QtCore as QC
import PyQt5.QtWidgets as QW
import PyQt5.QtWebEngineWidgets as QWEW
from bs4 import BeautifulSoup as bs
from lxml.html import fromstring

class Render(QWEW.QWebEnginePage):

    def __init__(self, url):
        self.app = QW.QApplication(sys.argv)
        QWEW.QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._load_finished)
        self.load(QC.QUrl(url))
        self.app.exec_()

    def processFinished(self, html):
        self.html = html
        self.app.quit()

    def _load_finished(self):
        self.html = self.toHtml(self.processFinished)


url = 'https://proxy-list.org/english/index.php'
app = None
def main():
    #this does the magic loads everything
    page = Render(url)
    return page

if __name__ == "__main__":
    res = main()
#    res = fromstring(res.html.toSting())
    soup = bs(res.html, 'html.parser')
    proxy_table = soup.find("div", {"class":"table"})
    rows = proxy_table.find_all("ul")
    for row in rows:
        details = row.find_all("li")
        ip = row.find("li", {"class":"proxy"}).get_text()
        ip = re.search(r"\d{1,2}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,4}", ip).group()
        https = row.find("li", {"class":"https"}).get_text()
        speed = row.find("li", {"class":"speed"}).get_text()
        type = row.find("li", {"class":"type"}).get_text()
        country = row.find("li", {"class":"country-city"}).get_text()

        print(ip, https, speed, type, country)

     #result is a QString.
#    result = result.toHtml()

     #QString should be converted to string before processed by lxml
     #formatted_result = str(result.toAscii())
#    formatted_result = str(result.encode('utf-8'))

     #Next build lxml tree from formatted_result
#    tree = html.fromstring(formatted_result)

     #Now using correct Xpath we are fetching URL of archives
#    archive_links = tree.xpath('//*[@id="proxy-table"]/div[2]/div/ul')
     #archive_links = tree.xpath('//div[@class="campaign"]/a/@href')
#    x_p = '//li[contains(@class, "proxy")]'
#    print(archive_links)
