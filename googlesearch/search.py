import sys, webbrowser
querytext=sys.argv[1:]
webbrowser.open('https://google.com/search?q='+''.join(querytext))
