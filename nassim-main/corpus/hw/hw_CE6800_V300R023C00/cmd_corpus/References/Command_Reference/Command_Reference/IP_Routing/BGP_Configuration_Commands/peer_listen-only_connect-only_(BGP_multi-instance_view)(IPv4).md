peer listen-only connect-only (BGP multi-instance view)(IPv4)
=============================================================

peer listen-only connect-only (BGP multi-instance view)(IPv4)

Function
--------



The **peer listen-only** command enables a peer group to listen to connection requests but not to send connection requests.

The **undo peer listen-only** command restores the default setting.

The **peer connect-only** command enables a peer group to send connection requests but not to accept connection requests.

The **undo peer connect-only** command restores the default setting.



By default, a peer listens to and accepts connection requests, and sends connection requests.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } { **listen-only** | **connect-only** }

**undo peer** { *ipv4-address* | *ipv6-address* } { **listen-only** | **connect-only** }

For CE6885-LL (low latency mode):

**peer** *ipv4-address* { **listen-only** | **connect-only** }

**undo peer** *ipv4-address* { **listen-only** | **connect-only** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **peer** *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

BGP multi-instance view


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
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-a] peer 10.1.1.1 connect-only

```