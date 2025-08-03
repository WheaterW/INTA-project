c-bsr
=====

c-bsr

Function
--------



The **c-bsr** command configures a Candidate-BootStrap Router (C-BSR).

The **undo c-bsr** command deletes a configured C-BSR.



By default, no C-BSR is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**c-bsr** *ipv6-address* [ *hash-length* [ *priority-value* ] ]

**undo c-bsr**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 global unicast address of a C-BSR. IPv6 PIM-SM must be enabled on the interface assigned an IPv6 address before other multicast configurations are performed on it.  To avoid frequent protocol changes caused by interface flapping, use the loopback interface address as the global IPv6 unicast address of the C-BSR. | The address is in the format of X:X:X:X:X:X:X:X. |
| *hash-length* | Specifies the hash mask length of a C-BSR. The hash mask length is used by the hash function to calculate an RP. | The value is an integer ranging from 0 to 128. |
| *priority-value* | Specifies the priority value of a C-BSR. | The value is an integer ranging from 0 to 255. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On a PIM-SM network, the BSR mechanism is used to dynamically elect a Rendezvous Point (RP). The BSR collects Candidate-Rendezvous Point (C-RP) information to form an RP-set, and then advertises the RP-set to the entire network. Based on the RP-set, all Routers in the network can calculate out the RP to which a specific multicast group corresponds. The BSR and other devices in the PIM-SM domain need to exchange a great deal of information and thus lots of bandwidth should be reserved between the C-BSR and other devices in the PIM-SM domain.One Router can function as both a C-RP and a C-BSR. One Router can be configured with multiple instances. Each instance can be configured with a maximum of one C-BSR. If the **c-bsr** command is run repeatedly in an instance, only the latest configuration takes effect.One or more C-BSRs need to be configured in a PIM-SM domain. The C-BSRs automatically elect a BSR that is responsible for collecting and advertising RP information. C-BSRs must be Routers on the backbone network. When the Router is configured as a C-BSR, an interface enabled with PIM-SM needs to be specified.The process of electing a BSR from C-BSRs is as follows:

* At first, each C-BSR considers itself as the BSR of the PIM-SM domain, and uses the interface IP address specified by using the **c-bsr** command as the BSR address to send Bootstrap messages.
* When a C-BSR receives a Bootstrap message from another Router, it compares the BSR information in the received Bootstrap message with the acknowledged BSR information in terms of priorities and IP addresses. In this process, the BSR with the higher priority is preferred. In the case of the same priority, the BSR with the higher IP address is preferred. If the BSR carried in a received the Bootstrap message is better than the current BSR, the C-BSR replaces its BSR address with the address of the BSR carried in the received Bootstrap message. Otherwise, the C-BSR keeps its BSR address and continues to consider itself as the BSR.

Example
-------

# In the public network instance, assign an IPv6 address, 2001:db8:2::2, to a C-BSR.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] c-bsr 2001:db8:2::2

```