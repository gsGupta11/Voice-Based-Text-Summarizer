def CreateFile(data,title):
    try:
        name ="../results/"+title+"_summary.txt"
        f = open(name, "w")
        f.write(data)
        f.close()
        return "File Successfully Written"
    except:
        return "Error! While Writing File"
