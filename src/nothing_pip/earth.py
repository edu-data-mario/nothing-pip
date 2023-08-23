import datetime


def calculate_earth_age():
    """
    지구의 나이를 계산합니다.

    Returns:
    지구의 나이 (단위: 년)
    """

    # 지구의 탄생 시기를 45억 년으로 가정합니다.
    birth_year = 4500000000

    # 현재 연도를 가져옵니다.
    current_year = int(datetime.now().year)

    # 지구의 나이를 계산합니다.
    age = current_year - birth_year

    return age
