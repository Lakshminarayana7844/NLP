expressions = [
    "x and y",
    "x or (not y)",
    "x and (y or (not x))"
]
for exp in expressions:
    variable={'x':False,'y':False}
    result=eval(exp,{},variable)
    print(result,"\n")
