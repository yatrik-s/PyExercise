# Exercide 6.9
data = 'X-DSPAM-Confidence: 0.8475'

atpos = data.find(':')
number = float(data[atpos + 1:])
print 'Number is: ', number
