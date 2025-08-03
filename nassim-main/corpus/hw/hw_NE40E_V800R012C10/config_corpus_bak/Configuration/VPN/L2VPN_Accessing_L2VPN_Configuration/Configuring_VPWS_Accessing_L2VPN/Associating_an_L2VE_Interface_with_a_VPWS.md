Associating an L2VE Interface with a VPWS
=========================================

This section describes how to associate an L2VE interface with a VPWS, specifically, how to configure a VPWS connection on an L2VE sub-interface to provide L2VPN functions.

#### Context

Perform the following steps on NPEs.


#### Procedure

* Configure a local CCC.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
     
     
     
     The MPLS L2VPN view is displayed.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) **virtual-ethernet** *interface-number* *interface-number*
     
     
     
     The L2VE sub-interface view is displayed.
  5. Run [**vlan-type**](cmdqueryname=vlan-type) **dot1q** *vlan-id*
     
     
     
     A VLAN ID is configured for the L2VE sub-interface.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  7. Run [**ccc**](cmdqueryname=ccc+interface+in-label+out-label) *ccc-connection-name* **interface** { *interface-name* | *acIfType* *acIfNum* } [ *raw* ] **in-label** *in-label-value* **out-label** *out-label-value* { **nexthop** *nexthop-address* | **out-interface** { *out-interface-name* | *outAcIfType* *outAcIfNum* } } [ **control-word** | **no-control-word** ]
     
     
     
     A local CCC is configured.
     
     
     
     **interface** *interface-type1* *interface-number1* refers to the interface connecting the PE to a CE, and the outbound interface is an L2VE sub-interface.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an LDP VPWS.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
     
     
     
     The MPLS L2VPN view is displayed.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) **virtual-ethernet** *interface-number interface-number*
     
     
     
     The L2VE sub-interface view is displayed.
  5. Run [**vlan-type**](cmdqueryname=vlan-type) **dot1q** *vlan-id*
     
     
     
     A VLAN ID is configured for the L2VE sub-interface.
  6. Run [**mpls l2vc**](cmdqueryname=mpls+l2vc) [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-layer2** | **ip-interworking**] | **access-port** | **ignore-standby-state** ] \*
     
     
     
     An LDP VPWS connection is created.
     
     
     
     If the AC interface on the peer PE is an Ethernet sub-interface, use **tagged** to change the local VC type to VLAN, or configure **raw** on the Ethernet sub-interface of the peer PE to change the peer VC type to Ethernet. The VC types for PEs at both ends of the VPWS must be consistent.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a BGP VPWS.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
     
     
     
     The MPLS L2VPN view is displayed.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn) *l2vpn-name* [ **encapsulation** *encapsulation-type* [ **control-word** | **no-control-word** ] ]
     
     
     
     A BGP VPWS VPN instance is created, and the MPLS L2VPN instance view is displayed.
     
     
     
     If heterogeneous interworking is required, specify *encapsulation-type* as **ip-interworking** for successful PW establishment.
  5. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
     
     
     
     An RD is configured for the MPLS L2VPN instance.
  6. Run [**vpn-target**](cmdqueryname=vpn-target) { *vpn-target* } & <1-16> [ **both** | **export-extcommunity** | **import-extcommunity** ]
     
     
     
     VPN targets are configured for the L2VPN instance.
  7. Run [**ce**](cmdqueryname=ce) *ce-Name* [ **id** *ce-id* [ **range** *ce-range* ] [ **default-offset** *ce-offset* ] ]
     
     
     
     A CE is created in the MPLS L2VPN instance.
  8. Run [**connection**](cmdqueryname=connection) [ **ce-offset** *ce-offset-id* ] **interface** { *interface-type* *interface-number* | *interface-name* } [ **tunnel-policy** *tunnel-policy-name* ] [ **raw** | **tagged** ] [ **secondary** ]
     
     
     
     A BGP VPWS connection is established.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.