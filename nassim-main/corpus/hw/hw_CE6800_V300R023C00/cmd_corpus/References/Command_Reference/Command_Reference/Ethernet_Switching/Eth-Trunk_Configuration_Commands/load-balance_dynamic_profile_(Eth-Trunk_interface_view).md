load-balance dynamic profile (Eth-Trunk interface view)
=======================================================

load-balance dynamic profile (Eth-Trunk interface view)

Function
--------



The **load-balance dynamic profile** command applies a dynamic load balancing profile to an Eth-Trunk interface.

The **undo load-balance dynamic profile** command deletes a dynamic load balancing profile from an Eth-Trunk interface.



By default, no dynamic load balancing profile is applied to an Eth-Trunk interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**load-balance dynamic profile** *profile-name*

**undo load-balance dynamic profile** *profile-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *profile-name* | Specifies the name of a dynamic load balancing profile. | The dynamic load balancing profile must exist on the device. |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The traditional static load balancing mode does not consider the usage of each member link, and unbalanced loads of member links may occur. Especially, when there are large flows, congestion or even packet loss may occur on member links.After the dynamic load balancing function is enabled, traffic of a LAG is dynamically load balanced among its member links, providing maximum load balancing between them.

**Prerequisites**

A dynamic load balancing profile has been created using the **load-balance profile dynamic profile-name** command in the system view. The default dynamic load balancing profile is named default.

**Precautions**

Load balancing is valid only for outgoing traffic; therefore, the load balancing modes for the interfaces at both ends of a link can be different and do not affect each other.


Example
-------

# Apply the dynamic load balancing profile test to Eth-Trunk1.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 1
[*HUAWEI-Eth-Trunk1] load-balance dynamic profile test

```