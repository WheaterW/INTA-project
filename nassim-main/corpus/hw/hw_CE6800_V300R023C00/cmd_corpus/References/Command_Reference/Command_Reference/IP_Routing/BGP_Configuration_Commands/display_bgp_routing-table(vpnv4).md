display bgp routing-table(vpnv4)
================================

display bgp routing-table(vpnv4)

Function
--------



The **display bgp routing-table** command displays information about routes in a specified time range in a BGP VPN routing table.




Format
------

**display bgp vpnv4 vpn-instance** *vpn-instance-name* **routing-table** [ **peer** *ipv4-address* { **received-routes** | **advertised-routes** } ] **time-range** *start-time* *end-time*

**display bgp instance** *instance-name* **vpnv4** **vpn-instance** *vpn-instance-name* **routing-table** **time-range** *start-time* *end-time*

**display bgp vpnv4 all routing-table** [ **peer** *ipv4-address* { **received-routes** | **advertised-routes** } ] **time-range** *start-time* *end-time*

**display bgp instance** *instance-name* **vpnv4** **all** **routing-table** **time-range** *start-time* *end-time*

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **time-range** *start-time* *end-time*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-distinguisher** *route-distinguisher* | Displays statistics about the BGP routes with a specified RD. | The RD can be in any of the following formats:   * 2-byte AS number:4-byte user-defined number, for example, 101:3. The AS number is an integer ranging from 0 to 65535, and the user-defined number is an integer ranging from 0 to 4294967295. The AS number and user-defined number cannot both be 0s. That is, an RD cannot be 0:0. * 4-byte AS number in the integer format:2-byte user-defined number, for example, 65537:3. An AS number ranges from 65536 to 4294967295, and a user-defined number ranges from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 0 to 65535. A user-defined number also ranges from 0 to 65535.   The AS number and the user-defined number cannot both be 0s. That is, an RD cannot be 0.0:0.   * IPv4 address:2-byte user-defined number, for example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number is an integer ranging from 0 to 65535. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **peer** *ipv4-address* | Displays information about the routes of a specified peer. | The value is in dotted decimal notation. |
| **received-routes** | Displays information about the routes received from the specified peer. | - |
| **advertised-routes** | Displays the routes advertised to a specified peer. | - |
| **time-range** *start-time* | Specifies a starting time ([0-10000]d[0-23]h[0-59]m[0-59]s). | The value is an integer ranging from 0 to 4294967295. |
| **time-range** *end-time* | Ending time ([0-10000]d[0-23]h[0-59]m[0-59]s). | The value is an integer ranging from 0 to 4294967295. |
| **instance** *instance-name* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all** | Displays statistics about all BGP VPNv4 routes. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To display the labeled routes in the BGP routing table, run **display bgp routing-table label** command.To display information about BGP VPNv4 routes and BGP VPN routes, run display bgp vpnv4 routing-table command.



**Precautions**

This command does not display the default routes that are advertised to peers using the **peer default-route-advertise** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the BGP labeled routes of all VPN instances.
```
<HUAWEI> display bgp vpnv4 all routing-table label
BGP Local router ID is 10.1.1.9
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
 Origin      : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

 Total number of routes from all PE: 3
 Route Distinguisher: 100:1
        Network           NextHop           In/Out Label
 *>i    10.22.22.22       10.3.3.9           NULL/1036

 Route Distinguisher: 100:4
        Network           NextHop           In/Out Label
 *>     10.2.3.0          10.2.3.1          1037/NULL
 *>     10.11.11.11       10.0.0.11         1038/NULL

 VPN-Instance vpn1, router ID 10.1.1.9:
 Total Number of Routes: 1
        Network           NextHop           In/Out Label
 *>i    10.22.22.22       10.3.3.9          NULL/1036
 VPN-Instance vpn2, router ID 10.1.1.9:
 Total Number of Routes: 0

```

**Table 1** Description of the **display bgp routing-table(vpnv4)** command output
| Item | Description |
| --- | --- |
| BGP Local router ID is | Router ID of the local BGP device. |
| Total number of routes from all PE | Number of routes from all Pes. |
| Total Number of Routes | Total number of routes. |
| Route Distinguisher | Route distinguisher (RD). |
| Network | Network address in the BGP labeled routing table. |
| NextHop | Next hop address used to forward the packet. |
| In/Out Label | Values of the incoming and outgoing labels. |