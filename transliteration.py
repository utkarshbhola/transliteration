from ai4bharat.transliteration import XlitEngine
e = XlitEngine("pa")
out = e.translit_sentence("namasthe")
print(out)
# output: {'ta': 'வணக்கம் உலகம்'}