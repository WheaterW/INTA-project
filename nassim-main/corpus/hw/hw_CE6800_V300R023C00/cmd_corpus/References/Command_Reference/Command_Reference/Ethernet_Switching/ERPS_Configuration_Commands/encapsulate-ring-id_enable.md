encapsulate-ring-id enable
==========================

encapsulate-ring-id enable

Function
--------



The **encapsulate-ring-id enable** command enables the function of encapsulating a ring network ID into the destination MAC address of ERPS packets.

The **undo encapsulate-ring-id enable** command disables the function of encapsulating a ring network ID into the destination MAC address of ERPS packets.



By default, the function of encapsulating a ring network ID into the destination MAC address of ERPS packets is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**encapsulate-ring-id enable**

**undo encapsulate-ring-id enable**


Parameters
----------

None

Views
-----

ERPS ring view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a Huawei device communicates with a non-Huawei device, if the destination MAC address of ERPS packets sent by the non-Huawei device carries a ring network ID, the Huawei device cannot communicate with the non-Huawei device. In this case, you need to run this command to enable the function of encapsulating a ring network ID into the destination MAC address of ERPS packets, so that the Huawei device can communicate with the non-Huawei device.

**Precautions**

If an interface has been added to an ERPS ring, the function of encapsulating a ring network ID into the destination MAC address of ERPS packets cannot be enabled or disabled. To enable or disable the function of encapsulating a ring network ID into the destination MAC address of ERPS packets, run the undo erps ring <ring-id> command in the interface view or run the undo port <interface-type> <interface-number> command in the ERPS ring view to delete the interface from the ERPS ring. Then, you can run this command to enable or disable the function of encapsulating a ring network ID into the destination MAC address of ERPS packets.


Example
-------

# Enable the function of encapsulating a ring network ID into the destination MAC address of ERPS packets.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 1
[*HUAWEI-erps-ring1] encapsulate-ring-id enable

```