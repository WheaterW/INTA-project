dcb app-profile
===============

dcb app-profile

Function
--------



The **dcb app-profile** command creates an APP profile and displays the APP profile view, or directly displays the view of the existing APP profile.

The **undo dcb app-profile** command deletes an APP profile.



By default, no APP profile is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dcb app-profile** *profile-name*

**undo dcb app-profile** *profile-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *profile-name* | Specifies the name of an APP profile. | The value is a string of 1 to 31 case-sensitive characters without spaces. The value can contain letters, digits, hyphens (-), and underscores (\_). It cannot contain the following characters: | > $ \* ^. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable the DCB-enabled device to interwork with a non-Huawei device, create an APP profile, specify a service priority in the APP TLV in the APP profile, and apply the APP profile to an interface. To create the APP profile, run this command.

**Follow-up Procedure**

Run the **application priority** command to specify a service priority.

**Precautions**

If an APP profile has been applied to an interface, you must unbind the APP profile from the interface so that you can delete this profile.


Example
-------

# Create an APP profile named myapp.
```
<HUAWEI> system-view
[~HUAWEI] dcb app-profile myapp
[*HUAWEI-dcb-app-myapp]

```