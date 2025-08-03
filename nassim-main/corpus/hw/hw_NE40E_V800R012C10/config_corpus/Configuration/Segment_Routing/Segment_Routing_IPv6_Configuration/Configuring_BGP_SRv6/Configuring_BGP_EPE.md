Configuring BGP EPE
===================

BGP egress peer engineering (EPE) is used to allocate Peer-Node and Peer-Adj SIDs to peers. These SIDs can be reported to a controller through BGP-LS for orchestrating E2E SRv6 TE Policies.

#### Context

BGP EPE allocates BGP peer SIDs to inter-AS paths, and BGP-LS advertises the peer SIDs to the controller. A forwarder that does not establish a BGP-LS peer relationship with the controller can run BGP-LS to advertise a peer SID to a BGP peer that has established a BGP-LS peer relationship with the controller. The BGP peer then runs BGP-LS to advertise the peer SID to the network controller.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
   
   
   
   SRv6 is enabled.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
   
   
   
   BGP is enabled, and the BGP view is displayed.
5. Run [**peer**](cmdqueryname=peer+as-number) *ipv6-address* **as-number** { *as-number-plain* | *as-number-dot* }
   
   
   
   A BGP peer is created.
6. Run [**ipv6-family unicast**](cmdqueryname=ipv6-family+unicast)
   
   
   
   The IPv6 unicast address family view is displayed.
7. Run [**peer**](cmdqueryname=peer) *ipv6-address* **enable**
   
   
   
   The device is enabled to exchange routing information with the specified peer.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the BGP view.
9. Enable BGP EPE.
   
   
   * Run the [**peer**](cmdqueryname=peer) *peerIpv6Addr* **egress-engineering** **srv6** **inherit-global-locator** command to enable BGP EPE and global-locator inheritance.
   * Run the [**peer**](cmdqueryname=peer) *peerIpv6Addr* **egress-engineering srv6 locator** *locator-name* command to enable BGP EPE and specify a locator to be used for SID allocation to a specific peer.
   
   If the two commands are both run, only the last command takes effect.
10. (Optional) Run [**segment-routing ipv6 egress-engineering sid-flavor**](cmdqueryname=segment-routing+ipv6+egress-engineering+sid-flavor) { **no-flavor** | **psp** | **psp-usp-usd** | **psp-usp-usd-coc** | **coc** | **psp-coc** | **psp-usp-usd-coc-next** | **psp-usd-next** } \*
    
    
    
    Global SID flavors are configured for BGP EPE. You can specify a Peer-Node and Peer-Adj to apply for SIDs with the corresponding flavors.
11. (Optional) Configure a static SID.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The [**peer**](cmdqueryname=peer) *peerIpv6Addr* **egress-engineering** **srv6** **inherit-global-locator** command must have been configured before you perform this step.
    
    The following commands can be configured separately or together based on the application scenario.
    
    
    
    * Run the [**peer**](cmdqueryname=peer) *peerIpv6Addr* **egress-engineering** **srv6** **static-sid** { **psp** *psp-sid* | **no-flavor** *no-flavor-sid* } command to configure a static uncompressed End.X SID (PSP) or End.X SID (no flavor).
    * Run the [**peer**](cmdqueryname=peer) *peerIpv6Addr* **egress-engineering** **srv6** **static-sid** { **psp compress** *psp-compress-sid* | **no-flavor compress** *no-flavor-compress-sid* } command to configure a static compressed End.X SID (PSP) or End.X SID (no flavor).
    * Run the [**peer**](cmdqueryname=peer) *peerIpv6Addr* **egress-engineering** **srv6** **static-sid** **psp-usp-usd** *sid-value* command to configure a static uncompressed End.X SID (PSP, USP, and USD).
    * Run the [**peer**](cmdqueryname=peer) *peerIpv6Addr* **egress-engineering** **srv6** **static-sid** { **psp-usp-usd** | **psp-usp-usd-coc** } **compress** *sid*-value command to configure a static compressed End.X SID (PSP, USP, and USD) or End.X SID (PSP, USP, USD, and COC).
      
      If a 16-bit compression locator is referenced, run the [**peer**](cmdqueryname=peer) *peerIpv6Addr* **egress-engineering** **srv6** **static-sid** { **psp-usp-usd** | **psp-usp-usd-coc-next** } **compress** *sid-value* command to configure a static 16-bit compressed End.X SID (PSP, USP, and USD) or End.X SID (PSP, USP, USD, COC, and NEXT).
    
    **Table 1** Effects of different command configuration combinations
    | Locator for SID Allocation to All BGP EPE Peers | Global-Locator Inheritance by a Specific BGP EPE Peer | Locator for SID Allocation to a Specific BGP EPE Peer | Static SID | Effect |
    | --- | --- | --- | --- | --- |
    | Configured | - | Configured | Not configured | The locator specified for SID allocation to a specific BGP EPE peer takes effect, and static SIDs are dynamically allocated. |
    | Configured | Configured | Not configured | Configured | The same locator is used for SID allocation to all BGP EPE peers.  For static SIDs, if only one type is specified, the other types of SIDs are dynamically allocated. |
    | Configured | Configured | Not configured | Not configured | The same locator is used for SID allocation to all BGP EPE peers, and static SIDs are dynamically allocated. |
    | Not configured | Not configured | Configured | Not configured | The locator specified for SID allocation to a specific BGP EPE peer takes effect, and static SIDs are dynamically allocated. |
    | Not configured | Configured | Not configured | Configured | SID configuration fails. To address this issue, run the [**segment-routing ipv6 egress-engineering locator**](cmdqueryname=segment-routing+ipv6+egress-engineering+locator) *locator-name* command before configuring a static SID. |
    | Not configured | Configured | Not configured | Not configured | No SIDs are allocated. |
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.