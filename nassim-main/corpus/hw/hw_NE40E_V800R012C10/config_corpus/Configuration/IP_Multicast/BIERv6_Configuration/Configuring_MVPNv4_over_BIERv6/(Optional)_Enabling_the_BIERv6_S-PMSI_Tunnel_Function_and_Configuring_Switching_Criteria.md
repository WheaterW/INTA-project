(Optional) Enabling the BIERv6 S-PMSI Tunnel Function and Configuring Switching Criteria
========================================================================================

An S-PMSI tunnel connects some PEs in the same MVPN and is used to transmit VPN data only to the PEs that require the data. To enable the S-PMSI tunnel function, perform this task.

#### Context

Perform this task only on the sender PE.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to enter the VPN instance view.
3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to enter the VPN instance IPv4 address family view.
4. Run the [**mvpn**](cmdqueryname=mvpn) command to enter the VPN instance IPv4 address family MVPN view.
5. (Optional) Run the [**bier load-balance-entropy source-group**](cmdqueryname=bier+load-balance-entropy+source-group) command to configure the entropy mode for MVPNv4 over BIERv6 load balancing.
   
   
   
   Perform this operation only if BIERv6 load balancing has been enabled using the [**max-load-balance**](cmdqueryname=max-load-balance) *number* command.
6. Run the [**spmsi-tunnel**](cmdqueryname=spmsi-tunnel) command to enter the MVPN S-PMSI view.
7. Run the [**group**](cmdqueryname=group) *group-address* { *group-mask* | *group-mask-length* } [ **source** *source-address* { *source-mask* | *source-mask-length* } ] [ **threshold** *threshold-value* ] **bier** [ **sub-domain** *sub-domain-val* ] [ **bsl** { **64** | **128** | **256** } ] [ **limit** *number* ], [**group**](cmdqueryname=group) *group-address* { *group-mask* | *group-mask-length* } **source** **wildcard** **bier** [ **sub-domain** *sub-domain-val* ] [ **bsl** { **64** | **128** | **256** } ] [ **limit** *number* ], or [**group**](cmdqueryname=group) **wildcard** **source wildcard** **bier** [ **sub-domain** *sub-domain-val* ] [ **bsl** { **64** | **128** | **256** } ] command to configure the address pool range and criteria for switching between I-PMSI and S-PMSI tunnels.
   
   
   
   The preceding command without **wildcard** specified is used to match (C-S, C-G) multicast services. The preceding commands with **wildcard** specified are used to match (C-\*, C-G) multicast services.
8. (Optional) Run the [**switch-delay**](cmdqueryname=switch-delay) *switch-delay* command to configure a delay to switch multicast traffic of the VPN instance from the I-PMSI tunnel to an S-PMSI tunnel.
   
   
   
   The device starts a switchover delay timer when using the I-PMSI tunnel to transmit multicast traffic. The device keeps monitoring the multicast traffic forwarding rate before the switchover delay timer expires. If the forwarding rate is consistently higher than the specified switchover threshold throughout the timer lifecycle, the device switches multicast traffic from the I-PMSI tunnel to an S-PMSI tunnel. If the forwarding rate is consistently lower than the specified switchover threshold throughout the timer lifecycle, the device still uses the I-PMSI tunnel to transmit multicast traffic.
9. Run the [**holddown-time**](cmdqueryname=holddown-time) *interval* command to set the delay for switching traffic from an S-PMSI tunnel back to the I-PMSI tunnel.
   
   
   
   In some cases, the multicast traffic forwarding rate may fluctuate around the specified switchover threshold. To prevent multicast data traffic from being frequently switched between S-PMSI and I-PMSI tunnels, the device starts the switchback delay timer when the forwarding rate falls below the specified threshold rather than performing an immediate switchback. The device keeps monitoring the forwarding rate before the switchback delay timer expires. If the rate remains consistently lower than the threshold throughout the timer period, the device switches multicast traffic back to the I-PMSI tunnel. Otherwise, the device still uses the S-PMSI tunnel to forward multicast traffic.
10. Run the [**quit**](cmdqueryname=quit) command to exit the MVPN S-PMSI view.
11. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance IPv4 address family MVPN view.
12. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance IPv4 address family view.
13. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance view.
14. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.