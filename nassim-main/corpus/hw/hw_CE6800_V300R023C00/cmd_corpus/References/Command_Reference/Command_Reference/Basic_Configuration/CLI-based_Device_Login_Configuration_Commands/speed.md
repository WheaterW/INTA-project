speed
=====

speed

Function
--------



The **speed** command sets the transmission rate of a user interface.

The **undo speed** command restores the default transmission rate.



By default, the transmission rate is 9600 bit/s.


Format
------

**speed** *speed-value*

**undo speed**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *speed-value* | Specifies the transmission rate. | The following are the supported transmission rates in bits/s: 1200, 2400, 4800, 9600, 19200, 38400, 57600 and 115200. |



Views
-----

VTY-type user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The configuration is effective only when the serial interface works in the asynchronous interactive view.


Example
-------

# Set the transmission rate of the console user interface to 115200 bit/s.
```
<HUAWEI> system-view
[~HUAWEI] user-interface console 0
[~HUAWEI-ui-console0] speed 115200

```