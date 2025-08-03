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
     
     
     
     The VPN-Target extended community attributes are configured for the VPN instance IPv4 address family. The VPN instance can receive and process VPNv4 routes.
  7. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
     
     
     
     Multicast routing is enabled for the VPN instance IPv4 address family.
  8. Run [**mvpn**](cmdqueryname=mvpn)
     
     
     
     The VPN instance IPv4 address family MVPN view is displayed.
  9. Run [**sender-enable**](cmdqueryname=sender-enable)
     
     
     
     The PE is configured as a sender PE.
  10. Run [**c-multicast signaling**](cmdqueryname=c-multicast+signaling) **bgp**
      
      
      
      BGP is configured as the signaling protocol for transmitting C-multicast routes.
  11. Run [**auto-discovery inter-as**](cmdqueryname=auto-discovery+inter-as)
      
      
      
      The inter-AS auto-discovery function is enabled.
  12. Run [**ipmsi-tunnel**](cmdqueryname=ipmsi-tunnel)
      
      
      
      The MVPN I-PMSI view is displayed.
  13. Run [**mldp (MVPN I-PMSI view)**](cmdqueryname=mldp+%28MVPN+I-PMSI+view%29)
      
      
      
      mLDP is used to establish an I-PMSI tunnel.
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
  5. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
     
     
     
     The RD of the VPN instance IPv4 address family is configured.
  6. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target1* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
     
     
     
     The VPN-Target extended community attributes are configured for the VPN instance IPv4 address family. The VPN instance can receive and process VPNv4 routes.
  7. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
     
     
     
     Multicast routing is enabled for VPN instance IPv4 address family.
  8. Run [**mvpn**](cmdqueryname=mvpn)
     
     
     
     The VPN instance IPv4 address family MVPN view is displayed.
  9. Run [**c-multicast signaling**](cmdqueryname=c-multicast+signaling) **bgp**
     
     
     
     BGP is configured as the signaling protocol for transmitting C-multicast routes.
  10. Run [**auto-discovery inter-as**](cmdqueryname=auto-discovery+inter-as)
      
      
      
      The inter-AS auto-discovery function is enabled.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.