import random
char_array = ['A',"B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def generate_visit_id():
    visit_id = ""
    for i in range(3):
        visit_id += char_array[random.randint(0,25)]
    visit_id = visit_id + "-" + f'{random.randrange(1, 10**3):03}'
    return visit_id

print(generate_visit_id())