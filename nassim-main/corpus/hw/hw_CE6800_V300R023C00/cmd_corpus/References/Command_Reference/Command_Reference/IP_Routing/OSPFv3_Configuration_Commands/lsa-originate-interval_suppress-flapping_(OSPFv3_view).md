lsa-originate-interval suppress-flapping (OSPFv3 view)
======================================================

lsa-originate-interval suppress-flapping (OSPFv3 view)

Function
--------



The **lsa-originate-interval suppress-flapping** command configures a suppression period in case the OSPFv3 LSAs to be sent flap.

The **undo lsa-originate-interval suppress-flapping** command restores the default suppression period.



By default, the suppression period is 10s, and the suppression threshold is 30.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**lsa-originate-interval suppress-flapping** *interval* [ **threshold** *count* ]

**undo lsa-originate-interval suppress-flapping**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the suppression period that takes effect when the OSPFv3 LSAs to be sent flap. | The value is an integer ranging from 0 to 600, in seconds. The default value is 10s If the value is set to 0, OSPFv3 LSAs are not suppressed. |
| **threshold** *count* | Specifies the suppression threshold that takes effect when the OSPFv3 LSAs to be sent flap. | The value is an integer ranging from 3 to 100. The default value is 30. |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If the sent OSPFv3 LSAs do not flap, you can run the **lsa-originate-interval** command to set the interval at which LSAs are sent to prevent frequent LSA sending. If the sent OSPFv3 LSAs flap, you can run the **lsa-originate-interval suppress-flapping** command to set a flapping suppression period to minimize the impact of frequent flapping on services. In this case, the device uses the larger value as the flapping suppression time.The process in which received OSPFv3 LSAs flap and the suppression state is entered is as follows:

* OSPFv3 starts a flapping counter. If the interval between two successive OSPFv3 LSAs is less than or equal to 5s, OSPFv3 records a flapping event and increases the flapping\_count by 1. If the interval between two OSPFv3 LSAs is greater than 10s before the flapping\_count reaches the threshold, the device clears the flapping\_count. If the configured suppression period is less than or equal to 5s, the device does not detect or suppress OSPFv3 LSA flapping.
* Suppression phase: When the flapping\_count is greater than or equal to the configured suppression threshold, flapping suppression starts.
* Suppression time: The device does not generate new LSAs within the configured suppression time. The actual suppression time is the larger value between the configured suppression time and the time calculated by the lsa-arrival-interval command.
* Suppression exit: After the suppression time expires, the flapping\_count is cleared and the device exits suppression.
* Note: The interval between two consecutive LSAs refers to the interval between the time when the LSA is received and the time when the LSA in the LSDB is updated last time.

Example
-------

# Set the suppression period that takes effect when the OSPFv3 LSAs to be sent flap to 200s.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] lsa-originate-interval suppress-flapping 200

```