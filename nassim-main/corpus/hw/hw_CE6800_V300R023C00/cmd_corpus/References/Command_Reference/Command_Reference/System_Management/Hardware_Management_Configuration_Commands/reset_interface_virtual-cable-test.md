reset interface virtual-cable-test
==================================

reset interface virtual-cable-test

Function
--------



The **reset interface virtual-cable-test** command clears the last virtual-cable-test detection result.




Format
------

**reset interface** { *interface-type* *interface-number* | *interface-name* } **virtual-cable-test**

**reset interface virtual-cable-test**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Interface type. | The value range depends on the device configuration. |
| *interface-number* | Specifies the interface index. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |



Views
-----

10GE interface view,25GE interface view,User view,Management interface view,System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To clear the test result of the cable connected to an Ethernet interface, run this command.

**Precautions**

This command takes effect only on electrical interfaces or interfaces that have GE copper modules installed.


Example
-------

# Clear the last test result of virtual-cable-test.
```
<HUAWEI> reset interface 10GE 1/0/1 virtual-cable-test

```