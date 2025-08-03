ipv6 nd stale-timeout (System view)
===================================

ipv6 nd stale-timeout (System view)

Function
--------



The **ipv6 nd stale-timeout** command sets the timeout period of the STALE state of ND entries.

The **undo ipv6 nd stale-timeout** command restores the default setting.



By default, the timeout period of the STALE state of ND entries is 1200 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd stale-timeout** *seconds*

**undo ipv6 nd stale-timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *seconds* | Specifies the timeout period of the STALE state of ND entries. | The value is an integer that ranges from 60 to 172800, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The STALE state of an ND entry indicates that whether the neighbor is reachable is unknown. Probing whether the neighbor is reachable is not performed unless there is a packet to be sent to this neighbor.The timeout period of the STALE state of ND entries is a variable. If you want to quickly clear invalid ND entries, you can set the timeout period to a smaller value through the **ipv6 nd stale-timeout** command to speed up entry aging.

**Prerequisites**

The IPv6 function has been enabled on the interface using the **ipv6 enable** command in the interface view.

**Configuration Impact**

After the **ipv6 nd stale-timeout** command is run, the status of ND entries can be updated after the timeout period of the STALE state of ND entries expires.

**Precautions**

The system probes the validity of ND entries again after the timeout period of the STALE state of ND entries expires. If the neighbor is reachable, the ND entry status changes to REACHABLE; otherwise, the ND entry is deleted.An ND entry contains information about the IPv6 address of the neighbor, link-layer address of the neighbor, status of the ND entry, interface name of the ND entry, time when the ND entry is created, VLAN ID of the ND entry, and VPN name of the neighbor. For detailed explanation, see the description of the output of the **display ipv6 neighbors** command.


Example
-------

# Set the timeout period of the STALE state of ND entries to 2400 seconds for the entire device.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd stale-timeout 2400

```