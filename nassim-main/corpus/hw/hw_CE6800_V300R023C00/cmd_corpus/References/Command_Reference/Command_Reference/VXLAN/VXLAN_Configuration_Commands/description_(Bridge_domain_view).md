description (Bridge domain view)
================================

description (Bridge domain view)

Function
--------



The **description** command configures a bridge domain (BD) description.

The **undo description** command deletes a description of a bridge domain.



By default, no bridge domain description is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**description** *description*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *description* | Specifies a bridge domain description. | The value is a string of 1 to 80 case-sensitive characters, spaces supported. |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If you have run the **bridge-domain** command to configure multiple BDs to transmit different services, run the **description** command in the corresponding BD view to configure a description for the BD. The description of a BD helps you quickly understand the function of the BD, facilitating service management.


Example
-------

# Configure the description VLAN for the bridge domain with ID 10.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] description VLAN

```