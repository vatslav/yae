__author__ = 'django'
import re


string = '333334 333 123 2334 33345 54443 2195433333332 123333333 44444'
pattern = '[\d]*(?<!3)3{2,4}(?!3)[\d]*'
#print(re.findall(pattern, string))
string = '''333334 333 123 2334 33345 54443 2195433333332
123333333 44444 will ponn'''
print(string[:])