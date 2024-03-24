from bs4 import BeautifulSoup
import pandas as pd

class mtkUnit():

    def writeToHtml(self, id, data) -> None:
        path = '.\\output\\{}.html'.format(id)
        with open(path, "a", encoding='UTF-8') as f:
            f.write(data)
            f.close()

    def readFromHtml(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return (f.read())
        
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
    
    def htmlTableParser(self, target):
        df = pd.DataFrame()
        for t in target:
            data = []
            idx = 0
            for row in t.find_all('tr'):
                row_data = []
                if idx == 0:
                    idx = 1
                    for cell in row.find_all('th'):
                        row_data.append(cell.text)
                else:
                    for cell in row.find_all('td'):
                        row_data.append(cell.text)
                if len(row_data) == 4:
                    data.append(row_data)
            sub = pd.DataFrame(data)
            df = pd.concat([df, sub], ignore_index=True)
       
        return df