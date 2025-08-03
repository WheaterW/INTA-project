ipv6 nd nud attempts
====================

ipv6 nd nud attempts

Function
--------



The **ipv6 nd nud attempts** command sets the number of probe retransmissions for ND entries in the PROBE state.

The **undo ipv6 nd nud attempts** command restores the default configuration.



By default, the number of probe retransmissions for ND entries in the PROBE state is 3.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd nud attempts** *attempts*

**undo ipv6 nd nud attempts**

**undo ipv6 nd nud attempts** *attempts*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *attempts* | Specifies the number of probe retransmissions for ND entries in the PROBE state. | The value is an integer ranging from 1 to 10. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If an ND entry is in the PROBE state, the neighbor is no longer known to be reachable. The device sends unicast NS messages to detect the validity of the ND entry. If a response is received from the neighbor, the ND entry enters the REACH state, indicating that the neighbor is known to have been reachable. If no response is received from the neighbor, the ND entry is deleted.You are advised to run the **ipv6 nd nud attempts** command to set the number of probe retransmissions for ND entries in the PROBE state to a larger value in the following situations:

* The link reliability on the network is poor, and packet loss may occur during packet transmission.
* The peer device is busy processing services and cannot process NS messages in time.This prevents ND entries from being mistakenly deleted, hence negatively affecting packet forwarding efficiency if no response is received from the neighbor within the specified period (calculated as Default number of probe retransmissions x Default interval of probe retransmissions).

**Prerequisites**

IPv6 has been enabled using the **ipv6 enable** command.


Example
-------

# Set the number of probe retransmissions for ND entries in the PROBE state on 100GE 1/0/1 to 5.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd nud attempts 5

```