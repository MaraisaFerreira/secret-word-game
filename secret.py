secret_pass = 'software'
chances = 5

correct_letters = []

while True:
    if chances <= 0:
        print('\n***** Você Perdeu! *****')
        break

    secret_template = ''
    for c in secret_pass:
        if c in correct_letters:
            secret_template += c
        else:
            secret_template += '-'

    print(f'\nPalavra Secreta: {secret_template}\n')

    if secret_template == secret_pass:
        print(f'***** Você Venceu! *****')
        break

    char = input('Digite 1 letra: ')
    char = char.lower()

    if len(char) > 1 or not char or char.isdigit():
        print('Você só pd escolher 1 letra.')
        continue
    else:

        if char in secret_pass:
            correct_letters.append(char)

            print(f'Correto, A letra "{char}", existe na palavra.')

        else:
            chances -= 1
            print(f'A letra "{char}" não existe na palavra secreta.\nVocê ainda tem mais {chances} chances.')




