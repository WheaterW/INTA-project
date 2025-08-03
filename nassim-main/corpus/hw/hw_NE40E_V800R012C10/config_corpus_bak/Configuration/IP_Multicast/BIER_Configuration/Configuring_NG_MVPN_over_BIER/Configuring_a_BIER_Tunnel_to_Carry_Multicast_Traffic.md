Configuring a BIER Tunnel to Carry Multicast Traffic
====================================================

NG MVPNs use BIER P2MP tunnels to carry multicast traffic.

#### Context

Each edge node in a BIER sub-domain must be configured with a BFR-ID that is unique to the sub-domain. In the NG MVPN over BIER scenario, a BFR-ID needs to be configured for the sender PE and receiver PEs. Ps do not require BFR-IDs, but you need to enable BIER on the Ps.


#### Procedure

* Perform the following steps on a PE to be configured as a sender PE:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**multicast mvpn**](cmdqueryname=multicast+mvpn)*mvpn-id*
     
     
     
     An MVPN ID is configured.
  3. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance)*vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  4. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The VPN instance IPv4 address family view is displayed.
  5. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
     
     
     
     Multicast routing is enabled in the VPN instance IPv4 address family view.
  6. Run [**mvpn**](cmdqueryname=mvpn)
     
     
     
     The VPN instance IPv4 address family MVPN view is displayed.
  7. Run [**c-multicast signaling bgp**](cmdqueryname=c-multicast+signaling+bgp)
     
     
     
     BGP is configured as the signaling protocol for transmitting C-multicast routes.
  8. Run [**sender-enable**](cmdqueryname=sender-enable)
     
     
     
     The PE is configured as a sender PE.
  9. (Optional) Run [**vpn-target (VPN instance IPv4 address family MVPN view)**](cmdqueryname=vpn-target+%28VPN+instance+IPv4+address+family+MVPN+view%29)
     
     
     
     MVPN targets are configured in the VPN instance IPv4 address family MVPN view.
  10. (Optional) Configure the PIM-SM MDT setup mode:
      
      
      + To set up PIM-SM MDTs across the public network, run the [**rpt-spt mode**](cmdqueryname=rpt-spt+mode) command.
      + To set up PIM-SM MDTs not across the public network, run the [**spt-only mode**](cmdqueryname=spt-only+mode) command.
  11. Run [**ipmsi-tunnel**](cmdqueryname=ipmsi-tunnel)
      
      
      
      The MVPN I-PMSI view is displayed.
  12. Run [**bier**](cmdqueryname=bier+%28MVPN-IPMSI+view%29) [ **sub-domain** *sub-domain-val* ] [ **bsl** { **64** | **128** | **256** } ]
      
      
      
      The I-PMSI tunnel type is set to BIER.
  13. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Perform the following steps on a PE to be configured as a receiver PE:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**multicast mvpn**](cmdqueryname=multicast+mvpn)*mvpn-id*
     
     
     
     An MVPN ID is configured.
  3. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance)*vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  4. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The VPN instance IPv4 address family view is displayed.
  5. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
     
     
     
     Multicast routing is enabled in the VPN instance IPv4 address family view.
  6. Run [**mvpn**](cmdqueryname=mvpn)
     
     
     
     The VPN instance IPv4 address family MVPN view is displayed.
  7. (Optional) Run [**vpn-target (VPN instance IPv4 address family MVPN view)**](cmdqueryname=vpn-target+%28VPN+instance+IPv4+address+family+MVPN+view%29)
     
     
     
     MVPN targets are configured in the VPN instance IPv4 address family MVPN view.
  8. Run [**c-multicast signaling**](cmdqueryname=c-multicast+signaling) **bgp**
     
     
     
     BGP is configured as the signaling protocol for transmitting C-multicast routes.
  9. (Optional) Run [**vrf-route-import compatible draft**](cmdqueryname=vrf-route-import+compatible+draft)
     
     
     
     The VRF Route Import Extended Community carried in BGP Update messages is configured to use the format defined in an IETF draft.
     
     
     
     If a non-Huawei device uses the message encapsulation format defined in an IETF draft, run the [**vrf-route-import compatible draft**](cmdqueryname=vrf-route-import+compatible+draft) command to enable a Huawei device to use the message encapsulation format defined in the draft so that the Huawei device can communicate with the non-Huawei device.
  10. (Optional) Configure the PIM-SM MDT setup mode:
      
      
      + To set up PIM-SM MDTs across the public network, run the [**rpt-spt mode**](cmdqueryname=rpt-spt+mode) command.
      + To set up PIM-SM MDTs not across the public network, run the [**spt-only mode**](cmdqueryname=spt-only+mode) command.
  11. (Optional) Run [**export msdp**](cmdqueryname=export+msdp)
      
      
      
      The transmission of (S, G) entry information in BGP Source Active A-D routes to the RP through MSDP SA messages is enabled.
      
      
      
      If PIM-SM MDT setup is not across the public network, you can configure a PE or CE as a VPN instance's RP. If a CE is configured as an RP, the CE needs to establish an MSDP peer relationship with its connected PE. To enable this PE to transmit (S, G) entry information in BGP Source Active A-D routes to the CE configured as the RP, run the [**export msdp**](cmdqueryname=export+msdp) command.
  12. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.