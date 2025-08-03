display bgp bfd session
=======================

display bgp bfd session

Function
--------



The **display bgp bfd session** command displays information about BFD sessions between BGP peers.




Format
------

**display bgp** [ **instance** *instance-name* ] **bfd** **session** **all**

**display bgp** [ **instance** *instance-name* ] **bfd** **session** **peer** *ipv4-address*

**display bgp bfd session vpnv4 vpn-instance** *vpn-instance-name* **peer** *ipv4-address*

**display bgp instance** *instance-name* **bfd** **session** **vpnv4** **vpn-instance** *vpn-instance-name* **peer** *ipv4-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-name* | Specifies the name of a BGP instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **all** | Displays all BFD sessions established by BGP. | - |
| **peer** *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| **vpnv4** | Indicates the BGP-VPNv4 address family. | - |
| **vpn-instance** *vpn-instance-name* | Displays information about BFD sessions of an IPv4 VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The display bgp bfd session command with different parameters specified displays different information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all BFD sessions established by BGP.
```
<HUAWEI> display bgp bfd session all
--------------------------------------------------------------------------------
  Local_Address      Peer_Address       Interface
  10.1.12.2          10.1.12.1          10GE1/0/1
  Tx-interval(ms)    Rx-interval(ms)    Multiplier  Session-State         
     10           10           3       Up
  Wtr-interval(m) 
     0                           
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display bgp bfd session** command output
| Item | Description |
| --- | --- |
| Local\_Address | Local IP address. |
| Peer\_Address | Neighbor IP address. |
| Interface | Interface used to set up the BFD session.  Information about the interface is displayed only when the EBGP peer relationship is set up between it and its directly connected interface; otherwise, the interface information is displayed as Unknown. |
| Tx-interval(ms) | Interval at which BFD packets are sent, in milliseconds. |
| Rx-interval(ms) | Interval at which BFD packets are received, in milliseconds. |
| Multiplier | Remote detection multiplier. |
| Session-State | BFD status:   * BFD global disable: BFD is globally disabled. * Up: The BFD session is in the Up state. * Down: The BFD session is in the Down state. * Unknown: When BFD fails to go Up for the first time, whether the link is faulty is unknown. |
| Wtr-interval(m) | WTR time of the BFD session, in minutes. |