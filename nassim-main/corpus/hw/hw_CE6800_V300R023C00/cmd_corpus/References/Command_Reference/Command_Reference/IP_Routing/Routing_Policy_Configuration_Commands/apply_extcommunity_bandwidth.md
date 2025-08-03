apply extcommunity bandwidth
============================

apply extcommunity bandwidth

Function
--------



The **apply extcommunity bandwidth** command sets the bandwidth extended community attribute for routes.

The **undo apply extcommunity bandwidth** command deletes the bandwidth extended community attribute.



By default, no bandwidth extended community attribute values are set for routes.


Format
------

**apply extcommunity bandwidth** { *extCmntyString* | **none** }

**apply extcommunity bandwidth aggregate** [ **limit** *bandwidth-value* ]

**apply extcommunity bandwidth aggregate-upstream** [ **limit** *upstream-bandwidth* ]

**undo apply extcommunity bandwidth** [ *extCmntyString* | **none** ]

**undo apply extcommunity bandwidth aggregate** [ **limit** *bandwidth-value* ]

**undo apply extcommunity bandwidth aggregate-upstream** [ **limit** *upstream-bandwidth* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *extCmntyString* | Specifies the bandwidth extended community attribute value. | The value of the bandwidth extended community attribute consists of the AS number and bandwidth value. The format is AS number:bandwidth value, for example, 1:100, in which the AS number ranges from 1 to 65535, and the bandwidth value ranges from 1 to 4294967295. |
| **none** | Clears the bandwidth extended community attribute of routes. | - |
| **aggregate** | Indicates the aggregated bandwidth extended community attribute. | - |
| **limit** | Indicates the maximum value of the aggregated bandwidth extended community attribute. | - |
| *bandwidth-value* | Specifies the aggregated bandwidth. | The value is an integer ranging from 1 to 4294967295, in kbit/s. |
| **aggregate-upstream** | Indicates the aggregated uplink bandwidth extended community attribute. | - |
| *upstream-bandwidth* | Specifies the aggregated uplink bandwidth (kbit/s). | The value is an integer ranging from 1 to 4294967295, in kbit/s. |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After the apply extcommunity bandwidth command is run, the routes advertised by the device carry the bandwidth extended community attribute, which is used to identify sites. After the **apply extcommunity bandwidth aggregate-upstream** command is run, the routes advertised by the device carry the aggregated uplink bandwidth extended community attribute. BGP accumulates the uplink bandwidths of the routes for load balancing and uses the sum as the final result. If the final result is greater than the value of limit, the value of limit is used. Pay attention to the following points when using this command:Run the **route-policy** command first to enter the route-policy view.A route-policy can consist of multiple nodes. The relationship between different nodes is OR. The system checks each node in sequence based on the node sequence number. The later matched node overwrites the previous one.




Example
-------

# Add 1:1 to the bandwidth extended community attribute of routes.
```
<HUAWEI> system-view
[~HUAWEI] route-policy aaa permit node 1
[~HUAWEI-route-policy] apply extcommunity bandwidth 1:1

```

# Set the maximum value of the aggregated bandwidth extended community attribute to 100 kbit/s.
```
<HUAWEI> system-view
[~HUAWEI] route-policy aaa permit node 1
[~HUAWEI-route-policy] apply extcommunity bandwidth aggregate limit 100

```

# Clear the bandwidth extended community attribute of routes.
```
<HUAWEI> system-view
[~HUAWEI] route-policy aaa permit node 1
[~HUAWEI-route-policy] apply extcommunity bandwidth none

```

# Set the maximum value of the aggregated uplink bandwidth extended community attribute to 100 kbit/s.
```
<HUAWEI> system-view
[~HUAWEI] route-policy aaa permit node 1
[~HUAWEI-route-policy] apply extcommunity bandwidth aggregate-upstream limit 100

```