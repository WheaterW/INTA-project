peer listen-only connect-only (BGP view)(IPv4)
==============================================

peer listen-only connect-only (BGP view)(IPv4)

Function
--------



The **peer listen-only** command configures a peer to only listen to connection requests and not to proactively send connection requests.

The **undo peer listen-only** command cancels the function.

The **peer connect-only** command configures a peer to send connection requests but reject connection requests.

The **undo peer connect-only** command restores the default setting.



By default, a peer listens to and accepts connection requests, and sends connection requests.


Format
------

**peer** *ipv4-address* { **listen-only** | **connect-only** }

**undo peer** *ipv4-address* { **listen-only** | **connect-only** }


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

**Usage Scenario**

To enable a peer to listen to connection requests but not to send connection requests, run the **peer listen-only** command.To enable a peer to send connection requests but not to accept connection requests, run the **peer connect-only** command.

**Configuration Impact**

If the peer listen-only and **peer connect-only** commands are both run, the latest configuration overrides the previous one.

**Precautions**

The **peer connect-only** command or the **peer listen-only** command cannot be run on both devices that are peers of each other. Otherwise, the peer relationship cannot be established.


Example
-------

# Enable peer to send connection requests but rejects connection requests.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 200
[*HUAWEI-bgp] peer 10.1.1.1 connect-only

```