load-balance profile dynamic
============================

load-balance profile dynamic

Function
--------



The **load-balance profile dynamic** command creates a dynamic load balancing profile and displays the dynamic load balancing profile view. If the dynamic load balancing profile already exists, this command displays the dynamic load balancing profile view.

The **undo load-balance profile dynamic** command restores the dynamic load balancing profile to default.



By default, the system defines a dynamic load balancing profile named default.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**load-balance profile dynamic** *profile-name*

**undo load-balance profile dynamic** *profile-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *profile-name* | Specifies the name of a dynamic load balancing profile. | The value is a string of 1 to 31 case-sensitive characters. When double quotation marks are used around the string, spaces are allowed in the string. The string cannot contain the following characters: | > $. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can create a dynamic load balancing profile and run eth-trunk mode (dynamic load balancing profile view) in the profile to configure the dynamic load balancing mode for a LAG respectively.

**Precautions**

* The device supports only one dynamic load balancing profile.
* The default dynamic load balancing profile default cannot be deleted.
* If you create a dynamic load balancing profile while an existing profile exists, the existing profile is renamed and its non-default configurations will not be deleted.

Example
-------

# Create a dynamic load balancing profile named test.
```
<HUAWEI> system-view
[~HUAWEI] load-balance profile dynamic test

```