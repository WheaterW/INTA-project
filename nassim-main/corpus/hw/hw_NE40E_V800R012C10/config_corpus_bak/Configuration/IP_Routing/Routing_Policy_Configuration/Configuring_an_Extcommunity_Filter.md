Configuring an Extcommunity Filter
==================================

Configuring_an_Extcommunity_Filter

#### Context

An extended community (extcommunity) filter is used to filter BGP routes based on extcommunity attributes. BGP extcommunity attributes are classified as follows:

* VPN target: A VPN target controls route learning between VPN instances, isolating routes of VPN instances from each other. VPN targets include export and import ones. Before advertising Virtual Private Network version 4 (VPNv4) or Virtual Private Network version 6 (VPNv6) routes to a remote Multiprotocol Extensions for Border Gateway Protocol (MP-BGP) peer, a PE adds export VPN targets to the routes. After receiving the VPNv4 or VPNv6 routes, the remote MP-BGP peer determines which routes can be added to its local VPN instance routing table based on whether the export VPN targets carried in the routes match the import VPN target of the local VPN instance.
* Source of Origin (SoO): Several CEs at a VPN site may be connected to different PEs. Routes advertised from the CEs to the PEs may be advertised back to the VPN site after the routes traverse the VPN backbone network. This may cause routing loops at the VPN site. To prevent routing loops, SoO attributes can be configured for routes from different VPN sites for differentiation.
* Encapsulation: The encapsulation extcommunity attribute is classified as the VXLAN encapsulation extcommunity attribute or MPLS encapsulation extcommunity attribute. In EVPN VXLAN scenarios, EVPN routes carry the VXLAN encapsulation extcommunity attribute, and the value of this attribute can be set to 0:8 to filter EVPN routes. In EVPN MPLS scenarios, received EVPN routes do not carry the MPLS encapsulation extcommunity attribute in most cases. If a device receives EVPN routes carrying the MPLS encapsulation extcommunity attribute, the value of this attribute can be set to 0:10 to filter these routes.
* Segmented-nh: The segmented-nh extcommunity attribute can be added to intra-AS I-PMSI A-D routes in an NG MVPN scenario where segmented tunnels are used.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Extended community filters are used to filter only BGP routes because extended community attributes are private attributes of BGP.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure the following extcommunity filters as needed.
   
   
   
   Configure a VPN-Target extcommunity filter:
   
   * To configure a basic VPN-Target extcommunity filter, run the [**ip extcommunity-filter**](cmdqueryname=ip+extcommunity-filter) { *basic-extcomm-filter-num* | **basic** *basic-extcomm-filter-name* } [ **index** *index-number* ] { **deny** | **permit** } { **rt** { *as-number:nn* | *4as-number:nn* | *ipv4-address*:*nn* } } &<1-16> command.
   * To configure an advanced VPN-Target extcommunity filter, run the [**ip extcommunity-filter**](cmdqueryname=ip+extcommunity-filter) { *advanced-extcomm-filter-num* | **advanced** *advanced-extcomm-filter-name* }[ **index** *index-number* ] { **deny** | **permit** } *regular-expression* command.
   
   
   
   Configure an SoO extcommunity filter:
   
   * To configure a basic SoO extcommunity filter, run the [**ip extcommunity-list soo basic**](cmdqueryname=ip+extcommunity-list+soo+basic) *basic-extcomm-filter-name* [ **index** *index-number* ] { **permit** | **deny** } { *site-of-origin* } &<1-16> command.
   * To configure an advanced SoO extcommunity filter, run the [**ip extcommunity-list soo advanced**](cmdqueryname=ip+extcommunity-list+soo+advanced) *advanced-extcomm-filter-name* [ **index** *index-number* ] { **permit** | **deny** } *regular-expression* command.
   
   
   
   Configure an encapsulation extcommunity filter:
   
   * To configure a basic encapsulation extcommunity filter, run the [**ip extcommunity-list encapsulation basic**](cmdqueryname=ip+extcommunity-list+encapsulation+basic) *encapsulation-name* [ **index** *index-number* ] { **permit** | **deny** } { *encapsulation-value* } &<1-16> command.
   * To configure an advanced encapsulation extcommunity filter, run the [**ip extcommunity-list encapsulation advanced**](cmdqueryname=ip+extcommunity-list+encapsulation+advanced) *encapsulation-name* [ **index** *index-number* ] { **permit** | **deny** } *regular* command.
   
   
   
   Configure a segmented-nh extcommunity filter:
   
   * To configure a basic segmented-nh extcommunity filter, run the [**ip extcommunity-list segmented-nh basic**](cmdqueryname=ip+extcommunity-list+segmented-nh+basic) *segmented-nh-name* [ **index** *index-number* ] { **permit** | **deny** } { *segmented-nh-value* } &<1-16> command.
   * To configure an advanced segmented-nh extcommunity filter, run the [**ip extcommunity-list segmented-nh advanced**](cmdqueryname=ip+extcommunity-list+segmented-nh+advanced) *segmented-nh-name* [ **index** *index-number* ] { **permit** | **deny** } *regular* command.
   
   
   
   Multiple entries (or rules) can be defined in an extended community filter, and the relationship between them is OR, which means that the route matches the extended community filter if it matches one of the rules.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

* Run the [**display ip extcommunity-filter**](cmdqueryname=display+ip+extcommunity-filter) command to check information about the configured extended community filters.
* Run the [**display ip extcommunity-list soo**](cmdqueryname=display+ip+extcommunity-list+soo) [ *eclSooName* ] command to check detailed information about a configured SoO extended community filter.
* Run the [**display ip extcommunity-list encapsulation**](cmdqueryname=display+ip+extcommunity-list+encapsulation) [ *name* ] command to check detailed information about a configured encapsulation extended community filter.
* Run the [**display ip extcommunity-list segmented-nh**](cmdqueryname=display+ip+extcommunity-list+segmented-nh) [ *eclSnhName* ] command to check detailed information about a configured segmented-nh extended community filter.