reset lldp mdn statistics
=========================

reset lldp mdn statistics

Function
--------



The **reset lldp mdn statistics** command deletes statistics about non-LLDP packets that all interfaces receive or non-LLDP packets that a specified interface receives.




Format
------

**reset lldp mdn statistics interface** { *interface-type* *interface-number* | *interface-name* }

**reset lldp mdn statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface on which statistics about non-LLDP packets are deleted.  If this parameter is not specified, statistics about non-LLDP packets that all interfaces on the device receive are deleted. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To quickly locate and manage an MDN fault, you need to collect statistics about non-LLDP packets received by a device in a specified period. Before collecting statistics, run the reset lldp mdn statistics command to delete existing statistics about non-LLDP packets.



**Prerequisites**



LLDP has been globally enabled using the lldp enable command in the system view, and MDN has been enabled on the interface using the lldp mdn enable command in the interface view.



**Follow-up Procedure**



After running the reset lldp mdn statistics command to delete existing statistics about non-LLDP packets, run the **display lldp mdn statistics** command to view statistics about non-LLDP packets received by a device within a specific period of time.



**Precautions**



If you do not configure the interface parameter when running the reset lldp mdn statistics command, statistics about non-LLDP packets received by all interfaces are deleted. Exercise caution when running this command.




Example
-------

# Delete statistics about non-LLDP packets received by all interfaces.
```
<HUAWEI> reset lldp mdn statistics
Warning: This Command will clear MDN statistics of all the ports. Continue? [Y/N]y

```