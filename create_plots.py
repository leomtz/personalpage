from cvutils import *
cv=fetch_CV(r"data/CV.xlsx")
papers_timeline(cv, xkcd=False)
python_timeline(cv, xkcd=False)