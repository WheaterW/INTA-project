reset lldp statistics
=====================

reset lldp statistics

Function
--------



The **reset lldp statistics** command deletes statistics about Link Layer Discovery Protocol (LLDP) packets that all interfaces send and receive or LLDP packets that a specified interface sends and receives.




Format
------

**reset lldp statistics interface** { *interface-type* *interface-number* | *interface-name* }

**reset lldp statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface on which statistics about LLDP packets are to be deleted.  If this parameter is not specified, LLDP packet information on all interfaces is deleted. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If you want to quickly locate and process an LLDP fault, you must calculate the numbers of LLDP packets sent and received by a device for a specified period. Before collecting specific LLDP packet statistics, run the reset lldp statistics command to delete existing statistics about LLDP packets.



**Prerequisites**



LLDP has been enabled globally using the lldp enable command in the system view.



**Follow-up Procedure**



After running the reset lldp statistics command to delete existing statistics about LLDP packets, run the **display lldp statistics** command to view statistics about LLDP packets sent and received by a device within a specific period of time.



**Precautions**



If you do not configure the interface parameter when running the reset lldp statistics command, statistics about LLDP packets sent and received by all interfaces are deleted. Exercise caution when running this command.




Example
-------

# Delete statistics about LLDP packets that all interfaces send and receive.
```
<HUAWEI> reset lldp statistics
Warning: This Command will clear LLDP statistics of all the ports. Continue? [Y/N]y

```