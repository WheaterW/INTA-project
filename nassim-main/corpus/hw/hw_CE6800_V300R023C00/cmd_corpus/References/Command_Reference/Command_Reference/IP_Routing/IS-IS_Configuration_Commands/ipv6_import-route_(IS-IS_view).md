ipv6 import-route (IS-IS view)
==============================

ipv6 import-route (IS-IS view)

Function
--------



The **ipv6 import-route** command enables IS-IS to import IPv6 routes from other protocols.

The **undo ipv6 import-route** command disables IS-IS from importing IPv6 routes from other protocols.



By default, IS-IS does not import IPv6 routes from other protocols.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 import-route** { **direct** | **static** | { **ospfv3** | **ripng** | **isis** } [ *process-id* ] | **bgp** } [ **cost** *cost* | **tag** *tag* | { **route-policy** *route-policy-name* } | [ **level-1** | **level-2** | **level-1-2** ] ] \*

**ipv6 import-route** { { **ospfv3** | **ripng** | **isis** } [ *process-id* ] | **bgp** | **direct** } **inherit-cost** [ { **level-1** | **level-2** | **level-1-2** } | **tag** *tag* | **route-policy** *route-policy-name* ] \*

**undo ipv6 import-route** { **direct** | **static** | { **ospfv3** | **ripng** | **isis** } [ *process-id* ] | **bgp** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **direct** | Imports direct routes. | - |
| **static** | Imports static routes. | - |
| **ospfv3** | Imports OSPFv3 routes. | - |
| **ripng** | Imports RIPng routes. | - |
| **isis** | Imports IS-IS routes. Before you specify this parameter, enable an IS-IS process with a.  process-id different from the local one. | - |
| *process-id* | Specifies the process ID of the imported protocol. | The value is an integer ranging from 1 to 4294967295. The default value is 1. |
| **bgp** | Imports BGP routes. | - |
| **cost** *cost* | Specifies a cost for the imported route. | The value ranges from 0 to 4261412864, regardless of cost types. |
| **tag** *tag* | Assigns administrative tags to the imported routes. | The value is an integer ranging from 1 to 4294967295. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy so that only the routes that match the route-policy can be imported. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **level-1** | Imports routes to the Level-1 routing table. | - |
| **level-2** | Imports routes to the Level-2 routing table. | - |
| **level-1-2** | Imports routes to Level-1 and Level-2 routing tables.  If no level is specified in the command, routes are imported to the Level-2 routing table by default. | - |
| **inherit-cost** | Retains the original cost of the imported route. If this parameter is specified, you cannot configure the cost and cost type for the routes imported by IS-IS. | - |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When IS-IS and other routing protocols are deployed on a network, you can enable the traffic within an IS-IS domain to reach a destination outside the IS-IS domain using either of the following methods:

* Run the **ipv6 default-route-advertise** command to configure boundary devices in the IS-IS domain to advertise default routes to the IS-IS domain.
* Run the **ipv6 import-route** command to configure boundary devices in the IS-IS domain to import routes from other routing domains into the IS-IS domain.If there are multiple boundary devices in the IS-IS domain, optimal routes destined for another routing domain need to be selected. This requires all devices in the IS-IS domain learn all or some external routes.When the routes of other protocols are imported, you can set the cost values and types for the imported routes be specifying cost. You can also configure IS-IS to retain the original cost values of the imported routes by specifying inherit-cost. If you do not specify either cost or inherit-cost, the cost of the imported routes is 0.

**Prerequisites**

An IS-IS process has been created using the **isis** command, and the IPv6 has been enabled on IS-IS process using the **ipv6 enable** command.

**Configuration Impact**

1. Importing routes of other protocols may cause routing loops. Therefore, exercise caution when using this command. You are advised to use a route-policy when importing routes.
2. After a policy for importing routes is configured using the route-policy parameter in the command, the IS-IS process can import only the routes that meet the policy. This prevents the device from passively importing unnecessary routes. If no policy is specified for importing routes, a large number of unexpected routes may be imported. As a result, the number of routes exceeds the upper limit or the memory is overloaded.

**Precautions**

If no route-policy is used during route import, loops may occur or a large number of unexpected routes may be imported, causing problems such as route threshold crossing or memory overload. Therefore, you are advised to use a route-policy when importing routes.You are advised to configure cost inheritance to prevent routing loops.According to IS-IS, an IS-IS process supports a maximum of 256 LSP fragments. If an IS-IS process imports too many routes, the LSP fragment capacity may be insufficient, causing information loss. In this case, you can disable IS-IS from importing unnecessary routes or run the **lsp-fragment-extend** command to enable LSP fragment extension on the IS-IS device.When locator routes are leaked between IS-IS levels or imported between processes, locator TLVs are advertised in the target area by default. This behavior may affect path calculation of devices in the target area. You can use segment-routing ipv6 locator-inter-area disable to eliminate the impact.


Example
-------

# Configure IS-IS to import a static route and set the cost for the imported route to 15.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] ipv6 import-route static cost 15

```