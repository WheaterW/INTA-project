destination-group (Subscription view)
=====================================

destination-group (Subscription view)

Function
--------



The **destination-group** command associates a destination group to which the data sampled is sent.

The **undo destination-group** command deletes a destination group that is associated.



By default, no destination group is associated.


Format
------

**destination-group** *destination-name*

**undo destination-group** *destination-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *destination-name* | Specifies the name of a destination group to which the data sampled is sent. | The value is a string of 1 to 64 case-sensitive characters. The value is the name of an existing Destination-group. |



Views
-----

Subscription view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To enable a destination group that is created in the Telemetry view to take effect, run the **destination-group** command in the Subscription view to associate it.

**Precautions**



A maximum of five destination groups can be associated with each subscription using this command. Five IP addresses and five port numbers can be configured for each destination group.The destination group that is associated in the Subscription view must be created in the Telemetry view first. Otherwise, association fails.




Example
-------

# Create a destination group named a in the Telemetry view and associate it in the Subscription view.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] destination-group a
[*HUAWEI-telemetry-destination-group-a] quit
[*HUAWEI-telemetry] subscription aa
[*HUAWEI-telemetry-subscription-aa] destination-group a

```