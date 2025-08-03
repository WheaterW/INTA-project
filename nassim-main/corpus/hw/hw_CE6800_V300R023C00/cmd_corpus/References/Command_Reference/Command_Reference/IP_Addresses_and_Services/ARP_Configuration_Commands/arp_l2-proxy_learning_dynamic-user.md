arp l2-proxy learning dynamic-user
==================================

arp l2-proxy learning dynamic-user

Function
--------



The **arp l2-proxy learning dynamic-user disable** command disables ARP snooping entry learning on an interface.

The **undo arp l2-proxy learning dynamic-user disable** command enables ARP snooping entry learning on an interface.

The **arp l2-proxy learning dynamic-user max-user** command configures the maximum number of ARP snooping entries that an interface can learn.

The **undo arp l2-proxy learning dynamic-user max-user** command restores the default configuration.



By default, ARP snooping entry learning is enabled. The default maximum number of ARP snooping entries that an interface can learn is set to 0, indicating that the maximum number of ARP snooping entries is not limited.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**arp l2-proxy learning dynamic-user disable**

**arp l2-proxy learning dynamic-user max-user** *max-user-number*

**undo arp l2-proxy learning dynamic-user disable**

**undo arp l2-proxy learning dynamic-user max-user** [ *max-user-number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **max-user** *max-user-number* | Specifies the maximum number of ARP snooping entries that an interface can learn.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 0 to 131072. |



Views
-----

100GE Layer 2 sub-interface view,200GE Layer 2 sub-interface view,400GE Layer 2 sub-interface view,50GE Layer 2 sub-interface view,Eth-Trunk Layer 2 sub-interface view,Layer 2 sub-interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After receiving an ARP request packet, a device broadcasts the packet in its broadcast domain (BD). If a device receives a large number of ARP request packets within a period and broadcasts the packets, many network resources are consumed, causing network congestion. As a result, network performance deteriorates and user services are affected. Layer 2 proxy ARP can relieve the pressure on processing ARP packets by isolating ARP BDs. With this function enabled, a device preferentially uses learned ARP snooping entries to respond to received ARP request packets.When Layer 2 proxy ARP is enabled on a device, ARP snooping is automatically enabled. The device then creates ARP snooping entries by snooping ARP packets. The entries record senders' information. When most users obtain IP addresses through DHCP, attackers may frequently send bogus ARP packets to attack ARP snooping entries, causing Layer 2 proxy ARP failures. To prevent the preceding issue, run the **arp l2-proxy learning dynamic-user disable** command to disable ARP snooping entry learning on an interface, or run the arp l2-proxy learning dynamic-user max-use command to configure the maximum number of ARP snooping entries that an interface can learn.



**Prerequisites**

1. A Layer 2 sub-interface has been added to a BD.
2. Layer 2 proxy ARP has been enabled using the **arp l2-proxy enable** command in the BD view.


Example
-------

# Disable ARP snooping entry learning on 100GE 1/0/1.1.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[~HUAWEI-bd10] arp l2-proxy enable
[*HUAWEI] quit
[~HUAWEI] interface 100GE1/0/1.1 mode l2
[~HUAWEI-100GE1/0/1.1] encapsulation dot1q vid 100
[~HUAWEI-100GE1/0/1.1] bridge-domain 10
[~HUAWEI-100GE1/0/1.1] arp l2-proxy learning dynamic-user disable

```

# Set the maximum number of ARP snooping entries that 100GE 1/0/1.1 can learn to 50.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[~HUAWEI-bd10] arp l2-proxy enable
[*HUAWEI] quit
[~HUAWEI] interface 100GE1/0/1.1 mode l2
[~HUAWEI-100GE1/0/1.1] encapsulation dot1q vid 100
[~HUAWEI-100GE1/0/1.1] bridge-domain 10
[~HUAWEI-100GE1/0/1.1] arp l2-proxy learning dynamic-user max-user 50

```