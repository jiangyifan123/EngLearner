import time, json

def apax_chat():
	data = []
	values = [4, 3, 50, 9, 29, 19, 25, 9, 12, 7, 19, 5, 13, 9, 17, 2, 7, 4]
	now = round(time.time()) * 1000
	print(time.localtime(time.time()))
	for i in range(18):
		data.append([now, values[i]])
		now += 84600 * 1000
	return json.dumps(data, separators=(',', ':'))

# if __name__ == '__main__':
# 	d = apax_chat()