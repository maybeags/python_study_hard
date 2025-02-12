'''
chapter07_hangman 내에 hangman_complete 패키지 생성
hangman06.py을 옮기겠습니다.

hangman_arts.py 파일 생성       -> hangman05.py에 있던 logo / stages를 복사
hangman_word_list.py 파일 생성  -> hangman05.py에 있던 word_list를 복사

그리고 나머지 부분을 hangman06.py에 전부 복사

import 배웠습니다.
word_list에 나온 오류를 없애기 위한 코드를 작성하세요.

hangman07.py 생성
'''
import random
import hangman_arts
import hangman_word_list

end_of_game = False
lives = 6
chosen_word = random.choice(hangman_word_list.word_list)
# print(f"테스트 코드 : {chosen_word}")
display = []

for letter in chosen_word:
    display.append("_")

print(hangman_arts.logo)
while not end_of_game:

    guess = input("알파벳 입력하세요 >>> ").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f"당신의 기회는 {lives}번 남았습니다.")
        if lives == 0:
            print("모든 기회를 잃었습니다.")
            end_of_game = True
            print(f"정답은 {chosen_word}입니다.")

    if "_" not in display:
        print("정답입니다:)")
        end_of_game = True

    print("/".join(display))
    print(" ".join(display))
    print(hangman_arts.stages[lives])