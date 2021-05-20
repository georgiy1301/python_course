with open('for_homework_2.txt', 'r', encoding='utf-8') as f:
    a = [f'{line}. {" ".join(count.split())} - {len(count.split())} слов ' for line, count in enumerate(f, 1)]
    print(*a, f'всего строк - {len(a)}.')