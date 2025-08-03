bfd bind peer-ipv6
==================

bfd bind peer-ipv6

Function
--------



The **bfd bind peer-ipv6** command creates a BFD for IPv6 session, binds related information to the BFD session, and displays the BFD session view.



By default, the binding between a BFD session for IPv6 and a peer IPv6 address is not created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**bfd** *session-name* **bind** **peer-ipv6** *peer-ipv6* [ **vpn-instance** *vpn-name* ] [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ **source-ipv6** *source-ipv6* ] [ **select-board** *slot-id1* [ *slot-id2* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *session-name* | Specifies the name of a BFD for IPv6 session. | The value is a string of 1 to 64 case-insensitive characters without spaces. |
| *peer-ipv6* | Specifies the peer IPv6 address bound to a BFD for IPv6 session. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **vpn-instance** *vpn-name* | Specifies the name of a VPN instance bound to a BFD session for IPv6. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **interface** *interface-type* *interface-number* | Specifies the type and number of a Layer 3 interface to which a BFD session for IPv6 is bound. | - |
| *interface-name* | Specifies the local Layer 3 interface to which a BFD session is bound. | - |
| **source-ipv6** *source-ipv6* | Specifies the source IPv6 address carried in a BFD packet. If no source IPv6 address is specified, a device uses a source IPv6 address in either of the following modes before sending BFD packets:   * During negotiation on BFD session for IPv6 parameters, the device searches for the IPv6 address of an outbound interface connected to the remote end in the local routing table as the source IPv6 address before sending BFD packets. * During BFD for IPv6 detection, the device sets the source IPv6 address to a fixed value. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **select-board** *slot-id1* | Specifies the board to be forcibly selected by the BFD session state machine. | The value is a string of 1 to 19 case-sensitive characters, spaces not supported. |
| *slot-id2* | Specifies the board to be forcibly selected by the BFD session state machine.  If both slot-id1 and slot-id2 are configured, only one board is selected, and slot-id1 is preferred. If slot-id1 fails to be selected, slot-id2 is selected. If both boards fail to be selected, board selection stops. | The value is a string of 1 to 19 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To rapidly detect IPv6 link faults on a network, create a BFD session for IPv6.When creating the binding between a BFD session for IPv6 and a peer IPv6 address:

* If only the peer IPv6 address is specified, BFD detects faults in a multi-hop link.
* If both the peer IPv6 address and local interface are specified, BFD detects faults in a single-hop link. That is, BFD monitors a fixed route whose outbound interface is this interface and the next-hop address is the peer IPv6 address.
* This parameter is manually configured only when BFD works with Unicast Reverse Path Forwarding (URPF). This is because URPF checks the source IP address in received packets.
* If a source address is specified, the source-ipv6 parameter is used to ensure that BFD packets are not discarded after URPF is enabled. You must specify the correct source IPv6 address. This is because the system only checks whether the parameter is a valid source IPv6 address (for example, the address cannot be a multicast or broadcast address) and does not check the correctness.
* If both the peer IPv6 address and the VPN instance are specified, BFD detects faults in the multi-hop link for a specified VPN instance.
* If the peer IPv6 address, the VPN instance, and the local interface are specified, BFD detects faults in the single-hop link for a specified VPN instance.

**Prerequisites**

BFD has been globally enabled using the **bfd** command in the system view.

**Configuration Impact**

You can run the **bfd bind peer-ipv6** command to create the binding between a static BFD session for IPv6 and a peer IPv6 address.


Example
-------

# Create a BFD session for IPv6 named s1 so that BFD for IPv6 can detect faults in the multi-hop link to the peer IPv6 address 2001:db8::1.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd s1 bind peer-ipv6 2001:db8::1

```

# Create a BFD session for IPv6 named s1 so that BFD for IPv6 can detect faults in the multi-hop link to the peer IPv6 address 2001:db8::2.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd session bind peer-ipv6 2001:db8::2

```

# Create a static BFD for IPv6 session with the name atob and check the single-hop link from the local interface to the peer IPv6 address 2001:db8::1.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address 2001:db8::2 64
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] bfd atob bind peer-ipv6 2001:db8::1 interface 100GE 1/0/1

```

# Create a BFD for IPv6 session named selectboard and forcibly select the board to detect the multi-hop link with the peer IPv6 address being 2001:db8::1.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd selectboard bind peer-ipv6 2001:db8::1 select-board 3

```