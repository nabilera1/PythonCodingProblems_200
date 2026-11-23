# 기초 051–075
from testlib import G

PROBLEMS = [
# ───────────────── 11 리스트 Ⅰ ─────────────────
dict(
    id=51, title="봉우리 XV",
    story="19세기 중반 인도 측량국은 히말라야의 봉우리들에 번호만 붙여 두고 높이를 계산했습니다. 1852년 무렵, 계산 결과 '봉우리 XV'가 세계에서 가장 높다는 사실이 드러났습니다. 오늘날 에베레스트라 부르는 산입니다.",
    task="첫째 줄에 봉우리의 수 N, 둘째 줄에 N개의 높이가 주어집니다. 가장 높은 높이와, 그 높이가 **처음** 나타나는 위치(1부터 셈)를 공백으로 구분해 출력하십시오.",
    constraints="1 ≤ N ≤ 1000, 각 높이는 1 이상 10000 이하의 정수",
    examples=[("5\n8586 8848 8516 8848 8485", "8848 2")],
    hidden=["1\n100", "3\n5 4 3", "4\n1 2 3 4", "6\n7 7 7 7 7 7"],
    hint="`max(리스트)`로 최댓값을, `리스트.index(값)`으로 그 값이 처음 나오는 위치를 얻을 수 있습니다. 위치는 0부터 세므로 1을 더하십시오.",
    solution="n = int(input())\nheights = list(map(int, input().split()))\nbest = max(heights)\nprint(best, heights.index(best) + 1)",
    explanation="`index()`는 앞에서부터 찾아 처음 일치하는 위치를 돌려주므로 '처음 나타나는 위치'라는 조건이 저절로 만족됩니다. "
                "리스트를 두 번 훑는 풀이이지만 충분히 빠릅니다. 한 번만 훑고 싶다면 21번처럼 '지금까지의 최댓값과 그 위치'를 들고 다니면 됩니다. 이때 같은 값이 나와도 기록을 바꾸지 않도록 `>`를 써야 합니다.",
),
dict(
    id=52, title="평균보다 높은 학생",
    story="'평균 이상'이라는 말은 흔히 쓰이지만, 실제로 평균보다 높은 사람이 몇 명인지는 자료의 모양에 따라 크게 달라집니다. 한 명이 아주 높은 점수를 받으면 나머지 대부분이 평균 아래에 놓이기도 합니다.",
    task="첫째 줄에 학생 수 N, 둘째 줄에 N개의 점수(정수)가 주어집니다. 점수가 평균보다 **엄격하게 큰** 학생 수를 출력하십시오.",
    constraints="1 ≤ N ≤ 1000, 0 ≤ 점수 ≤ 100",
    examples=[("5\n50 50 70 80 90", "3"), ("4\n10 10 10 100", "1")],
    hidden=["1\n70", "3\n1 2 3", "3\n0 0 1", "6\n100 100 100 100 100 100", "7\n33 33 34 33 33 33 34"],
    hint="평균을 먼저 구한 뒤 리스트를 다시 훑으며 세십시오. 실수 비교가 걱정된다면 `점수 × N > 총합`으로 정수끼리 비교할 수 있습니다.",
    solution="n = int(input())\nscores = list(map(int, input().split()))\ntotal = sum(scores)\nprint(sum(1 for s in scores if s * n > total))",
    explanation="`s > total / n` 대신 양변에 n을 곱한 `s * n > total`을 쓰면 실수 오차가 끼어들 틈이 없습니다. 나눗셈을 곱셈으로 바꾸는 이 요령은 경시 문제에서 자주 쓰입니다. "
                "`sum(1 for ... if ...)`는 조건을 만족하는 원소의 개수를 셉니다. 반복문과 카운터 변수로 풀어도 물론 좋습니다.",
),
dict(
    id=53, title="회전 초밥",
    story="회전 초밥집의 레일은 원형이라 끝과 처음이 이어져 있습니다. 리스트를 오른쪽으로 한 칸 돌리면 마지막 원소가 맨 앞으로 옵니다. 원소가 N개라면 N칸을 돌렸을 때 제자리로 돌아옵니다.",
    task="첫째 줄에 N과 k, 둘째 줄에 N개의 정수가 주어집니다. 리스트를 오른쪽으로 k칸 회전한 결과를 출력하십시오.",
    constraints="1 ≤ N ≤ 1000, 0 ≤ k ≤ 10⁹",
    examples=[("5 2\n1 2 3 4 5", "4 5 1 2 3"), ("3 7\n10 20 30", "30 10 20")],
    hidden=["1 1000000000\n42", "4 0\n1 2 3 4", "4 4\n1 2 3 4", "6 1000000000\n1 2 3 4 5 6"],
    hint="k칸 회전은 `k % N`칸 회전과 같습니다. 오른쪽으로 k칸 돌리면 뒤쪽 k개가 앞으로 옵니다. 슬라이싱 두 개를 이어 붙이십시오.",
    solution="n, k = map(int, input().split())\na = input().split()\nk %= n\nprint(*(a[n - k:] + a[:n - k]))",
    explanation="10억 칸을 실제로 한 칸씩 돌리면 시간이 한참 걸리지만, `k % N`을 쓰면 회전은 언제나 N칸 미만으로 줄어듭니다. "
                "`a[-k:] + a[:-k]`로 써도 되지만 k가 0일 때 함정이 있습니다. `a[-0:]`은 리스트 전체이고 `a[:-0]`은 빈 리스트가 되기 때문입니다. 이 경우는 우연히 결과가 맞지만, 위처럼 `n - k`로 쓰면 그런 고민이 필요 없습니다. "
                "`collections.deque`의 `rotate(k)`도 같은 일을 합니다.",
),
dict(
    id=54, title="통장의 잔액",
    story="복식부기 장부에는 거래 하나하나와 함께 그 시점의 잔액이 적힙니다. 잔액은 처음부터 그때까지의 거래를 모두 더한 값, 곧 **누적합**입니다. 누적합은 제3부에서 가장 먼저 만나는 기법이기도 합니다.",
    task="첫째 줄에 거래 수 N, 둘째 줄에 N개의 거래 금액(입금은 양수, 출금은 음수)이 주어집니다. 잔액은 0원에서 시작합니다. "
         "첫째 줄에 각 거래 직후의 잔액을 차례로, 둘째 줄에 그 가운데 **가장 낮았던 잔액**을 출력하십시오.",
    constraints="1 ≤ N ≤ 1000, |금액| ≤ 10⁶",
    examples=[("4\n1000 -300 -900 500", "1000 700 -200 300\n-200")],
    hidden=["1\n-5", "3\n10 20 30", "5\n-1 -1 -1 -1 -1", "2\n1000000 -1000000"],
    hint="`balance` 변수에 거래를 하나씩 더하면서 그때마다 결과 리스트에 `append()` 하십시오.",
    solution="n = int(input())\nbalance = 0\nhistory = []\nfor x in map(int, input().split()):\n    balance += x\n    history.append(balance)\nprint(*history)\nprint(min(history))",
    explanation="리스트를 빈 상태로 만들고 `append()`로 하나씩 채워 가는 것은 가장 기본적인 리스트 사용법입니다. "
                "표준 라이브러리 `itertools.accumulate(거래들)`가 정확히 이 누적합을 만들어 줍니다. "
                "누적합 리스트가 있으면 'i번째부터 j번째 거래까지의 합'을 뺄셈 한 번으로 구할 수 있습니다. 이 사실은 151번 문제에서 큰 힘을 발휘합니다.",
),
dict(
    id=55, title="은메달",
    story="올림픽에서 공동 1위가 나오면 은메달 없이 곧바로 동메달로 넘어가기도 합니다. '두 번째로 큰 값'을 물을 때는 같은 값을 어떻게 다룰지부터 정해야 합니다.",
    task="첫째 줄에 N, 둘째 줄에 N개의 정수가 주어집니다. **서로 다른 값들 가운데** 두 번째로 큰 값을 출력하십시오. 서로 다른 값이 하나뿐이면 `없음`을 출력합니다.",
    constraints="1 ≤ N ≤ 1000, |각 수| ≤ 10⁹",
    examples=[("5\n3 9 9 4 1", "4"), ("3\n7 7 7", "없음")],
    hidden=["1\n5", "2\n1 2", "2\n2 1", "6\n-5 -1 -1 -3 -1 -5", "4\n1000000000 -1000000000 0 0"],
    hint="중복을 없앤 뒤 정렬하면 뒤에서 두 번째 원소가 답입니다. `set()`으로 중복을 없앨 수 있습니다.",
    solution='n = int(input())\nvalues = sorted(set(map(int, input().split())))\nprint(values[-2] if len(values) >= 2 else "없음")',
    explanation="`set`은 중복을 허락하지 않는 자료형입니다(제13단원에서 자세히 다룹니다). 정렬하지 않고 한 번만 훑는 방법도 있습니다. `first`와 `second` 두 변수를 두고, 새 값이 first보다 크면 first를 second로 내리면 됩니다. "
                "이 방법은 N이 아주 클 때 유리합니다. 직접 구현해 보고 `3 9 9 4 1`에서 9가 두 번 나올 때 어떻게 처리해야 하는지 확인해 보십시오.",
),
# ───────────────── 12 리스트 Ⅱ ─────────────────
dict(
    id=56, title="중앙값의 힘",
    story="어느 마을 주민 아홉 명의 평균 재산이 어느 날 갑자기 열 배로 뛰었습니다. 억만장자 한 명이 이사 왔기 때문입니다. 이럴 때도 줄을 세워 한가운데 사람을 보는 **중앙값**은 거의 변하지 않습니다. 극단값에 흔들리지 않는 대푯값입니다.",
    task="첫째 줄에 홀수 N, 둘째 줄에 N개의 정수가 주어집니다. 중앙값을 출력하십시오.",
    constraints="1 ≤ N ≤ 10⁵ (N은 홀수), |각 수| ≤ 10⁹",
    examples=[("5\n7 1 3 1000000000 2", "3")],
    hidden=["1\n-4", "3\n3 2 1", "7\n5 5 5 1 9 9 9", G("n = 99999\nprint(n)\nprint(*[random.randint(-10**9, 10**9) for _ in range(n)])", 1)],
    hint="정렬한 뒤 가운데 인덱스 `N // 2`의 원소를 고르십시오.",
    solution="n = int(input())\na = sorted(map(int, input().split()))\nprint(a[n // 2])",
    explanation="`sorted()`는 새 리스트를 돌려주고, `리스트.sort()`는 원래 리스트를 제자리에서 정렬합니다. 원본을 보존해야 하는지에 따라 골라 쓰십시오. "
                "파이썬의 정렬은 2002년 팀 피터스가 만든 **Timsort**로, 10만 개를 정렬하는 데 0.1초도 걸리지 않습니다. 표준 라이브러리 `statistics.median()`도 있습니다.",
),
dict(
    id=57, title="안정 정렬",
    story="파이썬의 정렬은 **안정적(stable)** 입니다. 기준값이 같은 원소들은 정렬 전의 순서를 그대로 지킵니다. 이 성질을 이용하면, 덜 중요한 기준으로 먼저 정렬한 뒤 더 중요한 기준으로 다시 정렬하는 방식으로 여러 기준을 한꺼번에 처리할 수 있습니다.",
    task="영어 단어들이 한 줄에 공백으로 구분되어 주어집니다. 단어를 **길이가 짧은 순서**로, 길이가 같으면 **사전 순서**로 정렬해 출력하십시오.",
    constraints="단어는 1개 이상 1000개 이하, 영어 소문자",
    examples=[("banana kiwi apple fig cherry date", "fig date kiwi apple banana cherry")],
    hidden=["a", "bb a ccc", "cab abc bca", "python is a very elegant language"],
    hint="먼저 `sort()`로 사전 순 정렬을 한 뒤, `sort(key=len)`으로 길이 순 정렬을 하십시오. 두 번째 정렬이 첫 번째 정렬의 순서를 망가뜨리지 않는 이유를 생각해 보십시오.",
    solution="words = input().split()\nwords.sort()\nwords.sort(key=len)\nprint(*words)",
    explanation="두 번째 정렬에서 길이가 같은 단어들은 안정성 덕분에 첫 번째 정렬이 만든 사전 순서를 그대로 유지합니다. "
                "`key=len`은 '각 원소에 `len`을 적용한 값으로 비교하라'는 뜻입니다. "
                "제16단원에서 람다를 배우면 `words.sort(key=lambda w: (len(w), w))` 한 번으로 끝낼 수 있습니다.",
),
dict(
    id=58, title="시상대",
    story="시상대에는 세 사람만 오릅니다. 점수가 같을 때 누구를 먼저 부를지 정해 두지 않으면 순위가 매번 달라질 수 있습니다. 좋은 문제는 이런 모호함을 남기지 않습니다.",
    task="첫째 줄에 참가자 수 N, 이어서 N줄에 `이름 점수`가 주어집니다. 점수가 높은 순서로, 점수가 같으면 이름의 사전 순서로 상위 3명을 한 줄에 하나씩 `이름 점수` 형식으로 출력하십시오.",
    constraints="3 ≤ N ≤ 1000, 이름은 서로 다른 영어 소문자, 0 ≤ 점수 ≤ 100",
    examples=[("5\nkim 90\nlee 95\npark 90\nchoi 80\nhan 95", "han 95\nlee 95\nkim 90")],
    hidden=["3\na 1\nb 2\nc 3", "4\nzed 50\namy 50\nbob 50\ncat 50", "4\nx 0\ny 100\nz 0\nw 99"],
    hint="`(-점수, 이름)` 쌍을 리스트에 담아 정렬하십시오. 점수에 마이너스를 붙이면 높은 점수가 앞으로 옵니다.",
    solution="n = int(input())\nrecords = []\nfor _ in range(n):\n    name, score = input().split()\n    records.append((-int(score), name))\nrecords.sort()\nfor neg, name in records[:3]:\n    print(name, -neg)",
    explanation="튜플은 앞 원소부터 차례로 비교되므로(18번 참고), `(-점수, 이름)`으로 정렬하면 '점수 내림차순, 이름 오름차순'이 한 번에 됩니다. "
                "부호를 뒤집는 요령은 숫자에만 쓸 수 있습니다. 문자열을 내림차순으로 정렬해야 한다면 57번처럼 안정 정렬을 두 번 하거나, `reverse=True`를 섞어 써야 합니다.",
),
dict(
    id=59, title="슬라이싱 연습장",
    story="슬라이싱 `[시작:끝:보폭]`은 파이썬이 가장 자랑하는 문법 가운데 하나입니다. 세 수만으로 앞부분, 뒷부분, 띄엄띄엄, 거꾸로를 모두 표현합니다.",
    task="첫째 줄에 N, 둘째 줄에 N개의 정수가 주어집니다. 다음 네 줄을 출력하십시오.\n\n"
         "1. 앞의 3개  2. 뒤의 3개  3. 짝수 번째 인덱스(0, 2, 4, …)의 원소  4. 전체를 거꾸로",
    constraints="3 ≤ N ≤ 100",
    examples=[("6\n10 20 30 40 50 60", "10 20 30\n40 50 60\n10 30 50\n60 50 40 30 20 10")],
    hidden=["3\n1 2 3", "4\n4 3 2 1", "7\n1 1 2 3 5 8 13"],
    hint="`a[:3]`, `a[-3:]`, `a[::2]`, `a[::-1]`.",
    solution="n = int(input())\na = input().split()\nprint(*a[:3])\nprint(*a[-3:])\nprint(*a[::2])\nprint(*a[::-1])",
    explanation="슬라이싱은 범위를 벗어나도 오류를 내지 않습니다. 리스트가 2개뿐이어도 `a[:3]`은 오류 없이 2개만 돌려줍니다. 반면 `a[5]`처럼 인덱스로 하나를 꺼낼 때는 `IndexError`가 납니다. "
                "또 슬라이싱 결과는 **새 리스트**입니다. 그래서 `b = a[:]`는 리스트를 복사하는 관용구로 쓰입니다.",
),
dict(
    id=60, title="폰 노이만의 병합",
    story="1945년 존 폰 노이만은 정렬된 두 묶음을 하나로 합치는 **병합(merge)** 을 바탕으로 한 정렬법을 고안했습니다. 두 줄의 맨 앞만 비교해 더 작은 쪽을 하나씩 꺼내는 것, 그것이 전부입니다.",
    task="첫째 줄에 N과 M, 둘째 줄에 오름차순으로 정렬된 N개의 정수, 셋째 줄에 오름차순으로 정렬된 M개의 정수가 주어집니다. "
         "두 리스트를 합쳐 오름차순으로 출력하십시오. **`sort()`나 `sorted()`를 쓰지 말고** 직접 병합하십시오.",
    constraints="1 ≤ N, M ≤ 10⁵, |각 수| ≤ 10⁹",
    examples=[("3 4\n1 4 9\n2 3 4 10", "1 2 3 4 4 9 10")],
    hidden=["1 1\n5\n5", "2 3\n10 20\n1 2 3", "3 1\n1 2 3\n100",
            G("n, m = 100000, 100000\nprint(n, m)\nprint(*sorted(random.randint(-10**9, 10**9) for _ in range(n)))\nprint(*sorted(random.randint(-10**9, 10**9) for _ in range(m)))", 2)],
    hint="두 리스트에 각각 손가락(인덱스 i, j)을 하나씩 얹으십시오. 더 작은 쪽을 결과에 넣고 그 손가락을 한 칸 옮깁니다. 한쪽이 바닥나면 남은 쪽을 통째로 붙이면 됩니다.",
    solution="n, m = map(int, input().split())\na = list(map(int, input().split()))\nb = list(map(int, input().split()))\ni = j = 0\nresult = []\nwhile i < n and j < m:\n    if a[i] <= b[j]:\n        result.append(a[i]); i += 1\n    else:\n        result.append(b[j]); j += 1\nresult += a[i:]\nresult += b[j:]\nprint(*result)",
    explanation="손가락이 한 번 지나간 원소는 다시 보지 않으므로 N + M번 만에 끝납니다. 정렬된 두 리스트를 합치는 최적의 방법입니다. 이 '두 손가락' 사고법은 제3부 '투 포인터'의 출발점입니다. "
                "`a[i] <= b[j]`에서 `<`가 아니라 `<=`를 쓰면 같은 값일 때 a 쪽이 먼저 나와 병합이 안정적이 됩니다. 표준 라이브러리에는 `heapq.merge`가 있습니다.",
),
# ───────────────── 13 튜플과 집합 ─────────────────
dict(
    id=61, title="벤 다이어그램",
    story="1880년 영국의 논리학자 존 벤은 집합 사이의 관계를 겹친 원으로 그리는 방법을 널리 알렸습니다. 파이썬의 집합은 `&`(교집합), `|`(합집합), `-`(차집합) 연산자로 이 그림을 그대로 계산합니다.",
    task="두 줄에 걸쳐 집합 A와 B의 원소(정수)들이 주어집니다. 같은 수가 여러 번 나올 수 있지만 집합에서는 한 번으로 칩니다. |A ∩ B|, |A ∪ B|, |A − B|를 공백으로 구분해 출력하십시오.",
    constraints="각 줄에 1개 이상 1000개 이하의 정수",
    examples=[("1 2 3 4\n3 4 5", "2 5 2"), ("1 1 1\n1", "1 1 0")],
    hidden=["1 2\n3 4", "5 6 7\n7 6 5", "-1 0 1\n0", "10 20 30 40 50\n1 2 3"],
    hint="`set(map(int, input().split()))`로 집합을 만든 뒤 `&`, `|`, `-` 연산자를 쓰십시오.",
    solution="a = set(map(int, input().split()))\nb = set(map(int, input().split()))\nprint(len(a & b), len(a | b), len(a - b))",
    explanation="집합은 원소가 '있느냐 없느냐'만 기억합니다. 순서도 개수도 기억하지 않습니다. 대신 `x in s` 검사가 원소 수와 관계없이 매우 빠릅니다. 리스트의 `in`은 처음부터 끝까지 훑어야 하는 것과 대조적입니다. "
                "대칭차집합 `a ^ b`(둘 중 한쪽에만 있는 원소)도 있습니다. 포함·배제의 원리 |A ∪ B| = |A| + |B| − |A ∩ B|가 성립하는지 확인해 보십시오.",
),
dict(
    id=62, title="처음 겹친 수",
    story="해시(hash)는 데이터에서 짧은 지문을 뽑아 '전에 본 적이 있는가'를 순식간에 답하게 해 줍니다. 파이썬의 집합과 딕셔너리는 해시 테이블로 만들어져 있습니다.",
    task="첫째 줄에 N, 둘째 줄에 N개의 정수가 주어집니다. 앞에서부터 읽어 갈 때 **이미 앞에서 나온 적이 있는 값**을 처음 만나면 그 값을 출력하십시오. 끝까지 그런 값이 없으면 `없음`을 출력합니다.",
    constraints="1 ≤ N ≤ 10⁵, |각 수| ≤ 10⁹",
    examples=[("6\n3 1 4 1 5 3", "1"), ("3\n1 2 3", "없음")],
    hidden=["1\n7", "2\n9 9", "5\n5 4 3 4 5", G("n = 100000\nprint(n)\nprint(*random.sample(range(10**9), n))", 3),
            G("n = 100000\nprint(n)\na = random.sample(range(10**9), n - 1)\na.append(a[50000])\nprint(*a)", 4)],
    hint="지금까지 본 값들을 집합 `seen`에 넣어 두면서, 새 값이 `seen`에 이미 있는지 검사하십시오.",
    solution='n = int(input())\nseen = set()\nanswer = "없음"\nfor x in map(int, input().split()):\n    if x in seen:\n        answer = x\n        break\n    seen.add(x)\nprint(answer)',
    explanation="`seen`을 리스트로 만들면 `in` 검사 한 번에 최대 N번 비교하므로 전체가 N²번, 곧 100억 번이 됩니다. 집합으로 바꾸기만 해도 거의 즉시 끝납니다. "
                "**자료구조의 선택이 곧 알고리즘의 속도**라는 것을 체감할 수 있는 문제입니다. 숨은 테스트에는 10만 개짜리 입력이 들어 있습니다.",
),
dict(
    id=63, title="셰익스피어의 어휘",
    story="학자들은 셰익스피어의 작품 전체에 서로 다른 단어가 3만 개 가까이 쓰였다고 추정합니다. 텍스트에 서로 다른 단어가 몇 개 쓰였는지를 세는 일은 문체 연구의 출발점입니다.",
    task="영어 문장 한 줄이 주어질 때 **서로 다른 단어**의 개수를 출력하십시오. 대소문자는 구별하지 않으며, 단어 앞뒤에 붙은 문장부호 `.,!?;:'\"`는 떼어 내고 셉니다.",
    examples=[("To be, or not to be: that is the question.", "8")],
    hidden=["Hello hello HELLO!", "a", "The cat saw the dog; the dog saw the cat.", "Is it? It is! 'It' is."],
    hint="각 단어에 `.lower()`와 `.strip(\".,!?;:'\\\"\")`를 적용한 뒤 집합에 넣으십시오.",
    solution="words = set()\nfor w in input().split():\n    words.add(w.strip(\".,!?;:'\\\"\").lower())\nprint(len(words))",
    explanation="`strip(문자들)`은 양 끝에서 주어진 문자들을 모두 벗겨 냅니다. 가운데 있는 문자는 건드리지 않으므로 `don't`의 작은따옴표는 남습니다. "
                "'To be, or not to be: that is the question.'에는 단어가 10개 있지만 to와 be가 두 번씩 나오므로 서로 다른 단어는 8개입니다. "
                "제17단원에서는 이 코드를 `len({w.strip(...).lower() for w in input().split()})` 한 줄로 줄이는 법을 배웁니다.",
),
dict(
    id=64, title="별자리 지도",
    story="2차원 좌표는 `(x, y)` 튜플로 나타내는 것이 자연스럽습니다. 튜플은 앞 원소부터 비교되므로 정렬하면 x 순서로, x가 같으면 y 순서로 저절로 정리됩니다.",
    task="첫째 줄에 점의 수 N, 이어서 N줄에 `x y`가 주어집니다. 점들을 x가 작은 순서로, x가 같으면 y가 작은 순서로 정렬해 한 줄에 하나씩 출력하십시오.",
    constraints="1 ≤ N ≤ 10⁵, |x|, |y| ≤ 10⁵",
    examples=[("5\n3 4\n1 1\n1 -1\n2 2\n3 3", "1 -1\n1 1\n2 2\n3 3\n3 4")],
    hidden=["1\n0 0", "3\n0 0\n0 0\n-1 5",
            G("n = 100000\nprint(n)\nfor _ in range(n):\n    print(random.randint(-10**5, 10**5), random.randint(-10**5, 10**5))", 5)],
    hint="각 점을 `(x, y)` 튜플로 리스트에 담고 `sort()` 하면 끝입니다. 줄이 많으므로 출력은 `\"\\n\".join(...)`으로 한 번에 하십시오.",
    solution='import sys\ninput = sys.stdin.readline\nn = int(input())\npoints = [tuple(map(int, input().split())) for _ in range(n)]\npoints.sort()\nprint("\\n".join(f"{x} {y}" for x, y in points))',
    explanation="입력과 출력이 10만 줄이 되면 `input()`과 `print()`를 반복해서 부르는 비용이 커집니다. `sys.stdin.readline`으로 읽고 결과를 모아 한 번에 출력하는 것은 제3부의 필수 습관이니 여기서 미리 익혀 두십시오. "
                "튜플은 **변경할 수 없는(immutable)** 리스트라고 생각하면 됩니다. 바로 그 성질 덕분에 집합의 원소나 딕셔너리의 키로 쓸 수 있습니다. 리스트는 그럴 수 없습니다.",
),
dict(
    id=65, title="생일 역설",
    story="한 반에 23명만 모여도 생일이 같은 두 사람이 있을 확률이 50%를 넘습니다. 직관과 너무 달라 '생일 역설'이라 불립니다. 비교해야 할 **쌍**의 수가 23 × 22 ÷ 2 = 253개나 되기 때문입니다.",
    task="첫째 줄에 사람 수 N, 이어서 N줄에 생일이 `월 일` 형식으로 주어집니다. 생일이 같은 두 사람이 있으면 `있음`, 없으면 `없음`을 출력하십시오.",
    constraints="1 ≤ N ≤ 400",
    examples=[("3\n3 15\n12 25\n3 15", "있음"), ("2\n1 1\n11 1", "없음")],
    hidden=["1\n2 29", "4\n1 2\n2 1\n1 12\n12 1", G("days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]\nds = [(m, d) for m in range(1, 13) for d in range(1, days[m - 1] + 1)]\nrandom.shuffle(ds)\nprint(len(ds))\nfor m, d in ds:\n    print(m, d)", 8),
            G("days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]\nds = [(m, d) for m in range(1, 13) for d in range(1, days[m - 1] + 1)]\nrandom.shuffle(ds)\nds.append(ds[100])\nprint(len(ds))\nfor m, d in ds:\n    print(m, d)", 9)],
    hint="생일을 `(월, 일)` 튜플로 만들어 집합에 넣으십시오. 집합의 크기가 사람 수보다 작아졌다면 무슨 뜻일까요?",
    solution='n = int(input())\nbirthdays = {tuple(map(int, input().split())) for _ in range(n)}\nprint("있음" if len(birthdays) < n else "없음")',
    explanation="집합은 중복을 하나로 합치므로 크기가 줄었다면 겹친 생일이 있다는 뜻입니다. 생일은 366가지뿐이므로 367명이 모이면 반드시 겹칩니다. 이것이 **비둘기집 원리**입니다. "
                "튜플을 집합에 넣을 수 있다는 점이 핵심입니다. `[3, 15]` 같은 리스트는 변경할 수 있어서 해시를 만들 수 없기 때문에 집합에 넣을 수 없습니다.",
),
# ───────────────── 14 딕셔너리 ─────────────────
dict(
    id=66, title="단어의 빈도",
    story="1935년 언어학자 지프는 어느 언어든 가장 흔한 단어가 두 번째로 흔한 단어보다 약 두 배, 세 번째보다 약 세 배 자주 쓰인다는 경험 법칙을 발견했습니다. 이 '지프의 법칙'도 단어마다 횟수를 세는 일에서 시작됩니다.",
    task="영어 소문자 단어들이 공백으로 구분되어 한 줄로 주어집니다. 각 단어의 등장 횟수를 **횟수가 많은 순서로**, 같으면 단어의 사전 순서로, 한 줄에 하나씩 `단어 횟수` 형식으로 출력하십시오.",
    examples=[("the cat and the hat and the bat", "the 3\nand 2\nbat 1\ncat 1\nhat 1")],
    hidden=["a", "b a b a", "z y x w", "go go go go"],
    hint="딕셔너리 `count`에서 `count[w] = count.get(w, 0) + 1`로 셉니다. 정렬할 때는 58번처럼 `(-횟수, 단어)`를 기준으로 삼으십시오.",
    solution="count = {}\nfor w in input().split():\n    count[w] = count.get(w, 0) + 1\nfor neg, w in sorted((-c, w) for w, c in count.items()):\n    print(w, -neg)",
    explanation="`get(키, 기본값)`은 키가 없을 때 오류 대신 기본값을 돌려줍니다. 처음 보는 단어도 0에서 세기 시작할 수 있는 이유입니다. "
                "`items()`는 (키, 값) 쌍들을 돌려줍니다. 같은 일을 `collections.Counter`가 한 줄로 해 줍니다. 91번에서 다룹니다.",
),
dict(
    id=67, title="전화번호부",
    story="종이 전화번호부는 이름순으로 정렬되어 있어 반씩 펼쳐 가며 찾을 수 있었습니다. 딕셔너리는 그보다도 빠릅니다. 이름을 해시로 바꾸어 곧바로 해당 칸을 찾아가기 때문입니다.",
    task="첫째 줄에 N, 이어서 N줄에 `이름 번호`가 주어집니다. 다음 줄에 질의 수 Q, 이어서 Q줄에 이름이 주어집니다. 각 질의마다 번호를 출력하되, 없는 이름이면 `없음`을 출력하십시오. 같은 이름이 두 번 등록되면 **나중 번호**가 유효합니다.",
    constraints="1 ≤ N, Q ≤ 10⁵",
    examples=[("3\nkim 010-0000-1111\nlee 010-0000-2222\nkim 010-0000-3333\n3\nkim\npark\nlee",
               "010-0000-3333\n없음\n010-0000-2222")],
    hidden=["1\na 1\n1\nb",
            G("n = 100000\nprint(n)\nnames = [f'u{random.randrange(60000)}' for _ in range(n)]\nfor x in names:\n    print(x, f'010-{random.randrange(10**4):04d}-{random.randrange(10**4):04d}')\nprint(n)\nfor _ in range(n):\n    print(f'u{random.randrange(80000)}')", 6)],
    hint="딕셔너리에 `book[이름] = 번호`로 넣으면 같은 이름은 덮어쓰입니다. 찾을 때는 `book.get(이름, \"없음\")`.",
    solution='import sys\ninput = sys.stdin.readline\nn = int(input())\nbook = {}\nfor _ in range(n):\n    name, number = input().split()\n    book[name] = number\nq = int(input())\nprint("\\n".join(book.get(input().rstrip(), "없음") for _ in range(q)))',
    explanation="`sys.stdin.readline`으로 읽은 줄은 끝에 줄바꿈 문자가 붙어 있습니다. 그래서 이름만 읽을 때는 `.rstrip()`이 필요합니다. 이것을 빠뜨리면 `\"kim\\n\"`을 찾게 되어 모두 `없음`이 나옵니다. 제3부에서 가장 흔한 실수입니다. "
                "번호를 정수로 바꾸지 않는 것도 중요합니다. 맨 앞의 0이 사라지기 때문입니다. 전화번호, 우편번호, 학번처럼 **셈을 하지 않는 숫자**는 문자열로 다루는 것이 원칙입니다.",
),
dict(
    id=68, title="모스 부호",
    story="1844년 새뮤얼 모스는 워싱턴에서 볼티모어로 \"What hath God wrought\"(하나님이 무엇을 이루셨는가)라는 성경 구절을 전신으로 보냈습니다. 점과 선 두 가지만으로 모든 글자를 나타내는 모스 부호의 시작이었습니다.",
    task="영어 대문자와 공백으로 된 문장을 국제 모스 부호로 바꾸어 출력하십시오. 글자 사이는 공백 하나, 단어 사이는 ` / `(공백-빗금-공백)로 구분합니다. A부터 Z까지의 부호는 다음과 같습니다(복사해서 쓰십시오).\n\n"
         "```\n.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..\n```",
    examples=[("SOS", "... --- ..."), ("HELLO WORLD", ".... . .-.. .-.. --- / .-- --- .-. .-.. -..")],
    hidden=["E", "WHAT HATH GOD WROUGHT", "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"],
    hint="`dict(zip(\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\", 부호문자열.split()))`로 표를 만들 수 있습니다. 단어마다 변환한 뒤 `\" / \".join()`으로 이으십시오.",
    solution='CODES = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split()\nMORSE = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", CODES))\nwords = input().split()\nprint(" / ".join(" ".join(MORSE[ch] for ch in w) for w in words))',
    explanation="`zip`은 두 순서열을 지퍼처럼 맞물려 쌍을 만들고, `dict()`는 그 쌍들로 딕셔너리를 만듭니다. 26줄짜리 딕셔너리를 손으로 쓰지 않아도 됩니다. "
                "모스 부호는 영어에서 자주 쓰이는 글자에 짧은 부호를 주었습니다(E는 점 하나, T는 선 하나). 나중에 배울 허프만 부호화와 같은 발상입니다.",
),
dict(
    id=69, title="아나그램 모임",
    story="글자의 순서만 바꾸어 다른 단어를 만드는 것을 아나그램이라 합니다. listen과 silent, evil과 live가 그렇습니다. 두 단어가 아나그램인지는 글자를 정렬해 보면 단번에 알 수 있습니다.",
    task="첫째 줄에 N, 둘째 줄에 N개의 영어 소문자 단어가 주어집니다. 서로 아나그램인 단어끼리 한 모임으로 묶을 때, **모임의 수**와 **가장 큰 모임의 크기**를 공백으로 구분해 출력하십시오. (같은 단어가 두 번 나오면 같은 모임에 두 번 들어갑니다.)",
    constraints="1 ≤ N ≤ 10⁵, 단어 길이 ≤ 10",
    examples=[("6\nlisten silent evil live vile enlist", "2 3")],
    hidden=["1\na", "3\nab ba ab", "4\nabc def ghi jkl",
            G("n = 100000\nprint(n)\nprint(*[''.join(random.choice('abc') for _ in range(random.randint(1, 6))) for _ in range(n)])", 7)],
    hint="`\"\".join(sorted(단어))`를 딕셔너리의 키로 삼아 개수를 세십시오.",
    solution="n = int(input())\ngroups = {}\nfor w in input().split():\n    key = \"\".join(sorted(w))\n    groups[key] = groups.get(key, 0) + 1\nprint(len(groups), max(groups.values()))",
    explanation="정렬된 글자열은 아나그램 모임마다 하나뿐인 **대표값(정규형)** 입니다. 여러 대상을 묶어야 할 때 '같은 모임이면 같아지는 값'을 찾아 딕셔너리 키로 삼는 기법은 매우 널리 쓰입니다. "
                "`sorted(\"listen\")`은 글자 리스트 `['e', 'i', 'l', 'n', 's', 't']`를 돌려주므로, 키로 쓰려면 `join`으로 다시 문자열로 만들어야 합니다(리스트는 키가 될 수 없습니다).",
),
dict(
    id=70, title="학생별 평균",
    story="성적 처리 프로그램은 '학생 → 점수 목록' 형태의 자료를 다룹니다. 딕셔너리의 값으로 리스트를 두면 이런 일대다 관계를 자연스럽게 담을 수 있습니다.",
    task="첫째 줄에 N, 이어서 N줄에 `이름 과목 점수`가 주어집니다. 학생 이름의 사전 순서로, 각 학생의 평균 점수를 소수점 아래 첫째 자리까지 `이름 평균` 형식으로 출력하십시오.",
    constraints="1 ≤ N ≤ 1000, 0 ≤ 점수 ≤ 100, 한 학생의 과목 수는 3개 이하",
    examples=[("5\nkim math 90\nlee math 85\nkim eng 81\nlee eng 70\nkim sci 100", "kim 90.3\nlee 77.5")],
    hidden=["1\nz art 0", "3\nb x 1\na x 2\nb y 2", "6\nm a 100\nm b 99\nm c 99\nn a 1\nn b 0\nn c 0"],
    hint="`scores.setdefault(이름, []).append(점수)`를 쓰면 처음 보는 이름에 빈 리스트를 만들어 주면서 곧바로 점수를 추가할 수 있습니다.",
    solution='n = int(input())\nscores = {}\nfor _ in range(n):\n    name, subject, score = input().split()\n    scores.setdefault(name, []).append(int(score))\nfor name in sorted(scores):\n    s = scores[name]\n    print(f"{name} {sum(s) / len(s):.1f}")',
    explanation="`setdefault`는 키가 없으면 기본값을 넣고, 있으면 기존 값을 돌려줍니다. `collections.defaultdict(list)`를 쓰면 `scores[name].append(...)`만으로 같은 일을 할 수 있습니다. "
                "딕셔너리를 `sorted()`에 넣으면 키들이 정렬되어 나옵니다. 딕셔너리 자체는 파이썬 3.7부터 **넣은 순서**를 기억합니다.",
),
# ───────────────── 15 함수 Ⅰ ─────────────────
dict(
    id=71, title="쌍둥이 소수",
    story="3과 5, 11과 13처럼 차이가 2인 소수의 쌍을 쌍둥이 소수라 합니다. 쌍둥이 소수가 무한히 많은지는 아직 풀리지 않은 문제입니다. 2013년 장이탕은 '차이가 7천만 이하인 소수 쌍은 무한히 많다'는 것을 증명해 수학계를 놀라게 했습니다.",
    task="`is_prime(n)` 함수를 정의하고 이를 이용해, 자연수 n 이하에서 두 수가 모두 n 이하인 쌍둥이 소수 쌍 (p, p+2)의 개수를 출력하십시오.",
    constraints="1 ≤ n ≤ 10⁵",
    examples=[("20", "4"), ("5", "1")],
    hidden=["1", "4", "100", "10000", "100000"],
    hint="34번 문제의 소수 판별을 함수로 감싸고 `return True` / `return False`로 결과를 돌려주십시오. 그다음 p = 2부터 n − 2까지 `is_prime(p) and is_prime(p + 2)`를 세면 됩니다.",
    solution="def is_prime(n):\n    if n < 2:\n        return False\n    i = 2\n    while i * i <= n:\n        if n % i == 0:\n            return False\n        i += 1\n    return True\n\nn = int(input())\nprint(sum(1 for p in range(2, n - 1) if is_prime(p) and is_prime(p + 2)))",
    explanation="함수 안의 `return`은 값을 돌려주는 동시에 함수를 즉시 끝냅니다. 그래서 34번의 `break`와 `else`가 필요 없어졌습니다. "
                "한 번 잘 만든 함수는 이름만으로 쓸 수 있습니다. `is_prime(p) and is_prime(p + 2)`는 거의 수학 문장처럼 읽힙니다. **추상화**의 힘입니다. "
                "20 이하의 쌍은 (3,5), (5,7), (11,13), (17,19) 네 쌍입니다. n이 수백만으로 커지면 101번에서 배울 에라토스테네스의 체가 필요합니다.",
),
dict(
    id=72, title="매미의 주기",
    story="북아메리카의 주기 매미는 13년 또는 17년마다 한꺼번에 땅 위로 나옵니다. 주기가 소수인 덕분에 천적의 주기와 겹치는 일이 드물다는 가설이 있습니다. 13년 매미와 17년 매미가 함께 나오는 해는 최소공배수인 221년마다 한 번뿐입니다.",
    task="`gcd(a, b)`와 `lcm(a, b)` 함수를 직접 정의하십시오. 첫째 줄에 N, 둘째 줄에 N개의 자연수가 주어질 때 이들 모두의 최소공배수를 출력하십시오.",
    constraints="1 ≤ N ≤ 100, 1 ≤ 각 수 ≤ 100",
    examples=[("2\n13 17", "221"), ("3\n4 6 10", "60")],
    hidden=["1\n7", "3\n1 1 1", "4\n2 4 8 16", "100\n" + " ".join(str(i) for i in range(1, 101))],
    hint="lcm(a, b) = a × b ÷ gcd(a, b)이고, 여러 수의 최소공배수는 lcm(lcm(a, b), c)처럼 앞에서부터 차례로 구합니다.",
    solution="def gcd(a, b):\n    while b:\n        a, b = b, a % b\n    return a\n\ndef lcm(a, b):\n    return a // gcd(a, b) * b\n\nn = int(input())\nresult = 1\nfor x in map(int, input().split()):\n    result = lcm(result, x)\nprint(result)",
    explanation="`a * b // gcd(a, b)` 대신 `a // gcd(a, b) * b`로 쓰면 중간값이 작아집니다. 파이썬에서는 상관없지만, 정수 크기가 제한된 언어에서는 오버플로를 막는 중요한 습관입니다. "
                "1부터 100까지의 최소공배수는 무려 41자리 수입니다. 파이썬 3.9부터는 `math.lcm(*nums)`가 이 일을 한 번에 합니다.",
),
dict(
    id=73, title="진법 변환기",
    story="컴퓨터는 2진법, 사람은 10진법, 프로그래머는 둘을 잇는 16진법을 즐겨 씁니다. 16진법 두 자리가 정확히 1바이트(8비트)이기 때문입니다.",
    task="함수 `to_base(n, b)`를 정의하여, 0 이상의 정수 n을 b진법 문자열로 바꾸어 출력하십시오. 10 이상의 자리는 `A`~`F`로 나타냅니다.",
    constraints="0 ≤ n ≤ 10¹⁸, 2 ≤ b ≤ 16",
    examples=[("255 16", "FF"), ("10 2", "1010")],
    hidden=["0 2", "1 16", "1000000000000000000 16", "1000000000000000000 3", "35 7", "4095 8"],
    hint="`n % b`가 맨 끝자리이고 `n // b`가 나머지 부분입니다. 끝자리부터 모은 뒤 뒤집으십시오. 자리 문자는 `\"0123456789ABCDEF\"[d]`로 얻을 수 있습니다.",
    solution='DIGITS = "0123456789ABCDEF"\n\ndef to_base(n, b):\n    if n == 0:\n        return "0"\n    out = []\n    while n > 0:\n        n, d = divmod(n, b)\n        out.append(DIGITS[d])\n    return "".join(reversed(out))\n\nn, b = map(int, input().split())\nprint(to_base(n, b))',
    explanation="n = 0일 때 반복문이 한 번도 돌지 않아 빈 문자열이 되는 함정을 따로 처리했습니다. **경계값**을 먼저 의심하는 습관이 중요합니다. "
                "11번 문제(초 → 시:분:초)와 같은 원리입니다. 파이썬에는 `bin()`, `oct()`, `hex()`가 있고, 거꾸로 b진법 문자열을 정수로 바꾸는 `int(\"FF\", 16)`도 있습니다.",
),
dict(
    id=74, title="요약 통계",
    story="파이썬 함수는 값 여러 개를 한꺼번에 돌려줄 수 있습니다. 사실은 튜플 하나를 돌려주는 것이고, 받는 쪽에서 그것을 풀어 담는 것입니다.",
    task="함수 `summary(nums)`가 최솟값, 최댓값, 평균을 **한꺼번에 돌려주도록** 정의하십시오. 첫째 줄에 N, 둘째 줄에 N개의 정수가 주어질 때 `최솟값 최댓값 평균`을 출력하되 평균은 소수점 아래 둘째 자리까지 나타냅니다.",
    constraints="1 ≤ N ≤ 1000, |각 수| ≤ 10⁶",
    examples=[("4\n3 -1 4 1", "-1 4 1.75")],
    hidden=["1\n5", "3\n-3 -3 -3", "5\n1000000 -1000000 1 2 3", "3\n1 2 4"],
    hint="`return min(nums), max(nums), sum(nums) / len(nums)`처럼 쉼표로 이어 쓰면 됩니다. 받을 때는 `lo, hi, avg = summary(nums)`.",
    solution='def summary(nums):\n    return min(nums), max(nums), sum(nums) / len(nums)\n\nn = int(input())\nlo, hi, avg = summary(list(map(int, input().split())))\nprint(f"{lo} {hi} {avg:.2f}")',
    explanation="`return a, b, c`는 `return (a, b, c)`와 같습니다. 이것을 세 변수로 나누어 받는 **언패킹**은 7번 문제의 `a, b = map(...)`과 같은 원리입니다. "
                "함수가 계산과 출력을 함께 하지 않고 **값만 돌려주게** 만들면 그 함수를 다른 곳에서도 다시 쓸 수 있습니다. 좋은 함수 설계의 첫 원칙입니다.",
),
dict(
    id=75, title="룬 알고리즘",
    story="1954년 IBM의 연구원 한스 페터 룬이 고안한 검사법은 오늘날에도 신용카드 번호 등에서 숫자 하나를 잘못 입력한 오류를 잡아냅니다. 마지막 자리는 앞 숫자들로부터 계산된 **검사 숫자**입니다.",
    task="숫자로만 된 문자열이 주어집니다. 아래 규칙에 따라 유효하면 `유효`, 아니면 `무효`를 출력하는 함수 `luhn(s)`를 만들어 쓰십시오.\n\n"
         "1. 맨 오른쪽 자리부터 왼쪽으로 가며, 오른쪽에서 **두 번째, 네 번째, …** 자리의 숫자를 두 배로 합니다.\n"
         "2. 두 배 한 값이 9보다 크면 9를 뺍니다.\n"
         "3. 모든 자리의 합이 10의 배수이면 유효합니다.",
    constraints="1 ≤ 길이 ≤ 100",
    examples=[("79927398713", "유효"), ("79927398710", "무효")],
    hidden=["0", "18", "4111111111111111", "4111111111111112", "1234567812345670", "1234567812345678", "59"],
    hint="문자열을 뒤집어 `enumerate()`로 돌리면, 인덱스가 홀수인 자리가 '두 배 할 자리'가 됩니다.",
    solution='def luhn(s):\n    total = 0\n    for i, ch in enumerate(reversed(s)):\n        d = int(ch)\n        if i % 2 == 1:\n            d *= 2\n            if d > 9:\n                d -= 9\n        total += d\n    return total % 10 == 0\n\nprint("유효" if luhn(input()) else "무효")',
    explanation="`enumerate()`는 (인덱스, 원소) 쌍을 함께 내놓습니다. 그래서 '몇 번째 자리인가'를 따로 세지 않아도 됩니다. 두 배 한 값에서 9를 빼는 것은 그 값의 두 자릿수를 더하는 것과 같습니다(예: 16 → 1 + 6 = 7 = 16 − 9). "
                "룬 알고리즘은 숫자 하나를 잘못 친 오류는 모두 잡아내고, 이웃한 두 숫자를 바꾸어 친 오류도 대부분 잡아냅니다(09 ↔ 90만은 놓칩니다). "
                "함수가 `True`/`False`만 돌려주고 출력 문구는 바깥에서 정하도록 나눈 점에도 주목하십시오.",
),
]
