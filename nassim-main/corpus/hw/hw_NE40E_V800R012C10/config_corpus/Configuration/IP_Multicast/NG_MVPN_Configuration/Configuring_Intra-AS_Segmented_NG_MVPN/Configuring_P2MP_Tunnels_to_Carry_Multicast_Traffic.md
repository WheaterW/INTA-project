Configuring P2MP Tunnels to Carry Multicast Traffic
===================================================

NG MVPN uses P2MP tunnels to carry multicast traffic. You can configure P2MP mLDP or RSVP-TE tunnels as needed.

#### Context

Both P2MP mLDP and RSVP-TE tunnels can be used to carry multicast traffic. [Table 1](#EN-US_TASK_0000001270193585__table_dc_vrp_feature_new_ngmvpn_000401) shows the differences between the two types of tunnels.

**Table 1** Differences between P2MP RSVP-TE and mLDP tunnels
| Category | mLDP Tunnel | RSVP-TE Tunnel |
| --- | --- | --- |
| Characteristics | P2MP mLDP tunnels do not support bandwidth reservation and cannot ensure service quality during network congestion. However, mLDP tunnel configurations are more simple than those of RSVP-TE tunnels. | P2MP RSVP-TE tunnels support bandwidth reservation and can ensure service quality during network congestion. |
| Usage scenario | Networks that do not require control over destination nodes  Networks that do not have high requirements for service quality | Networks that require control over destination nodes  Networks that have high requirements for service quality |
| Signaling packet transmission | Signaling packets do not need to be periodically sent, reducing network pressure. | Signaling packets need to be periodically sent to maintain the tunnel. If a large number of leaf nodes exist, the network is prone to congestion. |

In real-world situations, configure either P2MP mLDP or RSVP-TE tunnels on the ingress node. The type of the tunnel from the intermediate node to the egress is determined by the stitched tunnel's type configured on the intermediate node.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If P2MP RSVP-TE tunnels need to be used, configure a tunnel policy to bind VPN instances to RSVP-TE tunnels.



#### Procedure

* Configure the sender PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**multicast mvpn**](cmdqueryname=multicast+mvpn) *mvpn-id*
     
     
     
     An MVPN ID is set.
  3. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  4. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The VPN instance IPv4 address family view is displayed.
  5. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
     
     
     
     IP multicast routing is enabled in the VPN instance IPv4 address family.
  6. Run [**mvpn**](cmdqueryname=mvpn)
     
     
     
     The VPN instance IPv4 address family MVPN view is displayed.
  7. Run [**sender-enable**](cmdqueryname=sender-enable)
     
     
     
     The PE is configured as a sender PE.
  8. (Optional) Run [**vpn-target (VPN instance IPv4 address family MVPN view)**](cmdqueryname=vpn-target+%28VPN+instance+IPv4+address+family+MVPN+view%29)
     
     
     
     An MVPN target is configured for the VPN instance MVPN address family.
  9. Run [**c-multicast signaling**](cmdqueryname=c-multicast+signaling) **bgp**
     
     
     
     BGP is configured as the signaling protocol for transmitting C-multicast routes.
  10. (Optional) Run either of the following commands to configure the PIM-SM MDT setup mode:
      
      
      + To configure PIM-SM MDT setup across the public network, run the [**rpt-spt mode**](cmdqueryname=rpt-spt+mode) command.
      + To configure PIM-SM MDT setup not across the public network, run the [**spt-only mode**](cmdqueryname=spt-only+mode) command.
  11. Run [**ipmsi-tunnel**](cmdqueryname=ipmsi-tunnel)
      
      
      
      The MVPN I-PMSI view is displayed.
  12. Configure the I-PMSI tunnel setup mode.
      
      
      + To configure mLDP as the I-PMSI tunnel setup mode, run the [**mldp (MVPN I-PMSI view)**](cmdqueryname=mldp+%28MVPN+I-PMSI+view%29) command.
      + To configure RSVP-TE as the I-PMSI tunnel setup mode, perform the following steps:
        1. Run the [**mpls te (MVPN I-PMSI view)**](cmdqueryname=mpls+te+%28MVPN+I-PMSI+view%29) command to configure RSVP-TE as the I-PMSI tunnel setup mode.
        2. Run the [**p2mp-template (I-PMSI MPLS TE view)**](cmdqueryname=p2mp-template+%28I-PMSI+MPLS+TE+view%29) *p2mp-template-name* command to specify the tunnel template to be referenced by a P2MP RSVP-TE tunnel.
           
           If the tunnel template specified in the [**p2mp-template (I-PMSI MPLS TE view)**](cmdqueryname=p2mp-template+%28I-PMSI+MPLS+TE+view%29) command does not exist, a P2MP RSVP-TE tunnel fails to be set up. You can run the [**mpls te p2mp-template**](cmdqueryname=mpls+te+p2mp-template) command to create a tunnel template.
  13. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure the tunnel connection node.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* *matchMode* **node** *node*
     
     
     
     A route-policy is created, and its view is displayed.
  3. Run [**apply stitch-pmsi**](cmdqueryname=apply+stitch-pmsi) { **incoming** { **rsvp-te p2mp-template** *p2mp-template-name* [ **mldp** **root-ip** *root-ip-address* ] } | **mldp** [ **root-ip** *root-ip-address* ] | **rsvp-te p2mp-template** *p2mp-template-name* }
     
     
     
     A stitching tunnel is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     The system view is displayed.
  6. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  7. Run [**ipv4-family**](cmdqueryname=ipv4-family) **mvpn**
     
     
     
     The BGP-MVPN address family view is displayed.
  8. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name* **export**
     
     
     
     A route-policy is specified to filter routes to be advertised to a specified receiver PE.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the receiver PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**multicast mvpn**](cmdqueryname=multicast+mvpn) *mvpn-id*
     
     
     
     An MVPN ID is set.
  3. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  4. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The VPN instance IPv4 address family view is displayed.
  5. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
     
     
     
     IP multicast routing is enabled in the VPN instance IPv4 address family.
  6. Run [**mvpn**](cmdqueryname=mvpn)
     
     
     
     The VPN instance IPv4 address family MVPN view is displayed.
  7. (Optional) Run [**vpn-target (VPN instance IPv4 address family MVPN view)**](cmdqueryname=vpn-target+%28VPN+instance+IPv4+address+family+MVPN+view%29)
     
     
     
     An MVPN target is configured for the VPN instance MVPN address family.
  8. Run [**c-multicast signaling**](cmdqueryname=c-multicast+signaling) **bgp**
     
     
     
     BGP is configured as the signaling protocol for transmitting C-multicast routes.
  9. (Optional) Run [**vrf-route-import compatible draft**](cmdqueryname=vrf-route-import+compatible+draft)
     
     
     
     The VRF Route Import Extended Community carried in BGP Update messages is configured to use the format defined in an IETF draft.
     
     If a non-Huawei device uses the message encapsulation format defined in an IETF draft, run the [**vrf-route-import compatible draft**](cmdqueryname=vrf-route-import+compatible+draft) command to enable a Huawei device to use the message encapsulation format defined in the draft so that the Huawei and non-Huawei devices can communicate.
  10. (Optional) Run either of the following commands to configure the PIM-SM MDT setup mode:
      
      
      + To configure PIM-SM MDT setup across the public network, run the [**rpt-spt mode**](cmdqueryname=rpt-spt+mode) command.
      + To configure PIM-SM MDT setup not across the public network, run the [**spt-only mode**](cmdqueryname=spt-only+mode) command.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.