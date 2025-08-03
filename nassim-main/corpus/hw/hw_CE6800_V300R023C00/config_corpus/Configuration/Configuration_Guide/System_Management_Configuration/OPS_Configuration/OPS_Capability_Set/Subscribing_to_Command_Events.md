Subscribing to Command Events
=============================

Subscribing to Command Events

#### Application Phase

Subscription phase


#### Function Prototype

result1\_value, result2\_description = \_ops.cli.subscribe(tag, pattern, enter=False, sync=True, async\_skip=False, sync\_wait=30)


#### Parameter Description

| Parameter | Description | Value |
| --- | --- | --- |
| tag | Specifies conditions. | The value is a string of 1 to 8 case-sensitive characters, consists of letters, digits, and underscores (\_), and starts with a letter. The value of **tag** cannot be **and**, **or**, or **not**. If only one condition is subscribed to in the script, the value can be an empty string. If multiple conditions are subscribed to, the value cannot be empty and must be unique in the script. |
| pattern | Specifies a regular expression for matching commands. | The value is a string of 1 to 128 characters, excluding **\0**. |
| enter | Indicates when to match a regular expression. | The value is of the Boolean type:   * True: The regular expression is matched immediately after the command is entered. * False: After a command is entered, the system attempts to supplement keywords through the command tree and then matches the regular expression.   The default value is **False**. |
| sync | Indicates whether to wait until the script execution is complete after the command triggers an execution action. | The value is of the Boolean type:   * True: Wait until the script execution is complete. During this period, the script takes over the terminal I/O. * False: The script is executed in the background without waiting.   The default value is **True**. |
| async\_skip | Indicates whether to skip the original command when the **sync** value is **False**. | The value is of the Boolean type:   * True: The original command is skipped and not executed. * False: The original command is not skipped and is executed.   The default value is **False**. |
| sync\_wait | Indicates the time taken by a command to wait for the script execution if the **sync** value is **True**. | The value is an integer ranging from 1 to 100, in seconds.  If the script execution period exceeds the **sync\_wait** value, the script is executed in the background.  The default value is 30. |



#### Return Values

**\_ops** in the function prototype indicates an OPS object.

**result1\_value** and **result2\_description** in the function prototype indicate return values.

**result1\_value** is the first return value, with value 0 indicating a success, and value 1 indicating a failure.

**result2\_description** is the second return value and describes the result. This value is a character string.


#### Usage Description

When the CLI event subscription interface (\_ops.cli.subscribe) is used:

* If the original command of the device is subscribed to, **sync** is set to **True**, and the return value of **\_ops\_execute** is set to **0**, the original command of the device is skipped, that is, the original command of the device is invalid.
* If the original command of the device is subscribed to, **sync** is set to **False**, and the return value of **async\_skip** is set to **True**, the original command of the device is skipped, that is, the original command of the device is invalid.
* You are advised to specify the regular expression matching the command as a complete keyword or command.
  + If an incomplete command or keyword is used, and **enter** and **sync** are both set to **True**, the subscribed event will be mismatched. For example, if the regular expression is set to **display**, any command that contains **display** will match the event and trigger the action in the interface.
  + If an incomplete command or keyword is used, for example, **dis**, and **enter**, **sync**, and **async\_skip** are set to **True**, **False**, and **True** respectively, all commands that contain **dis** become invalid.
  + If an incomplete command or keyword is used, for example, **display**, and **enter** and **sync** are set to **False** and **True** respectively, any command that contains **display** will match the event and trigger the action in the interface.
  + If an incomplete command or keyword is used, for example, **display**, and **enter**, **sync**, and **async\_skip** are set to **False**, **False**, and **True** respectively, all commands that contain **display** become invalid.
* Do not specify the regular expression matching the command as a single space character.
  + If the regular expression is a single space character and the user enters only a single space, the action in the interface cannot be triggered.
  + If the regular expression is a single space character, and **enter**, **sync**, and **async\_skip** are all set to **True**, any command that contains spaces will match the subscribed event.
  + If the regular expression is a single space character, and **enter**, **sync**, and **async\_skip** are set to **True**, **False**, and **True** respectively, any command that contains spaces becomes invalid.
* If the regular expression matching the command contains a question mark (?), for example, "shutdow?", and the user enters **shutdow?**, the subscribed event is not matched.
* If the regular expression matching the command contains special characters other than the question mark (?), the device encodes the special characters twice when executing the Python script. For example, if the regular expression matching the command is "shutdown \\a", it becomes "shutdown \a" after being encoded once and "shutdown a" after being encoded twice. Therefore, when the user enters **shutdown a**, the subscribed event is matched. Ensure that special characters are visible after being encoded twice; otherwise, invisible characters cannot be entered in the CLI window, and subscribed events cannot be matched.
* It is recommended that the name of the command subscribed through \_ops.cli.subscribe be different from that of the Python script file. Otherwise, the Python script file cannot be copied or deleted.

If multiple simple events are defined using \_ops.cli.subscribe in the subscription phase but the simple events are not combined using the interface described in [Combining Multiple Conditions](vrp_ops_cfg_0036.html), the Python script assistant cannot be configured successfully.


#### Usage Examples

Run the [**display clock**](cmdqueryname=display+clock) command to check the current date and clock of the system and trigger the terminal to display "Hello World".

```
test.py 
def ops_condition(_ops):
       _ops.cli.subscribe("con11","display clock",True,True,False,30) 
       _ops.correlate("con11")
def ops_execute(_ops): 
       print("Hello World") 
       return 0
```