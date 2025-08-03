reset arp packet statistics
===========================

reset arp packet statistics

Function
--------



Using the **reset arp packet statistics** command, you can reset statistics about Address Resolution Protocol (ARP) packets.




Format
------

**reset arp packet statistics** [ **interface** [ *interface-name* | *interface-type* *interface-number* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Specifies a Layer 3 interface. After this parameter is specified, the command clears the statistics about the ARP packets received by this interface. | - |
| *interface-name* | Specifies a Layer 3 interface. After this parameter is specified, the command clears the statistics about the ARP packets received by this interface. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If the user wants to view statistics of ARP packets by using the **display arp packet statistics** command. In order to obtain accurate statistics, the user needs to execute the command to clear the existing statistics.



**Follow-up Procedure**



Run the **display arp packet statistics** command to view statistics about ARP packets.




Example
-------

# Clear the statistics about ARP packets on all the interface boards.
```
<HUAWEI> reset arp packet statistics

```

# Clear the statistics about the ARP packets sent and received by all Layer 3 interfaces.
```
<HUAWEI> reset arp packet statistics interface

```