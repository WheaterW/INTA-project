Configuring a P2MP LSP to Carry Multicast Traffic
=================================================

An NG MVPN uses P2MP LSPs to carry multicast traffic. You can configure either RSVP-TE P2MP or mLDP P2MP LSPs.

#### Context

P2MP LSPs that carry multicast traffic can be either RSVP-TE P2MP or mLDP P2MP LSPs. [Table 1](#EN-US_TASK_0000001225673368__table_dc_vrp_feature_new_ngmvpn_000401) lists the differences between RSVP-TE P2MP LSPs and mLDP P2MP LSPs.

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
  2. Run [**multicast mvpn**](cmdqueryname=multicast+mvpn) *mvpn-id*
     
     
     
     An MVPN ID is configured.
  3. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  4. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The VPN instance IPv4 address family view is displayed.
  5. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
     
     
     
     Multicast routing is enabled in for VPN instance IPv4 address family.
  6. Run [**mvpn**](cmdqueryname=mvpn)
     
     
     
     The VPN instance IPv4 address family MVPN view is displayed.
  7. Run [**c-multicast signaling**](cmdqueryname=c-multicast+signaling) **bgp**
     
     
     
     BGP is configured as the signaling protocol for transmitting C-multicast routes.
  8. Run [**sender-enable**](cmdqueryname=sender-enable)
     
     
     
     The PE is configured as a sender PE.
  9. (Optional) Run [**vpn-target (VPN instance IPv4 address family MVPN view)**](cmdqueryname=vpn-target+%28VPN+instance+IPv4+address+family+MVPN+view%29)
     
     
     
     An MVPN target is configured for the VPN instance MVPN address family.
  10. (Optional) Configure the PIM-SM MDT setup mode:
      
      
      + If you want PIM-SM MDTs to be set up across the public network, run the [**rpt-spt mode**](cmdqueryname=rpt-spt+mode) command.
      + If you want PIM-SM MDTs to be set up not across the public network, run the [**spt-only mode**](cmdqueryname=spt-only+mode) command.
  11. (Optional) Run [**import msdp**](cmdqueryname=import+msdp)
      
      
      
      The function of transmitting (S, G) entry information in Multicast Source Discovery Protocol (MSDP) Source Active (SA) messages to the remote PE through BGP Source Active A-D routes is enabled.
      
      If PIM-SM MDT setup is not across the public network, you can configure a PE or CE as a VPN instance's rendezvous point (RP). If a CE is configured as an RP, the CE needs to establish an MSDP peer relationship with its connected PE and transmit (S, G) entry information to the PE through MSDP SA messages. To enable this PE to transmit the (S, G) entry information to the remote PE through BGP Source Active A-D routes, run the [**import msdp**](cmdqueryname=import+msdp) command.
  12. Run [**ipmsi-tunnel**](cmdqueryname=ipmsi-tunnel)
      
      
      
      The MVPN I-PMSI view is displayed.
  13. Configure an I-PMSI tunnel establishment mode.
      
      
      + To use mLDP to establish an I-PMSI tunnel, run the [**mldp (MVPN I-PMSI view)**](cmdqueryname=mldp+%28MVPN+I-PMSI+view%29) command.
      + To use RSVP-TE to establish an I-PMSI tunnel, run the following steps:
        1. Run the [**mpls te (MVPN I-PMSI view)**](cmdqueryname=mpls+te+%28MVPN+I-PMSI+view%29) command to use RSVP-TE to establish an I-PMSI tunnel.
        2. Run the [**p2mp-template (I-PMSI MPLS TE view)**](cmdqueryname=p2mp-template+%28I-PMSI+MPLS+TE+view%29) *p2mp-template-name* command to specify the tunnel template to be referenced by an RSVP-TE P2MP LSP.
           
           If the tunnel template specified in the [**p2mp-template (I-PMSI MPLS TE view)**](cmdqueryname=p2mp-template+%28I-PMSI+MPLS+TE+view%29) command does not exist, the RSVP-TE P2MP LSP cannot be established. Before running the [**p2mp-template (I-PMSI MPLS TE view)**](cmdqueryname=p2mp-template+%28I-PMSI+MPLS+TE+view%29) command, ensure that the [**mpls te p2mp-template**](cmdqueryname=mpls+te+p2mp-template) command has been run.
  14. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Perform the following steps on a PE to be configured as a receiver PE:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**multicast mvpn**](cmdqueryname=multicast+mvpn) *mvpn-id*
     
     
     
     An MVPN ID is configured.
  3. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  4. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The VPN instance IPv4 address family view is displayed.
  5. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
     
     
     
     Multicast routing is enabled in for VPN instance IPv4 address family.
  6. Run [**mvpn**](cmdqueryname=mvpn)
     
     
     
     The VPN instance IPv4 address family MVPN view is displayed.
  7. (Optional) Run [**vpn-target (VPN instance IPv4 address family MVPN view)**](cmdqueryname=vpn-target+%28VPN+instance+IPv4+address+family+MVPN+view%29)
     
     
     
     An MVPN target is configured for the VPN instance MVPN address family.
  8. Run [**c-multicast signaling**](cmdqueryname=c-multicast+signaling) **bgp**
     
     
     
     BGP is configured as the signaling protocol for transmitting C-multicast routes.
  9. (Optional) Run [**vrf-route-import compatible draft**](cmdqueryname=vrf-route-import+compatible+draft)
     
     
     
     The VRF Route Import Extended Community carried in BGP Update messages is configured to use the format defined in an IETF draft.
     
     If a non-Huawei device uses the packet encapsulation format defined in an IETF draft, run the [**vrf-route-import compatible draft**](cmdqueryname=vrf-route-import+compatible+draft) command to enable a Huawei device to use the packet encapsulation format defined in the draft so that the Huawei and non-Huawei devices can communicate.
  10. (Optional) Configure the PIM-SM MDT setup mode:
      
      
      + If you want PIM-SM MDTs to be set up across the public network, run the [**rpt-spt mode**](cmdqueryname=rpt-spt+mode) command.
      + If you want PIM-SM MDTs to be set up not across the public network, run the [**spt-only mode**](cmdqueryname=spt-only+mode) command.
  11. (Optional) Run [**export msdp**](cmdqueryname=export+msdp)
      
      
      
      The function of transmitting (S, G) entry information in BGP Source Active A-D routes to the RP through MSDP SA messages is enabled.
      
      If PIM-SM MDT setup is not across the public network, you can configure a PE or CE as a VPN instance's RP. If a CE is configured as an RP, the CE needs to establish an MSDP peer relationship with its connected PE. To enable this PE to transmit (S, G) entry information in BGP Source Active A-D routes to the CE configured as the RP, run the [**export msdp**](cmdqueryname=export+msdp) command.
  12. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.