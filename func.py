nums = []
def add(a=1, b=0, x=False):
	if x:
		ans = a - b
	else:
		ans = a + b
	nums.append(ans)
	print(ans)

def average(numbers):
	avg = sum(numbers) / len(numbers)
	return avg


add()
add(3)
add(b=5)
add(5, 6, True)
print(average(nums))