peer log-change (BGP view)
==========================

peer log-change (BGP view)

Function
--------



The **peer log-change** command enables a BGP device to log the session status and events of a specified peer or a peer.

The **undo peer log-change** command cancels the configuration.



By default, a BGP device is enabled to log the session status and events of a specified peer.


Format
------

**peer** *ipv4-address* **log-change**

**undo peer** *ipv4-address* **log-change**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The **peer log-change** command can be used to enable a device to log the session status and events of a specified peer, facilitating service management.


Example
-------

# Configure a BGP device to log the session status and events of peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 200
[*HUAWEI-bgp] peer 10.1.1.1 log-change

```