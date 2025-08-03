Combining Multiple Conditions
=============================

Combining Multiple Conditions

#### Application Phase

Subscription phase


#### Function Prototype

result1\_value, result2\_description = \_ops.correlate(''correlation expression'')


#### Parameter Description

| Parameter | Description | Value |
| --- | --- | --- |
| correlation expression | Indicates a combined condition expression. | * The value is a string of 1 to 128 characters. * It consists of the tag name, brackets, and an operator (**and**, **or**, or **andnot**). Operators **and** and **andnot** have the same priority, which is greater than that of **or**. |



#### Return Values

**result1\_value** and **result2\_description** in the function prototype indicate return values.

**result1\_value** is the first return value, with value 0 indicating a success, and value 1 indicating a failure.

**result2\_description** is the second return value and describes the result. This value is a character string.


#### Usage Description

Typically, only a simple event can be subscribed to and a trigger condition can be registered in the subscription phase in a Python script. Using the multi-condition relationship combination, you can combine multiple simple events into a complex event to describe relationships between multiple simple events. The tag of each simple event must be unique.

For example, \_ops.correlate("((tag1 or tag2) andnot (tag3 or tag4))") indicates that the corresponding action is triggered when event tag1 or tag2 occurs but event tag3 or tag4 does not occur.

In a Python script, a maximum of eight simple events can be subscribed to and then combined using the multi-condition relationship combination API.


#### Usage Examples

When con1 and con2 are both met, the corresponding action is triggered.

```
test.py 
import ops 
def ops_condition(_ops): 
       ret1, reason1 = _ops.cli.subscribe("con1","display device",True,True,False,20)
       ret2, reason2 = _ops.cli.subscribe("con2","display this",True,True,False,20)
       _ops.correlate("con1 and con2") 
def ops_execute(_ops): 
       _ops.terminal.write("Hello world!",None) 
       return 0
```