traffic-segment unknown-segment
===============================

traffic-segment unknown-segment

Function
--------



The **traffic-segment unknown-segment** command configures the behavior of an unknown EPG.

The **undo traffic-segment unknown-segment** command deletes the behavior of an unknown EPG.



By default, the access control policy for unknown EPG members is permit. That is, unknown EPG members can communicate with each other.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**traffic-segment unknown-segment** { **permit** | **deny** }

**undo traffic-segment unknown-segment** { **permit** | **deny** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **permit** | Allows packets to pass. | - |
| **deny** | Discards the packets. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On a network, after EPGs are assigned to users, some servers belong to EPGs and some servers do not belong to any EPG. The servers that do not belong to any EPG are unknown EPG members. You can run the **traffic-segment unknown-segment** command to specify an access control policy for unknown EPG members to control traffic between unknown EPG members.


Example
-------

# Configure an access control policy for unknown EPG members to deny mutual access.
```
<HUAWEI> system-view
[~HUAWEI] traffic-segment enable
[*HUAWEI] traffic-segment unknown-segment deny

```