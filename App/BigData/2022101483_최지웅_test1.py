import numpy as np


heights = [1.83, 1.76, 1.69, 1.77, 1.73]
weights = [85.12, 74.13, 59.13, 80.12, 68.00]


np_heights = np.array(heights)
np_weights = np.array(weights)


np_bmis = np_weights / (np_heights ** 2)


np_bmis_rounded = np.round(np_bmis, 2)


obese_members = np_bmis >= 25


num_obese = np.sum(obese_members)


avg_height = np.mean(np_heights)
avg_weight = np.mean(np_weights)


avg_height_rounded = np.round(avg_height, 2)
avg_weight_rounded = np.round(avg_weight, 2)


print(f'신규회원들의 키\t\t\t:{" ".join(f"{h:.2f}" for h in np_heights)}')
print(f'신규회원들의 평균 키\t\t:{avg_height_rounded:.2f}')

print(f'신규회원들의 몸무게\t\t:{" ".join(f"{w:.2f}" for w in np_weights)}')
print(f'신규회원들의 평균 몸무게\t:{avg_weight_rounded:.2f}')

print(f'신규회원들의 BMI\t\t:{" ".join(f"{bmi:.2f}" for bmi in np_bmis_rounded)}')
print(f'신규 회원자들의 평균 BMI\t:{np.round(np.mean(np_bmis), 2):.2f}')


print(f'신규 회원 BMI 비만 대상자\t:{num_obese}명')
