dcb ets-profile
===============

dcb ets-profile

Function
--------



The **dcb ets-profile** command creates an enhanced transmission selection (ETS) profile and displays the ETS profile view, or displays the view of an existing ETS profile.

The **undo dcb ets-profile** command deletes an ETS profile.



By default, the system provides ETS profile default.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dcb ets-profile** *name*

**undo dcb ets-profile** *name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *name* | Specifies the name of an ETS profile. | The value is a string of 1 to 31 case-sensitive characters without spaces. The value can contain letters, digits, hyphens (-), and underscores (\_). It cannot contain the following symbols: | > $ \* ^. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **dcb ets-profile** command creates an ETS profile and displays the ETS profile view, or displays the view of an existing ETS profile. ETS ensures that traffic of the specified type is preferentially processed and improves bandwidth use efficiency.A maximum of eight ETS profiles, including the default ETS profile, can be configured. The default ETS profile can be modified but cannot be deleted.

**Follow-up Procedure**

After an ETS profile is created, you can run the **priority-group drr**, **priority-group shaping**, **priority-group queue**, **queue** { **pq** | **drr** }, and **queue shaping** commands to configure it.

**Precautions**

If an ETS profile has been applied to an interface, you must unbind the ETS profile from the interface before deleting this profile.


Example
-------

# Create an ETS profile myets.
```
<HUAWEI> system-view
[~HUAWEI] dcb ets-profile myets
[*HUAWEI-ets-myets]

```