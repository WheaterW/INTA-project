history-command max-size
========================

history-command max-size

Function
--------



The **history-command max-size** command sets the size of the history command buffer.

The **undo history-command max-size** command restores the default size of the history command buffer.



By default, you can store 10 history commands.


Format
------

**history-command max-size** *size-value*

**undo history-command max-size**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *size-value* | Specifies the size of the history buffer. | The value is an integer ranging from 0 to 256. |



Views
-----

VTY-type user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The command line interface provides a function to save the history commands automatically. You can invoke the history commands saved in the command line interface at any time.


Example
-------

# Set the vty user interface view size of the history command buffer to 20.
```
<HUAWEI> system-view
[~HUAWEI] user-interface vty 0 4
[~HUAWEI-ui-vty0-4] history-command max-size 20

```

# Set the console user interface view size of the history command buffer to 20.
```
<HUAWEI> system-view
[~HUAWEI] user-interface console 0
[~HUAWEI-ui-console0] history-command max-size 20

```