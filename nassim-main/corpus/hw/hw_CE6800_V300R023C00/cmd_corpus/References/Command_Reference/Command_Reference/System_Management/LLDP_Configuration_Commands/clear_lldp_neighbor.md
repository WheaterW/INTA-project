clear lldp neighbor
===================

clear lldp neighbor

Function
--------



The **clear lldp neighbor** command clears Link Layer Discovery Protocol (LLDP) neighbor information about a specific or all interfaces.




Format
------

**clear lldp neighbor interface** { *interface-type* *interface-number* | *interface-name* }

**clear lldp neighbor**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | - |
| **interface** *interface-type* *interface-number* | Clears neighbor information about a specified interface. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Before you view LLDP neighbor information learned for a specified period of time or by a specified interface, run the clear lldp neighbor command to clear existing LLDP neighbor information about the interface. If no interface is specified, this command clears neighbor information about all interfaces on the device.



**Prerequisites**



LLDP has been globally enabled using the lldp enable command in the system view, and LLDP has also been enabled on interfaces using the lldp enable command in the interface view.




Example
-------

# Delete existing LLDP neighbor information on all interfaces on a device.
```
<HUAWEI> clear lldp neighbor
Warning: This Command will clear the neighbor information of all the ports. Continue? [Y/N]:y

```