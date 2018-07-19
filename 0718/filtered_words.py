'''
将敏感字替换为***
'''
with open('filtered_words.txt', 'r', encoding='utf-8') as f:
    filter_words = f.readlines()
value = input('请输入： ')
for word in filter_words:
    result = word.strip('\n')
    if result in value:
        value = value.replace(result, len(result)*'*')
print(value)

