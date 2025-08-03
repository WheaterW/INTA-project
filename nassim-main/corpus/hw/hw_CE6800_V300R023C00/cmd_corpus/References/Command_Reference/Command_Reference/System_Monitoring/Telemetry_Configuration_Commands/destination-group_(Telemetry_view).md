destination-group (Telemetry view)
==================================

destination-group (Telemetry view)

Function
--------



The **destination-group** command creates one or more destination groups to which the data sampled is sent and enters the Destination-group view.

The **undo destination-group** command deletes a destination group to which the data sampled is sent.



By default, no destination groups to which the data sampled is sent are created.


Format
------

**destination-group** *destination-group-name*

**undo destination-group** *destination-group-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *destination-group-name* | Specifies the name of a destination group to which the data sampled is sent. | The value is a string of 1 to 64 case-sensitive characters containing letters and digits. Spaces are not supported between letters or digits. |



Views
-----

Telemetry view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To create one or more destination groups to receive the data sampled and sent by devices, run the **destination-group** command in the Telemetry view.

**Precautions**



A maximum of five destination groups can be associated to each subscription using this command. At most five combinations, each consisting of an IP address, a port number, and a VPN instance, can be configured for all destination groups. A destination group takes effect only after it is associated to a subscription in the Subscription view.If a destination group has been associated, it cannot be deleted using the **undo destination-group** command.




Example
-------

# Create a destination group named a to which the data sampled is sent in the Telemetry view.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] destination-group a

```