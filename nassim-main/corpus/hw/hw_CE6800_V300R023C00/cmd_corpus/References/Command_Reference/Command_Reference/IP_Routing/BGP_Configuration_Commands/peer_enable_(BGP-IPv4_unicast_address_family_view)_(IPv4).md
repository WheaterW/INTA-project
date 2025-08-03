peer enable (BGP-IPv4 unicast address family view) (IPv4)
=========================================================

peer enable (BGP-IPv4 unicast address family view) (IPv4)

Function
--------



The **peer enable** command enables a BGP device to exchange routes with a specified peer group in the address family view.

The **undo peer enable** command disables a BGP device from exchanging routes with a specified peer group.



By default, route exchange with a specified peer is enabled only in the BGP-IPv4 unicast address family.


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

BGP-IPv4 unicast address family view


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

If a peer has established a peer relationship in another address family when you run this command, running the **peer enable** command may disconnect and re-establish the peer relationship in all other address families of the peer (using the same address), causing route flapping. Therefore, exercise caution when running this command.


Example
-------

# Enable the device to exchange routing information with a specified peer in the address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer 10.1.1.1 enable

```