display isis bfd
================

display isis bfd

Function
--------



The **display isis bfd** command displays information on BFD-capable interfaces and about BFD session.

The **display isis ipv6 bfd** command displays information about an interface on which IPv6 BFD for IS-IS is enabled and an IPv6 BFD session for IS-IS.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display isis bfd** [ *process-id* | { **vpn-instance** *vpn-instance-name* } ] **session** { **all** | { **peer** *peer-addr* } | **interface** { *interface-name* | *interface-type* *interface-number* } }

**display isis** { *process-id* | { **vpn-instance** *vpn-instance-name* } } **bfd** **session** { **all** | { **peer** *peer-addr* } | **interface** { *interface-name* | *interface-type* *interface-number* } }

**display isis bfd** [ *process-id* | { **vpn-instance** *vpn-instance-name* } ] **interface**

**display isis** *process-id* **bfd** **interface**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display isis ipv6 bfd** [ *process-id* | { **vpn-instance** *vpn-instance-name* } ] **session** { **all** | { **peer** *peer-addr* } | **interface** { *interface-name* | *interface-type* *interface-number* } }

**display isis ipv6 bfd** [ *process-id* | { **vpn-instance** *vpn-instance-name* } ] **interface**

**display isis** { *process-id* | { **vpn-instance** *vpn-instance-name* } } **ipv6** **bfd** **session** { **all** | { **peer** *peer-addr* } | **interface** { *interface-name* | *interface-type* *interface-number* } }

**display isis** *process-id* **ipv6** **bfd** **interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an IS-IS process ID. | The value is an integer ranging from 1 to 4294967295. |
| **session** | Displays information about BFD session. | - |
| **all** | Display information about BFD sessions for IS-IS on all interfaces. | - |
| **peer** *peer-addr* | Specifies the address of a neighbor. | The value is a string case-sensitive characters. It cannot contain spaces. |
| **interface** | Displays information on BFD-capable interfaces. | - |
| **interface** *interface-type* *interface-number* | Display the BFD sessions for specified interface. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of an IPv6 address family-enabled VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To view information about an BFD session for IS-IS, run the display isis bfd session command.To view information about an IPv6 BFD session for IS-IS, run the display isis ipv6 bfd session command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the IPv4 BFD session for IS-IS.
```
<HUAWEI> display isis bfd 1 session all

                      BFD session information for ISIS(1)
                      -----------------------------------
Peer System ID : 2222.2222.2222        Interface : 100GE1/0/1
TX : 10            BFD State : up      Peer IP Address : 10.1.1.2
RX : 10            LocDis : 16386      Local IP Address: 10.1.1.1
Multiplier : 3     RemDis : 16386      Type : L2
Diag : No diagnostic information
Total BFD session(s): 1

```

# Display information about the IPv6 BFD session for IS-IS.
```
<HUAWEI> display isis ipv6 bfd 1 session all
IPv6 BFD session information for ISIS(1)
-----------------------------------------------------------------------------
Peer System ID : 0000.0000.0001        Type : L2              
Interface : 100GE1/0/1           
IPv6 BFD State : up      TX : 10            RX : 10            Multiplier : 3
LocDis : 16386      Local IPv6 Address: 2001:DB8::1
RemDis : 16386      Peer IPv6 Address : 2001:DB8::2
Diag : No diagnostic information

Total BFD session(s): 1

```

# Display information about the IPv6 BFD session for IS-IS of the neighbor with a specified IPv6 address.
```
<HUAWEI> display isis ipv6 bfd 1 session peer 2001:DB8::1
IPv6 BFD session information for ISIS(1)
-----------------------------------------------------------------------------

Peer System ID : 0000.0000.0001        Type : L2
Interface : 100GE1/0/1           
IPv6 BFD State : up      TX : 10            RX : 10            Multiplier : 3     
LocDis : 16386      Local IPv6 Address: 2001:DB8::1
RemDis : 16386      Peer IPv6 Address : 2001:DB8::2
Diag : No diagnostic information

Total BFD session(s): 1

```

**Table 1** Description of the **display isis bfd** command output
| Item | Description |
| --- | --- |
| BFD State | BFD status:   * Up: indicates that the BFD session is successfully set up. * Down: indicates that the BFD session fails to be set up. * Unknown: When BFD fails to go Up for the first time, whether the link is faulty is unknown. |
| Peer System ID | System ID of a neighbor. |
| Peer IPv6 Address | IPv6 link-local address of the neighbor. |
| Peer IP Address | IPv4 address of the peer interface. |
| Interface | Name of the local interface. |
| TX | Minimum interval at which BFD packets are sent to the neighbor. |
| RX | Minimum interval at which BFD packets are received from the neighbor. |
| LocDis | Local discriminator of the BFD session. |
| Local IPv6 Address | IPv6 link-local address of the local device. |
| Local IP Address | IPv4 address of the local interface. |
| Multiplier | Local detection multiplier. |
| RemDis | Remote discriminator of the BFD session. |
| Type | Level of a neighbor:   * L1: Level-1. * L2: Level-2. * L1L2: Level-1-2. |
| Diag | Diagnostic information. |
| Total BFD session(s) | Total number of BFD sessions. |
| IPv6 BFD State | IPv6 BFD status:   * Up: indicates that the IPv6 BFD session is successfully set up. * Down: indicates that the IPv6 BFD session fails to be set up. * Unknown: When BFD fails to go Up for the first time, whether the link is faulty is unknown. |