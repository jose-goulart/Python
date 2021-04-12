def getInput(question, type, repeater, min, max):
    i = 0
    array = []
    while(i < repeater):
        a = type(input(f"{question}"))
        if(type == int or type == float):
            if(a >= min and a <= max):
                array.append(a)
                i += 1
            else:
                if(type == int):
                    print(
                        f"Digite um inteiro maior ou igual a {min} e menor ou igual a {max}")
                elif(type == float):
                    print(
                        f"Digite um número maior que {min} e maior que {max}")
        else:
            array.append(a)
            i += 1
    return array


# def getSplitInput(question, type, split, repeater, min, max):
#     array = []
#     finalArray = []
#     i = 0
#     while(i < repeater):
#         array = [type(x) for x in input().split(split)]
#         i += i
#     for j in range(len(array)):
#         if(type == int or type == float):
#             if(array[j] >= min and array[j] <= max):
#                 finalArray.append(array[j])
#             else:
#                 if(type == int):
#                     print(
#                         f"Digite um inteiro maior ou igual a {min} e menor ou igual a {max}")
#                 elif(type == float):
#                     print(
#                         f"Digite um número maior que {min} e maior que {max}")
#         else:
#             finalArray.append(array[j])
#         return finalArray


# a = getSplitInput("Digite um inteiro: ", str, " ", 3, 1, 50)
# print(a)
