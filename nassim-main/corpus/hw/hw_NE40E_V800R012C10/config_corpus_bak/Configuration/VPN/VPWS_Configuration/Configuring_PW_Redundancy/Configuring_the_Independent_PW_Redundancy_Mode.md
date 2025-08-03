Configuring the Independent PW Redundancy Mode
==============================================

The independent PW redundancy mode allows a public network fault to trigger only the public network link switchover.

#### Context

In independent PW redundancy mode, the active/standby status of PWs is determined through signaling-based negotiation. When creating PWs on the local end, configure two PWs that connect to two remote PEs (one PW per PE). After they are configured, the two PWs are both in the primary state on the local end. The remote PEs then determine their status by means of E-Trunk or mVRRP, with one PE in the active state and the other in the standby state. Finally, the PW endpoints determine the primary and secondary PWs through negotiation. The independent mode applies to scenarios where PW redundancy is associated with E-Trunk. The independent mode, together with the bypass PW, can prevent links on the AC side from sensing faults on the network side but cannot prevent links on the network side from sensing faults on the AC side.


#### Procedure

1. Create a primary PW. For details, see [Configuring a VPWS PW](dc_vrp_vpws_cfg_3006.html).
2. Create a secondary PW. For details, see [(Optional) Configuring a Secondary VPWS Connection](dc_vrp_vpws_cfg_5002.html).
3. Configure the independent PW redundancy mode on the local device.
   1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the AC interface view.
   2. Run the [**mpls l2vpn redundancy**](cmdqueryname=mpls+l2vpn+redundancy) **independent** command to configure the independent PW redundancy mode.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
4. (Optional) Configure VPWS switching. For details, see [Configuring VPWS Switching](dc_vrp_vpws_cfg_5001.html).
   
   
   
   VPWS switching needs to be configured on SPEs during the establishment of an MS-PW. PW redundancy supports only dynamic VPWS switching.
5. Configure a bypass PW on the remote device.
   1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the AC interface view.
   2. Run the [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *tnl-policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** ] | **access-port** | **ignore-standby-state** ] \* **bypass** command to configure a bypass PW.
6. (Optional) Configure L2VPN dual-fed to reduce traffic loss caused by VPWS switching.
   
   
   * On an IPv4 network with PW redundancy configured, you can configure the following functions:
     
     + Run the [**mpls l2vpn stream-dual-receiving**](cmdqueryname=mpls+l2vpn+stream-dual-receiving) command to enable both the primary and secondary PWs on a CSG to receive packets. This helps prevent packet loss during a primary/secondary PW switchover.
     + Run the [**mpls l2vpn arp-dual-sending**](cmdqueryname=mpls+l2vpn+arp-dual-sending) [ **expire-time** *expire-time-value* ] command to configure the primary and secondary PWs to transparently transmit ARP packets. This helps reduce the packet loss caused by node failures of the primary PW.
       
       If you specify **expire-time** *expire-time*, the primary and secondary PWs will set an aging timer for transparently transmitted ARP packets.
   * On an IPv6 network with PW redundancy configured, run the [**mpls l2vpn nd-dual-sending**](cmdqueryname=mpls+l2vpn+nd-dual-sending) [ **expire-time** *expire-time* ] command to enable ND packet dual-fed. On an L2VPN with PW redundancy configured, only the primary PW transparently transmits ND packets, and the secondary PW cannot learn user-side ND entries. If the primary PW fails, the secondary PW learns user-side ND entries from received traffic. Traffic received during the ND entry learning process, however, is discarded. After ND packet dual-fed is enabled, both the primary and secondary PWs can transparently transmit ND packets, reducing packet loss.
     
     If **expire-time** *expire-time* is specified, the primary and secondary PWs both send ND packets, and an aging timer is set for ND entries.
7. In independent PW redundancy mode, ensure that the remote PEs determine their active/standby status by means of E-Trunk or mVRRP.
   
   
   
   If the remote devices determine their active/standby status by means of VRRP, run the [**mpls l2vc track admin-vrrp**](cmdqueryname=mpls+l2vc+track+admin-vrrp) **interface** *interface-type interface-number* **vrid** *virtual-router-id* **pw-redundancy** command to bind the service PW to the mVRRP group.
   
   **pw-redundancy** is mandatory in this case. If this parameter is not configured, after the PW is bound to the mVRRP group, packet forwarding on the local PW will be interrupted if mVRRP is in the standby state. If the parameter is configured, whether packets can be forwarded depends on the negotiated primary/secondary status of the local and remote PWs.
   
   If the active/standby status of the remote device is determined through E-Trunk, you do not need to bind the service PW to E-Trunk. For details about the E-Trunk configuration, see [Configuring PW Status Negotiation](dc_vrp_vpws_cfg_6020.html).
8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.