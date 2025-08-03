display bgp evpn all routing-table statistics
=============================================

display bgp evpn all routing-table statistics

Function
--------



The **display bgp evpn all routing-table statistics** command displays statistics information about all of BGP EVPN routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp evpn all routing-table statistics**

**display bgp** [ **instance** *instance-name* ] **evpn** **all** **routing-table** **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-name* | Displays statistics information about EVPN routes of a specified BGP instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check statistics information about BGP EVPN routes of all instances for maintenance, run the display bgp evpn all routing-table statistics command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about all of BGP EVPN routes.
```
<HUAWEI> display bgp evpn all routing-table statistics
Total number of routes from all PE: 2
 Number of A-D Routes: 2
 Number of Mac Routes: 0
 Number of Inclusive Multicast Routes: 0
 Number of ES Routes: 0
 Number of Ip Prefix Routes: 0
 Number of ARP Routes: 0

```

**Table 1** Description of the **display bgp evpn all routing-table statistics** command output
| Item | Description |
| --- | --- |
| Total number of routes from all PE | Number of EVPN routes received from all PEs. |
| Number of A-D Routes | Number of Ethernet auto-discovery routes. |
| Number of Mac Routes | Number of MAC advertisement routes. |
| Number of Inclusive Multicast Routes | Number of inclusive multicast routes. |
| Number of ES Routes | Number of Ethernet segment routes. |
| Number of Ip Prefix Routes | Number of IP prefix routes. |
| Number of ARP Routes | Number of arp routes. |