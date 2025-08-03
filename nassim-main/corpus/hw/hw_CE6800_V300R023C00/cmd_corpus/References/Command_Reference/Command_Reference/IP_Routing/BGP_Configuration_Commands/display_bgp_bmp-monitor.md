display bgp bmp-monitor
=======================

display bgp bmp-monitor

Function
--------



The **display bgp bmp-monitor** command displays information about the BGP peers monitored by a BMP session in all address families or in a specified address family.




Format
------

**display bgp bmp-monitor ipv4** { *ipv4-address* | *ipv6-address* }

**display bgp bmp-monitor ipv6** *ipv6-address*

**display bgp bmp-monitor vpnv4 vpn-instance** *vpn-instance-name* *ipv4-address*

**display bgp bmp-monitor vpnv6 vpn-instance** *vpn-instance-name* *ipv6-address*

**display bgp bmp-monitor all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a BGP peer. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies the IPv6 address of a BGP peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **ipv4** | Displays information about BGP peers monitored by a BMP session in the IPv4 unicast address family. | - |
| **ipv6** | Displays information about BGP peers monitored by a BMP session in the IPv6 unicast address family. | - |
| **vpnv4** | Displays information about BGP peers monitored by a BMP session in the VPNv4 address family. | - |
| **vpn-instance** *vpn-instance-name* | Displays information about BGP peers monitored by a BMP session in the VPN instance address family. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **vpnv6** | Displays information about BGP peers monitored by a BMP session in the VPNv6 address family. | - |
| **all** | Displays information about BGP peers monitored by a BMP session in all address families. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To check information about the BGP peers monitored by a BMP session in all address families or in a specified address family, run the **display bgp bmp-monitor** command. The information includes the type of route reported to the monitoring server, IP address of the server with which a BMP session is established, BMP session alias, and BMP session status.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about BGP peers monitored by a BMP session in the IPv6 unicast address family.
```
<HUAWEI> display bgp bmp-monitor ipv6 2001:DB8:1::2
*>BGP ipv6-family unicast :
  Peer                     Session Ip               Alias      State  route-mode
  2001:DB8:1::2                 2001:DB8:1::2                            down   in pre-policy/in post-policy

```

# Display information about BGP peers monitored by a BMP session in all address families.
```
<HUAWEI> display bgp bmp-monitor all

 0.0.0.0/:: : monitor public / private
 Route modes: a - add-path, A - all, m - path-marking, ID - route-identifier

*>BGP ipv4-family unicast :
  Peer            Session Ip      Alias      State   route-mode
  10.1.1.1        10.10.10.10                down    in post-policy
                  10.10.10.10                down    in pre-policy
  10.2.2.2        10.10.10.12                down    in pre-policy
  0.0.0.0         10.10.10.11                up      local-rib(A/m)
                  10.10.10.12                down    local-rib

*>BGP ipv6-family unicast :
  Peer            Session Ip      Alias      State    route-mode
  2001:DB8:2::2   10.10.10.13     a          down     in pre-policy
  0.0.0.0         10.10.10.12                down     local-rib(a)
                  10.10.10.13     a          down     local-rib

```

**Table 1** Description of the **display bgp bmp-monitor** command output
| Item | Description |
| --- | --- |
| Peer | IP address of a monitored BGP peer. |
| Session Ip | IP address of the server with which a BMP session is established. |
| Alias | Alias of a BMP session. If no alias is specified, the field is empty. |
| State | Status of the BMP session:   * down. * up. |
| route-mode | Type of route reported to the monitoring server:   * in pre-policy: all received RIB-in routes. * in post-policy: RIB-in routes accepted by an import policy. * out pre-policy: all RIB-out routes, regardless of whether they match an export policy. * out post-policy: RIB-out routes that match an export policy. * local-rib: Local-RIB routes. * local-rib(a): Local-RIB Add-Path routes. |
| Route modes | BMP monitoring routing mode. |
| BGP ipv4-family unicast | BGP-IPv4 unicast address family. |
| BGP ipv6-family unicast | BGP-IPv6 unicast address family. |