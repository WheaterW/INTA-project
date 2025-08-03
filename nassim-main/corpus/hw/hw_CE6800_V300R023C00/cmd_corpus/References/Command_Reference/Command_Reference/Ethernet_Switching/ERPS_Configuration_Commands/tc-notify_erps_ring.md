tc-notify erps ring
===================

tc-notify erps ring

Function
--------



The **tc-notify erps ring** command configures an ERPS ring to notify other ERPS rings of its topology change.

The **undo tc-notify erps ring** command disables an ERPS ring from notifying other ERPS rings of its topology change.



By default, an ERPS ring does not notify other ERPS rings of its topology change.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**tc-notify erps ring** { *ring-id1* [ **to** *ring-id2* ] } &<1-10>

**undo tc-notify erps ring** { *ring-id1* [ **to** *ring-id2* ] } &<1-10>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ring-id1* | Specifies ID1 of an ERPS ring. | The value is an integer ranging from 1 to 255.  The value of <ring-id2> must be greater than or equal to <ring-id1>. |
| **to** *ring-id2* | Specifies ID2 of an ERPS ring. | The value is an integer ranging from 1 to 255.  The value of <ring-id2> must be greater than or equal to <ring-id1>. |



Views
-----

ERPS ring view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If other ERPS rings are not notified of the topology change in an ERPS ring, the MAC address entries remain unchanged on the other ERPS rings and user traffic is interrupted. To ensure nonstop traffic transmission, run the **tc-notify erps ring** command to specify an ERPS ring for which the topology change notifications are sent.

**Prerequisites**

The **version v2** command has been run to specify ERPSv2.

**Configuration Impact**

After receiving the topology change notification from an ERPS ring, the other ERPS rings send Flush-FDB packets on their own rings. Then, all the devices on the upper-layer network delete the original MAC addresses and learn new MAC addresses to ensure normal traffic transmission.

If you run this command multiple times, all configurations take effect.

**Precautions**

When the topology of an ERPS ring changes, the ERPS ring notifies sub-rings of the topology change. If the ERPS sub-ring that has been specified to receive the topology change notification does not exist, the configuration does not take effect.


Example
-------

# Configure ERPS ring 5 to notify ERPS rings 1 through 3 of its topology change.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 5
[*HUAWEI-erps-ring5] version v2
[*HUAWEI-erps-ring5] tc-notify erps ring 1 to 3

```