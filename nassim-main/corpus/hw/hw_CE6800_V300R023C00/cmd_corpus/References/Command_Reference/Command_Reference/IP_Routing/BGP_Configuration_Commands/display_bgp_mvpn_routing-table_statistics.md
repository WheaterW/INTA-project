display bgp mvpn routing-table statistics
=========================================

display bgp mvpn routing-table statistics

Function
--------



The **display bgp mvpn routing-table statistics** command displays the statistics of BGP Multicast Virtual Private Network (MVPN) routes.




Format
------

**display bgp mvpn** { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** **all-type** **statistics**

**display bgp mvpn** { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** **type** { **1** | **2** | **3** | **4** | **5** | **6** | **7** } **statistics**

**display bgp mvpn vpn-instance** *vpn-instance-name* **routing-table** **all-type** **statistics**

**display bgp mvpn vpn-instance** *vpn-instance-name* **routing-table** **type** { **1** | **2** | **3** | **4** | **5** | **6** | **7** } **statistics**

**display bgp mvpn all routing-table peer** *ipv4-address* { **advertised-routes** | **received-routes** } **all-type** **statistics**

**display bgp mvpn all routing-table peer** *ipv4-address* { **advertised-routes** | **received-routes** } **type** { **1** | **2** | **3** | **4** | **5** | **6** | **7** } **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays statistics about all BGP MVPN routes. | - |
| **route-distinguisher** *route-distinguisher* | Displays statistics about BGP routes with the specified Route Distinguisher (RD). | The RD can be in any of the following formats:   * 2-byte AS number:4-byte user-defined number, for example, 101:3. The AS number ranges from 0 to 65535, and the user-defined number ranges from 0 to 4294967295. If both the AS number and user-defined number are 0, that is, the RD is 0:0, the MVPN instance is a public network MVPN instance. * 4-byte AS number in integer format:2-byte user-defined number, for example, 65537:3. An AS number ranges from 65536 to 4294967295, and a user-defined number ranges from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 0 to 65535. A user-defined number also ranges from 0 to 65535. * IPv4 address:2-byte user-defined number, for example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number is an integer ranging from 0 to 65535. |
| **all-type** | Displays all types of MVPN route statistics. | - |
| **type** **1** | Displays intra-AS I-PMSI A-D route statistics. | - |
| **2** | Displays inter-AS I-PMSI A-D route statistics. | - |
| **3** | Displays S-PMSI A-D route statistics. | - |
| **4** | Displays Leaf A-D route statistics. | - |
| **5** | Displays Source Active A-D route statistics. | - |
| **6** | Displays Shared Tree Join C-multicast route statistics. | The value is in dotted decimal notation. |
| **7** | Displays Source Tree Join C-multicast route statistics. | - |
| **vpn-instance** *vpn-instance-name* | Displays the BGP routes of the specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **peer** *ipv4-address* | Displays statistics about routes of a specified peer. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **advertised-routes** | Displays statistics about the routes advertised to a specified peer. | - |
| **received-routes** | Displays statistics about the routes learned from a specified peer. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view the statistics of BGP Multicast Virtual Private Network (MVPN) routes, run the display bgp mvpn routing-table statistics command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about intra-AS I-PMSI A-D routes of the VPN instance VPNA.
```
<HUAWEI> display bgp mvpn vpn-instance VPNA routing-table type 1 statistics
Total number of routes of IPv4-MVPN-family for vpn-instance VPNA: 3

```

# Display all types of MVPN route statistics.
```
<HUAWEI> display bgp mvpn all routing-table all-type statistics
Total number of routes from all PE: 5
    Number of Intra-AS I-PMSI A-D Routes: 3
    Number of Inter-AS I-PMSI A-D Routes: 0
    Number of S-PMSI A-D Routes: 0
    Number of Leaf A-D Routes: 0
    Number of Source Active A-D Routes: 0
    Number of Shared Tree Join Routes: 0
    Number of Source Tree Join Routes: 2

 Total number of routes of IPv4-MVPN-family for vpn-instance VPNA: 5
    Number of Intra-AS I-PMSI A-D Routes: 3
    Number of Inter-AS I-PMSI A-D Routes: 0
    Number of S-PMSI A-D Routes: 0
    Number of Leaf A-D Routes: 0
    Number of Source Active A-D Routes: 0
    Number of Shared Tree Join Routes: 0
    Number of Source Tree Join Routes: 2

```

**Table 1** Description of the **display bgp mvpn routing-table statistics** command output
| Item | Description |
| --- | --- |
| Total number of routes from all PE | Number of routes received from provider edges (PEs) in the BGP MVPN routing table. |
| Total number of routes of IPv4-MVPN-family for vpn-instance VPNA | Number of the routes of the specified VPN instance in the BGP MVPN routing table. |
| Number of Intra-AS I-PMSI A-D Routes | Number of intra-AS I-PMSI A-D routes. |
| Number of Inter-AS I-PMSI A-D Routes | Number of inter-AS I-PMSI A-D routes. |
| Number of S-PMSI A-D Routes | Number of S-PMSI A-D routes. |
| Number of Leaf A-D Routes | Number of Leaf A-D routes. |
| Number of Source Active A-D Routes | Number of Source Active A-D routes. |
| Number of Shared Tree Join Routes | Number of Shared Tree Join routes. |
| Number of Source Tree Join Routes | Number of Source Tree Join routes. |