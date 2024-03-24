from playwright.sync_api import Playwright, sync_playwright, expect
from bs4 import BeautifulSoup

class Crawler():
    url = None
    m_headless = False
    id = None
    output = '.\\output\\'

    def run(self, playwright: Playwright) -> None:
        if self.url != None and self.id !=None:
            print('cell run url {}{}'.format(self.url, self.id,))
            browser = playwright.chromium.launch(headless=self.m_headless)
            context = browser.new_context()
            page = context.new_page()

            page.goto(self.url + self.id)
            page.get_by_text("持股比重").first.click()
            page.get_by_role("cell", name="查看更多").get_by_role("paragraph").click()
            html = page.content()
            
            # ---------------------
            context.close()
            browser.close()
            return html
  
        return None
    
    def parserHtmltoCSV(self, path, data):
        soup = BeautifulSoup(data, "html.parser")
        tables = soup.find_all(class_='v-table-cell')
        for t in tables:
            #print("================")
            print(t.getText())
        
        tls = soup.find_all(class_='table-list')
        df = self.htmlTableParser(tls)
        #print (df)
        #print (path)
        df.to_csv(path, index = False, header=False)

    def getData(self, id):
        self.id = id
        with sync_playwright() as playwright:
            source = self.run(playwright)
            if source != None:
                out = '{}{}.csv'.format(self.output, self.id)
                #print(out, str(source))
                self.parserHtmltoCSV(out, str(source))
                return '{"ret":200, "msg":"done!!"}'
            
            return '{"ret":400, "msg":"Crawler data faild!!"}'
        
    def setHeadless(self, _headless=False):
        self.m_headless = _headless
        print(' headless:{} ', self.m_headless)