summary (IS-IS view)
====================

summary (IS-IS view)

Function
--------



The **summary** command enables IS-IS route summarization.

The **undo summary** command disables IS-IS route summarization.



By default, IS-IS route summarization is disabled.


Format
------

**summary** *ip-address* *mask* [ **avoid-feedback** | **generate\_null0\_route** | **tag** *tag-value* | **cost** *cost-value* | [ **level-1** | **level-2** | **level-1-2** ] ] \*

**undo summary** *ip-address* *mask* [ **level-1** | **level-2** | **level-1-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the address segment of the summary route. | The value is in dotted decimal notation. |
| *mask* | Specifies the address mask of the summary route. | The value is in dotted decimal notation. |
| **avoid-feedback** | Avoid learning your own published aggregation routes from another level. If there is a learning route in another level that is the same as the summary address, it is assumed that the route is infiltrated into another level and published by other devices after they have learned the summary route published by the local device. At this point, avoid-feedback occurs and the route becomes inactive, removed from the RM routing table. | - |
| **generate\_null0\_route** | Generates Null 0 routes to prevent routing loops. After this parameter is specified, if a device receives a route with the same prefix from another device, the device preferentially selects the blackhole route of the local device. | - |
| **tag** *tag-value* | Specifies an administrative tag. | The value is an integer ranging from 1 to 4294967295. |
| **cost** *cost-value* | Specifies a cost for the summary route. | The value is an integer and varies with the cost type.   * When the cost type is narrow, narrow-compatible, or compatible, the value ranges from 1 to 63. * When the cost type is wide or wide-compatible, the value ranges from 1 to 16777215.   The cost type can be configured using the cost-style command. |
| **level-1** | Summarizes Level-1 routes. | - |
| **level-2** | Summarizes Level-2 routes.  If no level is specified, Level-2 routes are summarized. | - |
| **level-1-2** | Summarizes Level-1 and Level-2 routes. | - |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The IS-IS routing table of a device on a medium or large IS-IS network contains a large number of routing entries. Storing the routing table consumes a large number of memory resources, and transmitting and processing routes consume lots of network resources. IS-IS route summarization can solve this problem.Routes with the same IPv4 prefix can be summarized into one route. The system then advertises the summary route to other network segments. Route summarization on a large-scale IS-IS network reduces the number of routes in a routing table and minimizes system resource consumption. In addition, if a specific link frequently alternates between Up and Down, the links not involved in the route summarization will not be affected, which prevents route flapping and improves network security.Configuring route summarization does not affect the routing table on a local device. Each specific route is displayed in the routing table. Configuring route summarization, however, reduces the number of LSPs to be flooded. Any device that receives the LSP from the summarization-capable router has only one summary route in its routing table.

**Prerequisites**



An IS-IS process has been created and the IS-IS view has been displayed using the **isis** command.



**Precautions**

The routes to be summarized can be the routes discovered by IS-IS or routes imported from other routing protocols. The cost of the summarized route is the smallest cost of the routes that are summarized.


Example
-------

# Configure a summary route 10.10.0.0/8.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] summary 10.10.0.0 255.0.0.0

```