# 기초 076–100
from testlib import G

PROBLEMS = [
# ───────────────── 16 함수 Ⅱ: 재귀와 람다 ─────────────────
dict(
    id=76, title="하노이의 탑",
    story="1883년 프랑스의 수학자 에두아르 뤼카는 '브라흐마의 탑' 전설과 함께 이 퍼즐을 내놓았습니다. 원판 64개를 모두 옮기면 세상이 끝난다는 전설이었습니다. 1초에 한 번씩 옮겨도 5800억 년이 넘게 걸리니 걱정할 필요는 없습니다.",
    task="원판 n개가 1번 기둥에 크기 순서대로 쌓여 있습니다. 한 번에 한 장씩, 작은 원판 위에 큰 원판을 올리지 않으면서 모두 3번 기둥으로 옮기려 합니다. "
         "첫째 줄에 최소 이동 횟수를, 이어서 각 이동을 `출발 도착` 형식으로 한 줄에 하나씩 출력하십시오.",
    constraints="1 ≤ n ≤ 12",
    examples=[("2", "3\n1 2\n1 3\n2 3")],
    hidden=["1", "3", "10", "12"],
    hint="n개를 1번에서 3번으로 옮기려면, 위의 n−1개를 2번으로 옮기고, 가장 큰 원판을 3번으로 옮긴 뒤, n−1개를 다시 3번으로 옮기면 됩니다. 'n−1개를 옮기는 일'은 같은 문제의 더 작은 판입니다.",
    solution='def hanoi(n, src, via, dst):\n    if n == 0:\n        return\n    hanoi(n - 1, src, dst, via)\n    moves.append(f"{src} {dst}")\n    hanoi(n - 1, via, src, dst)\n\nmoves = []\nhanoi(int(input()), 1, 2, 3)\nprint(len(moves))\nprint("\\n".join(moves))',
    explanation="재귀 함수는 **같은 문제의 더 작은 판**을 스스로 불러 풉니다. 반드시 더 이상 쪼개지 않는 **기저 사례**(여기서는 n = 0)가 있어야 무한히 불리지 않습니다. "
                "이동 횟수를 T(n)이라 하면 T(n) = 2T(n−1) + 1이므로 T(n) = 2ⁿ − 1입니다. 이보다 적게 옮기는 방법은 없다는 것도 같은 논리로 증명됩니다. 가장 큰 원판은 적어도 한 번 움직여야 하고, 그 전후로 나머지 n−1개가 통째로 비켜 주어야 하기 때문입니다.",
),
dict(
    id=77, title="피보나치의 토끼",
    story="1202년 피사의 레오나르도, 곧 피보나치는 『산반서』에 토끼 문제를 실었습니다. 한 쌍의 토끼가 두 달째부터 매달 새끼 한 쌍을 낳는다면 토끼는 어떻게 불어날까요? 답은 각 항이 앞의 두 항의 합인 수열 0, 1, 1, 2, 3, 5, 8, …입니다.",
    task="F(0) = 0, F(1) = 1, F(n) = F(n−1) + F(n−2)입니다. n이 주어질 때 F(n)을 **재귀 함수와 메모이제이션**으로 구해 출력하십시오.",
    constraints="0 ≤ n ≤ 90",
    examples=[("10", "55"), ("0", "0")],
    hidden=["1", "2", "50", "90"],
    hint="재귀를 그대로 쓰면 F(90)은 우주의 나이보다 오래 걸립니다. 한 번 계산한 값을 딕셔너리에 저장해 두고, 다시 필요하면 꺼내 쓰십시오. `functools.lru_cache`가 이 일을 대신해 줍니다.",
    solution="from functools import lru_cache\n\n@lru_cache(maxsize=None)\ndef fib(n):\n    if n < 2:\n        return n\n    return fib(n - 1) + fib(n - 2)\n\nprint(fib(int(input())))",
    explanation="메모 없이 재귀하면 fib(n)의 호출 횟수 자체가 피보나치 수처럼 늘어나 지수적으로 폭발합니다. 같은 부분 문제를 수없이 다시 풀기 때문입니다. 저장해 두면 각 n을 한 번씩만 계산하므로 91번이면 끝납니다. "
                "`@lru_cache`처럼 함수 위에 붙는 것을 **데코레이터**라 합니다. 이 '부분 문제의 답을 저장해 다시 쓰기'가 바로 제3부의 핵심인 **동적 계획법**의 씨앗입니다.",
),
dict(
    id=78, title="디지털 근",
    story="15번에서 본 '자릿수의 합'을 한 자리가 될 때까지 되풀이하면 **디지털 근**을 얻습니다. 9875 → 29 → 11 → 2. 이 값은 놀랍게도 그 수를 9로 나눈 나머지와 깊은 관계가 있습니다.",
    task="최대 1000자리의 자연수가 주어질 때 그 디지털 근을 **재귀 함수로** 구해 출력하십시오.",
    examples=[("9875", "2"), ("9", "9")],
    hidden=["1", "10", "999999999999", "1" * 1000, "9" * 1000, "123456789"],
    hint="`dr(s)`: s가 한 자리면 그대로 돌려주고, 아니면 자릿수 합을 문자열로 바꾸어 다시 `dr`에 넣으십시오.",
    solution="def dr(s):\n    if len(s) == 1:\n        return s\n    return dr(str(sum(map(int, s))))\n\nprint(dr(input()))",
    explanation="1000자리 수의 자릿수 합은 많아야 9000이므로 재귀는 몇 번 만에 끝납니다. "
                "수학적으로 디지털 근은 `1 + (n − 1) % 9`(n ≥ 1일 때)입니다. 10 ≡ 1 (mod 9)이므로 어떤 수와 그 자릿수 합은 9로 나눈 나머지가 같기 때문입니다. 15번에서 말한 구거법의 원리가 바로 이것입니다. 두 방법의 답이 같은지 확인해 보십시오.",
),
dict(
    id=79, title="람다로 정하는 순위",
    story="`lambda`는 이름 없는 작은 함수입니다. 정렬 기준처럼 한 번 쓰고 버릴 함수를 그 자리에서 바로 적을 때 빛을 발합니다.",
    task="첫째 줄에 N, 이어서 N줄에 `이름 국어 영어 수학`이 주어집니다. 총점이 높은 순서로, 총점이 같으면 수학 점수가 높은 순서로, 그것도 같으면 이름의 사전 순서로 정렬해 이름을 한 줄에 하나씩 출력하십시오.",
    constraints="1 ≤ N ≤ 1000, 이름은 서로 다른 영어 소문자, 0 ≤ 점수 ≤ 100",
    examples=[("4\nkim 90 80 70\nlee 80 80 80\npark 100 100 100\nchoi 70 80 90", "park\nchoi\nlee\nkim")],
    hidden=["1\na 0 0 0", "3\nc 50 50 50\nb 50 50 50\na 50 50 50", "3\nx 100 0 50\ny 0 100 50\nz 50 50 50"],
    hint="각 학생을 `(이름, 국어, 영어, 수학)` 튜플로 담고 `sort(key=lambda s: (-(s[1]+s[2]+s[3]), -s[3], s[0]))`처럼 정렬하십시오.",
    solution="n = int(input())\nstudents = []\nfor _ in range(n):\n    name, *scores = input().split()\n    students.append((name, *map(int, scores)))\nstudents.sort(key=lambda s: (-(s[1] + s[2] + s[3]), -s[3], s[0]))\nprint(\"\\n\".join(s[0] for s in students))",
    explanation="`name, *scores = ...`의 별표는 '나머지를 모두 리스트로 받으라'는 뜻입니다. "
                "람다가 돌려주는 튜플이 곧 정렬의 우선순위 목록입니다. 숫자는 부호를 바꾸어 내림차순을 만들고, 문자열은 그대로 두어 오름차순을 유지합니다. "
                "예제에서 choi, lee, kim은 총점이 모두 240점이므로 두 번째 기준인 수학 점수(90, 80, 70)로 순서가 정해집니다.",
),
dict(
    id=80, title="모든 순열",
    story="서로 다른 n개를 한 줄로 세우는 방법은 n!가지입니다. 이를 빠짐없이, 겹치지 않게 만들어 내는 가장 자연스러운 방법은 '첫 자리를 정하고, 남은 것들로 나머지를 채우는' 재귀입니다. 이것이 **백트래킹**의 기본 틀입니다.",
    task="자연수 n이 주어질 때 1부터 n까지의 모든 순열을 **사전 순서로** 한 줄에 하나씩 출력하십시오. `itertools`는 쓰지 말고 재귀로 만드십시오.",
    constraints="1 ≤ n ≤ 7",
    examples=[("3", "1 2 3\n1 3 2\n2 1 3\n2 3 1\n3 1 2\n3 2 1")],
    hidden=["1", "2", "5", "7"],
    hint="`perm` 리스트와 `used` 표시를 두고, 아직 쓰지 않은 수를 작은 것부터 하나씩 넣어 본 뒤 재귀 호출하고, 돌아오면 다시 빼십시오.",
    solution='def go():\n    if len(perm) == n:\n        out.append(" ".join(map(str, perm)))\n        return\n    for x in range(1, n + 1):\n        if not used[x]:\n            used[x] = True\n            perm.append(x)\n            go()\n            perm.pop()\n            used[x] = False\n\nn = int(input())\nperm, used, out = [], [False] * (n + 1), []\ngo()\nprint("\\n".join(out))',
    explanation="'넣고 → 재귀 → 빼기'의 세 박자가 백트래킹의 뼈대입니다. 빼는 단계를 잊으면 다음 갈래에 이전 흔적이 남습니다. 작은 수부터 시도하므로 결과는 저절로 사전 순서가 됩니다. "
                "실전에서는 `itertools.permutations(range(1, n + 1))`이 같은 순서로 순열을 만들어 줍니다. 제2부 '재귀와 백트래킹'에서 이 틀을 N-Queen 같은 문제에 적용합니다.",
),
# ───────────────── 17 컴프리헨션 ─────────────────
dict(
    id=81, title="홀수의 제곱",
    story="컴프리헨션은 수학의 집합 조건제시법 {x² | x는 홀수, x ≤ n}을 거의 그대로 옮겨 놓은 문법입니다. 파이썬은 이 표기를 1950년대 언어 SETL과 함수형 언어 하스켈에서 빌려 왔습니다.",
    task="자연수 n이 주어질 때 n 이하인 홀수들의 제곱을 한 줄에 출력하십시오. **리스트 컴프리헨션 한 줄**로 만드십시오.",
    constraints="1 ≤ n ≤ 1000",
    examples=[("10", "1 9 25 49 81")],
    hidden=["1", "2", "15", "1000"],
    hint="`[식 for 변수 in 범위 if 조건]`의 꼴입니다. `range`의 보폭을 2로 하면 조건이 필요 없습니다.",
    solution="n = int(input())\nprint(*[x * x for x in range(1, n + 1, 2)])",
    explanation="`[x * x for x in range(1, n + 1) if x % 2 == 1]`도 같은 결과를 냅니다. 다만 위 풀이처럼 범위를 처음부터 홀수만 만들면 조건 검사를 절반 아낄 수 있습니다. "
                "컴프리헨션은 빈 리스트를 만들고 `append`하는 세 줄짜리 반복문을 한 줄로 줄여 줄 뿐 아니라, 대개 더 빠르기도 합니다.",
),
dict(
    id=82, title="행렬의 전치",
    story="행렬의 행과 열을 맞바꾸는 것을 전치라 합니다. 파이썬에서는 `zip(*행렬)`이라는, 마법 같은 한 줄로 전치를 할 수 있습니다.",
    task="첫째 줄에 R과 C, 이어서 R줄에 C개씩 정수가 주어집니다. 전치 행렬(C행 R열)을 출력하십시오.",
    constraints="1 ≤ R, C ≤ 100",
    examples=[("2 3\n1 2 3\n4 5 6", "1 4\n2 5\n3 6")],
    hidden=["1 1\n7", "1 4\n1 2 3 4", "4 1\n1\n2\n3\n4", "3 3\n1 2 3\n4 5 6\n7 8 9"],
    hint="행렬을 `[input().split() for _ in range(r)]`로 읽은 뒤, `zip(*m)`이 무엇을 내놓는지 출력해 보십시오.",
    solution="r, c = map(int, input().split())\nm = [input().split() for _ in range(r)]\nfor col in zip(*m):\n    print(*col)",
    explanation="`zip(*m)`에서 별표는 행렬의 각 행을 따로따로 `zip`에 넘깁니다. `zip(행1, 행2, …)`은 각 행의 첫 원소끼리, 둘째 원소끼리 묶어 내놓으므로, 그 결과가 곧 전치 행렬의 행입니다. "
                "컴프리헨션으로는 `[[m[i][j] for i in range(r)] for j in range(c)]`입니다. 이중 컴프리헨션에서 **바깥 for가 먼저** 읽힌다는 점을 눈여겨보십시오.",
),
dict(
    id=83, title="글자의 첫 등장",
    story="딕셔너리 컴프리헨션 `{키: 값 for …}`은 표를 한 줄로 만들어 냅니다. 같은 키가 여러 번 나오면 나중 값이 앞의 값을 덮어쓴다는 점을 기억해 두면 유용합니다.",
    task="영어 소문자 단어가 주어질 때, 단어에 쓰인 각 글자가 **처음** 나타나는 위치(0부터)를 글자의 사전 순서로 `글자:위치` 형식으로 한 줄에 출력하십시오.",
    constraints="1 ≤ 길이 ≤ 1000",
    examples=[("banana", "a:1 b:0 n:2"), ("python", "h:3 n:5 o:4 p:0 t:2 y:1")],
    hidden=["a", "zzz", "mississippi", "abcdefghijklmnopqrstuvwxyz"],
    hint="`{ch: w.index(ch) for ch in set(w)}` 또는, 거꾸로 훑으며 덮어쓰는 `{ch: i for i, ch in reversed(list(enumerate(w)))}`.",
    solution='w = input()\nfirst = {ch: i for i, ch in reversed(list(enumerate(w)))}\nprint(" ".join(f"{ch}:{first[ch]}" for ch in sorted(first)))',
    explanation="뒤에서부터 넣으면 같은 글자는 앞쪽 위치가 나중에 들어와 덮어쓰므로 결국 **처음 위치**만 남습니다. 이 방법은 단어를 한 번만 훑습니다. "
                "`{ch: w.index(ch) for ch in set(w)}`도 정답입니다. 다만 `index`가 매번 앞에서부터 찾으므로 글자 종류가 많으면 느려집니다. "
                "덮어쓰기 성질을 거꾸로 이용하면 `{ch: i for i, ch in enumerate(w)}`는 **마지막 위치** 표가 됩니다.",
),
dict(
    id=84, title="라마누잔의 고도 합성수",
    story="1915년 라마누잔은 자기보다 작은 어떤 수보다도 약수가 많은 수를 '고도 합성수'라 이름 붙이고 깊이 연구했습니다. 1, 2, 4, 6, 12, 24, 36, 48, 60, 120, …. 시계가 12시간, 원이 360도인 것은 우연이 아닙니다.",
    task="자연수 n이 주어질 때, 1 이상 n 이하의 수 가운데 약수가 가장 많은 수와 그 약수의 개수를 출력하십시오. 그런 수가 여럿이면 가장 작은 수를 출력합니다. 약수의 개수는 **컴프리헨션**으로 세십시오.",
    constraints="1 ≤ n ≤ 1000",
    examples=[("10", "6 4"), ("1", "1 1")],
    hidden=["2", "12", "100", "360", "1000"],
    hint="`counts = [sum(1 for d in range(1, k + 1) if k % d == 0) for k in range(1, n + 1)]`로 약수 개수 표를 만든 뒤 최댓값과 그 첫 위치를 찾으십시오.",
    solution="n = int(input())\ncounts = [sum(1 for d in range(1, k + 1) if k % d == 0) for k in range(1, n + 1)]\nbest = max(counts)\nprint(counts.index(best) + 1, best)",
    explanation="`sum(1 for … if …)`처럼 대괄호 없이 쓴 것은 **제너레이터 표현식**입니다. 리스트를 메모리에 만들지 않고 값을 하나씩 흘려보냅니다. "
                "1000 이하에서 답은 840(약수 32개)입니다. 840 = 2³ × 3 × 5 × 7처럼 작은 소수를 고루 가진 수가 약수가 많습니다. "
                "이 풀이는 약 50만 번 나눗셈을 합니다. n이 커지면 '각 d의 배수마다 1씩 더하는' 체 방식으로 바꾸면 훨씬 빨라집니다.",
),
dict(
    id=85, title="서로 다른 합",
    story="집합 컴프리헨션 `{…}`은 만들면서 동시에 중복을 없앱니다. '가능한 결과가 몇 가지인가'를 물을 때 가장 먼저 떠올릴 도구입니다.",
    task="첫째 줄에 N, 둘째 줄에 N개의 정수가 주어집니다. 서로 다른 위치의 두 수를 골라 더해서 만들 수 있는 **서로 다른 합**의 개수를 출력하십시오.",
    constraints="1 ≤ N ≤ 300, |각 수| ≤ 10⁶",
    examples=[("4\n1 2 3 4", "5"), ("3\n5 5 5", "1")],
    hidden=["1\n7", "2\n-1 1", "5\n1 10 100 1000 10000", G("n = 300\nprint(n)\nprint(*[random.randint(-50, 50) for _ in range(n)])", 10)],
    hint="`{a[i] + a[j] for i in range(n) for j in range(i + 1, n)}`의 크기를 구하십시오.",
    solution="n = int(input())\na = list(map(int, input().split()))\nprint(len({a[i] + a[j] for i in range(n) for j in range(i + 1, n)}))",
    explanation="`j`를 `i + 1`부터 시작하게 하면 같은 원소를 두 번 고르는 일도, (i, j)와 (j, i)를 두 번 세는 일도 피할 수 있습니다. "
                "1 2 3 4의 쌍 6개의 합은 3, 4, 5, 5, 6, 7이고 서로 다른 것은 5개입니다. N = 1이면 쌍이 없으므로 빈 집합이 되어 0입니다. "
                "`itertools.combinations(a, 2)`를 쓰면 `{x + y for x, y in combinations(a, 2)}`로 더 읽기 좋게 쓸 수 있습니다.",
),
# ───────────────── 18 예외 처리와 match ─────────────────
dict(
    id=86, title="안전한 나눗셈",
    story="실제 세상의 입력은 늘 깨끗하지 않습니다. 0으로 나누려 하거나, 숫자 자리에 글자를 적기도 합니다. `try`-`except`는 오류가 나도 프로그램 전체가 멈추지 않도록 그 자리에서 받아 내는 그물입니다.",
    task="첫째 줄에 N, 이어서 N줄에 두 값 `a b`가 주어집니다. 각 줄마다 `a // b`를 출력하되, b가 0이면 `0으로 나눌 수 없음`, a나 b가 정수가 아니면 `잘못된 입력`을 출력하십시오.",
    examples=[("4\n7 2\n-7 2\n3 0\nx 5", "3\n-4\n0으로 나눌 수 없음\n잘못된 입력")],
    hidden=["1\n0 7", "3\n1.5 1\n10 -3\n5 zero", "2\n0 0\n100 7"],
    hint="`int()` 변환과 나눗셈을 모두 `try` 안에 두고, `except ZeroDivisionError:`와 `except ValueError:`를 따로 쓰십시오.",
    solution='n = int(input())\nfor _ in range(n):\n    a, b = input().split()\n    try:\n        print(int(a) // int(b))\n    except ZeroDivisionError:\n        print("0으로 나눌 수 없음")\n    except ValueError:\n        print("잘못된 입력")',
    explanation="`except` 절은 위에서부터 차례로 맞는 것을 찾습니다. `except:`처럼 종류를 적지 않으면 오타로 생긴 오류까지 삼켜 버려 버그를 숨기게 되므로, 잡을 오류를 구체적으로 적는 것이 원칙입니다. "
                "`-7 // 2`가 −3이 아니라 −4인 것에 주목하십시오. 파이썬의 `//`는 **내림**(바닥) 나눗셈이라 음수에서는 0이 아니라 음의 무한대 쪽으로 내립니다. 그래서 `a == (a // b) * b + a % b`가 언제나 성립합니다.",
),
dict(
    id=87, title="숫자만 더하기",
    story="'허락보다 용서를 구하는 것이 쉽다(EAFP)'는 파이썬 공동체의 오래된 격언입니다. 미리 모든 경우를 검사하기보다 일단 해 보고 실패하면 처리하는 편이 간결할 때가 많습니다.",
    task="공백으로 구분된 토큰들이 한 줄로 주어집니다. 그 가운데 `int()`로 정수 변환이 되는 토큰만 골라 합을 출력하십시오.",
    examples=[("3 apple -2 4.5 10 +7", "18")],
    hidden=["hello", "0", "1e3 1000 ten", "-0 007 -5", "- + 12a a12 99"],
    hint="토큰마다 `try: total += int(t)` / `except ValueError: pass`.",
    solution="total = 0\nfor t in input().split():\n    try:\n        total += int(t)\n    except ValueError:\n        pass\nprint(total)",
    explanation="`int()`는 `+7`, `-0`, `007`은 받아들이지만 `4.5`나 `1e3`은 거부합니다. 실수 표기는 `float()`의 몫이기 때문입니다. "
                "`t.isdigit()`로 미리 검사하는 방법(LBYL, '뛰기 전에 살펴라')은 `-2`나 `+7`을 놓칩니다. 부호까지 정확히 검사하려면 조건이 복잡해집니다. EAFP 방식이 빛나는 경우입니다. "
                "덤으로, `int(\"1_000\")`이 1000이 된다는 사실도 알아 두십시오. 파이썬 3.6부터 숫자 안의 밑줄을 자릿수 구분자로 허용합니다.",
),
dict(
    id=88, title="match로 만든 계산기",
    story="파이썬 3.10에서 들어온 `match` 문은 값의 **모양**을 보고 갈래를 나눕니다. 단순한 값 비교에서는 `if`-`elif` 사슬보다 의도가 또렷하게 드러납니다.",
    task="첫째 줄에 N, 이어서 N줄에 `a 연산자 b`(a, b는 정수)가 주어집니다. 연산자 `+`, `-`, `*`, `//`, `%`의 결과를 출력하십시오. "
         "`//`나 `%`에서 b가 0이면 `0으로 나눌 수 없음`, 그 밖의 연산자이면 `지원하지 않는 연산`을 출력합니다. `match` 문을 쓰십시오.",
    examples=[("5\n7 + 5\n7 // 2\n7 % 0\n2 ** 10\n-7 % 3", "12\n3\n0으로 나눌 수 없음\n지원하지 않는 연산\n2")],
    hidden=["2\n0 * 100\n5 - 9", "3\n10 / 2\n1 // 0\n-8 // 3", "1\n123456789 * 987654321"],
    hint="`match op:` 아래에 `case \"+\":`, `case \"//\" | \"%\" if b == 0:`, `case _:` 같은 갈래를 두십시오. `|`는 '또는', `if`는 추가 조건(가드)입니다.",
    solution='n = int(input())\nfor _ in range(n):\n    a, op, b = input().split()\n    a, b = int(a), int(b)\n    match op:\n        case "//" | "%" if b == 0:\n            print("0으로 나눌 수 없음")\n        case "+":\n            print(a + b)\n        case "-":\n            print(a - b)\n        case "*":\n            print(a * b)\n        case "//":\n            print(a // b)\n        case "%":\n            print(a % b)\n        case _:\n            print("지원하지 않는 연산")',
    explanation="`case _:`는 어느 갈래에도 맞지 않을 때 실행되는 '나머지 전부'입니다. 가드(`if b == 0`)가 붙은 갈래를 맨 위에 둔 것은 0으로 나누는 경우를 먼저 걸러 내기 위해서입니다. "
                "`-7 % 3`이 2인 것은 86번에서 본 내림 나눗셈과 짝을 이루는 성질입니다. `match`는 3.10 이상에서만 동작하므로, Colab(3.12)에서는 문제없지만 오래된 환경에서는 문법 오류가 납니다.",
),
dict(
    id=89, title="로봇의 명령어",
    story="`match`의 진짜 힘은 **구조 분해**에 있습니다. `case [\"go\", k]:`는 '두 칸짜리 리스트이고 첫 칸이 \"go\"이면, 둘째 칸을 k라 부르라'는 뜻입니다. 모양을 검사하는 일과 값을 꺼내는 일을 한 번에 합니다.",
    task="로봇이 (0, 0)에서 북쪽을 보고 서 있습니다. 첫째 줄에 N, 이어서 N줄에 명령이 주어집니다. 명령은 `go k`(앞으로 k칸), `back k`(뒤로 k칸), `left`(왼쪽으로 90° 회전), `right`(오른쪽으로 90° 회전) 네 가지입니다. "
         "북쪽은 y가 커지는 방향, 동쪽은 x가 커지는 방향입니다. 모든 명령을 수행한 뒤 `x y 방향`을 출력하십시오. 방향은 `N`, `E`, `S`, `W` 중 하나입니다.",
    constraints="1 ≤ N ≤ 1000, 1 ≤ k ≤ 1000",
    examples=[("5\ngo 3\nright\ngo 2\nleft\nback 1", "2 2 N")],
    hidden=["1\nleft", "4\nright\nright\nright\nright", "3\nleft\ngo 10\nback 3", "6\nright\ngo 5\nright\ngo 5\nright\ngo 5"],
    hint="방향을 0~3의 번호로 두고 `DX = [0, 1, 0, -1]`, `DY = [1, 0, -1, 0]`처럼 표를 만드십시오. 오른쪽 회전은 번호 +1, 왼쪽 회전은 −1(4로 나눈 나머지)입니다.",
    solution='DX, DY, NAMES = [0, 1, 0, -1], [1, 0, -1, 0], "NESW"\nx = y = d = 0\nfor _ in range(int(input())):\n    match input().split():\n        case ["go", k]:\n            x += DX[d] * int(k); y += DY[d] * int(k)\n        case ["back", k]:\n            x -= DX[d] * int(k); y -= DY[d] * int(k)\n        case ["left"]:\n            d = (d - 1) % 4\n        case ["right"]:\n            d = (d + 1) % 4\nprint(x, y, NAMES[d])',
    explanation="방향 벡터 표 `DX`, `DY`는 격자 문제의 단골 도구입니다. 방향마다 `if`를 쓰는 대신 번호 하나로 모든 방향을 똑같이 다룰 수 있습니다. 제2부의 '시뮬레이션'과 '2차원 격자'에서 계속 쓰입니다. "
                "`case [\"go\", k]`는 명령이 정확히 두 단어일 때만 맞습니다. 그래서 잘못된 형식의 명령은 어느 갈래에도 걸리지 않고 조용히 무시됩니다.",
),
dict(
    id=90, title="끝을 알 수 없는 입력",
    story="35번에서는 0이라는 약속된 끝 표시가 있었습니다. 그런데 끝 표시 없이 입력이 그냥 끝나 버리기도 합니다. 이때 `input()`은 `EOFError`를 일으킵니다. EOF는 End Of File, 곧 '파일의 끝'입니다.",
    task="한 줄에 정수가 하나씩, 개수를 알 수 없게 주어집니다(적어도 하나). 입력이 끝날 때까지 읽어 **개수, 합, 최댓값**을 공백으로 구분해 출력하십시오.",
    examples=[("3\n-1\n4\n1\n5", "5 12 5")],
    hidden=["42", "-5\n-3", "1\n1\n1\n1\n1\n1\n1\n1\n1\n1"],
    hint="`while True:` 안에서 `try: x = int(input())`, `except EOFError: break`.",
    solution="nums = []\nwhile True:\n    try:\n        nums.append(int(input()))\n    except EOFError:\n        break\nprint(len(nums), sum(nums), max(nums))",
    explanation="예외 처리를 흐름 제어에 쓰는 대표적인 예입니다. 다른 방법으로는 `import sys` 후 `nums = [int(line) for line in sys.stdin]`이 있습니다. `sys.stdin`은 남은 줄을 끝까지 하나씩 내놓습니다. "
                "Colab에서 `%run`으로 직접 실행해 볼 때는 입력 칸에 아무것도 넣지 않고 엔터를 치면 EOF가 아니라 빈 문자열이 들어와 `ValueError`가 납니다. 채점기는 진짜 EOF를 보내므로 걱정하지 않아도 됩니다.",
),
# ───────────────── 19 표준 라이브러리 산책 ─────────────────
dict(
    id=91, title="Counter와 최빈값",
    story="'파이썬에는 배터리가 포함되어 있다(batteries included).' 표준 라이브러리가 풍부하다는 자랑입니다. `collections.Counter`는 세는 일에 특화된 딕셔너리입니다.",
    task="첫째 줄에 N, 둘째 줄에 N개의 정수가 주어집니다. 가장 많이 나온 값과 그 횟수를 출력하십시오. 그런 값이 여럿이면 **가장 작은 값**을 출력합니다.",
    constraints="1 ≤ N ≤ 10⁵, |각 수| ≤ 10⁹",
    examples=[("7\n3 1 3 2 1 5 1", "1 3"), ("4\n9 8 9 8", "8 2")],
    hidden=["1\n-7", "3\n5 6 7", G("n = 100000\nprint(n)\nprint(*[random.randint(-50, 50) for _ in range(n)])", 11)],
    hint="`Counter(리스트)`로 센 뒤, `min(c.items(), key=lambda kv: (-kv[1], kv[0]))`로 '횟수가 크고 값이 작은' 쌍을 고르십시오.",
    solution="from collections import Counter\nn = int(input())\nc = Counter(map(int, input().split()))\nvalue, freq = min(c.items(), key=lambda kv: (-kv[1], kv[0]))\nprint(value, freq)",
    explanation="`c.most_common(1)`은 동점일 때 **먼저 나온** 값을 돌려줍니다. 그래서 '가장 작은 값' 조건을 보장하지 못합니다. 예제 2에서 `most_common`을 쓰면 9가 나옵니다. "
                "도구를 쓸 때는 그 도구가 동점을 어떻게 처리하는지까지 확인해야 합니다. 문서를 읽는 습관이 필요한 이유입니다.",
),
dict(
    id=92, title="스물하나",
    story="카드 게임 '스물하나'에서는 합이 21을 넘지 않으면서 21에 가장 가까운 사람이 이깁니다. `itertools.combinations`는 가능한 모든 조합을 차례로 내놓아 이런 탐색을 한 줄로 만들어 줍니다.",
    task="첫째 줄에 카드 수 N과 상한 M, 둘째 줄에 N장의 카드 숫자가 주어집니다. 서로 다른 카드 3장을 골라 합이 M을 넘지 않으면서 M에 가장 가깝게 만들 때 그 합을 출력하십시오. 그런 조합은 반드시 존재합니다.",
    constraints="3 ≤ N ≤ 100, 1 ≤ 카드 숫자 ≤ 10⁵, 3 ≤ M ≤ 3×10⁵",
    examples=[("5 21\n5 6 7 8 9", "21"), ("4 15\n1 2 9 9", "12")],
    hidden=["3 100\n1 2 3", "6 500\n93 181 245 214 315 36",
            G("n = 100\nm = 150000\nprint(n, m)\nprint(*[random.randint(1, 100000) for _ in range(n)])", 12)],
    hint="`for trio in combinations(cards, 3):`로 모든 3장 조합을 돌며 `sum(trio) <= M`인 것 가운데 최댓값을 구하십시오.",
    solution="from itertools import combinations\nn, m = map(int, input().split())\ncards = list(map(int, input().split()))\nprint(max(s for t in combinations(cards, 3) if (s := sum(t)) <= m))",
    explanation="N = 100이면 조합은 C(100, 3) = 161,700가지로, 모두 살펴도 금방 끝납니다. 이처럼 **경우의 수를 먼저 계산해 보고** 완전 탐색이 가능한지 판단하는 습관이 중요합니다. "
                "제너레이터 안에서 `:=`로 합을 한 번만 계산했습니다. 쓰기 어렵다면 평범한 이중 조건문으로 풀어도 좋습니다.",
),
dict(
    id=93, title="며칠 남았을까",
    story="날짜 계산은 생각보다 까다롭습니다. 달마다 날수가 다르고, 윤년이 있으며, 그레고리력이 처음 시행된 1582년 10월에는 4일 다음 날이 15일이었습니다. 이런 일은 직접 계산하지 말고 `datetime` 모듈에 맡기는 것이 현명합니다.",
    task="두 줄에 걸쳐 날짜가 `YYYY-MM-DD` 형식으로 주어집니다. 첫째 줄에 첫 날짜의 요일(`월요일`~`일요일`)을, 둘째 줄에 첫 날짜에서 둘째 날짜까지의 날수(둘째 − 첫째, 음수 가능)를 출력하십시오.",
    constraints="연도는 1 이상 9999 이하",
    examples=[("2026-11-23\n2027-01-01", "월요일\n39")],
    hidden=["2000-01-01\n2000-01-01", "2024-03-01\n2024-02-28", "1582-10-15\n2026-11-23", "9999-12-31\n0001-01-01"],
    hint="`date.fromisoformat(문자열)`로 날짜 객체를 만들고, 두 날짜를 빼면 `timedelta`가 나옵니다. 그 `.days`가 날수입니다. 요일은 `.weekday()`(월요일이 0)입니다.",
    solution='from datetime import date\nd1 = date.fromisoformat(input())\nd2 = date.fromisoformat(input())\nprint("월화수목금토일"[d1.weekday()] + "요일")\nprint((d2 - d1).days)',
    explanation="`date` 객체끼리의 뺄셈, 비교, 정렬이 모두 자연스럽게 동작합니다. 2024년은 윤년이라 2월 28일과 3월 1일 사이에 2월 29일이 끼어 있어, 숨은 테스트의 답은 −1이 아니라 −2입니다. "
                "`datetime`은 그레고리력을 과거로 연장한 달력(proleptic Gregorian)을 씁니다. 그래서 1582년 이전 날짜는 역사 기록과 다를 수 있습니다. 요일 이름을 `\"월화수목금토일\"[i]`처럼 문자열 인덱싱으로 고르는 요령도 기억해 둘 만합니다.",
),
dict(
    id=94, title="정확한 제곱근",
    story="실수(float)는 유효숫자를 약 15~16자리까지만 기억합니다. 그래서 아주 큰 정수에 `** 0.5`를 쓰면 끝자리가 틀어집니다. `math.isqrt`는 정수만으로 계산하므로 몇 자리든 정확합니다.",
    task="정수 n이 주어질 때 ⌊√n⌋(제곱해서 n을 넘지 않는 가장 큰 정수)를 출력하십시오.",
    constraints="0 ≤ n ≤ 10⁴⁰",
    examples=[("10", "3"), ("1000000000000000000000000000000000000", "1000000000000000000")],
    hidden=["0", "1", "99", "100", str((10**8 + 1) ** 2 - 1), str((10**15 + 1) ** 2 - 1), str((10**18 + 1) ** 2 - 1), str((10**20) ** 2), str(2**127 - 1)],
    hint="`math.isqrt(n)`을 쓰십시오. `int(n ** 0.5)`가 어떤 입력에서 틀리는지도 직접 확인해 보십시오.",
    solution="import math\nprint(math.isqrt(int(input())))",
    explanation="예를 들어 n = (10⁸ + 1)² − 1, 겨우 17자리 수에 대해 `int(n ** 0.5)`는 10⁸이 아니라 10⁸ + 1을 답합니다. 실수로 바꾸는 순간 끝자리 정보가 사라지기 때문입니다. "
                "`isqrt`는 뉴턴 방법을 정수로만 수행하여 언제나 정확한 값을 줍니다. 경시 문제에서 '어떤 수가 완전제곱수인가'를 판정할 때는 반드시 `isqrt(n) ** 2 == n`을 쓰십시오.",
),
dict(
    id=95, title="bisect로 세기",
    story="20번 문제에서 예고했던 `bisect` 모듈입니다. 정렬된 리스트에서 어떤 값이 들어갈 자리를 **이분 탐색**으로 찾아 줍니다. 백만 개 중에서도 20번 남짓 비교하면 됩니다.",
    task="첫째 줄에 N, 둘째 줄에 N개의 정수, 셋째 줄에 질의 수 Q, 이어서 Q줄에 정수 x가 주어집니다. 각 질의마다 N개의 수 가운데 **x 이하인 수의 개수**를 출력하십시오.",
    constraints="1 ≤ N, Q ≤ 10⁵, |각 수| ≤ 10⁹",
    examples=[("5\n9 3 1 7 3\n3\n3\n0\n10", "3\n0\n5")],
    hidden=["1\n5\n2\n5\n4",
            G("n = q = 100000\nprint(n)\nprint(*[random.randint(-10**9, 10**9) for _ in range(n)])\nprint(q)\nfor _ in range(q):\n    print(random.randint(-10**9, 10**9))", 13)],
    hint="먼저 정렬한 뒤 `bisect_right(a, x)`를 쓰십시오. x와 같은 값들 **오른쪽**의 위치, 곧 x 이하인 원소의 개수를 돌려줍니다.",
    solution='import sys\nfrom bisect import bisect_right\ninput = sys.stdin.readline\nn = int(input())\na = sorted(map(int, input().split()))\nq = int(input())\nprint("\\n".join(str(bisect_right(a, int(input()))) for _ in range(q)))',
    explanation="질의마다 리스트를 처음부터 훑으면 10⁵ × 10⁵ = 100억 번이 걸리지만, 정렬 한 번(N log N) 뒤 이분 탐색(질의당 log N)을 하면 순식간입니다. "
                "`bisect_left`는 x 미만인 개수, `bisect_right`는 x 이하인 개수입니다. 둘의 차가 곧 x의 개수입니다. 제2부 '이분 탐색'에서 이 원리를 직접 구현해 봅니다.",
),
# ───────────────── 20 기초 종합 ─────────────────
dict(
    id=96, title="숫자 야구",
    story="서로 다른 세 숫자를 맞히는 '숫자 야구'는 연필과 종이만으로 즐기던 추리 놀이입니다. 숫자와 자리가 모두 맞으면 스트라이크, 숫자만 맞고 자리가 다르면 볼입니다.",
    task="첫째 줄에 정답, 둘째 줄에 추측이 주어집니다. 둘 다 1~9의 서로 다른 숫자 세 개로 된 문자열입니다. 스트라이크도 볼도 없으면 `OUT`, 그렇지 않으면 `xS yB`를 출력하십시오.",
    examples=[("123\n132", "1S 2B"), ("123\n456", "OUT")],
    hidden=["123\n123", "123\n312", "987\n789", "159\n951", "246\n248"],
    hint="스트라이크는 같은 자리의 글자가 같은 경우입니다. 볼은 '공통 숫자의 개수 − 스트라이크'로 구할 수 있습니다.",
    solution='answer, guess = input(), input()\nstrike = sum(a == g for a, g in zip(answer, guess))\nball = len(set(answer) & set(guess)) - strike\nprint("OUT" if strike == ball == 0 else f"{strike}S {ball}B")',
    explanation="`zip`으로 같은 자리끼리 짝지어 비교하고(82번), 집합의 교집합으로 공통 숫자를 셉니다(61번). 그동안 배운 도구 세 가지가 세 줄에 모였습니다. "
                "볼을 자리마다 따로 세지 않고 **전체에서 스트라이크를 빼는** 발상이 핵심입니다. `strike == ball == 0` 같은 연쇄 비교는 5번에서 본 것과 같습니다.",
),
dict(
    id=97, title="로마 숫자 만들기",
    story="로마 숫자에는 0이 없고 자릿값도 없습니다. I(1), V(5), X(10), L(50), C(100), D(500), M(1000)을 늘어놓되, 4는 IIII 대신 IV(5 − 1)처럼 작은 기호를 앞에 두어 빼는 규칙을 씁니다.",
    task="1 이상 3999 이하의 정수를 로마 숫자로 바꾸어 출력하십시오.",
    examples=[("1994", "MCMXCIV"), ("4", "IV")],
    hidden=["1", "9", "14", "40", "90", "400", "2026", "3888", "3999"],
    hint="`1000 M, 900 CM, 500 D, 400 CD, 100 C, 90 XC, 50 L, 40 XL, 10 X, 9 IX, 5 V, 4 IV, 1 I` 열세 쌍의 표를 만들고, 큰 것부터 뺄 수 있는 만큼 빼십시오. 12번의 거스름돈과 같은 탐욕 방식입니다.",
    solution='TABLE = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),\n         (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]\nn = int(input())\nout = []\nfor value, symbol in TABLE:\n    q, n = divmod(n, value)\n    out.append(symbol * q)\nprint("".join(out))',
    explanation="뺄셈 표기(CM, CD, XC, XL, IX, IV)를 처음부터 표에 넣어 두면 예외 처리 없이 거스름돈 문제와 똑같아집니다. **규칙의 예외를 데이터로 바꾸는** 좋은 예입니다. "
                "로마 숫자로 쓸 수 있는 가장 큰 수가 3999(MMMCMXCIX)인 것은 같은 기호를 세 번까지만 쓰는 관례 때문입니다.",
),
dict(
    id=98, title="로마 숫자 읽기",
    story="로마 숫자를 읽는 규칙은 의외로 간단합니다. 왼쪽에서 오른쪽으로 읽되, 어떤 기호가 **바로 오른쪽 기호보다 작으면** 그 값을 빼고, 그렇지 않으면 더합니다.",
    task="올바른 로마 숫자(1~3999)가 주어질 때 그 값을 출력하십시오.",
    examples=[("MCMXCIV", "1994"), ("III", "3")],
    hidden=["I", "IV", "IX", "XLII", "MMXXVI", "MMMCMXCIX", "CDXLIV"],
    hint="기호의 값을 딕셔너리로 만들고, 각 위치에서 다음 기호의 값과 비교하십시오. 마지막 기호는 언제나 더합니다.",
    solution='VALUE = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}\ns = input()\ntotal = 0\nfor i, ch in enumerate(s):\n    v = VALUE[ch]\n    if i + 1 < len(s) and v < VALUE[s[i + 1]]:\n        total -= v\n    else:\n        total += v\nprint(total)',
    explanation="97번과 98번을 함께 풀면, 정수 → 로마 숫자 → 정수로 돌아왔을 때 원래 수가 나오는지 1부터 3999까지 모두 시험해 볼 수 있습니다. 서로 반대인 두 함수로 **서로를 검증하는** 방법은 실무에서도 자주 쓰입니다. "
                "`i + 1 < len(s)` 검사를 먼저 둔 것은 25번에서 배운 단락 평가 덕분에 범위를 벗어난 인덱스를 건드리지 않기 위해서입니다.",
),
dict(
    id=99, title="끝말잇기 심판",
    story="끝말잇기의 규칙은 두 가지입니다. 앞 단어의 마지막 글자로 시작할 것, 그리고 이미 나온 단어를 다시 쓰지 말 것. 심판 프로그램은 규칙을 처음 어긴 순간을 정확히 짚어 내야 합니다.",
    task="첫째 줄에 N, 이어서 N줄에 단어가 하나씩 주어집니다. 끝까지 규칙을 지켰으면 `성공`을, 그렇지 않으면 규칙을 처음 어긴 단어의 순서를 `k번째 단어에서 실패` 형식으로 출력하십시오. (두음 법칙은 적용하지 않습니다.)",
    constraints="1 ≤ N ≤ 1000, 단어 길이 2 이상 10 이하",
    examples=[("4\n기차\n차표\n표범\n범인", "성공"), ("4\n우유\n유리\n리우\n우유", "4번째 단어에서 실패")],
    hidden=["1\n사과", "3\n사과\n과자\n사과", "2\n나무\n무지개", "3\n바다\n다리\n리본", "2\napple\nelephant"],
    hint="이미 나온 단어는 집합에 넣어 두고, 각 단어마다 '앞 단어의 끝 글자와 첫 글자 비교'와 '집합에 있는지'를 검사하십시오.",
    solution='n = int(input())\nused = set()\nprev = None\nresult = "성공"\nfor k in range(1, n + 1):\n    w = input()\n    if (prev is not None and prev[-1] != w[0]) or w in used:\n        result = f"{k}번째 단어에서 실패"\n        break\n    used.add(w)\n    prev = w\nprint(result)',
    explanation="첫 단어에는 앞 단어가 없으므로 `prev is not None` 검사가 필요합니다. 처음과 끝을 따로 생각하는 습관이 버그를 막습니다. "
                "주의할 점이 있습니다. 실패한 뒤에 `break`하면 남은 입력을 읽지 않게 됩니다. 이 문제는 출력이 하나뿐이라 괜찮지만, 여러 사례를 연달아 처리하는 문제에서는 남은 줄을 마저 읽어야 다음 사례가 어긋나지 않습니다.",
),
dict(
    id=100, title="가계부 결산",
    story="기초편의 마지막 문제입니다. 입력을 쪼개고, 딕셔너리에 모으고, 정렬하고, 서식에 맞춰 출력하는, 지금까지 익힌 모든 기술을 하나의 작은 프로그램에 담아 봅니다.",
    task="첫째 줄에 N, 이어서 N줄에 `MM-DD 항목 금액`이 주어집니다(수입은 양수, 지출은 음수). 다음을 차례로 출력하십시오.\n\n"
         "1. 항목 이름의 사전 순서로, 항목마다 `항목 합계`\n"
         "2. `잔액 전체합계`\n"
         "3. 지출(음수 금액)의 합이 가장 큰 날을 `최대 지출일 MM-DD (지출액)`. 같은 날이 여럿이면 이른 날짜, 지출이 전혀 없으면 `최대 지출일 없음`\n\n"
         "모든 금액은 세 자리마다 쉼표를 넣고, 지출액은 양수로 나타냅니다.",
    constraints="1 ≤ N ≤ 1000, 날짜는 같은 해, |금액| ≤ 10⁸",
    examples=[("6\n11-01 월급 2500000\n11-02 식비 -12000\n11-02 교통 -1450\n11-05 식비 -30000\n11-05 도서 -18000\n11-07 식비 -9000",
               "교통 -1,450\n도서 -18,000\n식비 -51,000\n월급 2,500,000\n잔액 2,429,550\n최대 지출일 11-05 (48,000)")],
    hidden=["1\n01-01 용돈 10000", "3\n12-31 식비 -5000\n01-01 식비 -5000\n06-15 선물 -5000",
            "4\n03-02 환불 3000\n03-01 식비 -3000\n03-02 식비 -2000\n03-03 교통 -100000000"],
    hint="딕셔너리 두 개를 쓰십시오. 하나는 항목별 합계, 다른 하나는 날짜별 지출 합계입니다. 최대 지출일은 `(-지출액, 날짜)`가 가장 작은 것을 고르면 동점 처리까지 한 번에 됩니다.",
    solution='n = int(input())\nby_item, spent = {}, {}\nfor _ in range(n):\n    day, item, amount = input().split()\n    amount = int(amount)\n    by_item[item] = by_item.get(item, 0) + amount\n    if amount < 0:\n        spent[day] = spent.get(day, 0) - amount\nfor item in sorted(by_item):\n    print(f"{item} {by_item[item]:,}")\nprint(f"잔액 {sum(by_item.values()):,}")\nif spent:\n    day = min(spent, key=lambda d: (-spent[d], d))\n    print(f"최대 지출일 {day} ({spent[day]:,})")\nelse:\n    print("최대 지출일 없음")',
    explanation="`MM-DD` 형식은 자릿수가 고정되어 있어 문자열 비교만으로 날짜 순서가 맞습니다. 2번 문제에서 본 ISO 8601의 장점이 여기서 쓰입니다. "
                "`min(딕셔너리, key=…)`는 키들 가운데 기준값이 가장 작은 키를 돌려줍니다. 한글 항목 이름은 유니코드 순서로 정렬되며, 이것은 가나다순과 같습니다. "
                "기초편을 마친 것을 축하합니다. 이제 제2부에서 이 도구들로 **알고리즘**을 만들어 봅니다.",
),
]
