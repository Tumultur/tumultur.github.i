import pandas as pd
new = open("Entries.html", "w", encoding="utf8")
df = pd.read_csv("Entry_Metadata.csv")
link = df["Link"]
title = df["Title"]
eng = df["English"]
chn = df["Chinese"]
aut = df["Author"]
for i in range(0, len(df.index)):
    hyperlink = "<a class=\"entry-hyperlink\" href=\"%s\" target=_blank>%s</a>" % (link[i], title[i])
    description = "<p class=\"entry-description\">%s / %s</p>" % (eng[i], chn[i])
    author = "<p class=\"entry-author\">By %s</p>" % (aut[i])
    lines = "<div class=\"entry\">\n    %s\n    %s\n    %s\n</div>\n" % (hyperlink, description, author)
    new.write(lines)