display bgp brief
=================

display bgp brief

Function
--------



The **display bgp vpnv4 brief** command displays brief information about VPNv4 and VPN instances (IPv4 address family).




Format
------

**display bgp vpnv4 all brief**

**display bgp vpnv4 vpn-instance** *vpn-instance-name* **brief**

**display bgp instance** *instance-name* **vpnv4** **all** **brief**

**display bgp instance** *instance-name* **vpnv4** **vpn-instance** *vpn-instance-name* **brief**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specify a VPN-Instance (VRF) name. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **instance** *instance-name* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters. If spaces are used, the string must be enclosed in double quotation marks (" "). |
| **all** | Displays information about all VPNv4 and VPN instances (IPv4 address family). | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check information about VPNv4 and VPN instances (IPv4 address family), run the **display bgp vpnv4 brief** command. The VPN instances are displayed and arranged alphabetically by name.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about VPNv4 instances and all VPN instances (IPv4 address family).
```
<HUAWEI> display bgp vpnv4 all brief

VPNV4 :
  Rd Num              Peer Num            Route Num
  0                   1                   0

VPN-Instance(IPv4-family):
  VPN-Instance Name   Peer Num            Route Num
  vrf0                   0                   0
  vrf1                   0                   0
  vrf11                  0                   0
  vrf12                  0                   0
  vrf13                  0                   0
  vrf14                  0                   0
  vrf2                   0                   20
  vrf3                   0                   20
  vrf4                   0                   24
  vrf5                   0                   24
  vrf6                   0                   0
  vrf7                   0                   0
  vrf8                   0                   20

```

**Table 1** Description of the **display bgp brief** command output
| Item | Description |
| --- | --- |
| VPNV4 | BGP-VPNv4 address family. |
| Rd Num | Number of RDs. |
| Peer Num | Indicates the number of peers. |
| Route Num | Number of routes. |
| VPN-Instance Name | VPN instance name. |
| VPN-Instance(IPv4-family) | BGP-VPN instance IPv4 address family. |