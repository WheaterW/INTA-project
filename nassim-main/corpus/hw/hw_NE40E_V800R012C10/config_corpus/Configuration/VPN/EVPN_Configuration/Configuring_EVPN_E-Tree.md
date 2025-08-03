Configuring EVPN E-Tree
=======================

This section describes how to configure EVPN E-Tree to isolate traffic between different interfaces in the same broadcast domain.

#### Usage Scenario

As the number of services carried on an EVPN increases, the number of user MAC addresses managed by the EVPN is also increasing. The user MAC addresses are flooded on the network through EVPN routes. As a result, all interfaces in the same broadcast domain can communicate with each other at Layer 2. And broadcast, unknown unicast, and multicast (BUM) and unicast traffic cannot be isolated for users who do not need to communicate with each other. To isolate interfaces that do not need to communicate with each other in the same broadcast domain, you can deploy the EVPN E-Tree function on the network.

EVPN E-Tree implements the E-Tree model defined by the Metro Ethernet Forum (MEF) by setting the root or leaf attribute for AC interfaces. An AC interface with the leaf attribute is a leaf AC interface, and an AC interface with the root attribute is a root AC interface.

* A leaf AC interface and a root AC interface can send traffic to each other. However, flows between leaf AC interfaces are isolated from each other.
* A root AC interface can communicate with the other root AC interfaces as well as leaf AC interfaces.

EVPN E-Tree supports different types of tunnels, including MPLS LDP, MPLS TE, SRv6 BE, and SRv6 TE Policy.


#### Pre-configuration Tasks

Before configuring EVPN E-Tree, complete the following tasks:

* Configure [BD EVPN functions](dc_vrp_evpn_cfg_0065.html) or [basic EVPN functions](dc_vrp_evpn_cfg_0003.html) on the network.
* Configure MPLS (LDP or TE) tunnels, [EVPN VPLS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0023_copy.html), or [EVPN VPLS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpls_over_srv6-te_policy_copy.html) on the backbone network.

#### Procedure

* Configure EVPN E-Tree for a BD EVPN.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode** command to enter the view of a BD EVPN instance.
  3. Run the [**etree enable**](cmdqueryname=etree+enable) command to enable EVPN E-Tree.
  4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  5. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum* **mode l2** command to enter the view of the Layer 2 sub-interface that the BD is associated with.
  6. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to add the Layer 2 sub-interface to the BD.
  7. Run the [**evpn e-tree-leaf**](cmdqueryname=evpn+e-tree-leaf) command to configure the leaf attribute for the interface.
  8. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  9. (Optional) In an SRv6 scenario, configure the tunnel ID carried in the inclusive multicast route to be sent to an IPv6 neighbor.
     
     
     1. Run the [**evpn**](cmdqueryname=evpn) command to enter the global EVPN configuration view.
     2. Run the [**evpn tunnel-id**](cmdqueryname=evpn+tunnel-id) *tunnel-id-value* command to configure the tunnel ID carried in the inclusive multicast route to be sent to an IPv6 neighbor.
        
        *tunnel-id-value* is in the IPv6 address format. You are advised to set this parameter to a reachable IPv6 address.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure EVPN E-Tree for a basic EVPN.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* command to enter the view of an EVPN instance.
  3. Run the [**etree enable**](cmdqueryname=etree+enable) command to enable EVPN E-Tree.
  4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  5. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of the interface to be bound to the basic EVPN instance.
  6. Run the [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name* command to bind the interface to the EVPN instance.
  7. Run the [**evpn e-tree-leaf**](cmdqueryname=evpn+e-tree-leaf) command to configure the leaf attribute for the interface.
  8. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  9. (Optional) In an SRv6 scenario, configure the tunnel ID carried in the inclusive multicast route to be sent to an IPv6 neighbor.
     
     
     1. Run the [**evpn**](cmdqueryname=evpn) command to enter the global EVPN configuration view.
     2. Run the [**evpn tunnel-id**](cmdqueryname=evpn+tunnel-id) *tunnel-id-value* command to configure the tunnel ID carried in the inclusive multicast route to be sent to an IPv6 neighbor.
        
        *tunnel-id-value* is in the IPv6 address format. You are advised to set this parameter to a reachable IPv6 address.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

* Run the [**display bgp evpn all routing-table**](cmdqueryname=display+bgp+evpn+all+routing-table) [ { **ad-route** | **mac-route** } *prefix* ] command to check the leaf attribute carried in routes.
* Run the [**display traffic-statistics discard evpn etree**](cmdqueryname=display+traffic-statistics+discard+evpn+etree) [ **slot** *slot-id* ] command to check statistics about lost packets between leaf nodes in an EVPN E-Tree scenario.