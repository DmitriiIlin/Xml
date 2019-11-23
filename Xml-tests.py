import unittest, Xml_1

availible_tags=["name","age","sex","languages","pc"]
tags_value=[["Petya"],["23"],["true"],["9","7","8"],["Linux","Intel Core i7-8700","64","5000"]]
q_ty_of_tag_names=[7,0,0,0,0]

class Xml_Tests(unittest.TestCase):

    def test_for_second_task(self):
        #проверка списка всех значений (по всем узлам) для конкретного тега, если задано его название
        for i in range(0 , len(availible_tags)):
            res_1=Xml_1.get_all_values_for_input_tag(availible_tags[i])
            res_2=tags_value[i]
            print(res_1,res_2)
            self.assertEqual(res_1,res_2)
    
    def test_for_third_task(self):
         #Проверка ф-ции которая возвращает количество узлов в документе, включая дочерние, оснащённые заданным атрибутом
         for i in range(0 , len(availible_tags)):
             res_1=len(Xml_1.q_ty_of_nodes(availible_tags[i]))
             res_2=q_ty_of_tag_names[i]
             print(res_1,res_2)
             self.assertEqual(res_1,res_2)


if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()