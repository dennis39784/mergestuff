import argparse
from collections import OrderedDict

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file2merge", help="file argument to be merged with default")
    myargs = parser.parse_args()

    defDict = OrderedDict({})
    svrDict = OrderedDict({})
    targDict = OrderedDict({})

    with open(myargs.file2merge) as svrFile:
        with open("envDefault") as defFile:
            for line in defFile.readlines():
                line = line.replace(" ", "")
                defAttr, defValue = line.strip().split("=")
                defDict[defAttr] = defValue

            for sline in svrFile.readlines():
                sline = sline.replace(" ", "")
                svrAttr, svrValue = sline.strip().split("=")
                svrDict[svrAttr] = svrValue

            print("Default Keys: ", defDict.keys())
            print("Server: ", svrDict)

            for defkey, defitem in defDict.items():
                targKey = defkey
                targVal = svrDict.get(defkey,defitem)
                targDict[targKey] = targVal

            with open("envTarget", "w+") as targFile:
                for tAttr, tValue in targDict.items():
                    print(tAttr + " = " + tValue, file=targFile)

            # Now look for attributes in server specific files not in Default
            with open("envTarget", "a") as targFile:
                for svrAttr, svrValue in svrDict.items():
                    if svrAttr not in defDict:
                        targDict[svrAttr] = svrValue
                        print(svrAttr + " = " + svrValue, file=targFile)

            print("Note that the server specific attributes will be added to the end only")
            print("Target Dict: ", targDict.items())

main()
