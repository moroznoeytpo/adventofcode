def look_and_say(text: str) -> str:
	result = ""
	current_word = None
	count = 0

	for i in text:
		if i == current_word:
			count += 1
		else:
			if current_word:
				result += f"{count}{current_word}"
			current_word = i
			count = 1
	if count:
		result += f"{count}{current_word}"
	return result

input_text = "1321131112"
for _ in range(40):
	input_text = look_and_say(input_text)
print(len(input_text))

for _ in range(10):
	input_text = look_and_say(input_text)
print(len(input_text))
