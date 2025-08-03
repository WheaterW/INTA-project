ipv6 summary
============

ipv6 summary

Function
--------



The **ipv6 summary** command enables IS-IS IPv6 route summarization.

The **undo ipv6 summary** command disables IS-IS IPv6 route summarization.



By default, IS-IS IPv6 route summarization is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 summary** *ipv6-address* *prefix-length* [ **explicit** ] [ **avoid-feedback** | **generate\_null0\_route** | **tag** *tag-value* | [ **level-1** | **level-2** | **level-1-2** ] ] \*

**undo ipv6 summary** *ipv6-address* *prefix-length* [ **level-1** | **level-2** | **level-1-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the address segment of the routes to be summarized. | The value is a 32-digit hexadecimal number in format X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the mask length of an IPv6 address.. | The value is an integer ranging from 0 to 128. |
| **explicit** | Indicates strict matching based on the algorithm. Only the specified algorithm can be used for route summarization. | - |
| **avoid-feedback** | Avoids learning locally advertised summary routes from another level. If there is a learned route with the same address as a summary route in another level, the device believes that the route was leaked to another level and advertised by another level by a remote device after the remote device learned the summary route from the local device. In this case, avoid-feedback takes effect, and the route becomes inactive and is removed from the RM routing table. | - |
| **generate\_null0\_route** | Generates Null 0 routes to prevent routing loops. | - |
| **tag** *tag-value* | Specifies an administrative tag value. | The value is an integer ranging from 1 to 4294967295. |
| **level-1** | Summarizes routes in the Level-1 area. | - |
| **level-2** | Summarizes routes in the Level-2 area.  If no level is specified, Level-2 routes are summarized. | - |
| **level-1-2** | Summarizes routes in Level-1 and Level-2 areas. | - |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An IS-IS routing table on a medium or large IS-IS network may contain a large number of routing entries. Storing the routing entries consumes a large number of memory resources, and transmitting and processing such routing information consumes a large number of network resources. IS-IS route summarization can solve this problem.Route summarization allows multiple routes with the same IPv6 prefix to be summarized into one route, which reduces the number of routing entries and system resource consumption. In addition, if a specific link frequently alternates between up and down, the link status changes will not be advertised to devices that are located beyond the summary route network segment, preventing route flapping and improving network stability.Configuring route summarization does not affect the routing table on a local device. Each specific route is displayed in the routing table. Configuring route summarization, however, reduces LSPs to be flooded. Any device that receives the LSP from the summarization-capable router has only one summary route in its routing table.

**Prerequisites**

An IS-IS process has been created using the **isis** command, and IPv6 has been enabled for this process using the **ipv6 enable** command.

**Precautions**

* The routes to be summarized can be IS-IS routes or imported IPv6 routes. The cost of the summary route is the smallest cost of all the summarized routes.
* The explicit parameter indicates that the summary route takes effect only for a specific algorithm. After this field is configured, if the algorithm of a specific route is not 0, the specific route does not participate in summarization.

Example
-------

# Set a summarized route 2001:db8::/32.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] ipv6 summary 2001:db8:: 32

```