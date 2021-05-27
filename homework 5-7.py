import json
with open('for_homework_7.json', 'w') as fw:
    with open('for_homework_7.txt', encoding='utf-8') as f:
        prof = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
        res = [prof, {'av_prof': round(sum([int(i) for i in prof.values() if int(i) > 0]) /
                                                   len([int(i) for i in prof.values() if int(i) > 0]))}]

    json.dump(res, fw, ensure_ascii=False, indent=4)