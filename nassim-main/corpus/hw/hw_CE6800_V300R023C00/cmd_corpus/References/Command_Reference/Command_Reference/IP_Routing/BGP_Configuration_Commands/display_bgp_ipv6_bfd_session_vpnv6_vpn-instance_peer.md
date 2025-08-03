display bgp ipv6 bfd session vpnv6 vpn-instance peer
====================================================

display bgp ipv6 bfd session vpnv6 vpn-instance peer

Function
--------



The **display bgp ipv6 bfd session vpnv6 vpn-instance peer** command displays information about BFD sessions in vpn instances between BGP peers.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp** [ **instance** *bgpName* ] **ipv6** **bfd** **session** **vpnv6** **vpn-instance** *vpn-instance-name* **peer** *ipv6-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *bgpName* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without any spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **vpnv6** | Displays information about the BFD sessions of a VPNv6 instance. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of the VPN instance that has the IPv6 address family enabled. | The value is a string of 1 to 31 case-sensitive characters. |
| **peer** *ipv6-address* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **peer bfd** and **peer bfd enable** commands can be used to change the parameters of BFD sessions between BGP peers.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display BFD sessions in VPN instances between BGP peers.
```
<HUAWEI> display bgp ipv6 bfd session vpnv6 vpn-instance vpn1 peer 2001:DB8:100::2
VPN-Instance vpn1:
  Local_Address  : 2001:DB8:100::1                                  
  Peer_Address   : 2001:DB8:100::2                                  
  Tx-interval(ms): 10          Rx-interval(ms): 10  
  Multiplier     : 3           Interface      : 100GE1/0/1
  Session-State  : Up
  Wtr-interval(m): 10

```

**Table 1** Description of the **display bgp ipv6 bfd session vpnv6 vpn-instance peer** command output
| Item | Description |
| --- | --- |
| Local\_Address | Local address. |
| Peer\_Address | Peer IP address. |
| Multiplier | Remote detection multiplier. |
| Interface | Interface used to set up the BFD session.  Information about the interface is displayed only when the EBGP peer relationship is set up between it and its directly connected interface; otherwise, the interface information is displayed as Unknown. |
| Session-State | BFD status:   * BFD global disable: BFD is disabled. * Up: The BFD session is in the Up state. * Down: The BFD session is in the Down state. * Unknown: indicates that BFD does not know whether the link is faulty when the link is not Up for the first time. |
| Tx-interval(ms) | Interval at which BFD packets are sent, in milliseconds. |
| Rx-interval(ms) | Interval for receiving BFD packets, in milliseconds. |
| Wtr-interval(m) | WTR time of the BFD session, in minutes. |