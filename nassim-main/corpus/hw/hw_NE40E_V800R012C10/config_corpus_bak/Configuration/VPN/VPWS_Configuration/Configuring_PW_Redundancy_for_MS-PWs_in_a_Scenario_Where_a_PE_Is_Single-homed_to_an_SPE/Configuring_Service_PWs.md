Configuring Service PWs
=======================

Service PWs consist of common PWs and bypass PWs. If tunnel protection is available on the public network, you do not need to configure any bypass PW.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172369892__fig_dc_vrp_cfg_01918401), PE1 is single-homed to the SPE. To implement MS-PW redundancy:

* Configure a dynamic SS-PW between PE1 and the SPE.
* Configure dynamic VPWS switching in master/slave mode on the SPE.
* Configure a bypass PW between PE2 and PE3.

**Figure 1** MS-PW redundancy when a PE is single-homed to an SPE  
![](images/fig_dc_vrp_cfg_01918401.png)

#### Procedure

* Perform the following configurations on PE1.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the AC interface view for the service PW.
  3. Run the [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *ip-address* | **pw-template** *pw-template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** ] | **access-port** | **ignore-standby-state** ] \* command to configure PE1 to access the SPE over a dynamic PW.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + When creating a PW, you need to specify the IP address and VC ID of the destination PE. The VC IDs at both ends of a VC must be the same.
     + According to the default tunnel policy, a dynamic PW uses the LSP as its bearer tunnel, and the load balancing number is 1. To use a different type of tunnel, set the **tunnel-policy** *policy-name* parameter for the PW to reference the corresponding tunnel policy. Before referencing a tunnel policy, perform operations described in [Configuring a Tunnel Policy](dc_vrp_tnlm_cfg_0037.html) and [Applying a Tunnel Policy to a VPN](dc_vrp_tnlm_cfg_0038.html).
     + The encapsulation types at both ends of a PW must be the same.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Perform the following configurations on the SPE.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**mpls switch-l2vc**](cmdqueryname=mpls+switch-l2vc) [ **instance-name** *instance-name* ] *ip-address* *vc-id* [ **tunnel-policy** *policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] ] **between** *ip-address vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] ] **backup** *ip-address* *vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *sw-endpoint-address* | [ **endpoint** *sw-endpoint4-address* ] } **color** *color-value* ] ] **encapsulation** *encapsulation-type* [ **control-word-transparent** ] command to configure a dynamic MS-PW in master/slave mode.
  3. (Optional) Run the [**mpls switch-l2vc**](cmdqueryname=mpls+switch-l2vc) *ip-address* *pwId* **encapsulation** *encapsulation-type* **reroute** { **delay** *delay-time* | **immediately** | **never** } command to configure a switchback policy for the PWs in master/slave redundancy mode.
  4. (Optional) Run the [**mpls switch-l2vc**](cmdqueryname=mpls+switch-l2vc) *ip-address* *vc-id* **encapsulation** *encapsulation-type* **switchover** command to manually switch traffic from the primary PW to the secondary PW.
     
     
     
     This command is typically used only in debugging and fault scenarios. Running this command forcibly switches service traffic to the secondary PW.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Perform the following steps on PE2 and PE3.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the AC interface view for the service PW.
  3. Run the [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *ip-address* | **pw-template** *pw-template-name* } \* *vc-id* [ [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-interworking** | **ip-layer2** ] | **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | **access-port** | [ **secondary** ] ] \* command to specify PW primary/secondary status.
     
     
     + The primary PW must have the same encapsulation type as the secondary and bypass PWs.
     + The MTUs and control words of the AC interfaces on PE1, PE2, and PE3 must be the same. Otherwise, the PWs may go down, causing traffic interruption.
  4. Run the [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *ip-address* | **pw-template** *pw-template-name* } \* *vc-id* [ [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-interworking** | **ip-layer2** ] | **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | **access-port** | **bypass** ] \* command to configure a bypass PW.
     
     
     
     The status (enabled or disabled) of the control word function must be the same for the bypass and primary PWs.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.