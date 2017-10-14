urlfh = open("urls")

newWin = True

for url in urlfh:
    u = url[:-1]

    if u == '':
        newWin = True
    else:
        if newWin:
            print()
            print("firefox --new-window %s" % u)

            newWin = False
        else:
            print("firefox --new-tab %s" % u)

urlfh.close()

