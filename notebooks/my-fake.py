from faker import Faker

def generate_fake_data():
    # faker = Faker('ko_KR')  # 한국어 데이터를 생성하기 위해 'ko_KR' locale을 설정합니다.
    faker = Faker()  # 한국어 데이터를 생성하기 위해 'ko_KR' locale을 설정합니다.
    data_list = []

    for _ in range(10):  # 10개의 키와 값이 들어가도록 반복합니다.
        name = faker.name()
        job = [faker.job()]  # 리스트로 만들기 위해 job을 대괄호로 묶습니다.
        address = [faker.address()]  # 리스트로 만들기 위해 address를 대괄호로 묶습니다.

        data = {
            'name': name,
            'job': job,
            'address': address
        }
        data_list.append(data)

    return data_list

if __name__ == "__main__":
    fake_data_list = generate_fake_data()
    print(fake_data_list)