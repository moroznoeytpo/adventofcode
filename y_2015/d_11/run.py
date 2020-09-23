class Password:
	def __init__(self, input_text: str, error_ch: list):
		self.lengh = len(input_text)
		self.error_ch = error_ch
		self.alp = self.get_alp()
		self.alp_ex = self.alp + ['a', 'b']
		self.alp_str = "".join(self.alp)
		self.text = self.get_text(input_text)

	def get_text(self, input_text: str):
		text = list(input_text)
		if text and self.error_ch:
			set_a = False
			for i in range(self.lengh):
				if set_a:
					text[i] = 'a'
				elif text[i] in self.error_ch:
					set_a = True
					text[i] = chr(ord(text[i]) + 1)
		return text

	def get_alp(self) -> list:
		result = []
		for i in range(ord('a'), ord('z') + 1):
			if chr(i) not in self.error_ch:
				result.append(chr(i))
		return result

	def is_correct_passwrd(self) -> bool:
		incr = False
		good = True
		double = set()
		for i in range(self.lengh):
			if i < self.lengh - 2 and "".join(self.text[i:i+3]) in self.alp_str:
				incr = True
			if i < self.lengh - 1 and self.text[i] == self.text[i+1]:
				if i < self.lengh - 2 and self.text[i+1] == self.text[i+2]:
					return False
				else:
					double.add(self.text[i])
			if self.text[i] in self.error_ch:
				good = False
		return incr and good and len(double) >= 2

	def increment_password(self) -> None:
		for i in range(self.lengh, 0, -1):
			last = self.text[i - 1]
			try:
				self.text[i - 1] = self.alp[self.alp.index(last) + 1]
				return None
			except Exception:
				self.text[i - 1] = 'a'
		return None

	def generate(self):
		while not self.is_correct_passwrd():
			self.increment_password()
		return "".join(self.text)


input_text = "hepxcrrq"
error_ch = ['i', 'o', 'l']
obj = Password(input_text, error_ch)
print(obj.generate())
obj.increment_password()
print(obj.generate())
