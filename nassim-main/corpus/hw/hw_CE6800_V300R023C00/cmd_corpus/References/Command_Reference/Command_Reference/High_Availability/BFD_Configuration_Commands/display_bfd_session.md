display bfd session
===================

display bfd session

Function
--------



The **display bfd session** command displays information about BFD sessions.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display bfd session all** [ **for-ip** ]

**display bfd session static** [ **for-ip** ]

**display bfd session passive-dynamic** [ **peer-ip** *peer-ip* **remote-discriminator** *discr-value* ]

**display bfd session dynamic**

**display bfd session discriminator** *discr-value*

**display bfd session peer-ip** { *peer-ip* [ **vpn-instance** *vpn-name* ] | **default-ip** }

**display bfd session static-auto**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display bfd session peer-ipv6** *peer-ipv6* [ **vpn-instance** *vpn-name* ]

**display bfd session all for-ipv6**

**display bfd session static for-ipv6**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **for-ip** | Displays the configurations of the BFD sessions for detecting IP links. | - |
| **all** | Displays the configurations of all BFD sessions. | - |
| **static** | Displays information about static BFD sessions. | - |
| **peer-ip** *peer-ip* | Displays information about the BFD session with a specified peer IP address. | The value is in dotted decimal notation. |
| **default-ip** | Displays statistics about multicast BFD sessions. | - |
| **peer-ipv6** *peer-ipv6* | Displays the configuration of the BFD6 session bound to a specified peer IPv6 address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **passive-dynamic** | Displays information about the BFD sessions that are passively created. | - |
| **remote-discriminator** *discr-value* | Displays information about the BFD sessions with a specified remote discriminator. | The value is an integer ranging from 1 to 4294967295. |
| **dynamic** | Displays information about all dynamic BFD sessions and static BFD sessions with automatically negotiated discriminators. | - |
| **discriminator** *discr-value* | Displays information about the BFD session with a specified local discriminator. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-name* | Displays information about the BFD session bound to a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **static-auto** | Displays statistics about the static BFD session with the automatically negotiated discriminators. | - |
| **for-ipv6** | Displays the configuration of the BFD6 session for monitoring an IPv6 link.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view information about BFD sessions, run the **display bfd session** command with one or more parameters.

**Prerequisites**



BFD has been globally enabled using the **bfd** command in the system view.



**Precautions**

* When the BFD session changes from Down to Up, and the WTR time is not zero, the notification that the BFD session goes Up can be received only after the WTR time expires.
* If a static BFD session with automatically negotiated discriminators and a dynamic BFD session have the same configurations, you can view that the shared BFD session belongs to both the static session with automatically negotiated discriminators and the dynamic session in terms of the BFD session type.
* The **display bfd session dynamic** command displays information about both dynamic and static sessions. The statically self-negotiated sessions are treated as dynamic sessions.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about all BFD sessions.
```
<HUAWEI> display bfd session all
S: Static session
D: Dynamic session
IP: IP session
IF: Single-hop session
PEER: Multi-hop session
AUTO: Automatically negotiated session
VXLAN: VXLAN session
(w): State in WTR
(*): State is invalid
Total UP/DOWN Session Number : 0/1
--------------------------------------------------------------------------------
Local      Remote     PeerIpAddr      State     Type        InterfaceName
--------------------------------------------------------------------------------
111        222        10.10.10.2      Down      S/IP-PEER          -
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display bfd session** command output
| Item | Description |
| --- | --- |
| State | Status of the BFD session:   * Up: The BFD session is in the Up state. * Down: The BFD session is in the Down state. * AdmDown: The BFD session is in the AdminDown state. After the shutdown (BFD session view) command is run, the BFD session becomes AdminDown. * Up(w): indicates that the BFD session is in the Up state and during the WTR time. * Up(\*)/Down(\*): indicates that the BFD session is in the invalid state. * Init: The BFD session is in the Init state. |
| Local | Local BFD session discriminator. |
| Remote | Remote discriminator of the BFD session. |
| PeerIpAddr | Peer IP address of the BFD session. |
| Type | Type of the BFD session:   * S/IP-PEER: indicates a session created statically and bound to an IP link. * S/IP-IF: indicates a session created statically and bound to an interface. * D/IP-PEER: indicates a session created dynamically and bound to an IP link. * D/IP-IF: indicates a session created dynamically and bound to an interface. * S/AUTO-IF: indicates the static single-hop BFD session with automatically negotiated discriminators. * S/AUTO-PEER: indicates the static multi-hop BFD session with automatically negotiated discriminators. * S/AUTO-VXLAN: indicates the VXLAN BFD session with automatically negotiated discriminators. |
| InterfaceName | Outbound interface bound to the BFD session. In multi-hop BFD, this field is displayed as - because no interface is bound to a BFD session. |
| IP | IP session. |
| Total UP/DOWN Session Number | UP BFD Session Number/DOWN BFD Session Number. |
| VXLAN | Vxlan session. |
| AUTO | Automatically negotiated session. |
| PEER | Multi-hop session. |
| IF | Single-hop session. |