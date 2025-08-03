Verifying the MCE (IPv6) Configuration
======================================

After the multi-VPN-instance CE (MCE) is configured, the
VPN routing and forwarding (VRF) table of the MCE contains the routes
to the local area network (LAN) and remote sites for each type of
service.

#### Prerequisites

All MCE configurations are complete.
#### Procedure

* Run the [**display
  ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* [ **verbose** ] command to check the VRF
  table on the MCE.