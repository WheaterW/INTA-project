databits
========

databits

Function
--------



The **databits** command configures the number of data bits of a user interface.

The **undo databits** command restores the default number of data bits of a user interface.



By default, the default number of data bits of a user interface is 8.


Format
------

**databits** *databitvalue*

**undo databits**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *databitvalue* | Sets the number of data bits. | The value is an enumerated type, which is 5, 6, 7 or 8. |



Views
-----

VTY-type user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If the number of data bits configured on a device is different from that configured on the terminal emulation program, run the databits command to configure the number of data bits on the device to be the same as that on the terminal emulation program.You are advised to use the default number of data bits of a user interface.


Example
-------

# Set the number of data bits of a console user interface to 7.
```
<HUAWEI> system-view
[~HUAWEI] user-interface console 0
[~HUAWEI-ui-console0] databits 7

```