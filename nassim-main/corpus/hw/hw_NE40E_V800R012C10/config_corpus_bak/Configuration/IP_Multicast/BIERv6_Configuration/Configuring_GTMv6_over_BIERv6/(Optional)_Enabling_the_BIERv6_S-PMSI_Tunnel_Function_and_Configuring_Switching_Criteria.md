(Optional) Enabling the BIERv6 S-PMSI Tunnel Function and Configuring Switching Criteria
========================================================================================

An S-PMSI tunnel connects to some PEs on the network-side public network and is used to transmit user-side public network multicast traffic to the PEs that require the traffic. To enable the S-PMSI tunnel function, perform this task.

#### Context

Perform this task only on the sender PE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast ipv6 vpn-public**](cmdqueryname=multicast+ipv6+vpn-public)
   
   
   
   The public network IPv6 address family MVPN view is displayed.
3. (Optional) Run [**bier load-balance-entropy source-group**](cmdqueryname=bier+load-balance-entropy+source-group)
   
   
   
   The entropy mode is configured for GTMv6 over BIERv6 load balancing.
   
   
   
   Perform this operation only if BIERv6 load balancing has been enabled using the [**max-load-balance**](cmdqueryname=max-load-balance) *number* command.
4. Run [**spmsi-tunnel**](cmdqueryname=spmsi-tunnel)
   
   
   
   The public network IPv6 MVPN S-PMSI view is displayed.
5. Run [**group**](cmdqueryname=group) *group-address* *group-mask-length* [ **source** *source-address* *source-mask-length* ] [ **threshold** *threshold-value* ] { **bier** [ **sub-domain** *sub-domain-val* ] [ **bsl** { **64** | **128** | **256** } ] } [ **limit** *number* ]
   
   
   
   The address pool range and criteria for switching between I-PMSI and S-PMSI tunnels are configured.
6. (Optional) Run [**switch-delay**](cmdqueryname=switch-delay) *switch-delay*
   
   
   
   A delay to switch multicast traffic of the VPN instance from the I-PMSI tunnel to an S-PMSI tunnel is configured.
   
   
   
   After the switchover delay is configured using this command, the device starts the delay timer when using the I-PMSI tunnel to transmit multicast traffic. The device keeps monitoring the multicast traffic forwarding rate before the switchover delay timer expires. If the forwarding rate is consistently higher than the specified switchover threshold throughout the timer period, the device switches multicast traffic from the I-PMSI tunnel to an S-PMSI tunnel. If the forwarding rate is consistently lower than the specified switchover threshold throughout the timer period, the device still uses the I-PMSI tunnel to transmit multicast traffic.
7. (Optional) Run [**tunnel-withdraw-delay**](cmdqueryname=tunnel-withdraw-delay) *tunnel-withdraw-delay*
   
   
   
   A delay is configured to withdraw the S-PMSI tunnel after traffic is switched from the S-PMSI tunnel back to the I-PMSI tunnel.
8. Run [**holddown-time**](cmdqueryname=holddown-time) *interval*
   
   
   
   A delay for switching traffic from an S-PMSI tunnel back to the I-PMSI tunnel is configured.
   
   
   
   In some cases, the multicast traffic forwarding rate may fluctuate around the specified switchover threshold. To prevent multicast data traffic from being frequently switched between S-PMSI and I-PMSI tunnels, the device starts the switchback delay timer when the forwarding rate falls below the specified threshold rather than performing an immediate switchback. The device keeps monitoring the forwarding rate before the delay timer for the switchback from the S-PMSI tunnel expires. If the rate remains consistently lower than the threshold throughout the timer period, the device switches multicast traffic back to the I-PMSI tunnel. Otherwise, the device still uses the S-PMSI tunnel to forward multicast traffic.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the public network IPv6 MVPN S-PMSI view.
10. Run [**quit**](cmdqueryname=quit)
    
    
    
    Exit the public network IPv6 address family MVPN view.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.