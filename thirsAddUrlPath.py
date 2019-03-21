from flask import Flask
app=Flask(__name__)

def urlAddPath():
    return "After adding of URL routing i.e. another way  of using routing apart from using decorator"

def urlAddRule(enter):
    return "Dynamic Web Page creation and you have added this %s endpoint string"%enter
app.add_url_rule('/','',urlAddPath)
app.add_url_rule('/<enter>','enter',urlAddRule)
if __name__=='__main__':
    app.run(debug=True)
