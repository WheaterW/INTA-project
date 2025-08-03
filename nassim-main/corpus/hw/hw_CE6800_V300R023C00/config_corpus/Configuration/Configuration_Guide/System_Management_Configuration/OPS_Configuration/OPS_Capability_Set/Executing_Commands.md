Executing Commands
==================

Executing Commands

#### Application Phase

Execution phase


#### Function Prototype

result1\_string, result2\_next, result3\_description = \_ops.cli.execute(fd, command, choice=None)


#### Parameter Description

| Parameter | Description | Value |
| --- | --- | --- |
| fd | Specifies a CLI channel handle. | It is generated through the API described in [Opening a CLI Channel](vrp_ops_cfg_0039.html). |
| command | Specifies a command to be executed. | Only one command can be executed each time. For example, after entering the **system-view im** command, you do not need to press **Enter**. The CLI automatically adds a carriage return. |
| choice | Specifies auto reply for interactive commands. | The value is a list in the format of key:value. **key** is the keyword in the interactive prompt, and **value** is the reply to the provided text, for example, choice = {"Continue?": "n", "save": "n"}. A maximum of eight options are supported. Multiple lines are entered for multi-line commands. For example, choice={"": "a\r\nb\r\n\a"}. |



#### Return Values

**result1\_string**, **result2\_next**, and **result3\_description** in the function prototype indicate return values.

**result1\_string** is the first return value. If **None** is returned, the command fails to be sent to the CLI window or command execution times out. Otherwise, the command output is returned. Each data packet is 32 KB in size.

**result2\_next** is the second return value. If **Next** is 0, no more output will be displayed. If **Next** is 1, more output will be displayed. This interface is still called for obtaining the next batch of data, except that you must set **command=None** and **choice=None**.

**result3\_description** is the third return value and describes the result. This value is a character string.


#### Usage Description

Using the executing command API, you can enable a script to automatically execute commands. Only one command can be executed each time. If the **choice** parameter is specified, interactive information will be displayed after a command is executed, implementing interaction between users and devices.


#### Usage Examples

After the following configuration is added, the assistant runs the [**undo statistics-task a**](cmdqueryname=undo+statistics-task+a) command to cancel the performance statistics task when the subscription conditions are met.

```
_ops.cli.execute(handle,"undo statistics-task a",choice) 
```