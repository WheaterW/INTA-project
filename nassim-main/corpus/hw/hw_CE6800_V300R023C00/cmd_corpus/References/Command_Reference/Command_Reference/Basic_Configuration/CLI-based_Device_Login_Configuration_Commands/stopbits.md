stopbits
========

stopbits

Function
--------



The **stopbits** command configures the stop bit of a user interface.

The **undo stopbits** command restores the stop bit of a user interface.



By default, the stop bit is 1 bit.


Format
------

**stopbits** *stopbitvalue*

**undo stopbits**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *stopbitvalue* | Specifies the stop bit. | The value is an enumerated type, which is 1.5, 1, 2. |



Views
-----

CONSOLE-type user interface view,VTY-type user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* If the stop bit of a user interface is 1 bit, the corresponding number of data bits is 8.
* If the stop bit of a user interface is 1.5 bits, the corresponding number of data bits is 5.
* If the stop bit of a user interface is 2 bits, the corresponding number of data bits is 6, 7, or 8.

Example
-------

# Set the stop bit of a console user interface to 1.5 bits.
```
<HUAWEI> system-view
[~HUAWEI] user-interface console 0
[~HUAWEI-ui-console0] stopbits 1.5

```