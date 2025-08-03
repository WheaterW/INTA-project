Configuring Interworking Between LDP VPLS and BGP AD VPLS
=========================================================

To enable an LDP VPLS network to communicate with a BGP AD VPLS network, configure interworking between LDP VPLS and BGP AD VPLS.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172370128__fig_dc_vrp_vpls_cfg_601201), an LDP VPLS network is deployed among PE1, PE2, and PE3, and a BGP AD VPLS network is deployed among PE2, PE3, and PE4. To configure interworking between LDP VPLS and BGP AD VPLS, configure hybrid VSIs on PE2 and PE3. In this scenario, the hybrid VSIs on PE2 and PE3 establish LDP PWs with the VSI on PE1 and establish BGP AD PWs with the VSI on PE4.

**Figure 1** Interworking between LDP VPLS and BGP AD VPLS  
![](images/fig_dc_vrp_vpls_cfg_601201.png)  


#### Procedure

1. Establish LDP PWs. The configuration is similar to that in "Configuring LDP VPLS." For details, see [Creating a VSI and Configuring LDP Signaling](dc_vrp_vpls_cfg_5004.html).
2. Establish BGP AD PWs. The configuration is similar to that in "Configuring BGP AD VPLS." For details, see [Creating a VSI and Configuring BGP AD Signaling](dc_vrp_vpls_cfg_5059.html).
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * On PE2 or PE3, the LDP and BGP AD PWs must be configured in the same VSI.
   * If you run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ [**static**](cmdqueryname=static) ] command to create a hybrid VSI, LDP PWs must be established prior to BGP AD PWs. If you run this command without specifying the [**static**](cmdqueryname=static) keyword, there is no special requirement on the PW configuration order.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.