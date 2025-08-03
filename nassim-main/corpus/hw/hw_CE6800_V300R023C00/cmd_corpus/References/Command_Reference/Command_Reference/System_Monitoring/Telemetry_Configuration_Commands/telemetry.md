telemetry
=========

telemetry

Function
--------



The **telemetry** command displays the telemetry view.




Format
------

**telemetry** [ **openconfig** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **openconfig** | Displays the telemetry view of the OpenConfig type. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



Before configuring the OpenConfig-based telemetry function, run the command to enter the telemetry view.



**Precautions**

* Only users of level 3 (management level) or users in the management group (manage-ug) can configure telemetry or telemetry ietf.
* The effect of configuring the keyword openconfig is the same as that of no such configuration. The scenario where no openconfig keyword is configured is reserved for upgrade compatibility.

Example
-------

# Display the telemetry view.
```
<HUAWEI> system-view
[~HUAWEI] telemetry

```