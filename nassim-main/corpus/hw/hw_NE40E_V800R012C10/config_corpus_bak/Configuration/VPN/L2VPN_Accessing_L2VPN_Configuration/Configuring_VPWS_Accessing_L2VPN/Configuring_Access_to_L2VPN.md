Configuring Access to L2VPN
===========================

This section describes how to configure an IP address for an L3VE sub-interface and bind the sub-interface to a VPN to implement access to L2VPN.

#### Context

Perform the following steps on NPEs.


#### Procedure

* Network-side user access to LDP VPWS
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number interface-number*
     
     
     
     The L3VE sub-interface view is displayed.
  3. Run [**vlan-type**](cmdqueryname=vlan-type) **dot1q** *vlan-id*
     
     
     
     A VLAN ID is configured for the VE sub-interface.
  4. Run [**mpls l2vc**](cmdqueryname=mpls+l2vc) { **ip-address** | ****pw-template**** **pw-template-name** } \***vc-id** [ [ ****control-word**** | ****no-control-word**** ] | [ ****raw**** | ****tagged**** ] | ****tunnel-policy**** **policy-name** [ ****endpoint**** **endpoint-address** ****color**** **color-value** ] | ****ignore-standby-state**** ] \*
     
     
     
     An LDP VPWS connection is created.
     
     
     
     If the AC interface on the peer PE is an Ethernet sub-interface, configure **tagged** to change the local VC type to VLAN, or configure **raw** on the Ethernet sub-interface of the peer end to change the peer VC type to Ethernet. The VC types for PEs at both ends of the VPWS connection must be consistent.
  5. (Optional) Run [**mpls l2vc track l2ve-service-state**](cmdqueryname=mpls+l2vc+track+l2ve-service-state)
     
     
     
     Association between the L2VE interface service status and L3VE interface PW status is enabled.
     
     
     
     After this command is run on an L3VE interface, the system adjusts the active/standby status of PWs on the L3VE interface based on the active/standby service status on the L2VE interface. When the L2VE interface service is in the standby state, the PW status on the L3VE interface is changed to standby. When the L2VE interface service is in the active state, the PW status on the L3VE interface is changed to active.
  6. Configure a routing protocol for route exchange with LDP VPWS-enabled devices.
     
     
     
     For configuration details, see *NE40E Configuration Guide - IP Routing*.
  7. (Optional) Run [**mpls l2vpn l3ve delay-up**](cmdqueryname=mpls+l2vpn+l3ve+delay-up) *time*
     
     
     
     The time to wait before the L3VE interface can go up after the L2VPN service recovers is configured.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Network-side user access to local CCC
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number* *interface-number*
     
     
     
     The L3VE sub-interface view is displayed.
  3. Run [**vlan-type**](cmdqueryname=vlan-type) **dot1q** *vlan-id*
     
     
     
     A VLAN ID is configured for the VE sub-interface.
  4. (Optional) Run [**mpls l2vpn l3ve delay-up**](cmdqueryname=mpls+l2vpn+l3ve+delay-up) *time*
     
     
     
     The time to wait before the L3VE interface can go up after the L2VPN service recovers is configured.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**ccc**](cmdqueryname=ccc+interface+in-label+out-label) *ccc-connection-name* **interface** { *interface-name* | *acIfType* *acIfNum* } [ *raw* ] **in-label** *in-label-value* **out-label** *out-label-value* { **nexthop** *nexthop-address* | **out-interface** { *out-interface-name* | *outAcIfType* *outAcIfNum* } } [ **control-word** | **no-control-word** ]
     
     
     
     A local CCC is configured.
     
     
     
     In a local CCC accessing L3VPN scenario, **interface** *interface-type1* *interface-number1* refers to the interface connecting the PE to the CE, and the outbound interface is an L3VE sub-interface.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Network-side user access to LDP VPLS
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number interface-number*
     
     
     
     The L3VE sub-interface view is displayed.
  3. Run [**vlan-type**](cmdqueryname=vlan-type) **dot1q** *vlan-id*
     
     
     
     A VLAN ID is configured for the VE sub-interface.
  4. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name*
     
     
     
     The L3VE interface is bound to a VSI.
  5. Configure a routing protocol for route exchange with devices that access LDP VPLS.
     
     
     
     For configuration details, see *NE40E Configuration Guide - IP Routing*.
  6. (Optional) Run [**mpls l2vpn l3ve delay-up**](cmdqueryname=mpls+l2vpn+l3ve+delay-up) *time*
     
     
     
     The time to wait before the L3VE interface can go up after the L2VPN service recovers is configured.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.