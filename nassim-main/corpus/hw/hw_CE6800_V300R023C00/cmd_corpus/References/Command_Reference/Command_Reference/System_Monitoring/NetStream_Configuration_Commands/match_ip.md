match ip
========

match ip

Function
--------



The **match ip** command configures aggregation keywords in an IPv4 flexible flow statistics template.

The **undo match ip** command deletes aggregation keywords from an IPv4 flexible flow statistics template.



By default, no aggregation keyword is configured in an IPv4 flexible flow statistics template.


Format
------

**match ip** { **destination-address** | **destination-port** | **tos** | **protocol** | **source-address** | **source-port** | **source-mac** | **destination-mac** | **ethernet-type** | **vlan** }

**undo match ip** { **destination-address** | **destination-port** | **tos** | **protocol** | **source-address** | **source-port** | **source-mac** | **destination-mac** | **ethernet-type** | **vlan** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **destination-address** | Indicates that flows are aggregated based on destination addresses. | - |
| **destination-port** | Indicates that flows are aggregated based on destination ports. | - |
| **tos** | Indicates that flows are aggregated based on ToS fields. | - |
| **protocol** | Indicates that flows are aggregated based on protocol types. | - |
| **source-address** | Indicates that flows are aggregated based on source addresses. | - |
| **source-port** | Indicates that flows are aggregated based on source ports. | - |
| **source-mac** | Indicates that flows are aggregated based on the source MAC address . | - |
| **destination-mac** | Indicates that flows are aggregated based on the destination MAC address. | - |
| **ethernet-type** | Indicates that flows are aggregated based on Ethernet type. | - |
| **vlan** | Indicates that flows are aggregated based on VLAN. | - |



Views
-----

IPv4 flexible flow statistics template view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

During NetStream implementation, you can run the **match ip** command to configure aggregation keywords in a flexible flow statistics template.

**Prerequisites**

The netstream record ip (system view) command has been executed to create an IPv4 flexible flow statistics template.

**Precautions**

When you run the **match ip** command to configure the aggregation keywords, only one keyword can be configured each time. If you run this command multiple times in the same view, a set of multiple aggregation keywords is configured. If a template has been applied to an interface, you cannot modify or delete aggregation keywords from the template.


Example
-------

# Set the flexible flow statistics template abc123 to aggregate flows based on the source port.
```
<HUAWEI> system-view
[~HUAWEI] netstream record abc123 ip
[*HUAWEI-netstream-record-ipv4-abc123] match ip source-port

```