Verifying the DHCPv4 Parameter Configuration
============================================

After adjusting DHCPv4 parameters, verify DHCPv4 server information and the storage path of the DHCPv4 data.

#### Prerequisites

DHCPv4 parameters have been adjusted.


#### Procedure

* Run the [**display dhcp-server item**](cmdqueryname=display+dhcp-server+item) *ip-address* [ **vpn-instance** *vpn-instance* ] command to check DHCPv4 server information.
* Run the [**display dhcp server database**](cmdqueryname=display+dhcp+server+database) command to check the storage path and file information in DHCPv4 data.
* Run the [**display dhcp upgrade**](cmdqueryname=display+dhcp+upgrade) command to check the lease configuration for DHCPv4 users to determine the time when the NE40E restarts.