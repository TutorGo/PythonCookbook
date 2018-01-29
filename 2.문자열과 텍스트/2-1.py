import os

# listdir 이용하면 해당 디렉터리에 있는 파일들의 리스트를 구할 수 있다 . 이니 현재 디렉토리 이다
filenames = os.listdir('.')
file_list = [name for name in filenames if name.endswith(('.py', '.md'))]
print(file_list)
# any는 항목을 돌면서 하나라도 True라면 True를 반환 합니다
check_py = any(name.endswith('py') for name in filenames)
print(check_py)