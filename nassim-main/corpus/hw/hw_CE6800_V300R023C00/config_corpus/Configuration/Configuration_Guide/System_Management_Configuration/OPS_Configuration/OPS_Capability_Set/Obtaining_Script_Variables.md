Obtaining Script Variables
==========================

Obtaining Script Variables

#### Application Phase

Subscription and execution phases


#### Function Prototype

result1\_value, result2\_description = \_ops.context.retrieve(varName)


#### Parameter Description

| Parameter | Description | Value |
| --- | --- | --- |
| varName | Specifies the name of a variable. | The value is a string of 1 to 16 characters. |



#### Return Values

**result1\_value** and **result2\_description** in the function prototype indicate return values.

**result1\_value** is the first return value. **None** is returned if the specified variable fails to be restored. If the variable is restored successfully, the first value is the specified variable.

**result2\_description** is the second return value and describes the result. This value is a character string.


#### Usage Description

This API is used in scripts to obtain variables from contexts. After a variable value is obtained, the variable is deleted.


#### Usage Examples

Save the read script variables and obtain the values of the variables.

```
test.py 
import ops 
test = ops.ops() 
print ("test context retrieve") 
a, description = test.context.retrieve("varInt1") 
print ("retrieve varInt1 = ", a) 
a, description = test.context.retrieve("varStr2") 
print ("retrieve varStr2 = ", a) 
```