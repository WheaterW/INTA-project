bfd bind peer-ip (System view)
==============================

bfd bind peer-ip (System view)

Function
--------



The **bfd bind peer-ip** command creates a BFD session, specifies the peer IP address, and displays the BFD session view.

The **bfd bind peer-ip source-ip auto** command creates a static BFD session with automatically negotiated discriminators.



By default, no binding between a BFD session and a peer IP address is created.


Format
------

**bfd** *session-name* **bind** **peer-ip** *peer-ip* [ **vpn-instance** *vpn-name* ] [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ [ **source-ip** *source-ip* ] [ **select-board** *slot-id1* [ *slot-id2* ] ] | [ **select-board** *slot-id1* [ *slot-id2* ] ] [ **source-ip** *source-ip* ] ]

**bfd** *session-name* **bind** **peer-ip** *peer-ip* [ **vpn-instance** *vpn-name* ] [ **interface** { *interface-name* | *interface-type* *interface-number* } ] { **source-ip** *source-ip* [ **select-board** *slot-id1* [ *slot-id2* ] ] | [ **select-board** *slot-id1* [ *slot-id2* ] ] **source-ip** *source-ip* } **auto**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *session-name* | Specifies·the·name·of·a·BFD·session. | The value is a string of 1 to 64 case-insensitive characters without spaces. |
| **peer-ip** *peer-ip* | Specifies the peer IP address bound to a BFD session. | The value is in dotted decimal notation. |
| **vpn-instance** *vpn-name* | Specifies the name of a VPN instance bound to a BFD session. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **interface** *interface-type* *interface-number* | Specifies the local Layer 3 interface to which a BFD session is bound. | - |
| **interface** *interface-name* | Specifies the local Layer 3 interface to which a BFD session is bound. | - |
| **source-ip** *source-ip* | Specifies the source IPv4 address carried in BFD packets.  If this parameter is not specified, the system searches the local routing table for the IP address of an outbound interface connected to the remote end and uses the IP address as the source IP address before sending BFD packets. This parameter usually does not need to be specified. | The value is in dotted decimal notation. |
| **select-board** *slot-id1* | Specifies the board that a BFD session state machine forcibly selects.  If both slot-id1 and slot-id2 are specified, only one board is selected. The board specified by slot-id1 is preferentially selected. If this board fails to be selected, the board specified by slot-id2 is then selected. If both the boards fail to be selected, the BFD session state machine no longer selects boards. Forcible board selection is not supported by the BFD session bound to a physical interface.   * slot-id1: specifies the slot ID of a board. * slot-id2: specifies the slot ID of another board. | The value is a string of 1 to 19 case-sensitive characters, spaces not supported. |
| *slot-id2* | Specifies the board that a BFD session state machine forcibly selects.  If both slot-id1 and slot-id2 are specified, only one board is selected. The board specified by slot-id1 is preferentially selected. If this board fails to be selected, the board specified by slot-id2 is then selected. If both the boards fail to be selected, the BFD session state machine no longer selects boards. Forcible board selection is not supported by the BFD session bound to a physical interface.   * slot-id1: specifies the slot ID of a board. * slot-id2: specifies the slot ID of another board. | The value is a string of 1 to 19 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To rapidly detect link faults on a network, create a BFD session.When creating the binding between a BFD session and a peer IP address:

* If only the peer IP address is specified, BFD detects faults in a multi-hop link.
* If both the peer IP address and local interface are specified, BFD detects faults in a single-hop link. That is, BFD monitors a fixed route whose outbound interface is this interface and the next-hop address is the peer IP address.
* If both the peer IP address and the VPN instance are specified, BFD detects faults in the multi-hop link for a specified VPN instance.
* If the peer IP address, the VPN instance, and the local interface are specified, BFD detects faults in the single-hop link for a specified VPN instance.A BFD session is established to rapidly detect faults in links on a network. A device needs to establish a BFD session with a remote device on which a dynamic BFD session is established to detect faults in static routes. In this case, the **bfd bind peer-ip source-ip auto** command is used to create a BFD session with automatically negotiated discriminators.When creating a static BFD session with automatically negotiated discriminators:
* If only the peer IP address is specified, BFD detects faults in a multi-hop link.
* If both the peer IP address and local interface are specified, BFD detects faults in a single-hop link. That is, BFD monitors a fixed route whose outbound interface is this interface and the next-hop address is the peer IP address.
* If the source IP address is specified for the interface whose physical status is to be monitored by BFD, BFD packets are correctly forwarded after URPF has been enabled. The source-ip parameter must be configured correctly because the system checks only the validity of the source IP address. A multicast or broadcast address is an invalid source IP address.
* If both the peer IP address and the VPN instance are specified, BFD detects faults in the multi-hop link for a specified VPN instance.
* If the peer IP address, the VPN instance, and the local interface are specified, BFD detects faults in the single-hop link for a specified VPN instance.One-arm BFD echo is used when two devices are directly connected and only one of them supports BFD. A one-arm BFD echo session can be established on the device that supports BFD. After receiving a one-arm BFD echo session packet, the device that does not support BFD immediately loops back the packet, implementing quick link failure detection.When a one-arm BFD echo session is created:
* If the source IP address is specified and URPF is enabled, BFD packets can be correctly forwarded. The source IP address must be configured correctly because the system checks only the validity of the source IP address format. A multicast or broadcast address is invalid.
* If a VPN instance is specified, a single-hop link for VPN routes is monitored.
* If the source IP address is specified, the device searches the routing table for the outbound interface address based on the value of peer-ip, and uses the address as the destination address in BFD packets. The device uses the value of source-ip as the source address.
* If no source address is specified, the device searches the routing table for the outbound interface address based on the value of peer-ip, and uses the address as the source and destination addresses in BFD packets.

**Prerequisites**

BFD has been globally enabled using the **bfd** command in the system view.

**Configuration Impact**



You can run the **bfd bind peer-ip** command to create the binding between a static BFD session and a peer IP address.



**Follow-up Procedure**

Run the **discriminator** command to create local and remote discriminators for the BFD session.


Example
-------

# Create a BFD session named session so that BFD can detect faults in the multi-hop link to the IP address 10.10.20.2.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd session bind peer-ip 10.10.20.2
[*HUAWEI-bfd-session-session]

```

# Create a static BFD session with automatically negotiated discriminators.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.1.1.1 24
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] bfd atob bind peer-ip 10.1.1.2 interface 100GE 1/0/1 source-ip 10.1.1.1 auto

```

# Create a BFD session named atob so that BFD can detect faults in the single-hop link from the local interface to the peer interface whose IP address is 10.2.2.1.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] ip address 10.2.2.2 24
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] bfd atob bind peer-ip 10.2.2.1 interface 100GE 1/0/1
[*HUAWEI-bfd-session-atob]

```