# gap = "Bu gapda faqat shu so'z rangli bo'ladi."
# soz = "shu"

# # ANSI escape kodidan foydalanamiz
# qizil = "\033[31m"
# tugat = "\033[0m"

# # Gapni bo'lib, rangni qo'llaymiz
# qismlar = gap.split(soz)
# print(f"{qismlar[0]}{qizil}{soz}{tugat}{qismlar[1]}")

def sontop_PC(x) :
 """이 함수에서 컴퓨터는 1에서 x까지의 숫자를 생각합니다.
 그리고 사용자는 그 숫자를 찾아야 합니다. 인수로서
 x는 기본값 10이 지정됩니다.
 바꿀 수 있어요.
 예를 들어: sontop_PC(50) " 여기
 1에서 50까지의 숫자가 플레이됩니다.
 """
 # 게임을 시작하자, 컴퓨터가 숫자를 생각해 냈습니다.
 console.print(f"\n1부터 {x}까지의 숫자가 생각났습니다. 찾아보세요", style='bold yellow')
 # 숫자는 무작위로 선택됩니다
 숫자 = r.randint(1, x)

 # 루프를 멈추기 위해 플래그를 사용합니다.
 플래그 = 1

 # 추측은 0부터 시작합니다
 추측 사용자 = 0

 # 시작
 플래그 동안:
 숫자 출력
 답변 = 입력(">>>\n")

 # 정답 숫자를 확인할 수 있습니다
 answer.isdigit()인 경우:

 답변 = int(답변)
 답변이 숫자 <인 경우:
 console.print(f"제가 생각해 낸 숫자는 {answer}보다 큽니다", style='bold yellow')
 추측 사용자 += 1
 elif 정답 > 번호:
 console.print(f"제가 생각한 숫자는 {answer}보다 작습니다", style='bold yellow')
 추측 사용자 += 1
 elif 정답 == 숫자:
 console.print("찾으셨습니다", style='rgb(0,255,0) bold')
 추측 사용자 += 1
 플래그 = 0

 # 숫자가 없으면...
 또 다른:
 print("정수를 입력하세요")

 # 함수가 종료되고 사용자가 추측한 횟수를 반환합니다.
 guess_user를 반환합니다.