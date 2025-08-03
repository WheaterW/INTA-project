screen-length temporary
=======================

screen-length temporary

Function
--------



The **screen-length temporary** command sets the number of lines in each screen of the terminal.

The **undo screen-length temporary** command restores the number of rows in each screen of the terminal to the default value.



By default, the number of rows in one screen is 24.


Format
------

**screen-length** *screen-length* **temporary**

**undo screen-length temporary**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *screen-length* | Specifies the number of lines displayed on the split screen. | It is an integer data type. The value ranges from 0 to 512. Zero indicates the split screen is disabled. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The screen-length temporary command can be used to set the maximum line number on the current terminal. The configuration is temporary and is not effective after disconnection or system reboot.

**Follow-up Procedure**

If the output line number exceed the configured line number then you can enable the split-screen function temporarily to stop the output.

**Precautions**

* You are not advised to adjust the number of lines supported by the terminal screen.
* Only the output of query commands and command help is restricted by the screen height. The output of other information, such as the output of configuration commands, is not restricted by the screen height.

Example
-------

# Set the number of lines in each screen of the terminal to 30.
```
<HUAWEI> screen-length 30 temporary

```