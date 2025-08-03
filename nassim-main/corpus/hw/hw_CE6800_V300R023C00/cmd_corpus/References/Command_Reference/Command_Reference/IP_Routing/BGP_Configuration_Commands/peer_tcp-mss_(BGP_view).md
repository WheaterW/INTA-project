peer tcp-mss (BGP view)
=======================

peer tcp-mss (BGP view)

Function
--------



The **peer tcp-mss** command configures a TCP MSS value used when the local device establishes TCP connections with a peer.

The **undo peer tcp-mss** command deletes the configured TCP MSS value.



By default, no TCP MSS is configured for the local device to establish TCP connections with a peer.


Format
------

**peer** *ipv4-address* **tcp-mss** *tcp-mss-number*

**undo peer** *ipv4-address* **tcp-mss**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *tcp-mss-number* | Specifies the TCP MSS value used for TCP connection establishment. | The value is an integer ranging from 176 to 4096, in bytes. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **peer tcp-mss** command to configure a TCP MSS value used during TCP connection establishment with the specified peer. The value ranges from 176 to 4096 and is used to fragment TCP packets when the path MTU is unavailable. Such configuration improves network performance.

**Precautions**

If you change the tcp-mss-number value, the TCP connection will be re-established.If both the peer tcp-mss and peer path-mtu auto-discovery commands are run, note the following rules:

* If the local device obtains the path MTU, the smaller value of TCP MSS and path MTU takes effect.
* If the local device fails to obtain the path MTU, TCP MSS takes effect.


Example
-------

# Configure a TCP MSS value for the local device to establish TCP connections with the peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] peer 10.1.1.1 tcp-mss 200

```