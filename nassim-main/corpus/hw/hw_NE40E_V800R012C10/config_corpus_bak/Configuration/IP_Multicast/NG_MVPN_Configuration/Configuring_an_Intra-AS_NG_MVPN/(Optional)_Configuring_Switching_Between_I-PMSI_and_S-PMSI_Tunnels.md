(Optional) Configuring Switching Between I-PMSI and S-PMSI Tunnels
==================================================================

(Optional)_Configuring_Switching_Between_I-PMSI_and_S-PMSI_Tunnels

#### Context

An NG MVPN uses the I-PMSI tunnel to send multicast data to receivers. The I-PMSI tunnel transmits multicast traffic to all PEs on the same MVPN, regardless of whether these PEs have receivers. If some PEs do not have receivers, this implementation will cause redundant traffic, wasting bandwidth resources and increasing PEs' burdens. Selective-PMSI (S-PMSI) tunnels can address the preceding issue. After multicast traffic data is switched from an I-PMSI tunnel to an S-PMSI tunnel, only PEs that have receivers can receive the traffic. Therefore, S-PMSI tunnels can prevent redundant traffic, reduce bandwidth consumption, and relieve the workload of PEs.


#### Procedure

* Perform the following steps on a PE to be configured as a sender PE:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The VPN instance IPv4 address family view is displayed.
  4. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
     
     
     
     Multicast routing is enabled for the VPN instance IPv4 address family.
  5. Run [**mvpn**](cmdqueryname=mvpn)
     
     
     
     The VPN instance IPv4 address family MVPN view is displayed.
  6. (Optional) Run the [**ipmsi-to-spmsi switch immediately**](cmdqueryname=ipmsi-to-spmsi+switch+immediately) command to enable immediate switching from an I-PMSI tunnel to an S-PMSI tunnel.
     
     
     
     After immediate switching from an I-PMSI tunnel to an S-PMSI tunnel is configured, upon the generation of an (S, G) entry with an MTI as the outbound interface on the sender PE, an S-PMSI tunnel is created and traffic is immediately switched from an I-PMSI tunnel to the S-PMSI tunnel.
     
     Compared with the original implementation, immediate switching from an I-PMSI tunnel to an S-PMSI tunnel allows traffic corresponding to an (S, G) entry to be switched to an S-PMSI tunnel earlier, thereby reducing multicast traffic loss.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After this command is run, the switching threshold configured in the MVPN S-PMSI view does not take effect.
  7. Run [**spmsi-tunnel**](cmdqueryname=spmsi-tunnel)
     
     
     
     The MVPN S-PMSI view is displayed.
  8. Run [**group**](cmdqueryname=group+MVPN+S-PMSI) *group-address* { *group-mask* | *group-mask-length* } [ **source** *source-address* { *source-mask* | *source-mask-length* } ] [ **threshold** *threshold-value* ] { **mldp** | **rsvp-te p2mp-template** *p2mp-te-template-name* } [ **limit** *number* ]
     
     
     
     An address pool range and criteria for switching between I-PMSI and S-PMSI tunnels are configured.
  9. (Optional) Run [**switch-delay**](cmdqueryname=switch-delay) *switch-delay*
     
     
     
     A delay is configured for the VPN instance to switch multicast traffic from an I-PMSI tunnel to an S-PMSI tunnel.
     
     
     
     The sender PE starts a switchover delay timer when using an I-PMSI tunnel to transmit multicast traffic. The sender PE keeps monitoring the multicast traffic forwarding rate before the switchover delay timer expires. If the forwarding rate is consistently higher than the specified switchover threshold throughout the timer lifecycle, the sender PE switches multicast traffic from the I-PMSI tunnel to an S-PMSI tunnel. If the forwarding rate is consistently lower than the specified switchover threshold throughout the timer lifecycle, the sender PE still uses the I-PMSI tunnel to transmit multicast traffic.
  10. Run [**holddown-time**](cmdqueryname=holddown-time) *interval*
      
      
      
      The delay for switching traffic from an S-PMSI tunnel back to an I-PMSI tunnel is set.
      
      
      
      In some cases, the multicast data forwarding rate may fluctuate around the specified switching threshold. To prevent multicast data from being frequently switched between the I-PMSI and S-PMSI tunnels, the sender PE does not immediately switch data back to the I-PMSI tunnel when detecting that the forwarding rate is below the specified switching threshold. Instead, the sender PE starts a switchback hold timer. This step configures the timer value. Before the timer expires, the sender PE continues to detect the multicast data forwarding rate. If the forwarding rate is consistently below the specified switching threshold throughout the timer lifecycle, the sender PE switches multicast data back to the I-PMSI tunnel. If the rate remains consistently lower than the threshold throughout the timer period, the device switches multicast traffic back to the I-PMSI tunnel. Otherwise, the device continues to use the S-PMSI tunnel to forward multicast traffic.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* (Optional) Perform the following steps on each receiver PE:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The VPN instance IPv4 address family view is displayed.
  4. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
     
     
     
     Multicast routing is enabled for the VPN instance IPv4 address family.
  5. Run [**mvpn**](cmdqueryname=mvpn)
     
     
     
     The VPN instance IPv4 address family MVPN view is displayed.
  6. (Optional) Run [**tunnel-detect-delay**](cmdqueryname=tunnel-detect-delay) *tunnel-detect-delay*
     
     
     
     A delay for checking tunnel status when the bearer tunnel of VPN instance multicast data changes is configured.
     
     
     
     If dual-root 1+1 protection is configured for P2MP RSVP-TE tunnels in an I-PMSI scenario, a primary/backup I-PMSI tunnel switchover may be performed before an S-PMSI tunnel is created. To resolve this problem, a tunnel status check delay timer needs to be started on the leaf PE. Before the timer expires, the leaf PE deletes the tunnel protection group and does not check the status of the primary I-PMSI or S-PMSI tunnel. After the timer expires, the leaf PE starts to check the primary I-PMSI or S-PMSI tunnel status again.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.