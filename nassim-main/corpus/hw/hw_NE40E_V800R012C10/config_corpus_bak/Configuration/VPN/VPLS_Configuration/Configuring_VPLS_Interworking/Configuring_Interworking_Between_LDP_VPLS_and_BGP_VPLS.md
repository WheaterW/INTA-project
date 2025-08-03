Configuring Interworking Between LDP VPLS and BGP VPLS
======================================================

To enable an LDP VPLS network to communicate with a BGP VPLS network, configure interworking between LDP VPLS and BGP VPLS.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172370131__fig_dc_vrp_vpls_cfg_601301), an LDP VPLS network is deployed between PE1 and the SPE, and a BGP VPLS network is deployed among the SPE, PE2, and PE3. Interworking between LDP VPLS and BGP VPLS needs to be configured on the SPE for CE1, CE2, and CE3 to communicate.

**Figure 1** Interworking between LDP VPLS and BGP VPLS  
![](images/fig_dc_vrp_vpls_cfg_601301.png)  


#### Procedure

1. Configure LDP VPLS on PE1. For configuration details, see [Configuring LDP VPLS](dc_vrp_vpls_cfg_5003.html).
2. Perform the following configurations on the SPE:
   
   
   * Configure LDP VPLS on the SPE. For configuration details, see [Configuring LDP VPLS](dc_vrp_vpls_cfg_5003.html).
   * Configure BGP VPLS on the SPE. For configuration details, see [Configuring BGP VPLS](dc_vrp_vpls_cfg_6005.html).
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   On the SPE, LDP VPLS and BGP VPLS must be configured in the same VSI.
3. Configure BGP VPLS on PE2. For configuration details, see [Configuring BGP VPLS](dc_vrp_vpls_cfg_6005.html).
4. Configure BGP VPLS on PE3. For configuration details, see [Configuring BGP VPLS](dc_vrp_vpls_cfg_6005.html).
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.