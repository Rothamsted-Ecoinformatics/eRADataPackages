import json
import pandas

columns = []

data = pandas.read_csv("data/broadbalkWheatData.csv")

cols = list(data.columns)

for col in cols:
    print(col + ", data type =  " + str(data[col].dtype))
    coldesc = {"titles":col}
    val = input("description: ")
    if val:
        coldesc["dc:description"] = val

    dt = data[col].dtype
    if dt = "object":
        coldesc["datatype"] = "string"
    val = input("datatype: ")
    if val:
        coldesc["datatype"] = val
        
    val = input("unit: ")
    if val:
        coldesc["http://purl.org/linked-data/sdmx/2009/attribute#unitMeasure"] = {"@id":val}
    
        
    
    columns.append(coldesc)

md = {
    "@context":"http://www.w3.org/ns/csvw",
    "url":"data/broadbalkWheatData.csv",
    "dc:title":"Broadbalk wheat yield data, 1968 to 2018",
    "dc:description":"Winter wheat grain, nutrient and fertiliser data for continuous wheat (section 1) and first wheat in rotation (sections 2, 3, 4, 5, 7). Winter wheat varieties selected primarily for their yield potential and also for breadmaking qualities. Herbicides and pesticides are applied as required, including spring and summer fungicides. The plots are regularly limed. grain and straw nutrients are no measured for every year. 2015 was sown to spring wheat and is not included",
    "dc:creator":"Rothamsted Research"
}
md["tableSchema"] = {}
md["tableSchema"]["columns"] = columns

fout = open("data/metadata.json", "w")
fout.writelines(json.dumps(md, sort_keys=True, indent=4))
fout.close()