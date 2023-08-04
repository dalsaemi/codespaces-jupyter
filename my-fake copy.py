# %%
from faker import Faker

faker = Faker('ko_KR')  # 한국어 데이터를 생성하기 위해 'ko_KR' locale을 설정합니다.

name = faker.name()
job = faker.job() # 리스트로 만들기 위해 job을 대괄호로 묶습니다.
address = faker.address() # 리스트로 만들기 위해 address를 대괄호로 묶습니다.

print(name, job, address)
print(f'name: {name}, job: {job}, address: {address}')
# %%
