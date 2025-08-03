dcb pfc
=======

dcb pfc

Function
--------



The **dcb pfc** command creates a Priority-based Flow Control (PFC) profile and displays the PFC profile view, or displays the view of an existing PFC profile.

The **undo dcb pfc** command deletes a PFC profile.



By default, the system provides the PFC profile default.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dcb pfc** [ *profilename* ]

**undo dcb pfc** *profilename*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *profilename* | Specifies the name of a PFC profile. | The value is a string of 1 to 31 case-sensitive characters that can contain letters, digits, hyphens (-), and underscores (\_). It cannot contain spaces and special characters | > $ \* ^ or start with an underscore (\_).  If this parameter is not specified, the default profile is displayed.  When a PFC profile is applied, if the configured PFC profile name conflicts with the command keyword, the command keyword takes effect preferentially. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

As an enhancement to the Pause mechanism, PFC defines eight queues on an Ethernet link and can stop or restart any queue. It provides lossless services for specified queues on an interface, without affecting other types of traffic on the interface.

**Follow-up Procedure**

You can run the **priority** (DCB PFC view) command to configure the profile.

**Precautions**

If a PFC profile has been applied to an interface, you must unbind the PFC profile from the interface before deleting the profile.


Example
-------

# Create a PFC profile mypfc.
```
<HUAWEI> system-view
[~HUAWEI] dcb pfc mypfc
[*HUAWEI-dcb-pfc-mypfc]

```