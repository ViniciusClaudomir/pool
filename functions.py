from time import sleep

def somar(value1, value2):
    result = int(value1) + int(value2)
    sleep(result)
    return result
def subtrair(value1, value2):
    return int(value1) - int(value2)

FUNC = {

    'somar':somar,
    'subtrair':subtrair

}