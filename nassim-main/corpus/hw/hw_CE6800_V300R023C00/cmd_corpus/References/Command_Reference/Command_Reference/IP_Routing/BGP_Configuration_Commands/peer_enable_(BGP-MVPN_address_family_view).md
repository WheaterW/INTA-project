peer enable (BGP-MVPN address family view)
==========================================

peer enable (BGP-MVPN address family view)

Function
--------



The **peer enable** command enables a device to exchange routes with a specified peer in the address family view.

The **undo peer enable** command disables a device from exchanging routes with a specified peer.



By default, a device is disabled from exchanging routing information with a specified peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv4-address* **enable**

**undo peer** *ipv4-address* **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |



Views
-----

BGP-MVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, only peer groups in the BGP-IPv4 unicast address family are automatically enabled to exchange routing information. In other words, after the **peer as-number** command is run in the BGP view, the system automatically configures the **peer enable** command. In other address family views, however, this function must be manually enabled.

**Configuration Impact**

Enabling or disabling a BGP peer in this address family causes the BGP connection with the peer in another address family to be disconnected and automatically renegotiated.

**Precautions**

If a peer has established a peer relationship in another address family, running the **peer enable** command may disconnect and re-establish all peer relationships with the peer, causing route flapping. Therefore, exercise caution when running this command.


Example
-------

# Enable the device to exchange routing information with a specified peer in the BGP MVPN address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.2 as-number 200
[*HUAWEI-bgp] ipv4-family mvpn
[*HUAWEI-bgp-af-mvpn] peer 10.1.1.2 enable

```