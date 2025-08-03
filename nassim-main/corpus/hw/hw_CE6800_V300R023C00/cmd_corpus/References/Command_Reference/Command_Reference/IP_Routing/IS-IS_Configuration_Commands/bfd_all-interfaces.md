bfd all-interfaces
==================

bfd all-interfaces

Function
--------



The **bfd all-interfaces** command sets values for BFD session parameters.

The **undo bfd all-interfaces** command restores the default values.



By default, the BFD session will set up with default values of parameters.


Format
------

**bfd all-interfaces** { **min-rx-interval** *receive-interval* | **min-tx-interval** *transmit-interval* | **detect-multiplier** *multiplier-value* | **frr-binding** } \*

**undo bfd all-interfaces** { **min-rx-interval** [ *receive-interval* ] | **min-tx-interval** [ *transmit-interval* ] | **detect-multiplier** [ *multiplier-value* ] | **frr-binding** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **min-rx-interval** *receive-interval* | Specifies the expected minimum interval at which BFD packets are received from a neighbor. | The value is an integer ranging from 3 to 1000, in milliseconds. The default value is 1000. |
| **min-tx-interval** *transmit-interval* | Specifies the minimum interval at which BFD packets are sent to a neighbor. | The value is an integer ranging from 3 to 1000, in milliseconds. The default value is 1000. |
| **detect-multiplier** *multiplier-value* | Specifies a local detection multiplier. | The value is an integer ranging from 3 to 50. The default value is 3. |
| **frr-binding** | Associates BFD session status with IS-IS auto FRR. If BFD detects a link fault on an interface, the BFD session goes Down, triggering FRR. Traffic is then quickly switched to the backup link, minimizing service loss. | - |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BFD can provide millisecond-level fault detection, help IS-IS to detect the faults that occur on neighboring devices or links more quickly, and instruct IS-IS to recalculate routes for correct packet forwarding. The bfd all-interfaces command can be used to set values for BFD session parameters.

**Prerequisites**

BFD has been enabled globally, An IS-IS process has been created, the IS-IS process has been enabled on a specified interface, and BFD has been enabled in the IS-IS process.

**Configuration Impact**

The minimum interval at which BFD packets are received is obtained after the negotiation between the local receive-interval and the remote transmit-interval. If the local end does not receive any BFD packet from its neighbor within the period (minimum interval at which BFD packets are received x multiplier-value), the local end declares the neighbor Down.

**Precautions**

If only BFD session parameters are set and the **bfd all-interfaces enable** command is not run, no BFD session can be established.The priority of BFD configured on an interface is higher than that of BFD configured in a process. If BFD is enabled on an interface, a BFD session is established according to the BFD parameters set on the interface.


Example
-------

# Configure BFD in an IS-IS process and set the minimum interval at which BFD packets are sent to 300 ms.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] bfd all-interfaces enable
[*HUAWEI-isis-1] bfd all-interfaces min-tx-interval 300

```