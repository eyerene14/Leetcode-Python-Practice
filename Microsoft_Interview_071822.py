'''s = {'email': 'will@msft.com'}

for k,v in s.items():
    if v.find('@') >= 0:
        s[k] = 'secret'

print(s)'''

def 

Facebook table
Name	City
X	    SF
Y	    NY
Z	    LA

Linkedin table
Name	City
A	    NY
X	    SF
C	    LA



SELECT *
FROM facebook
LEFT JOIN linkedin 
ON facebook.name = linkedin.name 
WHERE facebook.city = 'SF'

Name  City Name  City 
f.X		f.SF l.X		l.SF
f.Y		f.NY Null		Null
f.Z		f.LA

SELECT *
FROM facebook
LEFT JOIN linkedin 
ON facebook.name = linkedin.name AND facebook.city = 'SF'

FROM facebook f, linkedin l
WHERE f.name = l.name
AND f.city = 'SF'

------------------------


A phrase is a palindrome if, 
after converting all uppercase letters into lowercase letters 
it reads the same forward and backward. 

Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.




pal1 = 'abba'
pal2 = 'world?????'      ---> "world"    
pal3 = 'mannam'

def pallindrom(str):
	
  for i in range(0,len(str)/2):
  	end = len(str)-1-i
    
    # check if str[i] or str[end] is not alphanumeric
    if not str[i].isalpha() or not str[end].isalpha():
    	# skip that one
      # if str[end].isalpha() returns false
      # keep moving until seeing an alphanumberic char
      while (end >= i && str[end].isaphla()):
      	end -= 1
      # if the other case
      i += 1
    

    if str[i] != str[end]
    	return False
    elif not str[i].isalpha() or str[end].isalpha():
    	return False
      
  return True
		
[0:1],[-1:]




            1st    2nd
i        :   0      1
end      :   3      2
str[i]   :   a      b
str[end] :   a      b


            1st    2nd
i        :   0      
end      :   5      
str[i]   :   w     
str[end] :   ?     