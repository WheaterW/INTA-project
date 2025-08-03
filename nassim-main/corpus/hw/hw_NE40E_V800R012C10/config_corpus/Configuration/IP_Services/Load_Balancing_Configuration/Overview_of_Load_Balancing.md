Overview of Load Balancing
==========================

Load balancing is classified as equal-cost multiple path (ECMP) or unequal-cost multiple path (UCMP). ECMP is automatically implemented by routing protocols, with no need for manual configuration, whereas UCMP is implemented using commands.

#### Load Balancing Classification

Based on the load balancing traffic among different links, load balancing is classified into two types:

* ECMP evenly balances traffic among multiple equal-cost paths to the same destination, irrespective of bandwidth. Equal-cost paths have the same cost to the destination.
* UCMP proportionally balances traffic among multiple equal-cost paths to the same destination based on different bandwidths, improving bandwidth utilization.