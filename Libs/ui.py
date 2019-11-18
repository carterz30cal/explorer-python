def Menu(data,title="",numbered=False,filler=".",up="|",across="-",corner="0"):
    longest=len(title)
    for d in range(len(data)):
        dl = len(data[d])
        if dl > longest:
            longest = dl
        if dl % 2 == 1:
            data[d] = data[d] + filler
        if numbered:
            data[d] = str(d+1) + "-" + data[d]
        """
        #changes spaces to be filler, i decided that spaces looked nicer, might become an option when formatting is necessary
        ndata = ""
        for l in data[d]:
            if l == " ":
                ndata = ndata + l
            else:
                ndata = ndata + l
        data[d] = ndata
        """
    longest = longest + 2
    if (longest%2) == 1:
        longest = longest + 1
    ret = corner + across*longest + corner
    if not title == "":
        ret = ret + "\n" + up + int((longest-len(title))/2)*filler + title + int((longest-len(title))/2)*filler + up
    else:
        ret = ret + "\n" + up + longest*filler + up
    for d in data:
        okboomer = int((longest-len(d))/2)*filler
        ret = ret + "\n" + up + okboomer + d + okboomer + up
    #ret = ret + "\n" + up + longest*filler + up
    ret = ret + "\n" + corner + across*longest + corner
    print(ret)

#Menu(["hhhhhhh","oh hai guys","wasson my epic dudes"],"A graph to show epicness",True)
# Test menu thingymobob
