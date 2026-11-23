# 응용 126–150
from testlib import G

PROBLEMS = [
# ───────────────── 26 이분 탐색 ─────────────────
dict(
    id=126, title="이분 탐색 손으로 짜기",
    story="1946년에 처음 소개된 이분 탐색이 버그 없이 출판된 것은 1962년의 일이라는 이야기가 있습니다. 2006년에는 자바 표준 라이브러리의 이분 탐색에서조차 오버플로 버그가 발견되었습니다. 단순해 보이지만 경계를 정확히 다루기는 생각보다 어렵습니다.",
    task="첫째 줄에 N, 둘째 줄에 오름차순으로 정렬된 N개의 정수(중복 가능), 셋째 줄에 Q, 이어서 Q줄에 정수 x가 주어집니다. 각 x가 **처음 나타나는 위치**(1부터)를 출력하고, 없으면 −1을 출력하십시오. `bisect`를 쓰지 말고 직접 구현하십시오.",
    constraints="1 ≤ N, Q ≤ 10⁵, |각 수| ≤ 10⁹",
    examples=[("6\n1 3 3 3 7 9\n4\n3\n9\n4\n-5", "2\n6\n-1\n-1")],
    hidden=["1\n5\n2\n5\n6", "5\n2 2 2 2 2\n2\n2\n1",
            G("n = q = 100000\nprint(n)\nprint(*sorted(random.randint(-10**5, 10**5) for _ in range(n)))\nprint(q)\nfor _ in range(q):\n    print(random.randint(-10**5, 10**5))", 22)],
    hint="구간 [lo, hi)를 두고 `a[mid] < x`이면 lo = mid + 1, 아니면 hi = mid로 줄이십시오. 끝나면 lo는 'x 이상인 첫 위치'입니다. 그 자리에 x가 있는지 확인하십시오.",
    solution='import sys\ninput = sys.stdin.readline\n\ndef lower_bound(a, x):\n    lo, hi = 0, len(a)\n    while lo < hi:\n        mid = (lo + hi) // 2\n        if a[mid] < x:\n            lo = mid + 1\n        else:\n            hi = mid\n    return lo\n\nn = int(input())\na = list(map(int, input().split()))\nout = []\nfor _ in range(int(input())):\n    x = int(input())\n    i = lower_bound(a, x)\n    out.append(i + 1 if i < n and a[i] == x else -1)\nprint("\\n".join(map(str, out)))',
    explanation="반열린 구간 [lo, hi)를 쓰면 '찾는 값이 없을 때'와 '맨 끝보다 클 때'를 따로 다루지 않아도 됩니다. lo는 언제나 'x 이상인 첫 원소의 위치'(없으면 N)로 수렴합니다. 이것이 `bisect_left`가 하는 일입니다. "
                "반복할 때마다 구간이 절반으로 줄기 때문에 10⁵개에서도 17번이면 끝납니다. "
                "자바의 버그는 `(lo + hi) / 2`가 정수 범위를 넘어 음수가 된 것이었습니다. 파이썬에서는 일어나지 않지만, 다른 언어에서는 `lo + (hi - lo) / 2`로 써야 합니다.",
),
dict(
    id=127, title="업다운 게임",
    story="'1부터 100 사이의 수를 맞혀 봐. 틀리면 더 큰지 작은지 알려 줄게.' 가장 똑똑하게 질문하면 최악의 경우 몇 번 만에 맞힐 수 있을까요? 매번 가운데를 묻는 것이 최선이고, 그 답은 2의 거듭제곱과 관련이 있습니다.",
    task="1 이상 N 이하의 수 하나를 맞히려 합니다. 추측할 때마다 정답, 업, 다운 중 하나를 듣습니다. 최선의 전략으로 **최악의 경우에도 반드시 맞히는** 데 필요한 추측 횟수를 출력하십시오.",
    constraints="1 ≤ N ≤ 10¹⁸",
    examples=[("100", "7"), ("1", "1")],
    hidden=["2", "3", "7", "8", "1023", "1024", "1000000000000000000"],
    hint="k번의 추측으로 구별할 수 있는 수는 최대 1 + 2 + 4 + … + 2^(k−1) = 2^k − 1개입니다. 2^k − 1 ≥ N인 가장 작은 k를 구하십시오.",
    solution="n = int(input())\nprint(n.bit_length())",
    explanation="첫 추측은 1개를 확인하고 나머지를 두 쪽으로 나눕니다. 그래서 k번이면 2ᵏ − 1개까지 감당할 수 있습니다. 2ᵏ − 1 ≥ N인 가장 작은 k는 N을 2진수로 썼을 때의 자릿수, 곧 `N.bit_length()`와 같습니다. "
                "`math.log2`로 계산하면 N = 2ᵏ 근처에서 실수 오차가 생길 수 있습니다. 정수 연산만으로 답하는 `bit_length()`가 안전합니다. "
                "10¹⁸개 중에서도 60번이면 충분합니다. 이분 탐색의 위력을 실감할 수 있는 숫자입니다.",
),
dict(
    id=128, title="k제곱근",
    story="94번의 `math.isqrt`는 제곱근만 다룹니다. 세제곱근이나 10제곱근의 정수 부분이 필요하면 직접 만들어야 합니다. 이분 탐색은 '답이 될 수 있는 정수'의 범위를 반씩 줄여 나가는 가장 믿을 만한 방법입니다.",
    task="정수 n과 k가 주어질 때, xᵏ ≤ n을 만족하는 가장 큰 정수 x를 출력하십시오.",
    constraints="0 ≤ n ≤ 10¹⁰⁰, 2 ≤ k ≤ 100",
    examples=[("27 3", "3"), ("1000000 6", "10")],
    hidden=["0 2", "1 100", "2 2", "26 3", "64 6", "63 6", "1" + "0" * 100 + " 2", "1" + "0" * 100 + " 100", str(12345678901234567890 ** 5) + " 5", str(12345678901234567890 ** 5 - 1) + " 5"],
    hint="lo = 0, hi = n + 1(또는 더 작은 상한)로 두고, `mid ** k <= n`이면 lo = mid, 아니면 hi = mid로 줄이십시오. 정수 연산만 쓰므로 오차가 없습니다.",
    solution="n, k = map(int, input().split())\nlo, hi = 0, 1 << (n.bit_length() // k + 1)\nwhile hi - lo > 1:\n    mid = (lo + hi) // 2\n    if mid ** k <= n:\n        lo = mid\n    else:\n        hi = mid\nprint(lo)",
    explanation="불변식은 'lo^k ≤ n < hi^k'입니다. 이 성질을 반복 내내 유지하면서 hi − lo = 1이 될 때까지 줄이면 lo가 답입니다. 어떤 값을 lo에, 어떤 값을 hi에 넣을지를 이 불변식이 결정해 줍니다. "
                "상한을 n + 1로 잡으면 10¹⁰⁰에서 약 330번 반복하지만, n의 비트 수를 k로 나누어 상한을 잡으면 훨씬 줄어듭니다. `round(n ** (1/k))`는 실수 오차 때문에 큰 수에서 틀립니다. 마지막 두 숨은 테스트가 그 함정입니다.",
),
dict(
    id=129, title="예산 안의 짝",
    story="정렬된 두 목록에서 조건을 만족하는 짝을 세는 문제는 두 가지 방법으로 풀 수 있습니다. 이분 탐색을 여러 번 하는 방법과, 두 손가락을 반대 방향으로 움직이는 방법입니다. 둘 다 알아 두면 문제를 보는 눈이 넓어집니다.",
    task="첫째 줄에 N, M, X, 둘째 줄에 N개의 정수 A, 셋째 줄에 M개의 정수 B가 주어집니다. a + b ≤ X인 쌍 (a ∈ A, b ∈ B)의 개수를 출력하십시오. (같은 값이라도 위치가 다르면 다른 원소입니다.)",
    constraints="1 ≤ N, M ≤ 10⁵, |각 수|, |X| ≤ 10⁹",
    examples=[("3 4 10\n1 5 9\n2 5 8 1", "8")],
    hidden=["1 1 0\n0\n0", "1 1 -1\n0\n0", "3 3 100\n1 1 1\n1 1 1",
            G("n = m = 100000\nprint(n, m, random.randint(-10**9, 10**9))\nprint(*[random.randint(-10**9, 10**9) for _ in range(n)])\nprint(*[random.randint(-10**9, 10**9) for _ in range(m)])", 23)],
    hint="B를 정렬한 뒤 A의 각 원소 a마다 `bisect_right(B, X - a)`를 더하십시오.",
    solution="from bisect import bisect_right\nn, m, x = map(int, input().split())\na = list(map(int, input().split()))\nb = sorted(map(int, input().split()))\nprint(sum(bisect_right(b, x - v) for v in a))",
    explanation="이분 탐색 방식은 O((N + M) log M)입니다. 투 포인터 방식으로는 A를 오름차순, B를 내림차순으로 훑습니다. a가 커질수록 허용되는 b의 최댓값 X − a가 작아지므로 B의 손가락은 한 방향으로만 움직이고, 정렬 후 O(N + M)이 됩니다. "
                "답은 최대 10¹⁰이라 32비트 정수를 넘습니다. 다른 언어로 옮길 때는 64비트 정수를 써야 합니다.",
),
dict(
    id=130, title="방정식의 근",
    story="5차 이상의 방정식에는 일반적인 근의 공식이 없다는 것을 1824년 아벨이 증명했습니다. 그렇다고 근을 구할 수 없는 것은 아닙니다. 연속인 함수의 부호가 바뀌는 구간을 반씩 좁혀 가는 **이분법**은 어떤 방정식에도 쓸 수 있는 든든한 도구입니다.",
    task="정수 C가 주어질 때 방정식 x³ + x = C의 실수 근을 소수점 아래 넷째 자리까지 반올림해 출력하십시오. (x³ + x는 증가 함수이므로 실수 근은 하나뿐입니다.)",
    constraints="|C| ≤ 10⁹",
    examples=[("2", "1.0000"), ("10", "2.0000"), ("0", "0.0000")],
    hidden=["1", "-1", "1000000000", "-1000000000", "3", "-30", "123456"],
    hint="근은 −1000과 1000 사이에 있습니다. 구간의 가운데에서 함숫값과 C를 비교해 반쪽을 버리는 일을 100번 반복하면 실수가 표현할 수 있는 한계까지 정확해집니다.",
    solution='c = int(input())\nlo, hi = -1001.0, 1001.0\nfor _ in range(100):\n    mid = (lo + hi) / 2\n    if mid ** 3 + mid < c:\n        lo = mid\n    else:\n        hi = mid\nx = (lo + hi) / 2\nif abs(x) < 5e-5:\n    x = 0.0\nprint(f"{x:.4f}")',
    explanation="정수에서는 '구간 길이가 1이 될 때까지' 반복했지만, 실수에서는 정해진 횟수만큼 반복하는 것이 안전합니다. 구간 길이는 2002 / 2¹⁰⁰으로, 실수의 정밀도보다 훨씬 작아집니다. "
                "C = 0일 때 근이 아주 작은 음수로 계산되면 `-0.0000`이 출력되는 함정이 있습니다. 반올림한 결과가 0이 될 값은 0.0으로 바로잡아 이를 막았습니다. "
                "뉴턴 방법 x ← x − f(x)/f'(x)는 훨씬 빨리 수렴하지만, 출발점을 잘못 고르면 발산할 수 있습니다. 이분법은 느리지만 결코 배신하지 않습니다.",
),
# ───────────────── 27 스택과 큐 ─────────────────
dict(
    id=131, title="괄호의 짝",
    story="스택은 접시 더미처럼 마지막에 넣은 것을 먼저 꺼냅니다(LIFO). 괄호의 짝 맞추기는 스택을 위해 태어난 문제라 해도 과언이 아닙니다. 가장 최근에 열린 괄호가 가장 먼저 닫혀야 하기 때문입니다.",
    task="`()`, `[]`, `{}`로만 된 문자열이 주어질 때 올바르게 짝지어져 있으면 `YES`, 아니면 `NO`를 출력하십시오.",
    constraints="1 ≤ 길이 ≤ 10⁵",
    examples=[("{[()()]}", "YES"), ("([)]", "NO")],
    hidden=["(", ")", "()", "((((((((((", "[]{}()", "{[]}([])", "}{", "((())", "(" * 50000 + ")" * 50000, "(" * 50000 + ")" * 49999 + "]"],
    hint="여는 괄호는 스택에 넣고, 닫는 괄호를 만나면 스택 맨 위가 짝이 맞는 여는 괄호인지 확인한 뒤 꺼내십시오. 끝났을 때 스택이 비어 있어야 합니다.",
    solution='PAIR = {")": "(", "]": "[", "}": "{"}\nstack = []\nok = True\nfor ch in input():\n    if ch in "([{":\n        stack.append(ch)\n    elif not stack or stack.pop() != PAIR[ch]:\n        ok = False\n        break\nprint("YES" if ok and not stack else "NO")',
    explanation="실패하는 경우는 세 가지입니다. 닫는 괄호가 나왔는데 스택이 비어 있을 때, 짝이 맞지 않을 때, 그리고 끝났는데 열린 괄호가 남아 있을 때입니다. 세 경우를 빠짐없이 검사해야 합니다. "
                "파이썬 리스트의 `append()`와 `pop()`은 맨 뒤에서 일어나므로 매우 빠릅니다. 리스트가 곧 훌륭한 스택입니다. "
                "괄호 한 종류뿐이라면 스택 없이 '열린 괄호 개수' 하나로 충분합니다. 종류가 여럿일 때 스택이 필요한 이유를 생각해 보십시오.",
),
dict(
    id=132, title="후위 표기법",
    story="1924년 폴란드의 논리학자 우카시에비치는 괄호 없이 수식을 쓰는 표기법을 고안했습니다. 연산자를 피연산자 뒤에 두는 '역폴란드 표기법'은 1972년 휴렛팩커드의 공학용 계산기 HP-35에 채택되어 공학자들의 사랑을 받았습니다.",
    task="후위 표기식이 공백으로 구분된 토큰으로 주어집니다. 토큰은 정수 또는 `+`, `-`, `*`입니다. 식의 값을 출력하십시오. 식은 언제나 올바릅니다.",
    constraints="토큰 수 ≤ 10⁴, |정수| ≤ 100",
    examples=[("3 4 + 2 *", "14"), ("5 1 2 + 4 * + 3 -", "14")],
    hidden=["42", "-7 3 -", "2 3 4 * +", "1 2 - 3 - 4 -", " ".join(["2"] * 100) + " " + " ".join(["*"] * 99)],
    hint="수는 스택에 넣고, 연산자를 만나면 두 개를 꺼내 계산한 결과를 다시 넣으십시오. 먼저 꺼낸 것이 **오른쪽** 피연산자입니다.",
    solution='stack = []\nfor t in input().split():\n    if t in ("+", "-", "*"):\n        b = stack.pop()\n        a = stack.pop()\n        stack.append(a + b if t == "+" else a - b if t == "-" else a * b)\n    else:\n        stack.append(int(t))\nprint(stack[0])',
    explanation="`5 1 2 + 4 * + 3 -`는 중위 표기로 5 + (1 + 2) × 4 − 3입니다. 후위 표기에서는 계산 순서가 토큰의 순서 자체에 담겨 있으므로 괄호도 우선순위 규칙도 필요 없습니다. "
                "빼기와 나누기는 순서가 중요하므로 꺼내는 순서를 바꾸면 안 됩니다. `-7 3 -`에서 `-7`은 음수 하나이지 연산자가 아니라는 점도 확인해 보십시오. "
                "중위 표기를 후위 표기로 바꾸는 방법(다익스트라의 차량기지 알고리즘, 1961)도 스택을 씁니다.",
),
dict(
    id=133, title="카드 버리기",
    story="큐는 줄서기처럼 먼저 온 것이 먼저 나갑니다(FIFO). 파이썬 리스트의 `pop(0)`은 뒤의 원소를 모두 당겨야 해서 느립니다. 양쪽 끝을 모두 빠르게 다루는 `collections.deque`를 써야 합니다.",
    task="1부터 N까지 적힌 카드가 1번이 맨 위에 오도록 쌓여 있습니다. 카드가 한 장 남을 때까지 '맨 위 카드를 버리고, 그다음 맨 위 카드를 맨 아래로 옮기는' 일을 반복합니다. 마지막에 남는 카드를 출력하십시오.",
    constraints="1 ≤ N ≤ 5×10⁵",
    examples=[("6", "4"), ("1", "1")],
    hidden=["2", "3", "7", "8", "500000", "262144", "262145"],
    hint="`deque(range(1, N + 1))`에서 `popleft()`로 버리고, `append(popleft())`로 맨 아래로 옮기십시오.",
    solution="from collections import deque\nn = int(input())\nq = deque(range(1, n + 1))\nwhile len(q) > 1:\n    q.popleft()\n    q.append(q.popleft())\nprint(q[0])",
    explanation="`deque`의 `popleft()`는 O(1)이지만 리스트의 `pop(0)`은 O(N)입니다. N = 50만에서 리스트로 하면 수천억 번 이동이 필요해 끝나지 않습니다. 시간 제한 안에 끝나려면 **연산마다 비용이 얼마인지** 알고 자료구조를 골라야 합니다. "
                "결과를 표로 그려 보면 규칙이 보입니다. N이 2의 거듭제곱이면 답은 N이고, 그렇지 않으면 2 × (N − 2^⌊log₂N⌋)입니다. 111번 요세푸스 문제의 k = 2인 경우와 닮은꼴입니다.",
),
dict(
    id=134, title="다음 큰 수",
    story="'오른쪽에서 처음 만나는 나보다 큰 수'를 찾는 문제는 주가 분석(며칠 뒤에 오르는가)이나 기온 예보(며칠 뒤에 더 따뜻해지는가)에 그대로 쓰입니다. 비결은 아직 답을 찾지 못한 원소들을 스택에 쌓아 두는 것입니다.",
    task="첫째 줄에 N, 둘째 줄에 N개의 정수가 주어집니다. 각 원소마다 오른쪽에 있으면서 그보다 큰 수 가운데 가장 가까운 수를 출력하고, 없으면 −1을 출력하십시오.",
    constraints="1 ≤ N ≤ 10⁵, 1 ≤ 각 수 ≤ 10⁹",
    examples=[("6\n3 5 2 7 7 1", "5 7 7 -1 -1 -1")],
    hidden=["1\n5", "5\n1 2 3 4 5", "5\n5 4 3 2 1", G("n = 100000\nprint(n)\nprint(*[random.randint(1, 10**9) for _ in range(n)])", 24),
            G("n = 100000\nprint(n)\nprint(*range(n, 0, -1))", 25)],
    hint="스택에 '아직 답을 찾지 못한 원소의 인덱스'를 쌓아 둡니다. 새 원소가 스택 맨 위 원소보다 크면, 그 원소의 답은 새 원소입니다. 더 이상 작지 않을 때까지 꺼내십시오.",
    solution="n = int(input())\na = list(map(int, input().split()))\nans = [-1] * n\nstack = []\nfor i, x in enumerate(a):\n    while stack and a[stack[-1]] < x:\n        ans[stack.pop()] = x\n    stack.append(i)\nprint(*ans)",
    explanation="스택 안의 값들은 언제나 아래에서 위로 갈수록 작거나 같습니다(단조 스택). 이중 반복문처럼 보이지만 각 인덱스는 스택에 한 번 들어가고 한 번 나오므로 전체는 O(N)입니다. 이런 분석을 **분할 상환 분석**이라 합니다. "
                "모든 쌍을 비교하는 O(N²) 풀이는 내림차순으로 정렬된 숨은 테스트에서 시간 초과가 납니다.",
),
dict(
    id=135, title="우선순위 프린터",
    story="공용 프린터에 급한 문서가 들어오면 앞에서 기다리던 문서는 뒤로 밀립니다. 이 규칙을 그대로 흉내 내는 것이 큐 시뮬레이션입니다.",
    task="첫째 줄에 문서 수 N과 관심 있는 문서의 위치 M(0부터), 둘째 줄에 대기열 앞에서부터 각 문서의 중요도(1~9)가 주어집니다. "
         "프린터는 맨 앞 문서를 꺼내, 대기열에 그보다 중요도가 높은 문서가 하나라도 있으면 맨 뒤로 보내고, 없으면 인쇄합니다. M번 문서가 몇 번째로 인쇄되는지 출력하십시오.",
    constraints="1 ≤ N ≤ 100",
    examples=[("4 2\n1 2 3 4", "2"), ("6 0\n1 1 9 1 1 1", "5")],
    hidden=["1 0\n5", "3 1\n2 2 2", "5 4\n9 8 7 6 5", "5 0\n1 2 3 4 5", "10 3\n5 1 5 1 5 1 5 1 5 1"],
    hint="`deque`에 (중요도, 원래 위치) 쌍을 넣고 시뮬레이션하십시오. '더 중요한 문서가 있는가'는 `max()`로 확인할 수 있습니다.",
    solution="from collections import deque\nn, m = map(int, input().split())\nq = deque((p, i) for i, p in enumerate(map(int, input().split())))\nprinted = 0\nwhile q:\n    p, i = q.popleft()\n    if any(p < other for other, _ in q):\n        q.append((p, i))\n    else:\n        printed += 1\n        if i == m:\n            print(printed)\n            break",
    explanation="문서마다 원래 위치를 함께 저장해 두는 것이 핵심입니다. 중요도가 같은 문서가 여럿일 수 있어서 중요도만으로는 어느 문서인지 구별할 수 없기 때문입니다. "
                "N이 작아서 매번 대기열 전체를 훑어도 충분합니다. N이 크다면 중요도별 개수를 세어 두거나 힙(`heapq`)을 써서 '남은 최대 중요도'를 빠르게 알아내야 합니다.",
),
# ───────────────── 28 재귀와 백트래킹 ─────────────────
dict(
    id=136, title="N-퀸",
    story="1848년 체스 문제 작가 막스 베첼이 '서로 공격하지 않도록 8개의 퀸을 체스판에 놓는 방법'을 물었고, 가우스도 이 문제에 관심을 보였습니다. 답은 92가지이며, 1972년 다익스트라는 이 문제를 구조적 프로그래밍과 백트래킹의 교재로 삼았습니다.",
    task="N×N 체스판에 퀸 N개를 서로 공격할 수 없게(같은 행, 열, 대각선에 두 개가 없게) 놓는 방법의 수를 출력하십시오.",
    constraints="1 ≤ N ≤ 10",
    examples=[("4", "2"), ("8", "92")],
    hidden=["1", "2", "3", "5", "6", "10"],
    hint="한 행에 퀸은 정확히 하나이므로 행마다 열 하나를 고르면 됩니다. 이미 쓴 열, 이미 쓴 ↘ 대각선(r − c), ↙ 대각선(r + c)을 집합으로 기억해 두고, 겹치는 칸은 건너뛰십시오.",
    solution="def place(r):\n    if r == n:\n        return 1\n    total = 0\n    for c in range(n):\n        if c in cols or r - c in d1 or r + c in d2:\n            continue\n        cols.add(c); d1.add(r - c); d2.add(r + c)\n        total += place(r + 1)\n        cols.remove(c); d1.remove(r - c); d2.remove(r + c)\n    return total\n\nn = int(input())\ncols, d1, d2 = set(), set(), set()\nprint(place(0))",
    explanation="같은 ↘ 대각선 위의 칸들은 r − c가 같고, 같은 ↙ 대각선 위의 칸들은 r + c가 같습니다. 이 관찰 덕분에 대각선 검사가 집합 조회 한 번으로 줄어듭니다. "
                "막힌 갈래를 일찍 잘라 내는 **가지치기**가 백트래킹의 효율을 좌우합니다. 8×8에서 아무렇게나 놓는 방법은 약 44억 가지이지만, 이 프로그램은 2천 번 남짓의 시도로 92가지를 찾아냅니다.",
),
dict(
    id=137, title="부분집합의 합",
    story="주어진 수들 가운데 몇 개를 골라 정확히 S를 만드는 문제는 겉보기에 단순하지만, 수가 많아지면 효율적으로 풀 수 있는 방법이 알려지지 않은 'NP-완전' 문제입니다. 크기가 작을 때는 모든 부분집합을 차례로 살펴보는 것이 정직한 방법입니다.",
    task="첫째 줄에 N과 S, 둘째 줄에 N개의 정수가 주어집니다. 공집합이 아닌 부분집합 가운데 원소의 합이 S인 것의 개수를 출력하십시오. (같은 값이라도 위치가 다르면 다른 원소입니다.)",
    constraints="1 ≤ N ≤ 18, |S| ≤ 10⁶, |각 수| ≤ 10⁵",
    examples=[("5 0\n-7 -3 -2 5 8", "1"), ("3 2\n1 1 1", "3")],
    hidden=["1 0\n0", "1 5\n4", "18 0\n" + " ".join(["0"] * 18), G("print(18, 0)\nprint(*[random.randint(-20, 20) for _ in range(18)])", 26)],
    hint="재귀 함수 `go(i, s)`: i번째 원소를 넣는 경우와 넣지 않는 경우로 나누어 진행합니다. i = N에 이르렀을 때 합이 S이면 하나로 셉니다. S = 0이면 공집합을 빼는 것을 잊지 마십시오.",
    solution="def go(i, s):\n    if i == n:\n        return 1 if s == target else 0\n    return go(i + 1, s + a[i]) + go(i + 1, s)\n\nn, target = map(int, input().split())\na = list(map(int, input().split()))\nprint(go(0, 0) - (1 if target == 0 else 0))",
    explanation="모든 원소마다 '넣는다/안 넣는다' 두 갈래가 있으므로 부분집합은 2ᴺ개입니다. N = 18이면 약 26만 개로 충분히 살펴볼 수 있지만, N = 40이면 1조 개가 넘습니다. "
                "그럴 때는 수를 두 무리로 나누어 각각의 부분합을 모두 구한 뒤 짝을 맞추는 **중간에서 만나기**(meet in the middle) 기법으로 2^(N/2) 수준까지 줄일 수 있습니다. "
                "공집합의 합은 0이므로 S = 0일 때 공집합이 한 번 세어집니다. 그래서 마지막에 1을 뺐습니다.",
),
dict(
    id=138, title="조합 만들기",
    story="80번에서 순열을 만들었다면, 이번에는 순서가 상관없는 조합입니다. 앞에서 고른 수보다 **큰 수만** 고르도록 제한하면, 같은 조합이 순서만 바꾸어 다시 나오는 일이 자연스럽게 사라집니다.",
    task="N과 M이 주어질 때 1부터 N까지의 수 가운데 M개를 고르는 모든 조합을 오름차순으로 나열하여, 사전 순서로 한 줄에 하나씩 출력하십시오.",
    constraints="1 ≤ M ≤ N ≤ 12",
    examples=[("4 2", "1 2\n1 3\n1 4\n2 3\n2 4\n3 4")],
    hidden=["1 1", "5 5", "5 1", "12 6"],
    hint="재귀 함수 `go(start)`: 현재 조합의 길이가 M이면 기록하고, 아니면 start부터 N까지의 수를 하나씩 넣어 `go(그 수 + 1)`을 부르십시오.",
    solution='def go(start):\n    if len(comb) == m:\n        out.append(" ".join(map(str, comb)))\n        return\n    for x in range(start, n + 1):\n        comb.append(x)\n        go(x + 1)\n        comb.pop()\n\nn, m = map(int, input().split())\ncomb, out = [], []\ngo(1)\nprint("\\n".join(out))',
    explanation="80번의 순열과 다른 점은 `used` 배열 대신 `start` 인자를 둔 것 하나뿐입니다. 이 작은 차이가 '순서가 있는 선택'과 '순서가 없는 선택'을 가릅니다. "
                "남은 수가 모자라 M개를 채울 수 없는 갈래(예: x > N − (M − len(comb)) + 1)를 미리 잘라 내면 더 빨라집니다. 실전에서는 `itertools.combinations(range(1, n + 1), m)`이 같은 순서로 조합을 만들어 줍니다.",
),
dict(
    id=139, title="괄호의 카탈랑 수",
    story="올바른 괄호열의 개수 1, 1, 2, 5, 14, 42, …는 19세기 벨기에의 수학자 카탈랑의 이름을 딴 수열입니다. 이 수열은 다각형을 삼각형으로 나누는 방법의 수, 이진 트리의 모양의 수 등 놀랄 만큼 많은 곳에서 나타납니다.",
    task="n이 주어질 때 괄호 n쌍으로 만들 수 있는 올바른 괄호열을 모두 사전 순서(`(`가 `)`보다 앞)로 한 줄에 하나씩 출력하십시오.",
    constraints="1 ≤ n ≤ 8",
    examples=[("3", "((()))\n(()())\n(())()\n()(())\n()()()")],
    hidden=["1", "2", "4", "8"],
    hint="지금까지 쓴 여는 괄호 수 `open`과 닫는 괄호 수 `close`를 들고 다니십시오. `open < n`이면 `(`를, `close < open`이면 `)`를 붙일 수 있습니다. 앞의 것을 먼저 시도하면 사전 순서가 됩니다.",
    solution='def go(s, open_, close):\n    if len(s) == 2 * n:\n        out.append(s)\n        return\n    if open_ < n:\n        go(s + "(", open_ + 1, close)\n    if close < open_:\n        go(s + ")", open_, close + 1)\n\nn = int(input())\nout = []\ngo("", 0, 0)\nprint("\\n".join(out))',
    explanation="`close < open` 조건 하나가 '닫는 괄호가 여는 괄호보다 많아지는 순간'을 원천적으로 막아 줍니다. 그래서 만들어지는 모든 문자열이 올바르며, 131번 같은 검사를 따로 할 필요가 없습니다. 틀린 후보를 만들고 거르는 대신 **처음부터 옳은 것만 만드는** 것이 좋은 백트래킹입니다. "
                "n = 8이면 카탈랑 수 C₈ = 1430개가 나옵니다. 일반항은 C(2n, n) / (n + 1)입니다.",
),
dict(
    id=140, title="연산자 끼워 넣기",
    story="수 사이에 연산자를 끼워 넣는 퍼즐은 백트래킹의 단골 소재입니다. 이 문제에는 숨은 함정이 하나 있습니다. 나눗셈을 C 언어처럼 0 쪽으로 버리는지, 파이썬처럼 음의 무한대 쪽으로 내리는지입니다.",
    task="첫째 줄에 N, 둘째 줄에 N개의 수, 셋째 줄에 덧셈·뺄셈·곱셈·나눗셈 연산자의 개수(합은 N−1)가 주어집니다. 수의 순서는 그대로 두고 수 사이에 연산자를 모두 하나씩 끼워 넣어, 우선순위 없이 **왼쪽부터 차례로** 계산합니다. "
         "나눗셈은 정수 나눗셈이며 **몫의 소수점 아래를 0 쪽으로 버립니다**(예: −7 ÷ 2 = −3). 만들 수 있는 결과의 최댓값과 최솟값을 한 줄에 하나씩 출력하십시오.",
    constraints="2 ≤ N ≤ 11, 1 ≤ 각 수 ≤ 100, 중간 결과의 절댓값은 10⁹ 이하",
    examples=[("3\n3 4 5\n1 0 1 0", "35\n17"), ("3\n1 2 7\n0 1 0 1", "0\n-7")],
    hidden=["2\n5 6\n0 0 1 0", "2\n7 2\n0 0 0 1", "6\n1 2 3 4 5 6\n2 1 1 1", "11\n100 1 100 1 100 1 100 1 100 1 100\n3 3 2 2",
            G("n = 11\nprint(n)\nprint(*[random.randint(1, 100) for _ in range(n)])\nops = [0, 0, 0, 0]\nfor _ in range(n - 1):\n    ops[random.randrange(4)] += 1\nprint(*ops)", 27)],
    hint="남은 연산자 개수를 리스트로 들고 다니며, 개수가 남아 있는 연산자마다 하나씩 써 보고 재귀한 뒤 되돌리십시오. 0 쪽으로 버리는 나눗셈은 `int(a / b)`가 아니라 부호를 따로 처리해 정수만으로 계산하는 것이 안전합니다.",
    solution="def div(a, b):\n    q = abs(a) // abs(b)\n    return q if (a >= 0) == (b > 0) else -q\n\ndef go(i, value):\n    global best, worst\n    if i == n:\n        best, worst = max(best, value), min(worst, value)\n        return\n    for k in range(4):\n        if ops[k]:\n            ops[k] -= 1\n            x = a[i]\n            go(i + 1, value + x if k == 0 else value - x if k == 1 else value * x if k == 2 else div(value, x))\n            ops[k] += 1\n\nn = int(input())\na = list(map(int, input().split()))\nops = list(map(int, input().split()))\nbest, worst = -10**18, 10**18\ngo(1, a[0])\nprint(best)\nprint(worst)",
    explanation="예제 2에서 1 − 2 = −1, −1 ÷ 7은 0 쪽으로 버리면 0이지만 파이썬의 `//`로는 −1이 되어, 최댓값을 0이 아닌 −1로 잘못 답하게 됩니다. 문제의 약속을 언어의 기본 동작과 혼동하지 않는 것이 이 문제의 진짜 시험입니다. "
                "`int(a / b)`도 대개 맞지만, 실수 나눗셈을 거치므로 값이 아주 크면 오차가 생길 수 있습니다. 정수만으로 계산하는 `div` 함수가 더 안전합니다. "
                "연산자의 배치는 최대 10! / (각 개수!의 곱)가지라 많아야 수십만 가지입니다. 함수 안에서 바깥 변수를 바꾸기 위해 `global`을 썼습니다.",
),
# ───────────────── 29 클래스와 객체 ─────────────────
dict(
    id=141, title="분수 클래스",
    story="클래스는 데이터와 그 데이터를 다루는 방법을 한데 묶습니다. `__add__` 같은 **특수 메서드**를 정의하면 우리가 만든 객체도 `+`, `==`, `print()`와 자연스럽게 어울립니다. 파이썬이 '모든 것은 객체'라고 말하는 이유입니다.",
    task="`Fraction` 클래스를 직접 만들어(표준 라이브러리 `fractions`는 쓰지 말 것) `a/b 연산자 c/d` 꼴의 식을 계산하십시오. 연산자는 `+`, `-`, `*`, `/`입니다. "
         "결과는 기약분수 `p/q`(q > 0)로 출력하고, q = 1이면 정수만 출력합니다. 0으로 나누게 되면 `정의되지 않음`을 출력합니다.",
    constraints="|a|, |c| ≤ 10⁶, 1 ≤ b, d ≤ 10⁶",
    examples=[("1/2 + 1/3", "5/6"), ("3/4 * 4/3", "1"), ("-1/2 - 1/2", "-1")],
    hidden=["1/3 / 0/5", "0/7 + 0/9", "2/4 / 1/2", "-3/9 * 3/1", "999999/1000000 + 1/1000000", "1/1000000 - 1/999999", "-5/10 / -1/2"],
    hint="생성자 `__init__`에서 최대공약수로 약분하고, 분모가 음수이면 분자와 분모의 부호를 함께 바꾸십시오. `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__str__`를 정의하면 됩니다.",
    solution='from math import gcd\n\nclass Fraction:\n    def __init__(self, num, den=1):\n        if den == 0:\n            raise ZeroDivisionError\n        if den < 0:\n            num, den = -num, -den\n        g = gcd(num, den)\n        self.num, self.den = num // g, den // g\n\n    def __add__(self, o):\n        return Fraction(self.num * o.den + o.num * self.den, self.den * o.den)\n\n    def __sub__(self, o):\n        return Fraction(self.num * o.den - o.num * self.den, self.den * o.den)\n\n    def __mul__(self, o):\n        return Fraction(self.num * o.num, self.den * o.den)\n\n    def __truediv__(self, o):\n        return Fraction(self.num * o.den, self.den * o.num)\n\n    def __str__(self):\n        return str(self.num) if self.den == 1 else f"{self.num}/{self.den}"\n\ndef parse(s):\n    a, b = s.split("/")\n    return Fraction(int(a), int(b))\n\nx, op, y = input().split()\nx, y = parse(x), parse(y)\ntry:\n    match op:\n        case "+": print(x + y)\n        case "-": print(x - y)\n        case "*": print(x * y)\n        case "/": print(x / y)\nexcept ZeroDivisionError:\n    print("정의되지 않음")',
    explanation="약분을 생성자에서 한 번에 처리했기 때문에, 어떤 연산을 거쳐 만들어진 분수든 언제나 기약분수 상태를 유지합니다. 이처럼 객체가 항상 지켜야 할 성질을 **클래스 불변식**이라 합니다. "
                "`gcd(0, d)`는 d이므로 0/7은 0/1로 정리되어 `0`이 출력됩니다. "
                "표준 라이브러리 `fractions.Fraction`이 바로 이렇게 만들어져 있습니다. 직접 만들어 본 뒤 그 소스 코드를 읽어 보면 많은 것을 배울 수 있습니다.",
),
dict(
    id=142, title="신발끈 공식",
    story="다각형 꼭짓점의 좌표만 알면 넓이를 구할 수 있습니다. 좌표를 엇갈려 곱하는 모습이 신발끈을 묶는 것과 닮아 '신발끈 공식'이라 부르며, 18세기 가우스가 사용한 기록이 있습니다. 그 핵심은 두 벡터의 **외적**입니다.",
    task="`Point` 클래스에 뺄셈(`__sub__`)과 외적(`cross`) 메서드를 정의하고 이를 이용해 다각형의 넓이를 구하십시오. 첫째 줄에 꼭짓점 수 N, 이어서 N줄에 꼭짓점의 좌표가 둘레를 따라 차례로 주어집니다. 넓이를 소수점 아래 첫째 자리까지 출력하십시오.",
    constraints="3 ≤ N ≤ 10⁴, |좌표| ≤ 10⁵, 다각형은 자기 자신과 교차하지 않음",
    examples=[("4\n0 0\n4 0\n4 3\n0 3", "12.0"), ("3\n0 0\n1 0\n0 1", "0.5")],
    hidden=["3\n0 0\n0 1\n1 0", "5\n0 0\n2 0\n2 2\n1 1\n0 2", "4\n-100000 -100000\n100000 -100000\n100000 100000\n-100000 100000", "3\n1 1\n2 2\n3 3"],
    hint="원점 O에 대해 넓이 = |Σ OPᵢ × OPᵢ₊₁| / 2입니다(마지막 꼭짓점 다음은 첫 꼭짓점). 2차원 외적은 a.x × b.y − a.y × b.x입니다.",
    solution='class Point:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n\n    def __sub__(self, o):\n        return Point(self.x - o.x, self.y - o.y)\n\n    def cross(self, o):\n        return self.x * o.y - self.y * o.x\n\nn = int(input())\npts = [Point(*map(int, input().split())) for _ in range(n)]\ntwice = sum(pts[i].cross(pts[(i + 1) % n]) for i in range(n))\nprint(f"{abs(twice) / 2:.1f}")',
    explanation="외적의 합은 꼭짓점이 반시계 방향으로 주어지면 양수, 시계 방향이면 음수가 됩니다. 그래서 절댓값을 취했습니다. 이 부호로 다각형의 방향을 판별할 수도 있습니다. "
                "넓이의 두 배는 언제나 정수이므로 넓이는 `.0` 또는 `.5`로 끝납니다. 실수 오차 걱정이 없습니다. "
                "`__sub__`를 정의해 두었으므로 `(b - a).cross(c - a)`로 세 점의 방향(CCW)을 판정할 수 있습니다. 이것이 계산 기하의 가장 기본적인 연산입니다.",
),
dict(
    id=143, title="은행 계좌",
    story="객체 지향 설계의 교과서적인 예는 은행 계좌입니다. 잔액은 객체 안에 숨겨 두고 입금·출금 메서드를 통해서만 바꾸게 하면, 잔액이 음수가 되는 일을 한 곳에서 막을 수 있습니다. 이를 **캡슐화**라 합니다.",
    task="첫째 줄에 명령 수 Q, 이어서 Q줄에 명령이 주어집니다. 명령을 처리하며, 출력이 필요한 경우에만 한 줄씩 출력하십시오.\n\n"
         "- `open 이름`: 잔액 0인 계좌를 엽니다. 이미 있으면 `이미 있는 계좌`\n"
         "- `deposit 이름 금액`: 입금\n- `withdraw 이름 금액`: 출금. 잔액이 모자라면 `잔액 부족`(잔액은 그대로)\n"
         "- `transfer 보내는이 받는이 금액`: 이체. 잔액이 모자라면 `잔액 부족`(두 계좌 모두 그대로)\n"
         "- `balance 이름`: 잔액 출력\n\n없는 계좌가 관련된 명령에는 `없는 계좌`를 출력합니다.",
    constraints="1 ≤ Q ≤ 1000, 1 ≤ 금액 ≤ 10⁹",
    examples=[("8\nopen kim\nopen lee\ndeposit kim 5000\ntransfer kim lee 3000\nwithdraw lee 4000\nbalance lee\nbalance park\nopen kim", "잔액 부족\n3000\n없는 계좌\n이미 있는 계좌")],
    hidden=["1\nbalance x", "4\nopen a\nwithdraw a 1\ndeposit a 1\nbalance a", "5\nopen a\ndeposit a 10\ntransfer a b 5\ntransfer a a 10\nbalance a",
            "6\nopen a\nopen b\ndeposit a 7\ntransfer a b 7\nbalance a\nbalance b"],
    hint="`Account` 클래스에 `deposit`, `withdraw` 메서드를 두고, 잔액이 모자라면 직접 정의한 예외 `InsufficientFunds`를 일으키십시오. 계좌들은 `이름 → Account` 딕셔너리로 관리합니다.",
    solution='class InsufficientFunds(Exception):\n    pass\n\nclass Account:\n    def __init__(self):\n        self._balance = 0\n\n    def deposit(self, amount):\n        self._balance += amount\n\n    def withdraw(self, amount):\n        if amount > self._balance:\n            raise InsufficientFunds\n        self._balance -= amount\n\n    @property\n    def balance(self):\n        return self._balance\n\naccounts = {}\nout = []\nfor _ in range(int(input())):\n    cmd, *args = input().split()\n    try:\n        match cmd:\n            case "open":\n                if args[0] in accounts:\n                    out.append("이미 있는 계좌")\n                else:\n                    accounts[args[0]] = Account()\n            case "deposit":\n                accounts[args[0]].deposit(int(args[1]))\n            case "withdraw":\n                accounts[args[0]].withdraw(int(args[1]))\n            case "transfer":\n                src, dst = accounts[args[0]], accounts[args[1]]\n                src.withdraw(int(args[2]))\n                dst.deposit(int(args[2]))\n            case "balance":\n                out.append(str(accounts[args[0]].balance))\n    except KeyError:\n        out.append("없는 계좌")\n    except InsufficientFunds:\n        out.append("잔액 부족")\nprint("\\n".join(out))',
    explanation="이체에서 두 계좌를 **먼저 모두 찾은 뒤에** 출금하는 순서가 중요합니다. 출금부터 하면 받는 계좌가 없을 때 돈만 사라집니다. 실제 은행 시스템에서 '트랜잭션'이 중요한 이유가 이것입니다. "
                "`_balance`의 밑줄은 '바깥에서 직접 건드리지 말라'는 파이썬의 관례이고, `@property`는 메서드를 속성처럼 읽게 해 줍니다. 읽기는 허용하되 쓰기는 메서드로만 하도록 만든 것입니다. "
                "오류 상황을 반환값 대신 **예외**로 알리면, 정상 흐름의 코드가 오류 검사로 어지러워지지 않습니다.",
),
dict(
    id=144, title="최솟값을 기억하는 스택",
    story="스택에 넣고 빼는 것은 O(1)이지만, '지금 스택에서 가장 작은 값'을 물으면 보통은 전부 훑어야 합니다. 조금만 영리하게 설계하면 이 질문에도 O(1)로 답할 수 있습니다. 자료구조 설계 면접의 단골 문제입니다.",
    task="`MinStack` 클래스를 만들어 다음 명령을 처리하십시오. 첫째 줄에 Q, 이어서 Q줄에 명령이 주어집니다.\n\n"
         "- `push x`: x를 넣습니다.\n- `pop`: 맨 위 값을 꺼내 출력합니다.\n- `top`: 맨 위 값을 출력합니다.\n- `min`: 스택의 최솟값을 출력합니다.\n\n"
         "스택이 비어 있을 때 `pop`, `top`, `min`은 `EMPTY`를 출력합니다. **모든 연산이 O(1)이어야 합니다.**",
    constraints="1 ≤ Q ≤ 2×10⁵, |x| ≤ 10⁹",
    examples=[("8\npush 5\npush 3\nmin\npush 7\nmin\npop\npop\nmin", "3\n3\n7\n3\n5")],
    hidden=["2\npop\nmin", "4\npush 1\npush 1\npop\nmin",
            G("q = 200000\nprint(q)\nfor _ in range(q):\n    r = random.random()\n    if r < 0.45:\n        print('push', random.randint(-10**9, 10**9))\n    elif r < 0.7:\n        print('pop')\n    elif r < 0.85:\n        print('top')\n    else:\n        print('min')", 28)],
    hint="값만 넣지 말고 (값, 그때까지의 최솟값) 쌍을 넣으십시오. 그러면 꺼낸 뒤에도 그 아래 원소에 저장된 최솟값이 곧 남은 스택의 최솟값입니다.",
    solution='import sys\ninput = sys.stdin.readline\n\nclass MinStack:\n    def __init__(self):\n        self.data = []\n\n    def push(self, x):\n        m = x if not self.data else min(x, self.data[-1][1])\n        self.data.append((x, m))\n\n    def pop(self):\n        return self.data.pop()[0] if self.data else "EMPTY"\n\n    def top(self):\n        return self.data[-1][0] if self.data else "EMPTY"\n\n    def min(self):\n        return self.data[-1][1] if self.data else "EMPTY"\n\nst = MinStack()\nout = []\nfor _ in range(int(input())):\n    cmd = input().split()\n    if cmd[0] == "push":\n        st.push(int(cmd[1]))\n    else:\n        out.append(str(getattr(st, cmd[0])()))\nprint("\\n".join(out))',
    explanation="최솟값은 위에서 아래로 갈수록 바뀔 수만 있고, 각 층의 최솟값은 그 아래층들에만 의존합니다. 그래서 층마다 '여기까지의 최솟값'을 함께 저장하면 됩니다. 메모리를 두 배로 써서 시간을 얻은 것입니다. "
                "`getattr(st, \"top\")`은 문자열로 메서드를 찾아 줍니다. 명령 이름과 메서드 이름을 똑같이 지어 두면 `if`-`elif` 사슬 없이 명령을 연결할 수 있습니다.",
),
dict(
    id=145, title="카드 정렬",
    story="`@dataclass`는 파이썬 3.7에서 들어온 데코레이터로, 생성자와 비교 메서드를 자동으로 만들어 줍니다. `order=True`를 주면 필드들을 **선언된 순서대로** 비교하는 튜플 같은 정렬 기준까지 생깁니다.",
    task="트럼프 카드가 `숫자무늬` 꼴의 토큰으로 한 줄에 주어집니다(예: `10H`, `QS`, `2C`). 숫자의 순서는 2 < 3 < … < 10 < J < Q < K < A, 무늬의 순서는 C < D < H < S입니다. "
         "숫자 순서로, 숫자가 같으면 무늬 순서로 정렬해 출력하십시오. `@dataclass(order=True)`로 카드 클래스를 만들어 쓰십시오.",
    constraints="카드 1장 이상 52장 이하, 중복 없음",
    examples=[("10H QS 2C AD 10C", "2C 10C 10H QS AD")],
    hidden=["AS", "AS KS QS JS 10S", "2S 2H 2D 2C", "3H 2S"],
    hint="정렬에 쓸 필드(숫자 순위, 무늬 순위)를 먼저 선언하고, 표시용 문자열은 `field(compare=False)`로 비교에서 빼십시오.",
    solution='from dataclasses import dataclass, field\n\nRANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]\nSUITS = "CDHS"\n\n@dataclass(order=True)\nclass Card:\n    rank: int\n    suit: int\n    label: str = field(compare=False)\n\n    @classmethod\n    def parse(cls, token):\n        return cls(RANKS.index(token[:-1]), SUITS.index(token[-1]), token)\n\ncards = sorted(Card.parse(t) for t in input().split())\nprint(*(c.label for c in cards))',
    explanation="`10H`처럼 숫자가 두 글자인 카드가 있으므로 `token[0]`이 아니라 `token[:-1]`(마지막 글자를 뺀 전부)로 숫자를 잘라야 합니다. 겉보기와 달리 이 부분이 이 문제의 함정입니다. "
                "`@classmethod`로 만든 `parse`는 '문자열로부터 객체를 만드는 또 하나의 생성자' 역할을 합니다. `datetime.fromisoformat`(93번)이 바로 이런 메서드입니다. "
                "직접 `__lt__`를 정의해도 되지만, 데이터 클래스는 짧고 실수가 적습니다.",
),
# ───────────────── 30 응용 종합 ─────────────────
dict(
    id=146, title="LRU 캐시",
    story="캐시는 자주 쓰는 데이터를 빠른 곳에 잠시 보관합니다. 공간이 차면 무엇을 버릴까요? '가장 오랫동안 쓰이지 않은 것(Least Recently Used)'을 버리는 LRU 정책은 운영체제, 웹 브라우저, 데이터베이스 어디에나 쓰입니다.",
    task="첫째 줄에 캐시 크기 C와 요청 수 N, 둘째 줄에 N개의 요청(정수 키)이 주어집니다. 처음에 캐시는 비어 있습니다. 요청한 키가 캐시에 있으면 **적중**이고 그 키는 가장 최근에 쓴 것이 됩니다. "
         "없으면 키를 캐시에 넣고, 이때 캐시가 넘치면 가장 오래전에 쓴 키를 버립니다. 적중 횟수를 출력하십시오.",
    constraints="1 ≤ C ≤ 10⁵, 1 ≤ N ≤ 2×10⁵, 0 ≤ 키 ≤ 10⁹",
    examples=[("3 8\n1 2 3 1 4 2 1 5", "2")],
    hidden=["1 3\n7 7 7", "1 4\n1 2 1 2", "2 6\n1 2 1 3 1 2",
            G("c, n = 1000, 200000\nprint(c, n)\nprint(*[random.randint(0, 1500) for _ in range(n)])", 29)],
    hint="`collections.OrderedDict`는 넣은 순서를 기억하고, `move_to_end(키)`로 맨 뒤로 옮기거나 `popitem(last=False)`로 맨 앞을 꺼낼 수 있습니다.",
    solution="from collections import OrderedDict\nc, n = map(int, input().split())\ncache = OrderedDict()\nhits = 0\nfor key in input().split():\n    if key in cache:\n        hits += 1\n        cache.move_to_end(key)\n    else:\n        cache[key] = True\n        if len(cache) > c:\n            cache.popitem(last=False)\nprint(hits)",
    explanation="예제에서 4가 들어올 때 가장 오래 안 쓰인 2가 버려지므로, 다음 2 요청은 적중하지 못합니다. 적중은 두 번째 1과 마지막 직전의 1, 이렇게 두 번입니다. "
                "`OrderedDict`의 세 연산은 모두 O(1)입니다. 내부적으로 해시 테이블과 이중 연결 리스트를 함께 쓰기 때문입니다. "
                "함수 결과를 캐시하는 `functools.lru_cache`(77번)가 바로 이 정책을 씁니다.",
),
dict(
    id=147, title="편집 거리",
    story="1965년 소련의 수학자 레벤시테인은 한 문자열을 다른 문자열로 바꾸는 데 필요한 최소 편집 횟수를 정의했습니다. 맞춤법 검사기의 '혹시 이 단어를 찾으셨나요?', DNA 서열 비교, 표절 검사가 모두 이 거리를 씁니다.",
    task="두 줄에 걸쳐 문자열 A와 B가 주어집니다. 글자 하나 삽입, 삭제, 교체를 각각 1회로 칠 때 A를 B로 바꾸는 최소 횟수를 출력하십시오.",
    constraints="1 ≤ 각 길이 ≤ 500, 영어 소문자",
    examples=[("kitten\nsitting", "3"), ("flaw\nlawn", "2")],
    hidden=["a\na", "a\nb", "abc\nabcdef", "intention\nexecution",
            G("print(''.join(random.choice('ab') for _ in range(500)))\nprint(''.join(random.choice('ab') for _ in range(500)))", 30)],
    hint="D[i][j] = A의 앞 i글자를 B의 앞 j글자로 바꾸는 최소 횟수라 하면, D[i][j] = min(D[i−1][j] + 1, D[i][j−1] + 1, D[i−1][j−1] + (A[i] ≠ B[j]))입니다.",
    solution="a, b = input(), input()\nprev = list(range(len(b) + 1))\nfor i in range(1, len(a) + 1):\n    cur = [i] + [0] * len(b)\n    for j in range(1, len(b) + 1):\n        cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] != b[j - 1]))\n    prev = cur\nprint(prev[-1])",
    explanation="세 갈래는 각각 A의 글자 삭제(위), B의 글자 삽입(왼쪽), 교체 또는 일치(대각선)입니다. 마지막 글자를 어떻게 처리할지만 결정하면 나머지는 더 작은 같은 문제가 됩니다. 이것이 동적 계획법의 사고방식입니다. "
                "kitten → sitten(교체) → sittin(교체) → sitting(삽입)으로 3입니다. "
                "표 전체 대신 이전 행과 현재 행 두 줄만 썼으므로 메모리는 O(|B|)입니다(120번과 같은 기법). 시간은 O(|A| × |B|)로, 500 × 500 = 25만 칸입니다.",
),
dict(
    id=148, title="달력 그리기",
    story="1882년 독일의 크리스티안 첼러는 날짜만으로 요일을 계산하는 공식을 발표했습니다. 요일을 알면 달력을 그릴 수 있습니다. 첫날의 요일만큼 비우고, 일주일마다 줄을 바꾸면 됩니다.",
    task="연도와 월이 주어질 때 아래 예시와 같은 형식으로 달력을 출력하십시오. 첫 줄은 `YYYY-MM`, 둘째 줄은 요일 머리글이며, 날짜는 일요일부터 시작해 각각 폭 2로 오른쪽 정렬하고 공백 하나로 구분합니다.",
    constraints="1 ≤ 연도 ≤ 9999",
    examples=[("2026 11", "2026-11\nSu Mo Tu We Th Fr Sa\n 1  2  3  4  5  6  7\n 8  9 10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28\n29 30"),
              ("2026 2", "2026-02\nSu Mo Tu We Th Fr Sa\n 1  2  3  4  5  6  7\n 8  9 10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28")],
    hidden=["2024 2", "2000 1", "1 1", "9999 12", "2027 5"],
    hint="`calendar.monthcalendar(년, 월)`은 주마다 날짜 리스트를 주는데 월요일이 먼저 옵니다. `calendar.Calendar(firstweekday=6)`을 쓰면 일요일부터 시작합니다. 0은 빈칸입니다.",
    solution='import calendar\ny, m = map(int, input().split())\nprint(f"{y}-{m:02d}")\nprint("Su Mo Tu We Th Fr Sa")\nfor week in calendar.Calendar(firstweekday=6).monthdayscalendar(y, m):\n    print(" ".join(f"{d:2d}" if d else "  " for d in week))',
    explanation="빈칸도 폭 2의 공백으로 출력하므로, 첫 주가 수요일에 시작하면 앞에 공백이 아홉 칸 놓입니다. 줄 끝의 빈칸은 채점에서 무시됩니다. "
                "2026년 2월은 일요일에 시작하고 28일이라 정확히 네 줄로 끝나는, 몇 년에 한 번 오는 '꽉 찬 2월'입니다. "
                "`calendar` 없이 만들고 싶다면 `datetime.date(y, m, 1).weekday()`로 첫날의 요일을 얻고, 월의 날수는 `calendar.monthrange`나 윤년 규칙(17번)으로 직접 계산하면 됩니다.",
),
dict(
    id=149, title="로그 분석기",
    story="서버는 하루에도 수백만 줄의 로그를 남깁니다. 사람이 읽을 수 없는 양이므로 정규 표현식으로 필요한 줄을 골라내고 형식이 깨진 줄은 걸러 내는 것이 개발자의 일상입니다.",
    task="첫째 줄에 N, 이어서 N줄의 로그가 주어집니다. 올바른 줄의 형식은 `YYYY-MM-DD HH:MM:SS [수준] 메시지`이며, 수준은 영어 대문자 단어입니다. "
         "형식에 맞는 줄만 대상으로, 수준 이름의 사전 순서로 `수준 개수`를 출력하고, 마지막 줄에 가장 먼저 나온 ERROR 줄의 시각을 `첫 ERROR: 날짜 시각`으로 출력하십시오. ERROR가 없으면 `ERROR 없음`을 출력합니다.",
    constraints="1 ≤ N ≤ 10⁴, 형식에 맞는 줄은 적어도 하나",
    examples=[("5\n2026-11-23 09:00:01 [INFO] server started\n2026-11-23 09:00:05 [WARN] disk 81%\nbroken line here\n2026-11-23 09:01:00 [ERROR] db timeout\n2026-11-23 09:02:00 [INFO] retry ok",
               "ERROR 1\nINFO 2\nWARN 1\n첫 ERROR: 2026-11-23 09:01:00")],
    hidden=["1\n2026-01-01 00:00:00 [DEBUG] x", "3\n2026-01-01 00:00:00 [error] lower\n2026-01-01 00:00:00 [ERROR]\n2026-01-01 00:00:01 [ERROR] real",
            "4\n2026-1-01 00:00:00 [INFO] bad date\n2026-01-01 0:00:00 [INFO] bad time\n2026-01-01 00:00:00 INFO no bracket\n2026-12-31 23:59:59 [INFO] good"],
    hint="`re.fullmatch(r\"(\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}) \\[([A-Z]+)\\] (.+)\", 줄)`로 줄 전체가 형식에 맞는지 검사하면서 시각과 수준을 함께 뽑을 수 있습니다.",
    solution='import re\nPAT = re.compile(r"(\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}) \\[([A-Z]+)\\] (.+)")\ncount = {}\nfirst_error = None\nfor _ in range(int(input())):\n    m = PAT.fullmatch(input())\n    if not m:\n        continue\n    when, level = m.group(1), m.group(2)\n    count[level] = count.get(level, 0) + 1\n    if level == "ERROR" and first_error is None:\n        first_error = when\nfor level in sorted(count):\n    print(level, count[level])\nprint(f"첫 ERROR: {first_error}" if first_error else "ERROR 없음")',
    explanation="`fullmatch`는 줄 **전체**가 패턴과 맞아야 성공합니다. `search`나 `match`를 쓰면 앞이나 중간만 맞아도 통과해 버려 깨진 줄을 걸러 내지 못합니다. "
                "`\\d{4}`는 숫자 정확히 4개, `\\[`는 대괄호 글자 자체(특수 기호가 아님)를 뜻합니다. 메시지 부분 `(.+)`는 적어도 한 글자를 요구하므로 메시지가 빈 줄은 걸러집니다. "
                "패턴을 `re.compile`로 미리 컴파일해 두면 같은 패턴을 반복해서 쓸 때 효율적이고 읽기도 좋습니다.",
),
dict(
    id=150, title="텍스트 어드벤처 엔진",
    story="1976년 윌 크라우더가 만든 『콜로설 케이브 어드벤처』는 '북쪽으로 간다' 같은 문장 명령으로 동굴을 탐험하는 최초의 텍스트 어드벤처 게임 가운데 하나입니다. 그 엔진의 뼈대는 방을 꼭짓점, 통로를 간선으로 하는 **그래프**입니다. 제2부의 마지막 문제로 작은 게임 엔진을 만들어 봅니다.",
    task="첫째 줄에 통로 수 M, 이어서 M줄에 `방A 방향 방B`(방A에서 그 방향으로 가면 방B, 한 방향 통로), 다음 줄에 시작 방, 다음 줄에 명령 수 K, 이어서 K줄에 명령이 주어집니다. 방향은 `북`, `남`, `동`, `서` 중 하나입니다.\n\n"
         "- `go 방향`: 통로가 있으면 이동하고, 없으면 `갈 수 없습니다`를 출력합니다.\n"
         "- `look`: `현재 방: 출구1 출구2 …`를 출력합니다. 출구는 `북 남 동 서` 순서로 나열하고, 출구가 없으면 `현재 방: 출구 없음`을 출력합니다.\n\n"
         "모든 명령을 처리한 뒤 마지막 줄에 `최종 위치: 방, 방문한 방: n개`를 출력하십시오(시작 방 포함, 서로 다른 방의 수).",
    constraints="1 ≤ M, K ≤ 1000, 방 이름은 공백 없는 문자열",
    examples=[("4\n입구 북 복도\n복도 동 보물방\n복도 남 입구\n보물방 서 복도\n입구\n5\nlook\ngo 북\ngo 북\ngo 동\nlook",
               "입구: 북\n갈 수 없습니다\n보물방: 서\n최종 위치: 보물방, 방문한 방: 3개")],
    hidden=["1\nA 동 B\nC\n2\nlook\ngo 동", "3\nA 동 B\nB 서 A\nA 서 A\nA\n4\ngo 서\ngo 동\ngo 서\nlook",
            "4\nX 서 Y\nX 동 Z\nX 남 W\nX 북 V\nX\n1\nlook"],
    hint="방마다 `{방향: 다음 방}` 딕셔너리를 두는 '딕셔너리의 딕셔너리'로 그래프를 표현하십시오. `look`의 출구 순서는 `\"북남동서\"`를 차례로 훑으며 있는 것만 고르면 됩니다.",
    solution='m = int(input())\nworld = {}\nfor _ in range(m):\n    a, d, b = input().split()\n    world.setdefault(a, {})[d] = b\nroom = input()\nvisited = {room}\nfor _ in range(int(input())):\n    cmd = input().split()\n    match cmd:\n        case ["go", d]:\n            nxt = world.get(room, {}).get(d)\n            if nxt is None:\n                print("갈 수 없습니다")\n            else:\n                room = nxt\n                visited.add(room)\n        case ["look"]:\n            exits = [d for d in "북남동서" if d in world.get(room, {})]\n            print(f"{room}: {\' \'.join(exits) if exits else \'출구 없음\'}")\nprint(f"최종 위치: {room}, 방문한 방: {len(visited)}개")',
    explanation="예제의 두 번째 `go 북`은 복도에 북쪽 출구가 없어 실패합니다. 그다음 `go 동`으로 보물방에 이르므로 방문한 방은 입구, 복도, 보물방 세 곳입니다. "
                "통로가 한 방향이라는 점에 주의하십시오. 양방향 통로를 원하면 두 줄로 적어야 합니다. `world.get(room, {})`은 통로가 하나도 없는 방도 오류 없이 다루게 해 줍니다. "
                "딕셔너리, 집합, `match`, f-string이 모두 모인 이 작은 엔진에 아이템, 잠긴 문, 대사를 더해 가면 그대로 한 편의 게임이 됩니다. 응용편을 마친 것을 축하합니다. 이제 제3부, 정보올림피아드의 세계로 들어갑니다.",
),
]
