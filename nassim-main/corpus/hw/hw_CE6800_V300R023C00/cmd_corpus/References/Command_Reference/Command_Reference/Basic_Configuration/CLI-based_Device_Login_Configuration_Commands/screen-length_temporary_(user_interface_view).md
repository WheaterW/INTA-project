screen-length temporary (user interface view)
=============================================

screen-length temporary (user interface view)

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

VTY-type user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The screen-length temporary command can be used to set the maximum line number on the current terminal. The configuration is temporary and is not effective after disconnection or system reboot.


Example
-------

# Set the temporary number of lines in each console screen of the terminal to 30.
```
<HUAWEI> system-view
[~HUAWEI] user-interface console 0
[~HUAWEI-ui-console0] screen-length 30 temporary

```

# Set the temporary number of lines in each VTY screen of the terminal to 30.
```
<HUAWEI> system-view
[~HUAWEI] user-interface vty 0
[~HUAWEI-ui-vty0] screen-length 30 temporary

```