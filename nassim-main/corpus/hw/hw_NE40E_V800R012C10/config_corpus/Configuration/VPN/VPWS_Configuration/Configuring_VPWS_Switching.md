Configuring VPWS Switching
==========================

After VPWS switching is configured, PW labels are switched during traffic forwarding over an MS-PW.

#### Usage Scenario

An MS-PW requires PW label switching when forwarding traffic, necessitating the configuration of VPWS switching. VPWS switching needs to be configured on a high-performance SPE that is capable of establishing a large number of MPLS LDP sessions.

VPWS switching is required in the following scenarios:

* Two PEs are in different ASs, and no signaling connection or tunnel can be set up between the two PEs.
* The signaling of one PE differs from that of the other PE.
* If access devices support MPLS but cannot set up large numbers of LDP sessions, you can use the user facing provider edge (UFPE) as the UPE and the SPE as the LDP session switching node (similar to the signaling reflector).

VPWS switching can be static, dynamic, or hybrid. Determine which type to use according to the actual situation.


#### Pre-configuration Tasks

Before configuring dynamic VPWS switching, complete the following tasks:

* Enable MPLS L2VPN on each PE.
* [Configure SVC VPWS](dc_vrp_vpws_cfg_6000.html) on UPEs if static VPWS switching is required.
* [Configure LDP VPWS](dc_vrp_vpws_cfg_3004.html) on UPEs if dynamic VPWS switching is required.

#### Procedure

* Configure static VPWS switching.
  
  
  
  Perform the following configurations on the SPE.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view of the SPE is displayed.
  2. Run [**mpls switch-l2vc**](cmdqueryname=mpls+switch-l2vc) *ip-address vc-id* **trans** *trans-label* **recv** *received-label* [ **oam-packet pop flow-label** ] [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] ] **between** *ip-address vc-id* **trans** *trans-label* **recv** *received-label* [ **oam-packet pop flow-label** ] [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] ] **encapsulation** *encapsulation-type* [ **control-word** | **no-control-word** ]
     
     
     
     A static MS-PW is created.
     
     
     
     A PW label must be manually configured on each SPE for static VPWS switching.
     
     The prerequisites for setting up a static MS-PW are as follows:
     
     + On the ingress UPE of the MS-PW, the PW state is up so long as the AC state is up and the corresponding PSN tunnels exist.
     + On the SPE, if the status of PSN tunnels on both sides of a PW is up, the PW can be successfully established regardless of whether the PW encapsulation type on the SPE is consistent with that on the UPE.
     
     To facilitate management, it is recommended that you use the same PW encapsulation type (specified using the **encapsulation** parameter) on the SPE and UPE.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure dynamic VPWS switching.
  
  
  
  Perform the following configurations on the SPE.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view of the SPE is displayed.
  2. Run [**mpls switch-l2vc**](cmdqueryname=mpls+switch-l2vc) [ **instance-name** *instance-name* ] *ip-address* *vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] ] [ **oam-packet pop flow-label** ] **between** *ip-address vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] ] [ **oam-packet pop flow-label** ] **encapsulation** *encapsulation-type* [ **control-word-transparent** ]
     
     
     
     Dynamic VPWS switching is configured.
     
     
     
     After dynamic VPWS switching is configured on an SPE, the SPE receives remote labels from two neighboring nodes (UPEs or SPEs) through signaling and receives the control word and VCCV capability information from the two endpoint UPEs through signaling.
     
     When configuring dynamic VPWS switching, ensure that the PW encapsulation type (specified using the **encapsulation** parameter) on the SPE is the same as that on the UPE. Otherwise, the PW cannot go up.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When configuring dynamic VPWS switching, select **ip-layer2** if IP interworking is required between Huawei and non-Huawei devices and **ip-interworking** if IP interworking is required between Huawei devices.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure hybrid VPWS switching.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view of the SPE is displayed.
  2. Run [**mpls switch-l2vc**](cmdqueryname=mpls+switch-l2vc) [ **instance-name** *instance-name* ] *ip-address* *vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] ] [ **oam-packet pop flow-label** ] **between** *ip-address vc-id* **trans** *trans-label* **recv** *recv-label* [ **oam-packet pop flow-label** ] [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] ] **encapsulation** *encapsulation-type* [ **control-word-transparent** ]
     
     
     
     A static-dynamic hybrid MS-PW is configured.

#### Verifying the Configuration

After the configurations are complete, check the configurations.

* Run the [**display mpls switch-l2vc**](cmdqueryname=display+mpls+switch-l2vc) [ *ip-address* *vc-id* **encapsulation** *encapsulation-type* | **state** { **down** | **up** } | **brief** ] command on the SPE to check VPWS switching information.