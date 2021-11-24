from copy import deepcopy
list_foci=["Erbschaftssteuerrecht","Erbrecht"]
list_size=len(list_foci)
dynamic_list={
  "arr": [
    {
      "title": "What time do you want your appointment?",
      "options": "foci",
      "description": "",
      "response_type": "option"
    }
  ]
}
foci=[
    {
        "label": "Monday 1:00 pm",
        "value": {
            "input": {
                "text": "Monday 1:00 pm"
            }
        }
    }
]
copy_size=list_size-1
for x in range(copy_size):
    foci.append(deepcopy(foci[0]))
print(copy_size)
for foci_value in range(list_size):
    foci[foci_value]['label']=list_foci[foci_value]
    foci[foci_value]['value']['input']['text']=list_foci[foci_value]
print(foci)

#index 0
#print(dynamic_list)
#dynamic_list['arr'][0]['options'][0]['label']=dynamic_list['arr'][0]['options'][0]['label']="ABC"
#dynamic_list['arr'][0]['options'][0]['label']=dynamic_list['arr'][0]['options'][0]['value']['input']['text']="DEF"
###index 1
#dynamic_list['arr'][0]['options'][1]['label']=dynamic_list['arr'][0]['options'][1]['label']="GHI"
#dynamic_list['arr'][0]['options'][0]['label']=dynamic_list['arr'][0]['options'][1]['value']['input']['text']="JKL"
#print(dynamic_list)