(Optional) Configuring Multicast Traffic Forwarding over a BIERv6 I-PMSI Tunnel
===============================================================================

An inclusive-PMSI (I-PMSI) tunnel connects all PEs in the same MVPN. If a wildcard is used when an address pool range and criteria are configured for switching from an I-PMSI tunnel to a selective-PMSI (S-PMSI) tunnel, this configuration task is not required.

#### Prerequisites

A VPN instance has been created for the unicast network. For details, see the configuration examples in this document.


#### Context

An I-PMSI tunnel is established between a sender PE and all receiver PEs. Therefore, you need to complete the following configurations on the sender PE and all receiver PEs.


#### Procedure

1. Configure the sender PE.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**multicast mvpn**](cmdqueryname=multicast+mvpn) **ipv6-underlay** *mvpnid*
      
      
      
      An MVPN ID is configured.
      
      
      
      You are advised to set the MVPN ID to the loopback interface address of the local device.
   3. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      
      
      The VPN instance view is displayed.
   4. Run [**ipv4-family**](cmdqueryname=ipv4-family)
      
      
      
      The VPN instance IPv4 address family view is displayed.
   5. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
      
      
      
      Multicast routing is enabled in the VPN instance IPv4 address family view.
   6. Run [**mvpn**](cmdqueryname=mvpn)
      
      
      
      The VPN instance IPv4 address family MVPN view is displayed.
   7. Run [**sender-enable**](cmdqueryname=sender-enable)
      
      
      
      The PE is configured as the sender PE.
   8. Run [**ipv6 underlay enable**](cmdqueryname=ipv6+underlay+enable)
      
      
      
      IPv6 forwarding is enabled.
   9. Run [**src-dt4**](cmdqueryname=src-dt4) **locator** *locator-name* **sid** *sid-val* 
      
      
      
      A Src.DT4 SID is configured.
      
      
      
      The Src.DT4 SID must be an IPv6 address of the network segment to which the locator of the local device belongs.
   10. (Optional) Run [**vpn-target**](cmdqueryname=vpn-target)
       
       
       
       An MVPN target is configured for the VPN instance MVPN address family.
   11. (Optional) Configure a PIM-SM RPT setup mode.
       
       
       * Across the public network: To configure this mode, run the [**rpt-spt mode**](cmdqueryname=rpt-spt+mode) command.
       * Not across the public network: To configure this mode, run the [**spt-only mode**](cmdqueryname=spt-only+mode) command.
   12. (Optional) Run [**bier load-balance-entropy source-group**](cmdqueryname=bier+load-balance-entropy+source-group)
       
       
       
       The entropy mode is configured for MVPNv4 over BIERv6 load balancing.
       
       
       
       Perform this operation only if load balancing has been enabled using the [**max-load-balance**](cmdqueryname=max-load-balance) *number* command when configuring basic BIERv6 functions.
   13. Run [**ipmsi-tunnel**](cmdqueryname=ipmsi-tunnel)
       
       
       
       The MVPN I-PMSI view is displayed.
   14. Run [**bier**](cmdqueryname=bier+%28MVPN-IPMSI+view%29) [ **sub-domain** *sub-domain-val* ] [ **bsl** { **64** | **128** | **256** } ]
       
       
       
       The I-PMSI tunnel type is set to BIER.
   15. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the MVPN I-PMSI view.
   16. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the VPN instance IPv4 address family MVPN view.
   17. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the VPN instance IPv4 address family view.
   18. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the VPN instance view.
   19. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
2. Configure a receiver PE.
   
   
   
   Perform the following operations on all receiver PEs.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**multicast mvpn**](cmdqueryname=multicast+mvpn) **ipv6-underlay** *mvpn-id*
      
      
      
      An MVPN ID is configured.
      
      
      
      You are advised to set the MVPN ID to the loopback interface address of the local device.
   3. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      
      
      The VPN instance view is displayed.
   4. Run [**ipv4-family**](cmdqueryname=ipv4-family)
      
      
      
      The VPN instance IPv4 address family view is displayed.
   5. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
      
      
      
      Multicast routing is enabled in the VPN instance IPv4 address family view.
   6. Run [**mvpn**](cmdqueryname=mvpn)
      
      
      
      The VPN instance IPv4 address family MVPN view is displayed.
   7. (Optional) Run [**vpn-target**](cmdqueryname=vpn-target)
      
      
      
      An MVPN target is configured.
   8. Run [**c-multicast signaling**](cmdqueryname=c-multicast+signaling) **bgp**
      
      
      
      BGP is configured as the signaling protocol for transmitting C-multicast routes.
   9. Run [**ipv6 underlay enable**](cmdqueryname=ipv6+underlay+enable)
      
      
      
      IPv6 forwarding is enabled.
   10. (Optional) Run [**vrf-route-import compatible draft**](cmdqueryname=vrf-route-import+compatible+draft)
       
       
       
       The device is configured to encapsulate the VRF Route Import Extended Community in BGP Update messages using the format defined in a relevant IETF draft.
       
       
       
       By default, a Huawei device uses the message encapsulation format defined in an RFC to encapsulate the VRF Route Import Extended Community. If a non-Huawei device uses the message encapsulation format defined in the IETF draft, run the [**vrf-route-import compatible draft**](cmdqueryname=vrf-route-import+compatible+draft) command to enable the Huawei device to use the format defined in the IETF draft so that the two devices can communicate.
   11. (Optional) Configure a PIM-SM RPT setup mode.
       
       
       * Across the public network: To configure this mode, run the [**rpt-spt mode**](cmdqueryname=rpt-spt+mode) command.
       * Not across the public network: To configure this mode, run the [**spt-only mode**](cmdqueryname=spt-only+mode) command.
   12. (Optional) Run [**export msdp**](cmdqueryname=export+msdp)
       
       
       
       The function of transmitting (S, G) entry information in BGP Source Active A-D routes to the RP through MSDP SA messages is enabled.
       
       
       
       If PIM-SM RPT setup is not across the public network, you can configure a PE or CE as the VPN instance's RP. If a CE is configured as an RP, the CE needs to establish an MSDP peer relationship with its connected PE. To enable this PE to transmit the (S, G) entry information learned through BGP Source Active A-D routes to the CE (RP), run the [**export msdp**](cmdqueryname=export+msdp) command.
   13. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the VPN instance IPv4 address family MVPN view.
   14. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the VPN instance IPv4 address family view.
   15. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the VPN instance view.
   16. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.