prompt
======

prompt

Function
--------



The **prompt** command enables the prompt message to get the confirmation from the user to transfer the file or not.

The **undo prompt** command disables the prompt.



By default, the prompt is disabled.


Format
------

**prompt**

**undo prompt**


Parameters
----------

None

Views
-----

FTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

This command is applicable only for multiple file transfer commands mput and mget. In case of **mget** command, if the file already exists in the local device, system prompts the confirmation message whether to overwrite the file or not, irrespective of prompt is disabled or not.


Example
-------

# Enable FTP prompt mode.
```
<HUAWEI> ftp 10.1.1.1
Trying 10.1.1.1 ...
Press CTRL + K to abort
Connected to 10.1.1.1.
220 VRPV8 FTP service ready.
User(10.1.1.1:(none)):John
331 Password required for John.
Password:
230 User logged in.
[ftp] prompt
Info: Switching prompt on succeeded.

```