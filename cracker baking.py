cracker_lovers=40
vanilla_lovers=64
oreo_lovers=20

chocolate_cracker=16
pumpkin_cracker=12
mango_cracker=12
berry_vanilla=12
apple_vanilla=10
banana_vanilla=10
smore_oreo=12

total_cracker = chocolate_cracker+pumpkin_cracker+mango_cracker

if total_cracker > 40:
    print(f'way too much by {total_cracker%40} crackers')
elif total_cracker == 40:
    print('just right amount of crackers')
else:
    print(f'short of crackers by {40-total_cracker}')