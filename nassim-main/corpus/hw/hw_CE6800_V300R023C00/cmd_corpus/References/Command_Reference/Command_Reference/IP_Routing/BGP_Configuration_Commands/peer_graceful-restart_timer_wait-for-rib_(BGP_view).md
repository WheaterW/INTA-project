peer graceful-restart timer wait-for-rib (BGP view)
===================================================

peer graceful-restart timer wait-for-rib (BGP view)

Function
--------



The **peer graceful-restart timer wait-for-rib** command sets the maximum duration for a BGP restarter to wait for the End-of-RIB flag from a specified peer.

The **undo peer graceful-restart timer wait-for-rib** command deletes the configured duration.



By default, a BGP restarter waits for the End-of-RIB flag from a specified peer for a maximum of 600s.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**peer** *ipv4-address* **graceful-restart** **timer** **wait-for-rib** *time-value*

**undo peer** *ipv4-address* **graceful-restart** **timer** **wait-for-rib**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** *ipv6-address* **graceful-restart** **timer** **wait-for-rib** *time-value*

**undo peer** *ipv6-address* **graceful-restart** **timer** **wait-for-rib**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *time-value* | Specifies the maximum duration for waiting for the End-Of-RIB flag. | The value is an integer ranging from 3 to 3000, in seconds. |
| *ipv6-address* | Specifies the IPv6 address of a peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the local device reestablishes a BGP session with a specified peer, the local device should receive the End-Of-RIB flag from the specified peer within the period specified by this command. If the local device does not receive the End-Of-RIB flag within the period specified by this command, the local device exits the GR process and selects the optimal route from the existing routes.

**Configuration Impact**

If the command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Set the maximum duration during which a BGP restarter waits for the End-of-RIB flag from a specified peer to 100s.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] peer 10.1.1.1 graceful-restart timer wait-for-rib 100

```