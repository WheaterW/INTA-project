dcb enable
==========

dcb enable

Function
--------



The **dcb enable** command applies an Enhanced Transmission Selection (ETS) or APP profile to an interface.

The **undo dcb ets enable** command deletes an ETS profile from an interface.

The **undo dcb app-profile enable** command applies the default APP profile to an interface.

The **dcb app-profile disable** command deletes an APP profile from an interface.



By default, no ETS or APP profile is applied to an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dcb** { { **ets** **enable** *etsprofile* } | { **app-profile** { **enable** *appprofile* | **disable** } } } \*

**undo dcb** { { **ets** **enable** [ *etsprofile* ] } | { **app-profile** { { **enable** [ *appprofile* ] } | **disable** } } } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *etsprofile* | Specifies the name of an ETS profile. | The ETS profile must already exist. |
| *appprofile* | Specifies the name of an APP profile. | The APP profile must already exist. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

ETS ensures that traffic of high priorities is preferentially processed, maximizing the bandwidth usage. The **dcb ets enable** command applies an ETS profile to an interface.To enable the device configured with Data Center Bridging (DCB) to interwork with a non-Huawei device, create an APP profile, specify a service priority in the APP TLV in the APP profile, and apply the APP profile to an interface. To apply the APP profile to an interface, run this command.

**Prerequisites**

Run the **dcb app-profile** command to create an APP profile and displays the APP profile view, or directly display the view of the existing APP profile.Run the **dcb ets-profile** command to create an enhanced transmission selection (ETS) profile and display the ETS profile view, or display the view of an existing ETS profile.

**Precautions**

ETS and QoS configurations conflict on an interface.

* If an interface has QoS configurations such as shaping, WRED, and non-PQ scheduling, the ETS profile cannot be applied to the interface.
* If an ETS profile is applied to an interface, QoS configurations such as shaping, WRED, and non-PQ scheduling cannot be configured on the interface.

Before applying an APP profile to an interface, run the **dcb app-profile** command to create an APP profile in the system view. Otherwise, an error message is displayed.



Example
-------

# Apply the ETS profile myets to 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] dcb ets-profile myets
[*HUAWEI-ets-myets] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] dcb ets enable myets

```