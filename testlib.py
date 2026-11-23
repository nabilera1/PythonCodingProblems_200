"""문제 데이터 파일에서 쓰는 도우미.

G(code, seed): 큰 입력을 '생성하는 코드'로 표현한 숨은 테스트.
  code는 입력을 print로 출력하는 파이썬 코드이며, 앞에 `import random; random.seed(seed)`가 붙어 실행됩니다.
  노트북에는 입력 대신 이 코드만 저장되므로 파일이 가벼워집니다.
"""


def G(code: str, seed: int = 0) -> dict:
    return {"gen": f"import random\nrandom.seed({seed})\n" + code.strip("\n")}
