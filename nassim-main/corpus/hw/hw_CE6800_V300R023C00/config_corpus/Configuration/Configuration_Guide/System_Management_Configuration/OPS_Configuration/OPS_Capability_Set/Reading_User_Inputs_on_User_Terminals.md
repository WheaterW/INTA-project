Reading User Inputs on User Terminals
=====================================

Reading User Inputs on User Terminals

#### Application Phase

Execution phase and CLI event synchronization waiting mode


#### Function Prototype

result1\_value, result2\_description = \_ops.terminal.read(maxLen=512, timeout=30, vty=None)


#### Parameter Description

| Parameter | Description | Value |
| --- | --- | --- |
| maxLen | Specifies the maximum length of the entered character string. | The value is an integer ranging from 1 to 512.  The default value is 512. |
| timeout | Specifies a timeout period. | The value is an integer ranging from 0 to 60, in seconds.  The default value is 30. |
| vty | Specifies a user terminal. | The value is **None** or the VTY channel name obtained using environment("\_cli\_vty"). |



#### Return Values

**result1\_value** and **result2\_description** in the function prototype indicate return values.

**result1\_value** is the first return value.

* None: indicates that waiting times out or a user has pressed **Ctrl+C**.
* Null character string: indicates that a user has pressed **Enter**.
* 1: indicates that an error is returned. The specific error cause is described by the second return value.
* Other character strings: indicate the content entered by the user (only when the second return value is **success**).

**result2\_description** is the second return value.

* success: indicates that the user input is successfully read from the terminal.
* Other values: indicate the reason why the user input fails to be read from the terminal.

#### Usage Description

The CLI event must be subscribed, and you must wait until the script execution is complete after the command is executed. That is, the subscribed event must be defined through [\_ops.cli.subscribe](vrp_ops_cfg_0030.html#EN-US_TOPIC_0000001654962756__p39891328204311), and **sync** must be **True**.

This function enables you to obtain the information entered by users from a terminal and use it in scripts. A maximum of 10 ops.terminal.read APIs are supported in the same script.


#### Usage Examples

When a subscribed event is matched, you can enable the terminal to read and output user inputs.

```
test.py 
import ops 
def ops_condition(_ops): 
       ret = _ops.cli.subscribe("con1","device",True,True,False,20)
       ret = _ops.correlate("con1")
       return ret
def ops_execute(_ops): 
       _ops.terminal.write("Enter your passwd:",None) 
       passwrd,ret = _ops.terminal.read(10,15,None) 
       print(passwrd)
```