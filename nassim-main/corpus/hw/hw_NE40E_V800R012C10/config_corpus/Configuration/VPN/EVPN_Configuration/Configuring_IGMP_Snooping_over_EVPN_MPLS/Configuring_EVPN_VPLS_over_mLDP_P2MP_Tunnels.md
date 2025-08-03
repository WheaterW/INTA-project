Configuring EVPN VPLS over mLDP P2MP Tunnels
============================================

An EVPN can carry multicast services. To reduce redundant traffic and conserve bandwidth resources, you can configure EVPN to use mLDP P2MP tunnels for service transmission.

#### Usage Scenario

Multicast services, such as IPTV, multimedia conferencing, and Massive Multiplayer Online Role Playing Game (MMORPG) services, are becoming more and more common. As a result, the number of multicast services carried over EVPNs is growing. On the network shown in [Figure 1](#EN-US_TASK_0172370496__fig81422167111), PE1 is the root node, and PE2 and PE3 are leaf nodes. The multicast source and the receiver are on the access side. By default, an EVPN sends multicast service traffic from PE1 to PE2 and PE3 by means of ingress replication. Specifically, PE1 replicates a multicast packet into two copies and sends them to the P. The P then sends one copy to PE2 and the other copy to PE3. For each additional receiver, an additional copy of the multicast packet is sent. This increases the volume of traffic on the link between PE1 and the P, consuming bandwidth resources. To conserve bandwidth resources, you can configure EVPN to use mLDP P2MP tunnels to transmit multicast services. After the configuration is complete, PE1 sends only one copy of multicast traffic to the P. The P replicates the multicast traffic into copies and sends them to the leaf nodes, reducing the volume of traffic between PE1 and P.

**Figure 1** Carrying multicast services over an EVPN  
![](figure/en-us_image_0000001189114700.png)

#### Pre-configuration Tasks

Before configuring EVPN VPLS over mLDP P2MP tunnels, complete the following task:

* [Configure BD EVPN functions](dc_vrp_evpn_cfg_0065.html) on the EVPN.

#### Procedure

* Perform the following steps on the root node:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode**
     
     
     
     The view of a BD EVPN instance is displayed.
  3. Run [**inclusive-provider-tunnel**](cmdqueryname=inclusive-provider-tunnel)
     
     
     
     The EVI-IPMSI view is created and displayed.
  4. Run [**root**](cmdqueryname=root)
     
     
     
     The current device is specified as the root node for the multicast EVPN, and the EVI I-PMSI root view is displayed.
  5. Run [**mldp p2mp**](cmdqueryname=mldp+p2mp)
     
     
     
     An mLDP P2MP tunnel is specified for the BD EVPN instance to carry multicast services, and the EVI-IPMSI-ROOT-MLDP view is displayed.
  6. Run [**root-ip**](cmdqueryname=root-ip) *ip-address*
     
     
     
     An IP address is specified for the root node of the mLDP P2MP tunnel.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the EVI-IPMSI-ROOT view.
  8. (Optional) Run [**data-delay-time**](cmdqueryname=data-delay-time) *delay-time*
     
     
     
     A hold-off time for the mLDP P2MP tunnel to go up is set. If you want the mLDP P2MP tunnel to go up after all leaf nodes are configured, run this command to set a hold-off time for the mLDP P2MP tunnel to go up.
  9. (Optional) Run [**data-switch disable**](cmdqueryname=data-switch+disable)
     
     
     
     Multicast traffic is disabled from being forwarded through a P2P tunnel if the mLDP P2MP tunnel goes Down.
     
     Before an mLDP P2MP tunnel carries multicast services, you can establish a bypass tunnel to provide mLDP P2MP FRR protection for the primary mLDP P2MP tunnel. The bypass tunnel is a P2P tunnel. If both the primary P2MP tunnel and bypass P2P tunnel go down, the backup mLDP P2MP tunnel carries multicast services. After the bypass P2P tunnel for the primary mLDP P2MP tunnel goes Up, the P2P tunnel carries multicast services. Because the primary mLDP P2MP tunnel remains Down, a leaf node also receives multicast traffic from the backup mLDP P2MP tunnel. As a result, the leaf node receives and forwards duplicate copies of traffic. To prevent this issue, run this command to disable multicast traffic from being forwarded through a P2P tunnel when the mLDP P2MP tunnel goes Down.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Perform the following steps on each leaf node:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode**
     
     
     
     The view of a BD EVPN instance is displayed.
  3. Run [**inclusive-provider-tunnel**](cmdqueryname=inclusive-provider-tunnel)
     
     
     
     The EVI I-PMSI view is created and displayed.
  4. Run [**leaf**](cmdqueryname=leaf)
     
     
     
     The current device is specified as a leaf node for the multicast EVPN.
  5. (Optional) Run [**root-ip**](cmdqueryname=root-ip) *root-ip* **use-next-hop**
     
     
     
     In a cross-IGP-area EVPN VPLS scenario, you must run this command on a leaf node to configure the next hop of a BGP EVPN route as the root node IP address, which is used as the IP address of the ABR on the area border. Without this configuration, EVPN cannot use an mLDP P2MP tunnel for service transmission.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

Run the [**display evpn vpn-instance**](cmdqueryname=display+evpn+vpn-instance) **name** *vpn-instance-name* **inclusive-provider-tunnel** **verbose** command to check information about tunnels to which a multicast EVPN recurses.