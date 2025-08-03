ipv6 bfd all-interfaces
=======================

ipv6 bfd all-interfaces

Function
--------



The **ipv6 bfd all-interfaces** command configures parameters for IPv6 BFD sessions.

The **undo ipv6 bfd all-interfaces** command restores the default values.



By default, the minimum interval at which IPv6 BFD packets are sent or received is 1000, in milliseconds; the IPv6 BFD local detection multiplier is 3.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 bfd all-interfaces** { **min-rx-interval** *receive-interval* | **min-tx-interval** *transmit-interval* | **detect-multiplier** *multiplier-value* | **frr-binding** } \*

**undo ipv6 bfd all-interfaces** { **min-rx-interval** [ *receive-interval* ] | **min-tx-interval** [ *transmit-interval* ] | **detect-multiplier** [ *multiplier-value* ] | **frr-binding** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **min-rx-interval** *receive-interval* | Specifies the minimum interval at which IPv6 BFD packets are received from the peer end. | The value is an integer ranging from 3 to 1000, in milliseconds. The default value is 1000. |
| **min-tx-interval** *transmit-interval* | Specifies the minimum interval at which IPv6 BFD packets are sent to the peer end. | The value is an integer ranging from 3 to 1000, in milliseconds. The default value is 1000. |
| **detect-multiplier** *multiplier-value* | Specifies the IPv6 BFD local detection multiplier. | The value ranges from 3 to 50. The default value is 3. |
| **frr-binding** | Associates IPv6 BFD session status with IPv6 IS-IS auto FRR. If IPv6 BFD detects a link fault on an interface, the IPv6 BFD session goes Down, triggering FRR. Traffic is then quickly switched to the backup link, minimizing service loss. | - |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BFD can provide millisecond-level fault detection, help IS-IS to detect the faults that occur on neighboring devices or links more quickly, and instruct IS-IS to recalculate routes for correct packet forwarding. The ipv6 bfd all-interfaces command can be used to configure parameters for IPv6 BFD sessions.

**Prerequisites**

BFD has been enabled globally, An IS-IS process has been created, the IS-IS process has been enabled on a specified interface, and IPv6 BFD has been enabled in the IS-IS process.

**Configuration Impact**

The minimum interval at which IPv6 BFD packets are received is obtained after the receive-interval value and the remote transmit-interval value are compared. If the local end does not receive any BFD packet from its neighbor within the period (minimum receiving interval x multiplier-value), the local end declares the neighbor Down.

**Precautions**

If only IPv6 BFD session parameters are configured but the **ipv6 bfd all-interfaces enable** command is not run, no IPv6 BFD sessions can be established.The priority of BFD configured on an interface is higher than that of BFD configured in a process. If IPv6 BFD is enabled on an interface, IPv6 BFD sessions are established with the BFD parameters set on the interface.


Example
-------

# Configure IPv6 BFD for an IS-IS process and specify the minimum interval at which IPv6 BFD packets are sent to 300 ms.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] ipv6 bfd all-interfaces enable
[*HUAWEI-isis-1] ipv6 bfd all-interface min-tx-interval 300

```