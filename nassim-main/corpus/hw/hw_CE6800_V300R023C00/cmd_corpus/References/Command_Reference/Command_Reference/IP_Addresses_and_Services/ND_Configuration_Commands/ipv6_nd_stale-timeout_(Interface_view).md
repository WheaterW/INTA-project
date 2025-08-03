ipv6 nd stale-timeout (Interface view)
======================================

ipv6 nd stale-timeout (Interface view)

Function
--------



The **ipv6 nd stale-timeout** command sets the timeout period of the STALE state of ND entries.

The **undo ipv6 nd stale-timeout** command restores the default setting.



By default, the stale state aging time of ND entries is the same as that configured in the system view.

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

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The STALE state of an ND entry indicates that whether the neighbor is reachable is unknown. Probing whether the neighbor is reachable is not performed unless there is a packet to be sent to this neighbor.The timeout period of the STALE state of ND entries is a variable. If you want to quickly clear invalid ND entries, you can set the timeout period to a smaller value through the **ipv6 nd stale-timeout** command to speed up entry aging.

**Prerequisites**

After the **ipv6 nd stale-timeout** command is run, the status of ND entries can be updated after the timeout period of the STALE state of ND entries expires.

**Configuration Impact**

After the **ipv6 nd stale-timeout** command is run, the status of ND entries can be updated after the timeout period of the STALE state of ND entries expires.

**Precautions**

The system probes the validity of ND entries again after the timeout period of the STALE state of ND entries expires. If the neighbor is reachable, the ND entry status changes to REACHABLE; otherwise, the ND entry is deleted.An ND entry contains information about the IPv6 address of the neighbor, link-layer address of the neighbor, status of the ND entry, interface name of the ND entry, time when the ND entry is created, VLAN ID of the ND entry, and VPN name of the neighbor. For detailed explanation, see the description of the output of the **display ipv6 neighbors** command.


Example
-------

# Set the timeout period of the STALE state of ND entries to 3600 seconds on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd stale-timeout 3600

```