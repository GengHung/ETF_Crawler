import mysql.connector as connection
import pandas as pd
# for test two datafrom merge
if __name__ == '__main__':
    try:
        conn = connection.connect(
            host='localhost',
            user='mtkuser',
            password='86136982',
            database='crawler'
        )

        sqlcmd = 'select A, B, C from tt'
        df = pd.read_sql(sqlcmd, conn)
        result = df[df['C']== True]
        idxs = df.index[df['C'] == True].tolist()
        print(idxs)
        df = df.drop(index=idxs)
        #for r in result:
        result['aud'] = 'U'
        #print (result)
        df = pd.concat([df, result])
        print(df)
        df.to_csv('./dd.csv', index=False)
        

    except Exception as e:
        conn.close()
        print(str(e))
