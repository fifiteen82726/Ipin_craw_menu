# 把json 匯出
import json

open the file "filename" in write ("w") mode
file = open("result.json", "w")
just an example dictionary to be dumped into "filename"
output = {
 "contents": [
    {
      "name": "Pork",
      "productName": ["Pork noodle", "Pork rice"]
     
    },
    {
      "name": "Beef",
      "productName": ["Beef n", "Beed fuck"]
    }
  ]
}
dumps "output" encoded in the JSON format into "filename"
json.dump(output, file)
file.close()