from etl import Spy


a = Spy()
a.composer(["https://xml2.txodds.com/feed/odds/apmarkets.php?ident=huanhuba&passwd=7898789",
            "https://xml2.txodds.com/feed/odds/ap.php?ident=huanhuba&passwd=7898789&pgid=54209"], method='GET', headers=None)

for i in a.run(verify=True):
    print(i.url)
    print(i.response)
    print(i.status)
    print()