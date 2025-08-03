Saving Script Variables
=======================

Saving Script Variables

#### Application Phase

Subscription and execution phases


#### Function Prototype

result1\_value, result2\_description = \_ops.context.save(varName, value)


#### Parameter Description

| Parameter | Description | Value |
| --- | --- | --- |
| varName | Specifies the name of a variable. | The value is a string of 1 to 16 characters. |
| value | Specifies the value of a variable. | The value can be an integer or a string of characters.   * When the value is a string of characters, it is a string of 1 to 1024 characters. * When the value is an integer, it ranges from â2147483648 to +2147483647. |



#### Return Values

**result1\_value** and **result2\_description** in the function prototype indicate return values.

**result1\_value** is the first return value, with value 0 indicating a success, and value 1 indicating a failure.

**result2\_description** is the second return value and describes the result. This value is a character string.


#### Usage Description

A maximum of 100 script variables can be saved to the device. If two same variable names are configured, only the latter variable value will take effect.

If an OPS script wants to obtain a value from another script, this API can be used to enable the other script to store the variable value and then invoke the API described in [Obtaining Script Variables](vrp_ops_cfg_0047.html) to obtain the corresponding variable.


#### Usage Examples

Call the save API twice to store the two script variables. **varInt1** is 111, and **varStr2** is the character string **testString**.

```
test.py 
import ops 
test = ops.ops() 
print ("test context save") 
a, description = test.context.save("varInt1",111) 
print ("save varInt1 return",a) 
a, description = test.context.save("varStr2",'testString') 
print ("save varStr2 return",a) 
```