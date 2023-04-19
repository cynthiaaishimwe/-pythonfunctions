def year_of_birth(name,age):
 year = 2023 -age
 print(f"hello {name},you were born in {year}")

def my_country(country = "Kenya"):
 print(f"hello you are from {country}")

def hello(*names):
    for name in names:
        print(f"hello{name}")

def sum(*nums):
   answer = 0
   for num in nums:
      answer +=num
   return answer  

def multipy_many(**kwargs):
    answer = 1
    for num in kwargs.values():
      answer *= num
    return answer

def concatenate_args(*names):
    output = ""
    for name in names:
     output += name
    return output

def concatenate_kwargs(**kwargs):
    results =""
    for kwarg in kwargs.values():
       results = results + kwarg
    return print(results)