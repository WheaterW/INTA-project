match ipv6
==========

match ipv6

Function
--------



The **match ipv6** command configures aggregation keywords in an IPv6 flexible flow statistics template.

The **undo match ipv6** command deletes aggregation keywords from an IPv6 flexible flow statistics template.



By default, no aggregation keyword is configured in an IPv6 flexible flow statistics template.


Format
------

**match ipv6** { **destination-address** | **destination-port** | **tos** | **protocol** | **source-address** | **source-port** | **flow-label** | **source-mac** | **destination-mac** | **ethernet-type** | **vlan** }

**undo match ipv6** { **destination-address** | **destination-port** | **tos** | **protocol** | **source-address** | **source-port** | **flow-label** | **source-mac** | **destination-mac** | **ethernet-type** | **vlan** }


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
| **flow-label** | Indicates that flows are aggregated based on flow labels. | - |
| **source-mac** | Indicates that flows are aggregated based on the source MAC address . | - |
| **destination-mac** | Indicates that flows are aggregated based on the destination MAC address. | - |
| **ethernet-type** | Indicates that flows are aggregated based on ethernet type. | - |
| **vlan** | Indicates that flows are aggregated based on VLAN. | - |



Views
-----

IPv6 flexible flow statistics template view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **match ipv6** command to configure aggregation keywords in a flexible flow statistics template.

**Prerequisites**

The netstream record ipv6 (system view) command has been executed to create an IPv6 flexible flow statistics template.

**Precautions**

When you run the **match ipv6** command to configure the aggregation keywords, only one keyword can be configured each time. If you run this command multiple times in the same view, a set of multiple aggregation keywords is configured. If a template has been applied to an interface, you cannot modify or delete aggregation keywords from the template.


Example
-------

# Configure an IPv6 flexible flow statistics template abc123 to aggregate flows based on flow labels.
```
<HUAWEI> system-view
[~HUAWEI] netstream record abc123 ipv6
[*HUAWEI-netstream-record-ipv6-abc123] match ipv6 flow-label

```