bfd all-interfaces (OSPFv3 view)
================================

bfd all-interfaces (OSPFv3 view)

Function
--------



The **bfd all-interfaces** command sets the parameter values of a BFD session.

The **undo bfd all-interfaces** command restores the default parameter values of a BFD session.



By default, BFD is not enabled for OSPFv3.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**bfd all-interfaces** { **min-transmit-interval** *Tx-Value* | **min-receive-interval** *Rx-Value* | **detect-multiplier** *Mul-Value* | **frr-binding** } \*

**undo bfd all-interfaces** { **min-transmit-interval** [ *Tx-Value* ] | **min-receive-interval** [ *Rx-Value* ] | **detect-multiplier** [ *Mul-Value* ] | **frr-binding** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **min-transmit-interval** *Tx-Value* | Specifies the minimum interval at which BFD packets are sent to the remote device. | The value is an integer ranging from 3 to 1000, in milliseconds. |
| **min-receive-interval** *Rx-Value* | Specifies the minimum interval for receiving BFD messages from the peer. | The value is an integer ranging from 3 to 1000, in milliseconds. |
| **detect-multiplier** *Mul-Value* | Specifies the local detect multiplier. | The value is an integer ranging from 3 to 50. The default value is 3. |
| **frr-binding** | Associates the BFD session status with the link status on an interface. If BFD detects a link fault on an interface, the BFD session goes Down, triggering FRR. Traffic is then quickly switched to the backup link, minimizing service loss. | - |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The Rx-Value is obtained by negotiating the local min-receive-interval value with the peer min-transmit-interval value. If the local end does not receive any BFD packet from the peer end within the Rx-Value x Mul-Value interval (local detection time), the local end declares the neighbor Down.

**Prerequisites**

Before running this command, you need to run the **bfd all-interfaces enable** command to enable BFD in the OSPFv3 process.

**Precautions**



After BFD is enabled, OSPFv3 establishes BFD sessions only with the neighbors in the Full state.The preference of BFD configured on an interface is higher than that configured in the process.The bfd all-interfaces (OSPFv3) command and the ospfv3 bfd block command are mutually exclusive.




Example
-------

# Enable BFD for an OSPFv3 process.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] bfd all-interfaces enable
[*HUAWEI-ospfv3-1] bfd all-interfaces min-transmit-interval 30

```