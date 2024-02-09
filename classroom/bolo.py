def slice_calc(num_people, cake_sizes):
    cake_sizes.sort()
    higher_value = cake_sizes[-1]

    while sum(i // higher_value for i in cake_sizes) < num_people: 
        higher_value -= 1

    return higher_value

    # Divide cada bolo por uma qtd de fatias que vai diminuindo até que a quantidade de fatias seja suficiente para todos os convidados.
    # Exemplo: num_people = 5, cake_sizes = [9, 7, 5]
    # 9//9 + 7//9 + 5//9 = 1 < num_people? N [...]
    # 9//3 + 7//3 + 5//3 = 6 < num_people? S
    
people_amount = int(input())
cake_amount = int(input())
cake_sizes = [int(i) for i in input().split()]

print(slice_calc(people_amount, cake_sizes))