Configuring Interworking Between Traditional VPWS and EVPN VPWS over MPLS
=========================================================================

The aggregation layer of a network still uses traditional VPWS, whereas the core network has evolved to EVPN. To allow communication between different layers, interworking between traditional VPWS and EVPN VPWS over MPLS must be configured.

#### Context

As the metro network evolves to EVPN, a large number of devices at the aggregation layer still use traditional VPWS, making it difficult to complete E2E evolution to EVPN at one time. However, the core network has evolved to EVPN, necessitating interworking between traditional VPWS and EVPN VPWS over MPLS. This section describes how to configure interworking between traditional VPWS and EVPN VPWS over MPLS.

On the network shown in [Figure 1](#EN-US_TASK_0172370520__fig583817311216), CE1 with two sites attached is connected to a UPE through a NID (switch). The UPE and NPEs are connected through an MPLS network at the aggregation layer, and services are carried using a VPWS. NPE1, NPE2, and NPE3 are connected through an MPLS network at the core layer, and services are carried through EVPN VPWS over MPLS.

**Figure 1** Configuring interworking between traditional VPWS and EVPN VPWS over MPLS  
![](figure/en-us_image_0000001181213328.png)

* A UPE is dual-homed to NPE1 and NPE2, which improves access reliability. The UPE establishes a pair of primary and secondary PWs with the master and backup NPEs, respectively. Traffic is sent through the primary PW, and the UPE is enabled to receive traffic through both the primary and secondary PWs.
* On NPEs, VPWS accesses EVPN VPWS over MPLS through PW VE interfaces. Specifically, VPWS is configured on PW VE interfaces, PW VE sub-interfaces are bound to EVPL instances, and EVPL instances are bound to EVPN instances. PW VE sub-interfaces are configured with QinQ or dot1q VLAN tag termination to import traffic into EVPN VPWS over MPLS.

#### Pre-configuration Tasks

Before configuring interworking between traditional VPWS and EVPN VPWS over MPLS, complete the following tasks:

* Configure interfaces and their IP addresses on NPE1, NPE2, NPE3, and the UPE.
* Configure an IGP on NPE1, NPE2, NPE3, and the UPE to ensure route reachability.
* [Configure master/slave PW redundancy](dc_vrp_vpws_cfg_5008.html) on the UPE.
* [Configure EVPN VPWS over MPLS](dc_vrp_evpn_cfg_0020.html) on NPE1, NPE2, and NPE3.
* Configure basic MPLS LDP functions on NPE1, NPE2, NPE3, and the UPE.
* [Configure EVPL instances](dc_vrp_evpn_cfg_0021.html) on each of NPE1, NPE2, and NPE3.

Perform the following steps on the NPE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The PW VE interface view is displayed.
3. Run the [**mpls l2vc**](cmdqueryname=mpls+l2vc) [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged**] | **access-port** | **ignore-standby-state** ] command to create a VPWS connection.
4. Run [**esi**](cmdqueryname=esi) *esi*
   
   
   
   An ESI is configured.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum*
   
   
   
   A PW VE sub-interface is created, and the PW-VE sub-interface view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before running this command, ensure that the Layer 2 main interface does not have the [**port link-type**](cmdqueryname=port+link-type) **dot1q-tunnel** command configuration. If the configuration exists, run the [**undo port link-type**](cmdqueryname=undo+port+link-type) command to delete the configuration.
   
   In addition to a Layer 2 sub-interface, an Ethernet main interface, Layer 3 sub-interface, or Eth-Trunk interface can also function as an AC interface.
7. Configure an encapsulation type for the PW VE sub-interface.
   
   
   1. Run the [**encapsulation**](cmdqueryname=encapsulation) **dot1q-termination** [ **rt-protocol** ] command to configure the dot1q encapsulation type for a VLAN tag termination sub-interface.
      
      To enable the dot1q VLAN tag termination sub-interface to support routing protocols, configure **rt-protocol**.
   2. Configure the dot1q VLAN tag termination sub-interface using one or more of the following commands based on site requirements:
      * To configure a dot1q VLAN tag termination sub-interface, run the [**dot1q termination vid**](cmdqueryname=dot1q+termination+vid) *low-pe-vid* [ **vlan-group** *group-id* ] command.
      * To configure a dot1q VLAN tag termination sub-interface and a matching policy for the sub-interface, run the [**dot1q termination vid**](cmdqueryname=dot1q+termination+vid) *low-pe-vid* { **8021p** { *8val8021p1* [ **to** *val8021p2* ] } &<1-8> | **dscp** { *valdscp1* [ **to** *valdscp2* ] } &<1-10> | **eth-type pppoe** | **default** } [ **vlan-group** *group-id* ] command.
      * To configure a dot1q VLAN tag termination sub-interface and a matching policy for the sub-interface, run the [**dot1q termination vid**](cmdqueryname=dot1q+termination+vid) *low-pe-vid* { **8021p** { *val8021p1* [ **to** *val8021p2* ] } &<1-8> | **dscp** { *valdscp1* [ **to** *valdscp2* ] } &<1-10> | **default** } [ **vlan-group** *group-id* ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If you do not configure a matching policy, the dot1q VLAN tag termination sub-interface terminates the VLAN tags of packets carrying the specified VLAN ID. If you configure a matching policy, the dot1q VLAN tag termination sub-interface terminates the VLAN tags of packets carrying the specified VLAN ID+802.1p value/DSCP value/EthType.
8. Run [**evpl instance**](cmdqueryname=evpl+instance) *evpl-id*
   
   
   
   The PW VE sub-interface is bound to the EVPL instance.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display bgp evpn all routing-table**](cmdqueryname=display+bgp+evpn+all+routing-table) command on the NPEs and check for EVI AD routes received by the NPEs.