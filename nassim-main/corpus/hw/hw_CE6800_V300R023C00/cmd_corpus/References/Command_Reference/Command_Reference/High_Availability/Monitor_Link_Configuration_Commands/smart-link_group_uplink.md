smart-link group uplink
=======================

smart-link group uplink

Function
--------



The **smart-link group uplink** command adds a Smart Link group to a Monitor Link group as an uplink.

The **undo smart-link group uplink** command deletes a Smart Link group from a Monitor Link group.



By default, no Smart Link group is added to a Monitor Link group as an uplink.


Format
------

**smart-link group** *group-id* **uplink**

**undo smart-link group** *group-id* **uplink**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-id* | Specifies the ID of a Smart Link group. | The value is an integer ranging from 1 to 48. |



Views
-----

Monitor link group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a cascading network of Smart Link and Monitor Link, you can run the smart-link group uplink command to configure a Smart Link group as the uplink interface in a Monitor Link group to improve network reliability. If an uplink interface is a Smart Link group, the uplink interface fails only when both interfaces in the Smart Link group are Inactive or Down. If the uplink interface fails, Monitor Link sets the downlink interfaces to Down.



**Prerequisites**



A Smart Link group has been created using the **smart-link group** command.



**Precautions**

* A Smart Link group can be added to only one Monitor Link group.
* A Smart Link group can be configured only as the uplink interface in a Monitor Link group.
* If all uplink interfaces fail, Monitor Link sets the downlink interfaces to Down.


Example
-------

# Add Smart Link group 1 to Monitor Link group 2 as the uplink interface.
```
<HUAWEI> system-view
[~HUAWEI] smart-link group 1
[*HUAWEI-smlk-group1] quit
[*HUAWEI] monitor-link group 2
[*HUAWEI-mtlk-group2] smart-link group 1 uplink

```