display bgp mvpn brief
======================

display bgp mvpn brief

Function
--------



The **display bgp mvpn brief** command displays brief information about multicast VPN instances.




Format
------

**display bgp mvpn all brief**

**display bgp mvpn vpn-instance** *vpn-instance-name* **brief**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of an MVPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **all** | Displays information about all MVPN instances. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When the **display bgp mvpn brief** command is used to view information about multicast virtual private network (MVPN), VPN instances are listed in the lexicographic order of the VPN instance name.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about all MVPN instances.
```
<HUAWEI> display bgp mvpn all brief
  RD Num               Peer Num             Route Num            
    1                    2                    5                  
  VPN-Instance Name    Peer Num             Route Num            
    mcast1               0                    5

```

# Display brief information about MVPN instances and all VPN instances.
```
<HUAWEI> display bgp mvpn all brief

MVPN:
  RD Num               Peer Num             Route Num
    3                    2                    5

VPN-Instance(IPv4-MVPN-family):
  VPN-Instance Name    Peer Num             Route Num
    VPNA                 0                    5

```

**Table 1** Description of the **display bgp mvpn brief** command output
| Item | Description |
| --- | --- |
| RD Num | Number of Route Distinguishers (RDs). |
| Peer Num | Indicates the number of peers. |
| Route Num | Number of routes. |
| VPN-Instance Name | Name of a VPN instance. |
| MVPN | BGP-MVPN address family. |
| VPN-Instance(IPv4-MVPN-family) | VPN instance IPv4 MVPN address family. |