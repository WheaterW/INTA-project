Understanding RIPng Routing Loops
=================================

Understanding RIPng Routing Loops

#### Context

RIPng is a distance vector routing protocol. As RIPng devices advertise their routing tables to neighbors, routing loops may occur.

RIPng provides the following mechanisms to prevent routing loops:

* Counting to infinity: RIPng defines the metric of 16 as infinity. If the metric of a route reaches 16 due to a routing loop, this route is considered unreachable.
* Split horizon: With this mechanism, a RIPng device will not send the route learned from an interface to neighbors through the same interface. This mechanism reduces bandwidth consumption and avoids routing loops.
* Poison reverse: This mechanism allows a RIPng interface to set the cost of the route that it learns from a neighbor to 16 (indicating that the route is unreachable) and then send the route back to the neighbor. As a result, the neighbor deletes the useless route from its routing table to prevent routing loops.
* Suppress timer: This timer can prevent routing loops and reduce the possibility of learning incorrect routing information after incorrect routes are received.![](public_sys-resources/note_3.0-en-us.png) 
  
  If both split horizon and poison reverse are configured, only poison reverse takes effect.