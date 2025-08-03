Verifying the Configuration of Association Between Direct Routes and a VRRP Group
=================================================================================

After you associate direct routes with a Virtual Router Redundancy Protocol (VRRP) group, you can view information about the VRRP group and information in the routing table of the previous-hop device on the network side.

#### Prerequisites

Direct routes have been associated with a VRRP group.


#### Procedure

* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on the backup device in the VRRP group to check the modified direct route costs in the IP routing table.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) *ip-address* command on the VRRP group's previous-hop device on the network side to check whether network-to-user traffic lows through the master device in the VRRP group.