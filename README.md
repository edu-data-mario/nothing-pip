# nothing-pip
- 함께 배우고 가르치기 위해 만들어졌습니다.
- 누구나 python으로 제작한 프로그램을 누구에게나 사용하도록 배포할 수 있습니다.
- 아무것도 아닙니다.

### Start
- 차차 파이썬 프로그램 배포에 대한 [공식 문서](https://packaging.python.org/en/latest/tutorials/packaging-projects/)를 슬쩍 봐 주세요. 담에 필요하면 정독해 보세요.
- 여기서는 [PDM](https://pdm.fming.dev/latest/#introduction) 을 사용합니다. 설치 로그는 [0.1.0 릴리즈 노트](https://github.com/edu-data-mario/nothing-pip/releases/tag/0.1.0) 에 정리되어 있습니다.
```bash
# PDM 설치
$ curl -sSL https://pdm.fming.dev/install-pdm.py | python3 -
# 새로운 프로젝트 초기 구조 생성
$ mkdir nothing-pip & cd nothing-pip
$ pdm init
# 새로운 프로젝트의 파이썬 가성환경 활성화 - 다른 파이썬 환경과 구별됩니다.
$ source .venv/bin/activate
```

### Nothing
- 그리고 아래와 같이 한줄의 명령어로 누구나 사용 가능한 python 프로그램이 배포 되었습니다.
- id/password 는 [여기](https://pypi.org/account/register/)서 가입하세요.
```bash
$ pdm publish

Building sdist...
Built sdist at .../nothing-pip/dist/nothing_pip-0.2.0.tar.gz
Building wheel...
Built wheel at .../nothing-pip/dist/nothing_pip-0.2.0-py3-none-any.whl
Username: dmario24 
Password: 
Uploading nothing_pip-0.2.0-py3-none-any.whl
Uploading nothing_pip-0.2.0.tar.gz
 100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.9/4.9 kB
 100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.7/4.7 kB

View at:
https://pypi.org/project/nothing_pip/0.2.0/
https://pypi.org/project/nothing-pip/0.2.0/
```

### Showing off and promoting
- 이제 자랑의 시간입니다.
- 알리고 싶은 사람에게 아래의 링크나 명령어를 전달하세요.
- https://pypi.org/project/nothing_pip/
```bash
$ pip install nothing-pip
```

![검색도가능](https://github.com/edu-data-mario/nothing-pip/assets/134017660/8b5d19a5-0e8d-4a55-a59f-87cc0e7d9a30)

# END

```bash
*｡*.。*∧,,,∧
 ヾ(⌒(_=•ω•)_
- 끝입니다. 끄읏 ㅋㅋㅋ
- 뭔가 계속 해보고 싶다면 ...

▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█░░░░░░░░▀█▄▀▄▀██████░▀█▄▀▄▀██████░
░░░░░░░░░░░▀█▄█▄███▀░░░ ▀██▄█▄███▀░

▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▓▒▒▓▒▒▒▒
▒▒▒▒▓▒▒▓▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒
▒▓▒▒▒▒▒▒▒▒▓▒
▒▒▓▓▓▓▓▓▓▓▒▒
▒▒▒▒▒▒▒▒▒▒▒▒

  ．．．．．/)─―ヘ
  　　　━／　　　　＼
  　 ／　　　　●　　●丶
  　｜　　　　　　　▼　| (침묵)
  　｜　　　　　　　亠ノ 　
  　 U￣U￣￣￣U￣￣U

.　　　　　　　　　  ∧＿∧ 三＝
　　∧_∧ 　　　☆　  (˘ω˘　)三＝
=≡( ･ω･) ∧_∧ ,;　_ノ　つ ﾉつ 三＝
　 ⊂⊂ニ );)д｀((⊂ _ ＿⊂) 三＝
-=≡ (_(_／⊂　Ｏ)
　　　 　'/　 ヽ
　　　 　∪￣＼)

╭ ◜◝ ͡ ◜◝ ͡ ◜◝ ͡ ◜◝ ͡ ◜◝ ͡ ◜◝ ͡ ◜◝ ͡ ◜◝ ͡ ◜◝╮
             아래 도전을 진행해 보세요.
╰ ◟◞ ͜ ◟◞ ͜ ◟◞ ͜ ◟◞ ͜ ◟◞ ͜ ◟◞ ͜ ◟◞ ͜ ◟◞ ͜ ◟◞ ╯
O °
ᕱ ᕱ
( ･ω･)
/ つΦ . .. . ﹢ ⃰ ଂ ಇ

```
----
# Challenge - 1


### one tiny feature
- [0.2.0 릴리즈](https://github.com/edu-data-mario/nothing-pip/releases/tag/0.2.0) 를 내려받아 해보세요.
- [0.3.3 릴리즈](https://github.com/edu-data-mario/nothing-pip/releases/tag/0.3.3) 에 왼성 코드가 있습니다.
- ping <-> pong 기능을 만들어 봅시다.
- src/nothing_pip/ping.py 추가

### test
- 만든 기능 확인을 위해 테스트를 만들어 봅니다.
- tests/test_ping.py 추가
- test 하는법 여러 종류 한번씩 해보세요. 뭐가 다른지 ~
 ```bash
 $ pytest
 $ pytest -q
 $ pytest -q tests/test_class.py

 $ ---------- coverage: platform darwin, python 3.9.17-final-0 ----------
Name                          Stmts   Miss  Cover
-------------------------------------------------
src/nothing_pip/__init__.py       0      0   100%
src/nothing_pip/ping.py           4      0   100%
-------------------------------------------------
TOTAL                             4      0   100%
 ```
