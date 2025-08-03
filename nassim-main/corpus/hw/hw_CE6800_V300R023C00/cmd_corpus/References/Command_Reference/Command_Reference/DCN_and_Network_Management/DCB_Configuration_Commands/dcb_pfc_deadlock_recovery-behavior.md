dcb pfc deadlock recovery-behavior
==================================

dcb pfc deadlock recovery-behavior

Function
--------



The **dcb pfc deadlock recovery-behavior** command configures the packet processing behavior of a device during the recovery period of hardware-based deadlock detection.

The **undo dcb pfc deadlock recovery-behavior** command restores the default packet processing behavior of a device during the recovery period of hardware-based deadlock detection.



By default, the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, and CE6863E-48S8CQ forward packets during the recovery period of hardware-based deadlock detection.

By default, the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM discard packets during the recovery period of hardware-based deadlock detection.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dcb pfc deadlock recovery-behavior** { **forwarding** | **discard** } **slot** *slot-id*

**undo dcb pfc deadlock recovery-behavior** { **forwarding** | **discard** } **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **forwarding** | Configures a device to forward packets during the recovery period of hardware-based deadlock detection. | - |
| **discard** | Configures a device to discard packets during the recovery period of hardware-based deadlock detection. | - |
| **slot** *slot-id* | Specifies the slot ID. | The value is an integer. You can enter a question mark (?) and select a value from the displayed value range. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After deadlock detection and recovery are configured, you can run this command to modify the packet forwarding behavior during the recovery period of hardware-based deadlock detection.

**Precautions**

For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM:

* When the forwarding behavior is set to discard, a small number of packets may still be forwarded. In this case, run the **dcb pfc deadlock-recovery timer** and **dcb pfc deadlock-detect timer** commands to set a long detection period and recovery period to reduce the number of forwarded packets.
* If the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, or CE8850-HAM are deployed on the PFC-enabled network, the forwarding behavior must be set to discard for all devices on the network during the recovery period of hardware-based deadlock detection.


Example
-------

# Configure the card in slot 1 on a device to discard packets during the recovery period of hardware-based deadlock detection.
```
<HUAWEI> system-view
[~HUAWEI] dcb pfc deadlock recovery-behavior discard slot 1

```