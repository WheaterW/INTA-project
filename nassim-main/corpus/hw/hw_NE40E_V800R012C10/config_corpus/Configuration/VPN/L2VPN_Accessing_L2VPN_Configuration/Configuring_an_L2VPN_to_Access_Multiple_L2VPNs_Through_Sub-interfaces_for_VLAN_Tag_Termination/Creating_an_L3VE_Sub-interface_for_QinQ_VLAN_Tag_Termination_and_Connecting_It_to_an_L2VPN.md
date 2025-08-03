Creating an L3VE Sub-interface for QinQ VLAN Tag Termination and Connecting It to an L2VPN
==========================================================================================

If an L3VE sub-interface receives double-tagged service packets from a UPE, configure the L3VE sub-interface as a sub-interface for QinQ VLAN tag termination to access L2VPN.

#### Context

Perform the following steps on NPEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number interface-number*
   
   
   
   An L3VE sub-interface is created, and its view is displayed.
3. Run [**control-vid**](cmdqueryname=control-vid) *vid* **qinq-termination**
   
   
   
   The encapsulate mode of the sub-interface is configured as QinQ VLAN tag termination.
4. Run [**qinq termination pe-vid**](cmdqueryname=qinq+termination+pe-vid) *pe-vid* [ **to** *high-pe-vid* ] **ce-vid** *ce-vid* [ **to** *high-ce-vid* ] [ **vlan-group** *group-id* ]
   
   
   
   QinQ VLAN tag termination is configured on the L3VE sub-interface.
   
   
   
   When the L3VE sub-interface receives packets with double tags from users, it will terminate the packets whose inner tag is in the range specified by **ce-vid**.
5. Perform one of the following operations based on the L2VPN type:
   
   
   * Access to LDP VPWS: Run the [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *i*p-address** | ****pw-template**** **pw-template-name** } \***vc-id** [ [ ****control-word**** | ****no-control-word**** ] | [ ****raw**** | ****tagged**** ] | ****tunnel-policy**** **policy-name** [ ****endpoint**** **endpoint-address** ****color**** **color-value** ] | ****ignore-standby-state**** ] \* command to create an LDP VPWS connection.
   * Access to LDP VPLS: Run the [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* command to bind the L3VE interface to the VSI.
   * Access to local CCC:
     1. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     2. Run the [**ccc**](cmdqueryname=ccc+interface+in-label+out-label) *ccc-connection-name* **interface** { *interface-name* | *acIfType* *acIfNum* } [ *raw* ] **in-label** *in-label-value* **out-label** *out-label-value* { **nexthop** *nexthop-address* | **out-interface** { *out-interface-name* | *outAcIfType* *outAcIfNum* } } [ **control-word** | **no-control-word** ] command to configure a local CCC.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.