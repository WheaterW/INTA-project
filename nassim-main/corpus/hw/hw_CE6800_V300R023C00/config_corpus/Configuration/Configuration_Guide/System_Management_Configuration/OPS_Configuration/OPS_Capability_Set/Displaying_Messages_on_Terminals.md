Displaying Messages on Terminals
================================

Displaying Messages on Terminals

#### Application Phase

Execution phase


#### Function Prototype

result1\_value, result2\_description = \_ops.terminal.write(msg, vty=None)


#### Parameter Description

| Parameter | Description | Value |
| --- | --- | --- |
| msg | Specifies information displayed on a user terminal. | The value is a string of 1 to 512 case-sensitive characters. |
| vty | Specifies a user terminal. | If the value is **None**, messages can be displayed on the current user terminal. You can also obtain a VTY channel name through environment('\_cli\_vty'). |



#### Return Values

**result1\_value** and **result2\_description** in the function prototype indicate return values.

**result1\_value** is the first return value, with value 0 indicating a success, and value 1 indicating a failure.

**result2\_description** is the second return value and describes the result. This value is a character string.


#### Usage Description

This API displays user-defined information to a device to generate prompt information.


#### Usage Examples

When a subscribed event is matched, "Hello World!" is displayed on the CLI terminal.

```
test.py 
import ops 
def ops_condition(_ops): 
       ret = _ops.cli.subscribe("con1","device",True,True,False,20)
       ret = _ops.correlate("con1")
       return ret
def ops_execute(_ops): 
       _ops.terminal.write("Hello world!", None) 
       return 1
```