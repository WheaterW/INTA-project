destination-group
=================

destination-group

Function
--------



The **destination-group** command creates a destination group for a gRPC client and displays the destination group view of the gRPC client.

The **undo destination-group** command deletes the destination group of a gRPC client.



By default, no destination group is created for a gRPC client.


Format
------

**destination-group** *destination-group-name*

**undo destination-group** *destination-group-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *destination-group-name* | Specifies the destination group name of a gRPC client. | The value is a string of 1 to 64 case-sensitive characters containing letters, digits, or a combination of letters and digits. Spaces are not supported between letters or digits. |



Views
-----

GRPC client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To create one or more destination groups for the gRPC client in the gRPC client view to receive data from the device, run the **destination-group** command.

**Precautions**

* The device supports a maximum of two destination groups for the gRPC client. The destination groups take effect only after being associated with services.
* The telemetry service cannot be bound to the destination group of the gRPC client. When telemetry uses gRPC to transmit data, run the **destination-group** command in the telemetry view to associate the destination group to which the destination collector belongs.
* If the destination group of the gRPC client is associated with a service, the destination group cannot be deleted using the **undo destination-group** command.

Example
-------

# Create a gRPC client destination group named a.
```
<HUAWEI> system-view
[~HUAWEI] grpc
[~HUAWEI-grpc] grpc client
[~HUAWEI-grpc-client] destination-group a

```