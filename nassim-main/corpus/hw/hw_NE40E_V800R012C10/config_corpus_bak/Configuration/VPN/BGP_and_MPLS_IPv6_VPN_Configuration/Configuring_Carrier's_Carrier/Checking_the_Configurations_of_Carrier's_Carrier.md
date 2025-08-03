Checking the Configurations of Carrier's Carrier
================================================

After carrier's carrier is configured, you can view information about public network routes and VPN routes on PEs and CEs of the Level 2 carrier and Level 1 carrier.

#### Prerequisites

The carrier's carrier function has been configured.
#### Procedure

* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check the public routing tables on the CEs and PEs of the Level 1 carrier and PEs of the Level 2 carrier.
* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) [ [ *filter-option* ] [ **verbose** ] | **statistics** ] command to check the routing tables on the CEs of the Level 2 carrier.
* Run the [**display
  ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) [ *vpn-instance-name* ] command to check the VPN routing tables on the PEs of the Level 1 carrier.
* Run the [**display
  ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) [ *vpn-instance-name* ] command to check the VPN routing tables on the PEs of the Level 2 carrier.