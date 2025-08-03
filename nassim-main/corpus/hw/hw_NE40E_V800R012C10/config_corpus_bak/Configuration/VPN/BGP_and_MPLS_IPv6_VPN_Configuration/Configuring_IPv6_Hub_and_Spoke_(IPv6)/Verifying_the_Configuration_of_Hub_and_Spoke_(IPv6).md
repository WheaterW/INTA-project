Verifying the Configuration of Hub and Spoke (IPv6)
===================================================

After configuring hub & spoke, check VPN routing information
on the PE or CE.

#### Prerequisites

Hub & spoke has been configured.
#### Procedure

* Run the [**display
  ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* command to check routing information about VPN-in and VPN-out on
  the Hub-PE.
* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) command on the Hub-CE and all the Spoke-CEs to check routing
  information.