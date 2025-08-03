Verifying the Configuration
===========================

After carrier's carrier is configured, you can check information about public network routes and VPN routes on PEs and CEs of the Level 2 carrier and Level 1 carrier.

#### Prerequisites

The carrier's carrier function has been configured.


#### Procedure

* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check routing tables of the public network on PEs and CEs of both the Level 1 carrier and Level 2 carrier's networks.
* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* command to check routing tables of the private network on the Level 1 carrier PE and the Level 2 carrier PE.