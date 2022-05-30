import pandas as pd
new = open("Entries.html", "w", encoding="utf8")
df = pd.read_csv("Entry_Metadata.csv")
link = df["Link"]
title = df["Title"]
eng = df["English"]
chn = df["Chinese"]
aut = df["Author"]
for i in range(0, len(df.index)):
    hyperlink = "<a target=_blank, href=\"%s\">%s</a>" % (link[i], title[i])
    description = "<p>%s / %s</p>" % (eng[i], chn[i])
    author = "<p class=\"Author\">By %s</p>" % (aut[i])
    lines = "<div class=\"Entry\">\n    %s\n    %s\n    %s\n</div>\n" % (hyperlink, description, author)
    new.write(lines)