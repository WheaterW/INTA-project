(Optional) Configuring Multicast Traffic Forwarding over a BIERv6 I-PMSI Tunnel
===============================================================================

An I-PMSI tunnel connects all PEs on the network-side public network. If a wildcard is used when an address pool range and criteria are configured for the switching to a selective-PMSI (S-PMSI) tunnel, no I-PMSI tunnels need to be created.

#### Context

An I-PMSI tunnel is established between a sender PE and all receiver PEs. Therefore, you need to complete the following configurations on the sender PE and all receiver PEs.


#### Procedure

1. Configure the sender PE.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**multicast ipv6 mvpn**](cmdqueryname=multicast+ipv6+mvpn) **ipv6-underlay** *mvpnid*
      
      
      
      An MVPN ID is configured.
      
      
      
      You are advised to set the MVPN ID to the loopback interface address of the local device.
   3. Run [**multicast ipv6 routing-enable**](cmdqueryname=multicast+ipv6+routing-enable)
      
      
      
      Multicast routing is enabled.
   4. Run [**multicast ipv6 vpn-public**](cmdqueryname=multicast+ipv6+vpn-public)
      
      
      
      The public network IPv6 address family MVPN view is displayed.
   5. Run [**sender-enable**](cmdqueryname=sender-enable)
      
      
      
      The PE is configured as a sender PE.
   6. Run [**ipv6 underlay enable**](cmdqueryname=ipv6+underlay+enable)
      
      
      
      IPv6 forwarding is enabled.
   7. Run [**src-dt6**](cmdqueryname=src-dt6) **locator** *locator-name* **sid** *sid-val* [ **signal-format msid** ]
      
      
      
      A Src.DT6 SID is configured.
      
      
      
      The Src.DT6 SID must be an IPv6 address of the network segment to which the locator of the local device belongs.
      
      By default, the device uses the Prefix-SID to carry Src.DT6 SID information. To configure the device to use the MSID to carry Src.DT6 SID information, run the **signal-format msid** command.
   8. (Optional) Run [**target**](cmdqueryname=target) { *vrfRT* } &<1-8> [ *vrfRTType* ]
      
      
      
      An MVPN target is configured for the public network MVPN address family.
      
      
      
      Multiple MVPN targets can be configured for the public network MVPN address family, and a maximum of eight MVPN targets can be configured using one target command.
   9. (Optional) Run [**auto-discovery inter-as**](cmdqueryname=auto-discovery+inter-as)
      
      
      
      Inter-AS automatic discovery is enabled.
   10. (Optional) Configure a PIM-SM RPT setup mode.
       
       
       
       To allow ASM RPTs to be set up across the public network, run the [**rpt-spt mode**](cmdqueryname=rpt-spt+mode) command. To prevent ASM RPTs from being set up across the public network, run the [**spt-only mode**](cmdqueryname=spt-only+mode) command.
   11. (Optional) Run [**bier load-balance-entropy source-group**](cmdqueryname=bier+load-balance-entropy+source-group)
       
       
       
       The entropy mode is configured for GTMv6 over BIERv6 load balancing.
       
       
       
       Perform this operation only if load balancing has been enabled using the [**max-load-balance**](cmdqueryname=max-load-balance) *number* command.
   12. Run [**ipmsi-tunnel**](cmdqueryname=ipmsi-tunnel)
       
       
       
       The public network IPv6 MVPN I-PMSI view is displayed.
   13. Run [**bier**](cmdqueryname=bier+%28MVPN-IPMSI+view%29) [ **sub-domain** *sub-domain-val* ] [ **bsl** { **64** | **128** | **256** } ]
       
       
       
       The I-PMSI tunnel type is set to BIER IPv6.
   14. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the public network IPv6 MVPN I-PMSI view.
   15. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the public network IPv6 address family MVPN view.
   16. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
2. Configure a receiver PE.
   
   
   
   Perform the following operations on all receiver PEs.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**multicast ipv6 mvpn**](cmdqueryname=multicast+ipv6+mvpn) **ipv6-underlay** *mvpnid*
      
      
      
      An MVPN ID is configured.
      
      
      
      You are advised to set the MVPN ID to the loopback interface address of the local device.
   3. Run [**multicast ipv6 routing-enable**](cmdqueryname=multicast+ipv6+routing-enable)
      
      
      
      Multicast routing is enabled.
   4. Run [**multicast ipv6 vpn-public**](cmdqueryname=multicast+ipv6+vpn-public)
      
      
      
      The public network IPv6 address family MVPN view is displayed.
   5. (Optional) Run [**target**](cmdqueryname=target) { *vrfRT* } &<1-8> [ *vrfRTType* ]
      
      
      
      An MVPN target is configured for the public network MVPN address family.
      
      
      
      Multiple MVPN targets can be configured for the public network MVPN address family, and a maximum of eight MVPN targets can be configured using one target command.
   6. Run [**c-multicast signaling**](cmdqueryname=c-multicast+signaling) **bgp**
      
      
      
      BGP is configured as the signaling protocol for transmitting C-multicast routes.
   7. Run [**ipv6 underlay enable**](cmdqueryname=ipv6+underlay+enable)
      
      
      
      IPv6 forwarding is enabled.
   8. (Optional) Configure a PIM-SM RPT setup mode.
      
      
      
      To allow ASM RPTs to be set up across the public network, run the [**rpt-spt mode**](cmdqueryname=rpt-spt+mode) command. To prevent ASM RPTs from being set up across the public network, run the [**spt-only mode**](cmdqueryname=spt-only+mode) command.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the public network IPv6 address family MVPN view.
   10. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.