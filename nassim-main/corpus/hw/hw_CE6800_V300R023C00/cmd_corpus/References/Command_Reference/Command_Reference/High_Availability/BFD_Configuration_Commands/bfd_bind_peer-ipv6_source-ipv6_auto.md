bfd bind peer-ipv6 source-ipv6 auto
===================================

bfd bind peer-ipv6 source-ipv6 auto

Function
--------



The **bfd bind peer-ipv6 source-ipv6 auto** command creates a static BFD for IPv6 session with automatically negotiated discriminators and enters the BFD session view.



By default, no static BFD for IPv6 session with automatically negotiated discriminators is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**bfd** *sessname-value* **bind** **peer-ipv6** *peerip6-value* [ **vpn-instance** *vpnname-value* ] [ **interface** { *interface-value* | *ifType* *ifNum* } ] **source-ipv6** *sourceip6-value* [ **select-board** *slot-id* [ *slot-id2* ] ] **auto**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *sessname-value* | Specifies the name of a BFD for IPv6 session. | The value is a string of 1 to 64 case-insensitive characters without spaces. |
| **peer-ipv6** *peerip6-value* | Specifies the peer IPv6 address bound to a BFD for IPv6 session. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **vpn-instance** *vpnname-value* | Specifies the name of a VPN instance bound to a BFD session for IPv6. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **interface** *ifType* *ifNum* | Specifies the type and number of a Layer 3 interface to which a BFD session for IPv6 is bound. | - |
| **interface** *interface-value* | Specifies the name of the local Layer 3 interface bound to a BFD session for IPv6. | The interface can be a GE interface or its sub-interface, or an Eth-Trunk interface or its sub-interface. |
| **source-ipv6** *sourceip6-value* | Specifies the source IPv6 address carried in a BFD packet. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **select-board** *slot-id* | Specifies the board to be forcibly selected by the BFD session state machine. | The value is a string of 1 to 19 case-sensitive characters, spaces not supported. |
| *slot-id2* | Specifies the board to be forcibly selected by the BFD session state machine.  If both slot-id and slot-id2 are configured, only one board is selected, and slot-id is preferred. If slot-id fails to be selected, slot-id2 is selected. If both boards fail to be selected, board selection stops. | The value is a string of 1 to 19 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A BFD session for IPv6 is established to rapidly detect faults in IPv6 links on a network. A device needs to establish a BFD session with a remote device on which a dynamic BFD session is established to detect faults in static routes. In this case, the **bfd bind peer-ipv6 source-ipv6 auto** command is used to create a BFD session for IPv6 with automatically negotiated discriminators.When creating a static BFD session for IPv6 with automatically negotiated discriminators:

* If only the peer IPv6 address is specified, BFD detects faults in a multi-hop link.
* If both the peer IPv6 address and local interface are specified, BFD detects faults in a single-hop link. That is, BFD monitors a fixed route whose outbound interface is this interface and the next-hop address is the peer IPv6 address.
* If the source IPv6 address is specified for the interface whose physical status is to be monitored by BFD, BFD packets are correctly forwarded after URPF has been enabled. The source-ipv6 parameter must be configured correctly because the system checks only the validity of the source IPv6 address. A multicast or broadcast address is an invalid source IPv6 address.
* If both the peer IPv6 address and the VPN instance are specified, BFD detects faults in the multi-hop link for a specified VPN instance.
* If the peer IPv6 address, the VPN instance, and the local interface are specified, BFD detects faults in the single-hop link for a specified VPN instance.

**Follow-up Procedure**

After a static BFD session for IPv6 with automatically negotiated discriminators is created and the BFD session for IPv6 view is displayed:

* Run the **description** command to configure a description for the BFD session for IPv6.
* Run the **min-tx-interval** command to set a desired minimum interval at which BFD packets are sent.
* Run the **min-rx-interval** command to set a desired minimum interval at which BFD packets are received.
* Run the **detect-multiplier** command to set a local detection multiplier for the BFD session.
* Run the **process-pst** command to enable BFD to modify the PST if BFD detects a fault.
* Run the **wtr** command to set a WTR time for the BFD session for IPv6.

**Precautions**

* The difference between a static BFD session for IPv6 and a static BFD session for IPv6 with automatically negotiated discriminators is as follows:
* A static BFD session for IPv6 requires the configuration of local and remote discriminators.
* A static BFD session for IPv6 with automatically negotiated discriminators does not require the configuration of local or remote discriminator.
* If the IPv6 address of an outbound interface is changed after the BFD session for IPv6 has been configured, the IPv6 address carried in the BFD packets will not be changed.
* The source and peer IPv6 address must be configured if automatic negotiation on a local discriminator is enabled. A multicast or broadcast address is an invalid IPv6 address.
* The source IPv6 address must be configured if BFD for IPv6 with automatic negotiation on a local discriminator is enabled.
* You can run the **undo bfd session-name** command to delete a specified BFD session and its binding information.

Example
-------

# Create a static BFD for IPv6 session with the automatically negotiated discriminator atob and check the single-hop link from the local interface to the peer IP address 2001:db8:1::1.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address 2001:db8:1::2 127
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] bfd atob bind peer-ipv6 2001:db8:1::1 interface 100GE1/0/1 source-ipv6 2001:db8:1::2 auto

```

# Create a static BFD for IPv6 session with the automatically negotiated discriminator selectboard, forcibly select the board in slot 1, and check the multi-hop link whose local IP address is 2001:db8:1::2 and peer IP address is 2001:db8::1.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address 2001:db8:1::2 127
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] bfd selectboard bind peer-ipv6 2001:db8:1::1 source-ipv6 2001:db8:1::2 select-board 1 auto

```