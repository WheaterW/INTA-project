ipv6 nd neighbor-incomplete expire-time
=======================================

ipv6 nd neighbor-incomplete expire-time

Function
--------



The **ipv6 nd neighbor-incomplete expire-time** command sets the aging time of ND entries in Incomplete state.

The **undo ipv6 nd neighbor-incomplete expire-time** command restores the default aging time of ND entries in Incomplete state.



By default, the aging time of ND entries in Incomplete state is 300 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd neighbor-incomplete expire-time** *expire-time-value*

**undo ipv6 nd neighbor-incomplete expire-time** *expire-time-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *expire-time-value* | Specifies the aging time of ND entries in Incomplete state. | The value is an integer ranging from 1 to 36000 in seconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, ND probe is performed for ND entries in the Incomplete state. The status of an ND entry changes to Reachable when a neighbor is reachable. The local device ages out an ND entry after failing to receive a response to a probe packet from the peer device within a specified number of probes. If the rate at which NS messages are sent is limited, ND entries in the Incomplete state cannot be effectively probed for a long time, occupying entry resources. To speed up entry aging and release entry resources, configure a short aging time for ND entries in the Incomplete state.

**Prerequisites**

Before running the **ipv6 nd neighbor-incomplete expire-time** command to set the aging time of ND entries in Incomplete state, you need to run the **ipv6 enable** command in the interface view to enable the IPv6 function on the interface.

**Precautions**

The **ipv6 nd neighbor-incomplete expire-time** command does not take effect for remote entries.


Example
-------

# Set the aging time of ND entries in Incomplete state to 200s on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd neighbor-incomplete expire-time 200

```