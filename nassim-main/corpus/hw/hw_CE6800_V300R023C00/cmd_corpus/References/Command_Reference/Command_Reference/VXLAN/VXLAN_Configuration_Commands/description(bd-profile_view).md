description(bd-profile view)
============================

description(bd-profile view)

Function
--------



The **description** command configures a description for a bridge domain (BD) profile.

The **undo description** command deletes the description of a BD profile.



By default, no description is configured for a BD profile.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**description** *profdescStr*

**undo description** [ *profdescStr* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *profdescStr* | Specifies the description of a BD profile. | The value is a string of 1 to 80 case-sensitive characters, spaces supported. |



Views
-----

bd-profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If multiple BD profiles have been configured using the bridge-domain profile <profileId> command and each profile is bound to different services, run the **description** command in the corresponding BD profile view to configure a description for the profile. The description helps you quickly understand the function of the profile, which facilitates service management.


Example
-------

# Configure the description profile1 for BD profile 1.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain profile 1
[~HUAWEI-bd-profile1] description profile1

```