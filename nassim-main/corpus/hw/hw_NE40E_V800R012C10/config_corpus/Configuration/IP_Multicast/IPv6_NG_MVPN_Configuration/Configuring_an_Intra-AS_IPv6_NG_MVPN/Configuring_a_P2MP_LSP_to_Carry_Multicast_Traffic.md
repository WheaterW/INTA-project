Configuring a P2MP LSP to Carry Multicast Traffic
=================================================

An NG MVPN uses P2MP LSPs to carry multicast traffic. You can configure either RSVP-TE P2MP or mLDP P2MP LSPs.

#### Context

P2MP LSPs that carry multicast traffic can be either RSVP-TE P2MP or mLDP P2MP LSPs. [Table 1](#EN-US_TASK_0172367568__table_dc_vrp_feature_new_ngmvpn_000401) lists the differences between RSVP-TE P2MP LSPs and mLDP P2MP LSPs.

**Table 1** Differences between RSVP-TE P2MP LSPs and mLDP P2MP LSPs
| Compared Aspect | mLDP P2MP LSP | RSVP-TE P2MP LSP |
| --- | --- | --- |
| Main features | mLDP P2MP LSPs do not support bandwidth reservation and cannot ensure service quality during network congestion. mLDP P2MP LSPs are easier to configure than RSVP-TE P2MP LSPs. | RSVP-TE P2MP LSPs support bandwidth reservation and can ensure service quality during network congestion. |
| Application scenario | Networks that do not require control over destination nodes  Use mLDP P2MP LSPs to carry multicast traffic if high service quality is not required. | Networks that require control over destination nodes  Use RSVP-TE P2MP LSPs to carry multicast traffic if high service quality is required. |
| Signaling | Signaling packets do not need to be periodically sent, reducing network load. | Signaling packets need to be periodically sent to maintain the tunnel. If a large number of leaf nodes exist, network congestion is likely to occur. |

Select the type of tunnel as needed.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If P2MP LSP that carry multicast traffic is RSVP-TE P2MP LSP, you need to configure a tunnel policy to bind a VPN service to specified RSVP-TE P2MP LSP.



#### Procedure

* Perform the following steps on a PE to be configured as a sender PE:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**multicast ipv6 mvpn**](cmdqueryname=multicast+ipv6+mvpn) *mvpn-id*
     
     
     
     An MVPN ID is configured.
  3. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  4. Run [**ipv6-family**](cmdqueryname=ipv6-family)
     
     
     
     The VPN instance IPv6 address family view is displayed.
  5. Run [**multicast ipv6 routing-enable**](cmdqueryname=multicast+ipv6+routing-enable)
     
     
     
     Multicast routing is enabled in for VPN instance IPv6 address family.
  6. Run [**mvpn**](cmdqueryname=mvpn)
     
     
     
     The VPN instance IPv6 address family MVPN view is displayed.
  7. Run [**sender-enable**](cmdqueryname=sender-enable)
     
     
     
     The PE is configured as a sender PE.
  8. Run [**c-multicast signaling**](cmdqueryname=c-multicast+signaling) **bgp**
     
     
     
     BGP is configured as the signaling protocol for transmitting C-multicast routes.
  9. (Optional) Run [**vpn-target (VPN instance IPv6 address family MVPN view)**](cmdqueryname=vpn-target+%28VPN+instance+IPv6+address+family+MVPN+view%29)
     
     
     
     An MVPN target is configured for the VPN instance MVPN address family.
  10. (Optional) Configure the PIM-SM RPT setup mode:
      
      
      + To configure PIM-SM RPT setup across the public network, run the [**rpt-spt mode**](cmdqueryname=rpt-spt+mode) command.
      + To configure PIM-SM RPT setup not across the public network, run the [**spt-only mode**](cmdqueryname=spt-only+mode) command.
  11. Run [**ipmsi-tunnel**](cmdqueryname=ipmsi-tunnel)
      
      
      
      The MVPN I-PMSI view is displayed.
  12. Configure an I-PMSI tunnel establishment mode.
      
      
      + To use mLDP to establish an I-PMSI tunnel, run the [**mldp (IPv6 MVPN I-PMSI view)**](cmdqueryname=mldp+%28IPv6+MVPN+I-PMSI+view%29) command.
      + To use RSVP-TE to establish an I-PMSI tunnel, run the following steps:
        1. Run the [**mpls te (IPv6 MVPN I-PMSI view)**](cmdqueryname=mpls+te+%28IPv6+MVPN+I-PMSI+view%29) command to use RSVP-TE to establish an I-PMSI tunnel.
        2. Run the [**p2mp-template (IPv6 I-PMSI MPLS TE view)**](cmdqueryname=p2mp-template+%28IPv6+I-PMSI+MPLS+TE+view%29) *p2mp-template-name* command to specify the tunnel template to be referenced by an RSVP-TE P2MP LSP.
           
           If the tunnel template specified in the [**p2mp-template (IPv6 I-PMSI MPLS TE view)**](cmdqueryname=p2mp-template+%28IPv6+I-PMSI+MPLS+TE+view%29) command does not exist, the RSVP-TE P2MP LSP cannot be established. Before running the [**p2mp-template (IPv6 I-PMSI MPLS TE view)**](cmdqueryname=p2mp-template+%28IPv6+I-PMSI+MPLS+TE+view%29) command, ensure that the [**mpls te p2mp-template**](cmdqueryname=mpls+te+p2mp-template) command has been run.
  13. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Perform the following steps on a PE to be configured as a receiver PE:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**multicast ipv6 mvpn**](cmdqueryname=multicast+ipv6+mvpn) *mvpn-id*
     
     
     
     An MVPN ID is configured.
  3. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  4. Run [**ipv6-family**](cmdqueryname=ipv6-family)
     
     
     
     The VPN instance IPv6 address family view is displayed.
  5. Run [**multicast ipv6 routing-enable**](cmdqueryname=multicast+ipv6+routing-enable)
     
     
     
     Multicast routing is enabled in for VPN instance IPv6 address family.
  6. Run [**mvpn**](cmdqueryname=mvpn)
     
     
     
     The VPN instance IPv6 address family MVPN view is displayed.
  7. (Optional) Run [**vpn-target (VPN instance IPv6 address family MVPN view)**](cmdqueryname=vpn-target+%28VPN+instance+IPv6+address+family+MVPN+view%29)
     
     
     
     An MVPN target is configured for the VPN instance MVPN address family.
  8. Run [**c-multicast signaling**](cmdqueryname=c-multicast+signaling) **bgp**
     
     
     
     BGP is configured as the signaling protocol for transmitting C-multicast routes.
  9. (Optional) Run [**vrf-route-import compatible draft**](cmdqueryname=vrf-route-import+compatible+draft)
     
     
     
     The VRF Route Import Extended Community carried in BGP Update messages is configured to use the format defined in an IETF draft.
     
     
     
     If a non-Huawei device uses the message encapsulation format defined in an IETF draft, run the [**vrf-route-import compatible draft**](cmdqueryname=vrf-route-import+compatible+draft) command to enable a Huawei device to use the message encapsulation format defined in the draft so that the Huawei device can communicate with the non-Huawei device.
  10. (Optional) Configure the PIM-SM RPT setup mode:
      
      
      + To configure PIM-SM RPT setup across the public network, run the [**rpt-spt mode**](cmdqueryname=rpt-spt+mode) command.
      + To configure PIM-SM RPT setup not across the public network, run the [**spt-only mode**](cmdqueryname=spt-only+mode) command.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.