import-route (IS-IS view)
=========================

import-route (IS-IS view)

Function
--------



The **import-route** command enables IS-IS to import routes from other protocols.

The **undo import-route** command disables IS-IS from importing routes from other protocols.



By default, IS-IS does not import routes from any other protocol.


Format
------

**import-route** { **direct** | **static** | **rip** [ *process-id* ] | **bgp** [ **permit-ibgp** ] } [ **cost-type** { **external** | **internal** } | **cost** *cost* | **tag** *tag* | { **route-policy** *route-policy-name* } | [ **level-1** | **level-2** | **level-1-2** ] ] \*

**import-route** { **ospf** | **isis** } [ *process-id* ] [ **cost-type** { **external** | **internal** } | **cost** *cost* | **tag** *tag* | { **route-policy** *route-policy-name* } | [ **level-1** | **level-2** | **level-1-2** ] ] \*

**import-route** { **rip** [ *process-id* ] | **bgp** [ **permit-ibgp** ] | **direct** } **inherit-cost** [ { **level-1** | **level-2** | **level-1-2** } | **tag** *tag* | **route-policy** *route-policy-name* ] \*

**import-route** { **ospf** | **isis** } [ *process-id* ] **inherit-cost** [ { **level-1** | **level-2** | **level-1-2** } | **tag** *tag* | { **route-policy** *route-policy-name* } ] \*

**undo import-route** { **direct** | **static** | { **ospf** | **rip** | **isis** } [ *process-id* ] | **bgp** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **direct** | Imports direct routes. | - |
| **static** | Imports active static routes. | - |
| **rip** | Imports RIP routes. | - |
| *process-id* | Displays information about the ABR or ASBR of an OSPF route in a specified OSPF process. | The value is an integer ranging from 1 to 4294967295. The default value is 1. |
| **bgp** | Imports BGP routes. | - |
| **permit-ibgp** | Imports IBGP routes in a public network instance.  If you do not specify this parameter, the device imports EBGP routes only. | - |
| **cost-type** | The cost type of a route. | - |
| **external** | Sets the cost type to IS-IS external. | - |
| **internal** | Sets the cost type to IS-IS internal. | - |
| **cost** *cost* | Specifies the cost for imported routes. | The value is an integer, and the value range depends on the cost type.   * When the cost type of the device is wide or wide-compatible, the value ranges from 0 to 4261412864. * In other cases, the value ranges from 0 to 63.   The default value is 0.  To set the cost style, use the cost-style command. |
| **tag** *tag* | Specifies the administrative tag assigned to the imported routes. | The value is an integer ranging from 1 to 4294967295. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **level-1** | Imports routes to the Level-1 routing table. | - |
| **level-2** | Imports routes to the Level-2 routing table. | - |
| **level-1-2** | Indicates that routes are imported into Level-1 and Level-2 routing tables. | - |
| **ospf** | Imports OSPF routes. | - |
| **isis** | Imports IS-IS routes.  Before specifying this parameter, create an IS-IS process with a process ID different from the local process ID. | - |
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

When IS-IS and other routing protocols are deployed on a network, you can use either of the following methods to allow traffic within an IS-IS domain to reach a destination outside the IS-IS domain:

* Run the **default-route-advertise** command on border devices to configure them to advertise default routes to the IS-IS domain.
* Run the **import-route** command on border devices to import routes from other routing domains to IS-IS.If there is more than one border device in an IS-IS domain, the optimal route to another routing domain needs to be selected. In this case, devices in the IS-IS domain must learn all or some external routes. In this case, you can configure the border devices to import routes from other routing domains to IS-IS.To make the route cost more suitable for actual applications, you can set cost-type and cost for imported routes. If the cost and cost type are not specified, the default cost 0 and cost type (external) are used. You can also specify inherit-cost to configure IS-IS to retain the original costs of the imported external routes and use the original costs of these routes during route advertisement and calculation.In the IS-IS view, this command is valid only for the base topology. In the topology view of an IS-IS process, this command is valid for the local topology, and only direct, IS-IS, and static routes can be imported.

**Prerequisites**



An IS-IS process has been created using the **isis** command, and the protocol from which routes are imported has been configured.



**Configuration Impact**



After IS-IS imports routes from other protocols, the default tag value is 0. If the default tag value is used, route loop prevention may fail, causing routing loops.IS-IS does not have a good mechanism to prevent loops of imported external routes. Therefore, exercise caution when configuring IS-IS to import external routes to prevent loops caused by manual configurations.After a policy for importing routes is configured using the route-policy parameter in the command, the IS-IS process can import only the routes that meet the policy. This prevents the device from passively importing unnecessary routes. If no policy is specified for importing routes, a large number of unexpected routes may be imported. As a result, the number of routes exceeds the upper limit or the memory is overloaded.



**Precautions**



The import-route (IS-IS) command cannot import external default routes. To advertise the external default routes learned by IS-IS when updating the routing table within an IS-IS area, run the default-route-advertise (IS-IS) command.If no routing policy is used during route import, loops may occur or a large number of unexpected routes may be imported, causing problems such as route threshold crossing or memory overload. Therefore, you are advised to use the routing policy when importing routes.You are advised to configure cost inheritance to prevent routing loops.According to IS-IS, an IS-IS process supports a maximum of 256 LSP fragments. If an IS-IS process imports too many routes, the LSP fragment capacity may be insufficient, causing information loss. In this case, you can disable IS-IS from importing unnecessary routes or run the **lsp-fragment-extend** command to enable LSP fragment extension on the IS-IS device.




Example
-------

# Configure IS-IS to import static routes and set the cost of the route to 15.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] import-route static cost 15

```