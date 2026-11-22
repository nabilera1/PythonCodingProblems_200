"""문제 데이터(problems/*.py) → 위키독스 원고(pages/), 목차(TOC.md), README.md, Colab 노트북(notebooks/) 생성.

사용법:  python build.py
- 모든 모범답안을 실제로 실행해 예제 출력과 일치하는지 검증하고,
  숨은 테스트의 기대 출력을 자동으로 만듭니다. 하나라도 틀리면 빌드를 멈춥니다.
"""
import importlib.util, json, pathlib, subprocess, sys, textwrap
import config as C

ROOT = pathlib.Path(__file__).parent
PAGES, NB = ROOT / "pages", ROOT / "notebooks"


def norm(s: str) -> str:
    return "\n".join(line.rstrip() for line in s.strip("\n").splitlines()).strip("\n")


def run(code: str, inp: str) -> str:
    r = subprocess.run([sys.executable, "-c", code], input=inp + "\n", capture_output=True, text=True, timeout=10)
    if r.returncode:
        raise RuntimeError(r.stderr)
    return norm(r.stdout)


def load_problems():
    probs = {}
    for f in sorted((ROOT / "problems").glob("*.py")):
        spec = importlib.util.spec_from_file_location(f.stem, f)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        for p in m.PROBLEMS:
            assert p["id"] not in probs, f"중복 번호 {p['id']}"
            probs[p["id"]] = p
    return probs


def verify(p):
    tests = []
    for i, (inp, out) in enumerate(p["examples"], 1):
        got = run(p["solution"], inp)
        if got != norm(out):
            sys.exit(f"[{p['id']:03d}] 예제 {i} 불일치\n기대: {out!r}\n실제: {got!r}")
        tests.append([inp, norm(out), True])
    for inp in p["hidden"]:
        tests.append([inp, run(p["solution"], inp), False])
    return tests


# ───────────────────────── 위키독스 원고 ─────────────────────────
def colab_url(page_no):
    return (f"https://colab.research.google.com/github/{C.GITHUB_OWNER}/{C.GITHUB_REPO}"
            f"/blob/{C.GITHUB_BRANCH}/notebooks/{page_no:02d}.ipynb")


def badge(page_no):
    return f"[![Colab에서 열기](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url(page_no)})"


def fence(text, lang=""):
    return f"```{lang}\n{text}\n```"


def problem_md(p, with_answers=True):
    out = [f"## {p['id']:03d}. {p['title']}", "", p["story"], "", f"**문제** {p['task']}", ""]
    if p.get("constraints"):
        out += [f"**제한** {p['constraints']}", ""]
    for i, (inp, o) in enumerate(p["examples"], 1):
        n = f" {i}" if len(p["examples"]) > 1 else ""
        if inp:
            out += [f"**예제 입력{n}**", "", fence(inp), ""]
        out += [f"**예제 출력{n}**", "", fence(o.rstrip()), ""]
    if with_answers:
        out += answers_md(p)
    return out


def answers_md(p, heading=False):
    out = [f"### {p['id']:03d}. {p['title']}", ""] if heading else []
    out += ["<details>", "<summary>💡 힌트 보기</summary>", "", p["hint"], "", "</details>", "",
            "<details>", "<summary>✅ 정답과 해설 보기</summary>", "",
            fence(p["solution"], "python"), "", p["explanation"], "", "</details>", ""]
    return out


def page_md(page, probs):
    no, part, name, start = page
    ids = range(start, start + 5)
    out = [f"# {no:02d}. {name}", "",
           f"> {part} · 문제 {start:03d}–{start + 4:03d} · Python {C.PYTHON_TARGET} 기준", "",
           f"{badge(no)} ← 이 단원의 문제를 Colab에서 풀고 바로 채점할 수 있습니다.", "", "---", ""]
    for i in ids:
        out += problem_md(probs[i], with_answers=(C.HIDE_MODE == "details")) + ["---", ""]
    return "\n".join(out)


def answer_page_md(page, probs):
    no, _, name, start = page
    out = [f"# {no:02d}-해설. {name}", "", "문제를 먼저 충분히 고민한 뒤에 펼쳐 보십시오.", ""]
    for i in range(start, start + 5):
        out += answers_md(probs[i], heading=True)
    return "\n".join(out)


# ───────────────────────── Colab 노트북 ─────────────────────────
CHECKER = '''
import subprocess, sys, pathlib

def _norm(s):
    return "\\n".join(l.rstrip() for l in s.strip("\\n").splitlines()).strip("\\n")

def check(pid, time_limit=2.0):
    """p{번호}.py 를 모든 테스트로 실행해 채점합니다."""
    path = pathlib.Path(f"p{pid:03d}.py")
    if not path.exists():
        print(f"먼저 위의 %%writefile p{pid:03d}.py 셀을 실행하세요."); return
    ok = 0
    for i, (inp, exp, shown) in enumerate(TESTS[pid], 1):
        tag = f"예제 {i}" if shown else f"숨은 테스트 {i}"
        try:
            r = subprocess.run([sys.executable, str(path)], input=inp + "\\n",
                               capture_output=True, text=True, timeout=time_limit)
        except subprocess.TimeoutExpired:
            print(f"⏱ {tag}: 시간 초과 ({time_limit}초)"); continue
        got = _norm(r.stdout)
        if r.returncode:
            last = r.stderr.strip().splitlines()[-1] if r.stderr.strip() else "알 수 없는 오류"
            print(f"💥 {tag}: 실행 오류 → {last}")
        elif got == exp:
            ok += 1; print(f"✅ {tag}")
        elif shown:
            print(f"❌ {tag}\\n   입력: {inp!r}\\n   기대: {exp!r}\\n   실제: {got!r}")
        else:
            print(f"❌ {tag}  (입력: {inp[:60]!r})")
    total = len(TESTS[pid])
    print("─" * 30)
    print(f"🎉 {pid:03d}번 통과! ({ok}/{total})" if ok == total else f"{ok}/{total} 통과 — 다시 도전해 보세요.")
'''


def md_cell(src):
    return {"cell_type": "markdown", "metadata": {}, "source": src}


def code_cell(src, hidden=False):
    meta = {"cellView": "form"} if hidden else {}
    return {"cell_type": "code", "execution_count": None, "metadata": meta, "outputs": [], "source": src}


def notebook(page, probs, tests):
    no, part, name, start = page
    ids = list(range(start, start + 5))
    cells = [md_cell(f"# {no:02d}. {name}\n\n{part} · 문제 {start:03d}–{start + 4:03d}\n\n"
                     "**사용법**\n1. 바로 아래 **🔧 채점기 준비** 셀을 먼저 실행합니다(▶).\n"
                     "2. 각 문제의 `%%writefile` 셀에 코드를 작성하고 실행하면 파일로 저장됩니다.\n"
                     "3. 그 아래 `check(번호)` 셀을 실행하면 채점됩니다.\n"
                     "4. 직접 입력을 넣어 실행해 보려면 새 셀에 `%run p001.py`처럼 입력합니다.\n\n"
                     "> 정답과 해설은 위키독스 본문의 접힌 상자에 있습니다. 충분히 고민한 뒤에 펼쳐 보세요.")]
    tdict = {i: tests[i] for i in ids}
    cells.append(code_cell("#@title 🔧 채점기 준비 (먼저 실행하세요)\n" + f"TESTS = {tdict!r}\n" + CHECKER.strip() + "\nprint('채점기 준비 완료!')",
                           hidden=True))
    for i in ids:
        p = probs[i]
        body = [f"## {i:03d}. {p['title']}", "", p["task"]]
        if p.get("constraints"):
            body += ["", f"**제한** {p['constraints']}"]
        for k, (inp, o) in enumerate(p["examples"], 1):
            body += ["", f"**예제 {k}**"]
            if inp:
                body += ["입력", fence(inp)]
            body += ["출력", fence(o.rstrip())]
        cells.append(md_cell("\n".join(body)))
        cells.append(code_cell(f"%%writefile p{i:03d}.py\n# 여기에 코드를 작성하세요\n"))
        cells.append(code_cell(f"check({i})"))
    return {"nbformat": 4, "nbformat_minor": 0,
            "metadata": {"colab": {"provenance": []}, "kernelspec": {"name": "python3", "display_name": "Python 3"},
                         "language_info": {"name": "python"}},
            "cells": cells}


# ───────────────────────── 시작 페이지 · 목차 · README ─────────────────────────
START_MD = f"""# 0. 시작하기

이 책은 **구글 계정 하나만 있으면** 설치 없이 바로 풀 수 있는 파이썬 200문제입니다.

| 구분 | 문제 | 수준 |
|---|---|---|
| 제1부 기초 | 001–100 | 파이썬 문법을 처음 익히는 고등학생 |
| 제2부 응용 | 101–150 | 자료구조와 알고리즘적 사고 입문 |
| 제3부 정보올림피아드 | 151–200 | KOI 고등부 수준, 실전 입출력 형식 |

## 풀이 환경: Google Colab

각 단원 맨 위의 ![Colab](https://colab.research.google.com/assets/colab-badge.svg) 버튼을 누르면 그 단원의 문제가 담긴 노트북이 열립니다.

1. 구글 계정으로 로그인합니다.
2. **채점기 준비** 셀을 먼저 실행합니다.
3. `%%writefile p001.py` 셀에 코드를 쓰고 실행한 뒤, `check(1)`로 채점합니다.
4. 내 드라이브에 저장하려면 [파일] → [Drive에 사본 저장]을 누릅니다.

Colab의 기본 파이썬 버전은 {C.PYTHON_TARGET}입니다. 이 책의 모든 문제와 해답은 이 버전에서 실행되는지 검증했습니다.

## 정답 보기

각 문제 아래에는 두 개의 접힌 상자가 있습니다. 눌러 보십시오.

<details>
<summary>💡 힌트 보기</summary>

막혔을 때 방향만 살짝 알려 줍니다.

</details>

<details>
<summary>✅ 정답과 해설 보기</summary>

모범답안과 그 코드에 담긴 생각을 설명합니다. **채점을 통과한 뒤에** 펼쳐서 내 풀이와 비교해 보기를 권합니다.

</details>

## 입출력 규칙

- 입력은 `input()`으로 받고, `input("숫자: ")`처럼 안내 문구를 넣지 않습니다.
- 출력은 예제와 **글자 하나까지** 같아야 합니다. (줄 끝 공백은 무시합니다.)
- 제3부에서는 빠른 입력을 위해 `sys.stdin.readline`을 씁니다.
"""


def build():
    probs = load_problems()
    PAGES.mkdir(exist_ok=True); NB.mkdir(exist_ok=True)
    tests, built = {}, []
    for page in C.CURRICULUM:
        ids = range(page[3], page[3] + 5)
        if not all(i in probs for i in ids):
            continue
        for i in ids:
            tests[i] = verify(probs[i])
        (PAGES / f"{page[0]:02d}.md").write_text(page_md(page, probs), encoding="utf-8")
        if C.HIDE_MODE == "separate":
            (PAGES / f"{page[0]:02d}-answers.md").write_text(answer_page_md(page, probs), encoding="utf-8")
        (NB / f"{page[0]:02d}.ipynb").write_text(json.dumps(notebook(page, probs, tests), ensure_ascii=False, indent=1), encoding="utf-8")
        built.append(page)
    (PAGES / "00-start.md").write_text(START_MD, encoding="utf-8")

    parts = {"기초": ("1. 제1부 기초 100제", "part1"), "응용": ("2. 제2부 응용 50제", "part2"),
             "경시": ("3. 제3부 정보올림피아드 50제", "part3")}
    toc = ["- [0. 시작하기](pages/00-start.md)"]
    for key, (title, slug) in parts.items():
        pages = [pg for pg in built if pg[1] == key]
        if not pages:
            continue
        lines = [f"# {title}", ""] + [f"- {pg[0]:02d}. {pg[2]} ({pg[3]:03d}–{pg[3] + 4:03d})" for pg in C.CURRICULUM if pg[1] == key]
        (PAGES / f"{slug}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        toc.append(f"- [{title}](pages/{slug}.md)")
        for pg in pages:
            toc.append(f"  - [{pg[0]:02d}. {pg[2]}](pages/{pg[0]:02d}.md)")
            if C.HIDE_MODE == "separate":
                toc.append(f"  - [{pg[0]:02d}-해설. {pg[2]}](pages/{pg[0]:02d}-answers.md)")
    (ROOT / "TOC.md").write_text("\n".join(toc) + "\n", encoding="utf-8")

    readme = [f"# {C.BOOK_TITLE}", "",
              "구글 계정 하나로, 설치 없이, 브라우저에서 바로 푸는 파이썬 200문제.",
              "기초 100제 · 응용 50제 · 정보올림피아드(KOI 고등부 수준) 50제로 이루어져 있으며, "
              "모든 문제는 Google Colab에서 자동 채점됩니다.", "",
              "저자: 김동균"]
    (ROOT / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")
    print(f"빌드 완료: {len(built)}개 단원, {len(built) * 5}문제, 테스트 {sum(len(v) for v in tests.values())}개 검증")


if __name__ == "__main__":
    build()
