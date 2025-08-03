display bgp routing-table dampened
==================================

display bgp routing-table dampened

Function
--------



The **display bgp routing-table dampened** command displays BGP dampened routes.




Format
------

**display bgp** [ **vpnv4** **vpn-instance** *vpn-instance-name* ] **routing-table** [ **statistics** ] **dampened**

**display bgp instance** *instance-name* [ **vpnv4** **vpn-instance** *vpn-instance-name* ] **routing-table** [ **statistics** ] **dampened**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpnv4** | Displays the BGP routes of a VPNv4 instance. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |
| **statistics** | Displays statistics about BGP routes. | - |
| **dampened** | BGP-dampened routes. | - |
| **instance** *instance-name* | Specifies a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view the information about BGP dampened routes, run the display bgp routing-table dampened command with specified parameters.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display BGP dampened routes.
```
<HUAWEI> display bgp routing-table dampened
 BGP Local router ID is 10.0.0.2
 Status codes: * - valid, > - best, d - damped, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
 Origin      : i - IGP, e - EGP, ? - incomplete
 Total Number of Routes: 5
   Network           From              Reuse     Path/Origin
 d 10.1.0.0          10.110.156.30     00:09:33  700 i
 d 10.2.0.0          10.110.156.30     00:09:33  700 i
 d 10.3.0.0          10.110.156.30     00:09:33  700 i
 d 10.4.0.0          10.110.156.30     00:09:33  700 i
 d 10.5.0.0          10.110.156.30     00:09:33  700 i

```

**Table 1** Description of the **display bgp routing-table dampened** command output
| Item | Description |
| --- | --- |
| Total Number of Routes | Total number of dampened routes. |
| Network | Indicates the network address in the BGP routing table. |
| From | IP address of the peer from which the route is learned. |
| Reuse | Reuse value (in seconds). |
| Path | AS\_Path and Origin attributes of a route. |