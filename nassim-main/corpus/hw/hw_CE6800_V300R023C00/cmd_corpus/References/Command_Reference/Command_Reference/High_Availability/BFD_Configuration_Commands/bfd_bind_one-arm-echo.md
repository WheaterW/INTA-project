bfd bind one-arm-echo
=====================

bfd bind one-arm-echo

Function
--------



The **bfd bind one-arm-echo** command creates a one-arm BFD echo session.



By default, no one-arm BFD echo session is created.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**bfd** *sessname-value* **bind** **peer-ip** *ip-address* [ **vpn-instance** *vpn-name* ] **interface** { *interface-name* | *interface-type* *interface-number* } **source-ip** *ip-address* **per-link** **one-arm-echo**

**bfd** *sessname-value* **bind** **peer-ip** *ip-address* [ **vpn-instance** *vpn-name* ] **interface** { *interface-name* | *interface-type* *interface-number* } [ **source-ip** *ip-address* ] **one-arm-echo**

**bfd** *sessname-value* **bind** **peer-ip** *ip-address* [ **vpn-instance** *vpn-name* ] **interface** { *interface-name* | *interface-type* *interface-number* } [ **source-ip** *ip-address* ] **one-arm-echo** **destination-ip** *ip-address*

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**bfd** *sessname-value* **bind** **peer-ipv6** *ipv6-address* [ **vpn-instance** *vpn-name* ] **interface** { *interface-name* | *interface-type* *interface-number* } [ **source-ipv6** *source-ipv6* ] **one-arm-echo**

**bfd** *sessname-value* **bind** **peer-ipv6** *ipv6-address* [ **vpn-instance** *vpn-name* ] **interface** { *interface-name* | *interface-type* *interface-number* } [ **source-ipv6** *source-ipv6* ] **one-arm-echo** **destination-ipv6** *destination-ipv6-value*

**bfd** *sessname-value* **bind** **peer-ipv6** *ipv6-address* [ **vpn-instance** *vpn-name* ] **interface** { *interface-name* | *interface-type* *interface-number* } **source-ipv6** *source-ipv6* **per-link** **one-arm-echo**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *sessname-value* | Specifies the name of a one-arm BFD echo session. | The value is a string of 1 to 64 case-insensitive characters without spaces. |
| **peer-ip** *ip-address* | Specifies the peer IPv4 address bound to a one-arm BFD echo session. | The value is in dotted decimal notation. |
| **interface** *interface-type* *interface-number* | Specifies the type and number of the local Layer 3 interface bound to a one-arm BFD echo session. | - |
| **source-ip** *ip-address* | Specifies the source IPv4 address carried in BFD packets. If this parameter is not specified, the system searches the local routing table for the IP address of an outbound interface connected to the remote end and uses the IP address as the source IP address before sending BFD packets. This parameter usually does not need to be specified. | The value is in dotted decimal notation. |
| **one-arm-echo** | Indicates a one-arm BFD echo session. | - |
| **peer-ipv6** *ipv6-address* | Specifies the peer IPv6 address bound to a BFD for IPv6 session.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **source-ipv6** *source-ipv6* | Specifies the source IPv6 address carried in a BFD packet. If the source IPv6 address is not specified, the system searches the local routing table for an outbound interface to the peer IP address and uses the IPv6 address of this outbound interface as the source IPv6 address for sending BFD packets.  Generally, you do not need to set this parameter. When BFD is used with Unicast Reverse Path Forwarding (URPF), you must manually configure the source IPv6 address in BFD packets because URPF checks the source IPv6 address in received packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **vpn-instance** *vpn-name* | Specifies the name of the VPN instance bound to a one-arm BFD echo session. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **per-link** | Establishes a BFD session to monitor the link between member interfaces. | - |
| **destination-ip** *ip-address* | Specifies the destination IPv4 address of BFD packets. | The value is in dotted decimal notation. |
| **destination-ipv6** *destination-ipv6-value* | Specifies the destination IPv6 address of BFD packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

One-arm BFD echo is used when two devices are directly connected and only one of them supports BFD. A one-arm BFD echo session can be established on the device that supports BFD. After receiving a one-arm BFD echo session packet, the device that does not support BFD immediately loops back the packet, implementing quick link failure detection.When a one-arm BFD echo session is created:

* If the source IP address is specified and URPF is enabled, BFD packets can be correctly forwarded. The source IP address must be configured correctly because the system checks only the validity of the source IP address format. A multicast or broadcast address is invalid.
* If a VPN instance is specified, a single-hop link for VPN routes is monitored.
* If the source IP address is specified, the device searches the routing table for the outbound interface address based on the value of peer-ip, and uses the address as the destination address in BFD packets. The device uses the value of source-ip as the source address.
* If no source address is specified, the device searches the routing table for the outbound interface address based on the value of peer-ip, and uses the address as the source and destination addresses in BFD packets.

**Prerequisites**



BFD has been globally enabled using the **bfd** command in the system view.



**Precautions**

The differences between a one-arm BFD echo session and a common BFD session are as follows:

* When creating a one-arm BFD echo session, you need to specify only the local discr-value parameter in the **discriminator** command.
* You can only run the **min-echo-rx-interval** command to change the minimum interval at which one-arm BFD echo session packets are received.After a one-arm BFD echo session is created, changing the IP address of the outbound interface for BFD packets does not change the source IP address carried in the BFD packets.One-arm BFD echo sessions can apply only to single-hop detection.The **undo bfd session-name** command deletes a specified BFD session and its binding information.


Example
-------

# Create a one-arm BFD echo session named test.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] ip address 10.1.10.1 24
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] bfd test bind peer-ip 10.1.10.2 interface 100GE 1/0/1 one-arm-echo

```