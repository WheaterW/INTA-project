Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on the backup device in the VRRP group to check the adjusted cost for the direct routes in the IP routing table.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) *ip-address* command on the previous-hop device on the network side of the VRRP group to check whether the previous-hop device selects the route passing through the master device in the VRRP group for network-to-user traffic.