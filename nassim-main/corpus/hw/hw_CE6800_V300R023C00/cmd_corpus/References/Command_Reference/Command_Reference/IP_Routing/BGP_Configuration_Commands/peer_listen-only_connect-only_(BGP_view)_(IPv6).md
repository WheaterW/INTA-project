peer listen-only connect-only (BGP view) (IPv6)
===============================================

peer listen-only connect-only (BGP view) (IPv6)

Function
--------



The **peer listen-only** command enables a peer to listen to connection requests but not to send connection requests.

The **undo peer listen-only** command restores the default setting.

The **peer connect-only** command enables a peer to send connection requests but not to accept connection requests.

The **undo peer connect-only** command restores the default setting.



By default, a peer listens to and accepts connection requests, and sends connection requests.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* { **listen-only** | **connect-only** }

**undo peer** *ipv6-address* { **listen-only** | **connect-only** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



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
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 200
[*HUAWEI-bgp] peer 2001:DB8:1::1 connect-only

```