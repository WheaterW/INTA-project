drop-profile
============

drop-profile

Function
--------



The **drop-profile** command creates a WRED drop profile and enters the WRED drop profile view, or enters the existing WRED drop profile view.

The **undo drop-profile** command deletes a WRED drop profile.



By default, the system provides a WRED drop profile named default.


Format
------

**drop-profile** *drop-profile-name*

**undo drop-profile** *drop-profile-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *drop-profile-name* | Specifies the name of a WRED drop profile. | The value is a string of 1 to 31 case-sensitive characters without spaces or question marks (?). It cannot be b, br, bri, brie, or brief. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A WRED drop profile defines WRED parameters for packets of different priorities. After the WRED drop profile is applied to an interface or queues on an interface, congestion avoidance is implemented. The **drop-profile** command creates a WRED drop profile or enters the WRED drop profile view.

**Follow-up Procedure**

1. Run the **color** command in the WRED drop profile view to set WRED parameters.
2. Apply the WRED drop profile to an interface or queues on an interface.

**Precautions**



If the brief and drop-profile-name parameters are not specified, detailed information about all drop profiles is displayed.For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, and CE8850-HAM:You can configure a maximum of 16 drop profiles, including the default drop profile. The default drop profile can be modified but cannot be deleted.For the CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, and CE6885-LL (low latency mode):You can configure a maximum of 63 drop profiles, including the default drop profile. The default drop profile can be modified but cannot be deleted.




Example
-------

# Create WRED drop profile drop1 and enter the WRED drop profile view.
```
<HUAWEI> system-view
[~HUAWEI] drop-profile drop1
[*HUAWEI-drop-drop1]

```