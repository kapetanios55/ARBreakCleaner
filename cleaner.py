dirtyAnalytic = "<InsertAnalyticRuleHere>"

commentindex=dirtyAnalytic.find("//")

while (commentindex != -1):
    stringa= dirtyAnalytic[:commentindex-1]
    stringb= dirtyAnalytic[commentindex:]
    
    stringa=stringa.replace("\r\n", "")
    dirtyAnalytic=stringa+stringb
    commentindex=dirtyAnalytic.find("//")

    
    endofstringindex=dirtyAnalytic.find("\r\n")
    substring1 = dirtyAnalytic[commentindex:endofstringindex]
    
    dirtyAnalytic=dirtyAnalytic.replace(substring1,"")


step1string=dirtyAnalytic.replace("\r\n","")
cleanAnalytic= step1string.replace('\"','"')

print (cleanAnalytic)
