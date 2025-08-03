traffic-segment same-segment
============================

traffic-segment same-segment

Function
--------



The **traffic-segment same-segment** command configures the default access control policy for members in an EPG.

The **undo traffic-segment same-segment** command restores the default access control policy for members in an EPG.



By default, the access control policy for members in an EPG is none. That is, access control is not performed for members in an EPG. In this case, the device controls access to EPG members based on the default access control policy for EPG members.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**traffic-segment same-segment** { **none** | **permit** | **deny** }

**undo traffic-segment same-segment** { **none** | **permit** | **deny** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **none** | If no behavior is configured in a microsegmentation group, packet forwarding is not affected. | - |
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

On a network, users can deploy different servers in the same EPG. The servers in the same EPG are members of the EPG. You can run the **traffic-segment same-segment** command to specify an access control policy for members in an EPG to implement traffic control for members in the EPG.


Example
-------

# Configure the default access control policy for members in an EPG to allow mutual access.
```
<HUAWEI> system-view
[~HUAWEI] traffic-segment enable
[*HUAWEI] traffic-segment same-segment permit

```