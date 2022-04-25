"Criando uma lista de tipos mistos"
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    value_index = myMixedTypeList.index(item)
    print('Index: {}'.format(value_index))
    print('Valor: {}'.format(myMixedTypeList[value_index]))
    print("{} é um dado do tipo {}".format(item,type(item)))