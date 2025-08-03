display arp statistics
======================

display arp statistics

Function
--------



The **display arp statistics** command displays Address Resolution Protocol (ARP) entry statistics.




Format
------

**display arp statistics** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Displays statistics about ARP entries based on a specified interface name. | - |
| **interface** *interface-type* *interface-number* | Displays statistics about ARP entries based on a specified interface type and number. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To check ARP entry statistics or locate ARP faults, run the display arp statistics command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display ARP entry statistics on the interface.
```
<HUAWEI> display arp statistics interface 100GE 1/0/1
Dynamic: 0  (Resolved: 0  Incomplete: 0)  Static: 0  OpenFlow: 0
Redirect: 0

```

**Table 1** Description of the **display arp statistics** command output
| Item | Description |
| --- | --- |
| Static | Number of static ARP entries. |
| Redirect | Number of redirected ARP entries. |
| Dynamic | Number of dynamic ARP entries:   * Resolved: number of normal ARP entries. * Incomplete: number of fake ARP entries. |
| OpenFlow | Number of ARP entries delivered by the controller to the forwarder. |