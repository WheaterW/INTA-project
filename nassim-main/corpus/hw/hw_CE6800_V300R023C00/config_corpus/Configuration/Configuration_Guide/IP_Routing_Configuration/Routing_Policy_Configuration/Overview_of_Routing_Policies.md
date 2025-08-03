Overview of Routing Policies
============================

Overview of Routing Policies

#### Definition

Routing policies are used to filter routes and set attributes (including reachability attributes) for the routes in an attempt to change the paths through which network traffic passes as needed.


#### Purpose

Before advertising, receiving, and importing routes, a device enforces certain policies based on actual networking requirements to filter routes and change the attributes of the routes. [Table 1](#EN-US_CONCEPT_0000001176663529__table13861145817533) describes the functions of routing policies.

**Table 1** Routing policy functions
| Function | Description |
| --- | --- |
| Controls route advertisement. | Only routes that match the rules specified in a policy are advertised. |
| Controls route acceptance. | Only wanted and valid routes are accepted, which reduces the routing table size and improves network security. |
| Filters and controls routes to be imported. | To enrich routing information, a routing protocol may import routes discovered by other routing protocols. A device can be configured to import only the routes that satisfy the conditions of a routing policy and set attributes of the imported routes as required. |
| Sets attributes of routes matching specified conditions. | Attributes of routes that match specified routing policies can be modified as needed. |



#### Benefits

Routing policies offer the following benefits:

* Control the size of routing tables to conserve system resources.
* Improve network security by controlling route advertisement and acceptance.
* Improve network performance by allowing you to modify route attributes for proper traffic planning.