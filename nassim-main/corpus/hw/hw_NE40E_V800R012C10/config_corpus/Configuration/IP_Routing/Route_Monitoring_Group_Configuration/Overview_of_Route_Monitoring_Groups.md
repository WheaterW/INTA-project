Overview of Route Monitoring Groups
===================================

Overview of Route Monitoring Groups

#### Definition

All monitored network-side routes of the same type can be added to a group called a route monitoring group. Each route monitoring group is identified by a unique name.

A route monitoring group monitors the status of its member routes, each of which has a down-weight. The down-weight indicates the link quality. The higher the value, the more important the route. The down-weight can be set based on parameters, such as the link bandwidth, rate, and cost.

* If a route in the route monitoring group goes Down, its down-weight is added to the down-weight sum of the route monitoring group.
* If a route in the route monitoring group goes Up again, its down-weight is subtracted from the down-weight sum of the route monitoring group.


#### Purpose

Service modules can be associated with the route monitoring group, with a threshold configured for each service module for triggering a primary/backup access-side link switchover. If the down-weight sum of the route monitoring group reaches the threshold of a service module, the routing management (RM) module notifies the service module to switch services from the primary link to the backup link. If the down-weight sum of the route monitoring group falls below the threshold, the RM module notifies the service module to switch services back.


#### Benefits

If a service module is associated with a route monitoring group in a dual-system backup scenario, services can be switched to the backup link if the primary link fails, therefore preventing traffic overload and forwarding failures.