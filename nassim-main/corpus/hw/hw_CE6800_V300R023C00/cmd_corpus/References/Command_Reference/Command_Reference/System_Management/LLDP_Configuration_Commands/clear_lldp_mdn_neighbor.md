clear lldp mdn neighbor
=======================

clear lldp mdn neighbor

Function
--------



The **clear lldp mdn neighbor** command clears MDN neighbor information on all interfaces or a specified interface.




Format
------

**clear lldp mdn neighbor interface** { *interface-type* *interface-number* | *interface-name* }

**clear lldp mdn neighbor**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Clears MDN neighbor information on a specified interface.  If this parameter is not specified, MDN neighbor information of all interfaces is cleared. | - |
| **interface** *interface-name* | Clears MDN neighbor information on a specified interface.  If this parameter is not specified, MDN neighbor information of all interfaces is cleared. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To check MDN neighbor information learned by a device or a specified interface within a specified period of time, run the reset nd neighbor command to clear historical MDN neighbor information on the specified interface or all interfaces.



**Prerequisites**



LLDP has been enabled globally using the lldp enable (system view) command.LLDP MDN has been enabled globally or on an interface using the lldp mdn enable (system view) or lldp mdn enable (interface view) command.




Example
-------

# Clear MDN neighbor information of all interfaces on a device.
```
<HUAWEI> clear  lldp mdn neighbor
Warning: This Command will clear the neighbor information of all the ports. Continue? [Y/N]:Y

```

# Clear MDN neighbor information on 100GE 1/0/4.
```
<HUAWEI> clear lldp mdn neighbor interface 100GE 1/0/4

```