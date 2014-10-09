word = raw_input('Write Text: ')
word=word.lower()
out = []
c_prev = None
sum=0
	
for c in word:
	   value = ord(c)-96
	   sum=sum+value
	   out.append(value)
	   if c == c_prev:  # double if repeated character
	       sum = sum * 2
	        
	   c_prev = c  # store for next comparison
	   print out
	   print sum
