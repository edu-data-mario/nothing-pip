# example-package

### bigbang
```bash
$ pwd
/Users/m2/code/pd24
$ mkdir edu-pd24
$ cd edu-pd24
$ pdm init
Creating a pyproject.toml for PDM...
Please enter the Python interpreter to use
0. /Users/m2/.pyenv/shims/python3 (3.9)
1. /Users/m2/.pyenv/shims/python (3.9)
2. /Users/m2/.pyenv/shims/python3.11 (3.11)
3. /opt/homebrew/bin/python3.11 (3.11)
4. /Users/m2/.pyenv/versions/3.11.0/bin/python3.11 (3.11)
5. /Users/m2/.pyenv/shims/python3.10 (3.10)
6. /opt/homebrew/bin/python3.10 (3.10)
7. /Users/m2/.pyenv/versions/3.10.5/bin/python3.10 (3.10)
8. /Users/m2/.pyenv/versions/3.9.17/bin/python3.9 (3.9)
9. /Users/m2/.pyenv/shims/python3.9 (3.9)
10. /Users/m2/.pyenv/versions/3.9.16/bin/python3.9 (3.9)
11. /Users/m2/.pyenv/versions/miniforge3-4.10.3-10/bin/python3.9 (3.9)
 1 .gitignore +                                                                                                                                  X
12. /Users/m2/.pyenv/versions/3.9.13/bin/python3.9 (3.9)
13. /usr/bin/python3 (3.9)
14. /Users/m2/.pyenv/versions/3.9.2/bin/python3.9 (3.9)
15. /Users/m2/.pyenv/versions/3.8.17/bin/python3.8 (3.8)
16. /Users/m2/.pyenv/versions/3.7.17/bin/python3.7m (3.7)
17. /Users/m2/.pyenv/versions/3.7.17/bin/python3.7 (3.7)
18. /Users/m2/.pyenv/versions/3.7.13/bin/python3.7m (3.7)
19. /Users/m2/.pyenv/versions/3.7.13/bin/python3.7 (3.7)
20. /Users/m2/.pyenv/versions/3.6.15/bin/python3.6m (3.6)
21. /Users/m2/.pyenv/versions/3.6.15/bin/python3.6 (3.6)
22. /Users/m2/Library/Application Support/pdm/venv/bin/python (3.9)
Please select (0):
Would you like to create a virtualenv with /Users/m2/.pyenv/versions/3.9.17/bin/python3? [y/n] (y):
Virtualenv is created successfully at /Users/m2/code/pd24/edu-pd24/.venv
Is the project a library that is installable?
If yes, we will need to ask a few more questions to include the project name and build backend [y/n] (n):
License(SPDX name) (MIT):
Author name (dmario24):
Author email (becky2sawyer@gmail.com): data.mario24@gmail.com
Python requires('*' to allow any) (>=3.9):
Project is initialized successfully
$ tree
.
├── README.md
├── __pycache__
│   └── __init__.cpython-39.pyc
├── pyproject.toml
├── src
│   └── example_package
│       ├── __init__.py
│       └── __pycache__
│           └── __init__.cpython-39.pyc
└── tests
    ├── __init__.py
    └── __pycache__
        └── __init__.cpython-39.pyc

6 directories, 7 files
$ vi .gitignore
$ git init
/Users/m2/code/pd24/edu-pd24/.git/ 안의 빈 깃 저장소를 다시 초기화했습니다
$ git status
현재 브랜치 main

아직 커밋이 없습니다

추적하지 않는 파일:
  (커밋할 사항에 포함하려면 "git add <파일>..."을 사용하십시오)
	.gitignore
	README.md
	pyproject.toml
	src/
	tests/

커밋할 사항을 추가하지 않았지만 추적하지 않는 파일이 있습니다 (추적하려면 "git
add"를 사용하십시오)
$ git config user.name dmario24
$ git config user.email data.mario24@gmail.com
$ git add .
$ git commit -m "python pdm init"
[main (최상위-커밋) dcac4e7] python pdm init
 5 files changed, 175 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
 create mode 100644 pyproject.toml
 create mode 100644 src/example_package/__init__.py
 create mode 100644 tests/__init__.py
$
```
