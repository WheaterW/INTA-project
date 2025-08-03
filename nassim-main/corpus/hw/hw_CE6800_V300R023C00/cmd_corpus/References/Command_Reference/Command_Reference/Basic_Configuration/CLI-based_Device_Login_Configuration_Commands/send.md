send
====

send

Function
--------



The **send** command sends messages to a specified user interface.




Format
------

**send** { **all** | *ui-type* *ui-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Sends messages to all other user interfaces. | - |
| *ui-type* | Specifies the type of a user interface. | The value of ui-type can be vty or console. |
| *ui-number* | Specifies the number of a user interface that receives messages. | * When ui-type is set to console, the value of ui-number is 0. * When ui-type is set to vty, the value of ui-number ranges from 0 to the maximum number of VTY connections minus 1. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After entering a message in the user interaction interface, press **Enter** or **Ctrl+Z** to send the message, or press **Ctrl+C** to stop sending the message. After receiving the message, the target user interface immediately displays it.


Example
-------

# Send messages to all other user interfaces.
```
<HUAWEI> send all
Enter message, end with CTRL+Z or Enter; abort with CTRL+C:
hello~!
Send message? [Y/N]:Y

```

# Send a message to VTY 0.
```
<HUAWEI> send vty 0
Enter message, end with CTRL+Z or Enter; abort with CTRL+C:
hello, vty 0~!
Send message? [Y/N]:Y

```

# Send a message to the console user interface.
```
<HUAWEI> send console 0
Enter message, end with CTRL+Z or Enter; abort with CTRL+C:
Hello, console~!
Send message? [Y/N]:Y

```