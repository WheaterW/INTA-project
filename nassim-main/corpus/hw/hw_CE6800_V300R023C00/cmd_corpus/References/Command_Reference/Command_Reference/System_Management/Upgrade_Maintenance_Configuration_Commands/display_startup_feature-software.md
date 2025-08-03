display startup feature-software
================================

display startup feature-software

Function
--------



The **display startup feature-software** command displays the version of the currently installed feature package.




Format
------

**display startup feature-software**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To check the version of the currently installed feature package, run the display startup feature-software command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the version of the feature package.
```
<HUAWEI> display startup feature-software
------------------------------------------------------------------------------------------------------------------
FeatureName          Location                                 Status     Version              ActivatedTime
------------------------------------------------------------------------------------------------------------------
XXX                         XXX.cc                                   active       XXX       2021-04-29 07:40:07
XXX                         XXX.cc                                   active       XXX       2021-04-29 07:40:07
XXX                         XXX.ccx                                  active      XXX        2021-04-29 08:06:49
XXX                         XXX.cc                                   deactive   XXX       -
------------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display startup feature-software** command output
| Item | Description |
| --- | --- |
| FeatureName | Name of the currently enabled feature package. |
| Location | Feature package. |
| Status | Feature package status:  active: The feature package is installed on the device.  deactive: The feature package is not installed on the device. Whether a function in the active state takes effect is controlled by the service module corresponding to the feature package. |
| Version | Feature package version. |
| ActivatedTime | Time when a feature package is activated. |