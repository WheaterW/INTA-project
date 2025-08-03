Configuring a P2MP LSP to Carry Multicast Traffic
=================================================

An NG MVPN uses P2MP LSPs to carry multicast traffic. Only mLDP P2MP LSPs are supported.

#### Context

Currently, only mLDP P2MP tunnels can be used to carry multicast traffic. The mLDP P2MP tunnels are easy to configure. They are usually applied to networks that do not require control over destination nodes or high service quality. In addition, they do not require signaling packets to be periodically sent, reducing network pressure.

Perform the following steps on different PEs.


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
  5. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
     
     
     
     The RD of the VPN instance IPv4 address family is configured.
  6. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target1* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
     
     
     
     The VPN-target extended community is configured for VPN instance IPv4 address family. The VPN instance can receive and process VPNv4 routes.
  7. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
     
     
     
     Multicast routing is enabled for the VPN instance IPv4 address family.
  8. Run [**mvpn**](cmdqueryname=mvpn)
     
     
     
     The VPN instance IPv4 address family MVPN view is displayed.
  9. Run [**sender-enable**](cmdqueryname=sender-enable)
     
     
     
     The PE is configured as a sender PE.
  10. Run [**c-multicast signaling**](cmdqueryname=c-multicast+signaling) **bgp**
      
      
      
      BGP is configured as the signaling protocol for transmitting C-multicast routes.
  11. (Optional) Configure the PIM-SM MDT setup mode: 
      
      
      + If you want PIM-SM MDTs to be set up across the public network, run the [**rpt-spt mode**](cmdqueryname=rpt-spt+mode) command.
      + If you want PIM-SM MDTs to be set up not across the public network, run the [**spt-only mode**](cmdqueryname=spt-only+mode) command.
  12. Run [**auto-discovery inter-as**](cmdqueryname=auto-discovery+inter-as)
      
      
      
      Inter-AS auto discovery is enabled.
  13. (Optional) Run [**import msdp**](cmdqueryname=import+msdp)
      
      
      
      The function of transmitting (S, G) entry information in Multicast Source Discovery Protocol (MSDP) Source Active (SA) messages to the remote PE through BGP Source Active A-D routes is enabled.
      
      If PIM-SM MDT setup is not across the public network, you can configure a PE or CE as a VPN instance's rendezvous point (RP). If a CE is configured as an RP, the CE needs to establish an MSDP peer relationship with its connected PE and transmit (S, G) entry information to the PE through MSDP SA messages. To enable this PE to transmit the (S, G) entry information to the remote PE through BGP Source Active A-D routes, run the [**import msdp**](cmdqueryname=import+msdp) command.
  14. Run [**ipmsi-tunnel**](cmdqueryname=ipmsi-tunnel)
      
      
      
      The MVPN I-PMSI view is displayed.
  15. Run [**mldp (MVPN I-PMSI view)**](cmdqueryname=mldp+%28MVPN+I-PMSI+view%29)
      
      
      
      mLDP is used to establish an I-PMSI tunnel
  16. Run [**commit**](cmdqueryname=commit)
      
      
      
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
  5. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
     
     
     
     The RD of the VPN instance IPv4 address family is configured.
  6. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target1* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
     
     
     
     The VPN-target extended community is configured for VPN instance IPv4 address family. The VPN instance can receive and process VPNv4 routes.
  7. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
     
     
     
     Multicast routing is enabled for the VPN instance IPv4 address family.
  8. Run [**mvpn**](cmdqueryname=mvpn)
     
     
     
     The VPN instance IPv4 address family MVPN view is displayed.
  9. Run [**c-multicast signaling**](cmdqueryname=c-multicast+signaling) **bgp**
     
     
     
     BGP is configured as the signaling protocol for transmitting C-multicast routes.
  10. (Optional) Configure the PIM-SM MDT setup mode: 
      
      
      + If you want PIM-SM MDTs to be set up across the public network, run the [**rpt-spt mode**](cmdqueryname=rpt-spt+mode) command.
      + If you want PIM-SM MDTs to be set up not across the public network, run the [**spt-only mode**](cmdqueryname=spt-only+mode) command.
  11. Run [**auto-discovery inter-as**](cmdqueryname=auto-discovery+inter-as)
      
      
      
      Inter-AS auto discovery is enabled.
  12. (Optional) Run [**export msdp**](cmdqueryname=export+msdp)
      
      
      
      The function of transmitting (S, G) entry information in BGP Source Active A-D routes to the RP through MSDP SA messages is enabled.
      
      If PIM-SM MDT setup is not across the public network, you can configure a PE or CE as a VPN instance's RP. If a CE is configured as an RP, the CE needs to establish an MSDP peer relationship with its connected PE. To enable this PE to transmit (S, G) entry information in BGP Source Active A-D routes to the CE configured as the RP, run the [**export msdp**](cmdqueryname=export+msdp) command.
  13. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.