###############################################################
# 소수 판별 함수
import math

def is_prime_number(x):
    # 2부터 (x-1)까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    
    return True



print(is_prime_number(4))
print(is_prime_number(7))


###############################################################
# 에라토스테네스의 체
import math

n = 1000 # 2부터 1000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수인 것으로 초기화(0과 1은 제외)

for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n+1):
    if array[i]:
        print(i, end = ' ')