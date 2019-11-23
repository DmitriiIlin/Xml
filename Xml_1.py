import xml.etree.ElementTree as ETree

def get_information_from_file():
    xml1=ETree.parse('demo.xml')
    root=xml1.getroot()
    return root

def print_information():
    #names=["name"]
    information=get_information_from_file()
    for i in range(0,len(information)):
        print("-----------------")
        print("| Tag" +" " + information[i].tag.strip() + " " + information[i].text.strip() + " |")
        if len(information[i]) != 0:
            for j in range(0 , len(information[i])):
                if information[i][j].get("name") != None:
                    print("     " + information[i][j].get("name") + " " + information[i][j].text)
                else:
                    print("None")

def get_all_values_for_input_tag(input_information=None):
    #Формирует список значений для конкретного тега input_information
    tags_names=[]
    res=[]
    information=get_information_from_file()
    for i in range(0,len(information)):
        if information[i].tag.strip() not in tags_names:
            tags_names.append(information[i].tag.strip())
    #print(tags_names)
    if input_information in tags_names:
        for j in range(0,len(information)):
            if information[j].tag.strip() == input_information:
                if len(information[j]) > 0: 
                    for l in range(0,len(information[j])):
                        res.append(information[j][l].text)
                else:
                    res.append(information[j].text)
            else:
                pass
    else: 
        print("We dont have this TAG")
    return res
        
def q_ty_of_nodes(att=None):
    #Возвращает все узлы с атрибутом att
    information=get_information_from_file()
    nodes=[]
    nodes_with_att=[]
    for i in range(0,len(information)):
        nodes.append(information[i])
    for j in range(0,len(nodes)):
        if len(nodes[j]) == 0:
            pass
        else:
            for l in range(0,len(nodes[j])):
                nodes.append(nodes[j][l])
    #print(len(nodes),nodes)
    for everyelement in range(0,len(nodes)):
        if att in nodes[everyelement].attrib.keys():
            nodes_with_att.append(nodes[everyelement])
    return nodes_with_att







#print_information()
print(get_all_values_for_input_tag("pc"))
#print(q_ty_of_nodes("name"))