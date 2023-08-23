# nothing-pip
- 함께 배우고 가르치기 위해 만들어졌습니다.
- 누구나 python으로 제작한 프로그램을 누구에게나 사용하도록 배포할 수 있습니다.
- 아무것도 아닙니다.

### Start
- 차차 파이썬 프로그램을 배포에 대한 [공식 문서](https://packaging.python.org/en/latest/tutorials/packaging-projects/)를 참고해 주세요.
- 여기서는 [PDM](https://pdm.fming.dev/latest/#introduction) 을 사용합니다. [0.1.0 릴리즈 노트](https://github.com/edu-data-mario/nothing-pip/releases/tag/0.1.0) 에 정리되어 있습니다.
```bash
$ curl -sSL https://pdm.fming.dev/install-pdm.py | python3 -
$ mkdir nothing-pip & cd nothing-pip
$ pdm init
$ source .venv/bin/activate
```

### Nothing
- 한줄의 명령어로 누구나 사용 가능한 python 프로그램이 배포 되었습니다.
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

- 검색도 가능합니다.
![image](https://github.com/edu-data-mario/nothing-pip/assets/134017660/8b5d19a5-0e8d-4a55-a59f-87cc0e7d9a30)

### one tiny feature
- [bard](bard.google.com)에 질문을 던지고 src/nothing_pip/__pycache__/earth.py 에 함수를 작성합니다.
![image](https://github.com/edu-data-mario/nothing-pip/assets/134017660/948cc911-7b37-402d-9d8e-75112b195a4f)

### test
 ```bash
 $ pytest
 $ pytest -q
 $ pytest -q tests/test_class.py

 $ pytest --cov=nin_nostradamus_pip tests/
 ---------- coverage: platform darwin, python 3.9.17-final-0 ----------
 Name                                  Stmts   Miss  Cover
 ---------------------------------------------------------
 src/nin_nostradamus_pip/__init__.py       0      0   100%
 src/nin_nostradamus_pip/ping.py           4      0   100%
 ---------------------------------------------------------
 TOTAL                                     4      0   100%
 ```

