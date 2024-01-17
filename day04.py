drinks_foods = {"위스키": "초콜릿", "와인": "치즈", "소주": "삼겹살", "고량주": "양꼬치"}

# drink = input(drinks_foods.keys())
drinks_foods_keys = list(drinks_foods)
# print(drinks_foods_keys)

while True:
    menu = input(f'다음 술중에 고르세요.\n1){drinks_foods_keys[0]}, 2){drinks_foods_keys[1]}, 3){drinks_foods_keys[2]}, 4){drinks_foods_keys[3]}, 5) 종료 : ')
    if menu == '1':
        print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[0]]}입니다.\n')
    if menu == '2':
        print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[1]]}입니다.\n')
    if menu == '3':
        print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[2]]}입니다.\n')
    if menu == '4':
        print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[3]]}입니다.\n')
    if menu == '5':
        print(f'다음에 또 오세요\n')
        break
