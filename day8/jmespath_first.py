import json
import jmespath
from rich import print

with open(r"first.json","r",encoding='utf-8') as f:
    data=json.load(f)

result=jmespath.search('people[?age>`20`].[name,age]', data)
print(result)

#List and Slice Projections
print(jmespath.search('people[:2].name',data))

# Object Projections
print(jmespath.search("ops.*.numArgs",data))

# Flatten Projections
# The outer list is from the projection of reservations[*],
# and the inner list is a projection of state created from instances[*]
print(jmespath.search("reservations[*].instances[*].state",data))
#This is the problem that a Flatten Projection solves.
#To get the desired result, you can use [] instead of [*] to flatten a list.
#It flattens sublists into the parent list (not recursively, just one level).
print(jmespath.search("reservations[].instances[].state",data))

#Filter Projections
#A filter projection allows you to filter the LHS of the projection before evaluating the RHS of a projection
print(jmespath.search("machines[?state=='running'].name",data))
print(jmespath.search("machines[?state=='stopped'].name",data))

#Pipe Expressions
#pipe expression, <expression> | <expression>, to indicate that a projection must stop.
#If you tried people[*].first[0] that you just evaluate first[0] for each element in the people array,
#and because indexing is not defined for strings, the final result would be an empty array, []
print(jmespath.search("people[*].first[0]",data))
print(jmespath.search("people[*].first | [0]",data))
print('\n')
#Multiselect
#A multiselect list creates a list and a multiselect hash creates a JSON object.
print(jmespath.search("person[].[name,state.name]",data))
#multiselect hash has the same basic idea as a multiselect list, except it instead creates a hash instead of an array.
print(jmespath.search("person[].{Name:name,State:state.name}",data))

#Functions : JMESPath supports function expressions
print(jmespath.search('length("people")',data))
print(jmespath.search('max_by(people[?age!=`null`],&age).name',data))

myarray=[
    "foo",
    "foobar",
    "barfoo",
    "bar",
    "baz",
    "barbaz",
    "barfoobaz"
]

#The @ character refers to the current element being evaluated in myarray
print("myarray[?contains(@, 'foo') == `true`]",myarray)
