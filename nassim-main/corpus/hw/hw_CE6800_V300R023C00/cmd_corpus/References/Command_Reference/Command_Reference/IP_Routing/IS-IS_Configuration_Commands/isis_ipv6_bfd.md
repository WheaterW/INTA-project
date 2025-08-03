isis ipv6 bfd
=============

isis ipv6 bfd

Function
--------



The **isis ipv6 bfd** command configures IPv6 BFD parameters on an interface.

The **undo isis ipv6 bfd** command restores default IPv6 BFD parameters on an interface.



By default, the minimum interval at which IPv6 BFD packets are sent or received is 1000, in milliseconds; the IPv6 BFD local detection multiplier is 3.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**isis ipv6 bfd** { **min-tx-interval** *transmit-interval* | **min-rx-interval** *receive-interval* | **detect-multiplier** *multiplier-value* | **frr-binding** } \*

**undo isis ipv6 bfd** { **min-tx-interval** [ *transmit-interval* ] | **min-rx-interval** [ *receive-interval* ] | **detect-multiplier** [ *multiplier-value* ] | **frr-binding** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **min-tx-interval** *transmit-interval* | Specifies the minimum interval at which IPv6 BFD packets are sent to the peer end. | The value is an integer that ranges from 50 to 1000, in milliseconds. The default value is 1000 milliseconds. |
| **min-rx-interval** *receive-interval* | Specifies the minimum interval at which IPv6 BFD packets are received from the peer end. | The value is an integer ranging from 3 to 1000, in milliseconds. The default value is 1000. |
| **detect-multiplier** *multiplier-value* | Specifies the IPv6 BFD local detection multiplier. | The value ranges from 3 to 50. The default value is 3. |
| **frr-binding** | Binds the status of the IPv6 BFD session to IPv6 IS-IS Auto FRR. If IPv6 BFD detects a link fault on the interface, the IPv6 BFD session goes Down, triggering FRR on the interface. Then, traffic is switched from the faulty link to the backup link. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BFD can provide millisecond-level fault detection, help IS-IS to detect the faults that occur on neighboring devices or links more quickly, and instruct IS-IS to recalculate routes for correct packet forwarding. The isis ipv6 bfd command can be used to set values for BFD session parameters on a specified interface.

**Prerequisites**

BFD has been enabled globally, and run the **isis ipv6 bfd enable** command has been run on a specified interface.

**Configuration Impact**

The minimum interval at which IPv6 BFD packets are received is obtained after the receive-interval value and the remote transmit-interval value are compared. If the local end does not receive any BFD packet from its neighbor within the period (minimum interval at which IPv6 BFD packets are received x multiplier-value), the local end declares the neighbor Down.

**Precautions**

The priority of BFD configured on an interface is higher than that of BFD configured in a process. If BFD is enabled on an interface, BFD sessions are established with the BFD parameters set on the interface.The set IPv6 BFD session parameters take effect only when IPv6 BFD is enabled on the interface.


Example
-------

# Enable IPv6 BFD for IS-IS on 100GE1/0/1, and set the minimum interval at which IPv6 BFD packets are received to 400 ms and the local detection multiplier to 4.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] isis ipv6 enable 1
[*HUAWEI-100GE1/0/1] isis ipv6 bfd enable
[*HUAWEI-100GE1/0/1] isis ipv6 bfd min-rx-interval 400 detect-multiplier 4

```