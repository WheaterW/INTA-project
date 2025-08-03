info-center trapbuffer
======================

info-center trapbuffer

Function
--------



The **info-center trapbuffer size** command sets the number of traps to be displayed.

The **undo info-center trapbuffer size** command restores the default number of traps to be displayed.

The **info-center trapbuffer** command enables trap display.

The **undo info-center trapbuffer** command disables trap display.



A maximum of 256 traps can be displayed by default.


Format
------

**info-center trapbuffer size** *sizeValue*

**info-center trapbuffer**

**undo info-center trapbuffer size**

**undo info-center trapbuffer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **size** *sizeValue* | Specifies the number of traps to be displayed. | The value is an integer ranging from 0 to 1024. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To set the number of traps to be output, run the info-center trapbuffer size command.

**Prerequisites**

The trap display function has been enabled. Otherwise, traps cannot be output to the trap buffer for user query.

**Configuration Impact**

If the info-center trapbuffer size command is run more than once, the latest configuration overrides the previous one.

**Precautions**

If the number of traps to be displayed is set too small, some traps cannot be queried. If the number of traps to be displayed is set too large, excessive repeated traps may be displayed. The default number of traps to be displayed is recommended.


Example
-------

# Enable the device to send traps to the trap buffer and set the number of traps to be displayed to 30.
```
<HUAWEI> system-view
[~HUAWEI] info-center trapbuffer
[*HUAWEI] info-center trapbuffer size 30

```