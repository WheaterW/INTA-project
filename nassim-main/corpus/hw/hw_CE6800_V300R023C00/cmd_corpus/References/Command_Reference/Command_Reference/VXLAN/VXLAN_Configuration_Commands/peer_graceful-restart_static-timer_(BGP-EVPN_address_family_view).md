peer graceful-restart static-timer (BGP-EVPN address family view)
=================================================================

peer graceful-restart static-timer (BGP-EVPN address family view)

Function
--------



The **peer graceful-restart static-timer** command sets the maximum duration from the time the local device finds that the peer device is restarted to the time a BGP EVPN session is re-established.

The **undo peer graceful-restart static-timer** command deletes the configuration.



By default, the maximum duration from the time the local device finds that the peer device is restarted to the time a BGP EVPN session is re-established is 150s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv4-address* **graceful-restart** **static-timer** *restart-time*

**undo peer** *ipv4-address* **graceful-restart** **static-timer** *restart-time*

**undo peer** *ipv4-address* **graceful-restart** **static-timer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |
| *restart-time* | Specifies the maximum duration from the time the local device finds that the peer device is restarted to the time a BGP EVPN session is re-established. | The value is an integer ranging from 3600 to 2147483647, in seconds. |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, the maximum duration from the time the local device finds that the peer device is restarted to the time a BGP EVPN session is re-established is 150s. Even if you run the **graceful-restart timer restart time** command in the BGP view, the maximum wait time can be changed to 3600s at most. If some BGP EVPN sessions take more than 3600s to re-establish due to poor network conditions, you can run the **peer graceful-restart static-timer** command to set a proper wait time for a specified peer.

**Configuration Impact**

If the **graceful-restart timer restart** command is run in the BGP view and the **peer graceful-restart static-timer** command is run in any of its views, the latter command takes precedence over the former command.

**Precautions**

GR has been enabled using the **graceful-restart** command.


Example
-------

# Set the maximum duration from the time the local device finds that the peer device is restarted to the time a BGP EVPN session is re-established to 5000s.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] graceful-restart
[*HUAWEI-bgp] peer 1.1.1.1 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 1.1.1.1 enable
[*HUAWEI-bgp-af-evpn] peer 1.1.1.1 graceful-restart static-timer 5000

```