Controlling the Generation of Logs
==================================

To learn system running status or locate faults through logs, you can enable the function to generate logs for reused switch-group addresses.

#### Context

In the VPN instance on the source PE, if the number of multicast data flows that need to be switched is more than the number of group addresses in the switch-group-pool of a switch-multicast distribution tree (MDT), the group addresses in the switch-group-pool can be used repeatedly.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to enter the VPN instance view.
3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to enable the IPv4 address family for the VPN instance and enter the VPN instance IPv4 address family view.
4. Run the [**multicast-domain log switch-group-reuse**](cmdqueryname=multicast-domain+log+switch-group-reuse) command to enable the function to generate logs for reused switch-group addresses.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.