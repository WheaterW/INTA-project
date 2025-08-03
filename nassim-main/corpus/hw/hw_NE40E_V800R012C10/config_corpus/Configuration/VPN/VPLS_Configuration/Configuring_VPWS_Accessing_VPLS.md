Configuring VPWS Accessing VPLS
===============================

This section describes how to configure VPWS accessing VPLS on an HVPLS network where UPEs do not support VPLS.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0172370148__fig_dc_vrp_vpls_cfg_602901), when UPEs do not support VPLS, you can configure VPWS on UPEs and VPLS on SPEs for E2E service transport. From the perspective of an SPE, a VPWS or VPLS PW established statically or established using LDP from the SPE to a UPE is a spoke VPLS PW that does not follow the split horizon rule. From the perspective of a UPE, a PW established from itself to an SPE is a VPWS LDP PW. Similarly, in a common VPLS scenario, if PEs do not support VPLS, you can configure VPWS accessing VPLS on the PEs. For details, see [VPWS Accessing VPLS.](feature_0013661306.html)

**Figure 1** Typical HVPLS networking for VPWS accessing VPLS  
![](images/fig_dc_vrp_vpls_cfg_500201.png)  


#### Pre-configuration Tasks

Before configuring VPWS accessing VPLS, complete the following tasks:

* Configure IP addresses and IGP routes on UPEs, SPEs, and Ps.
* Configure LSR IDs and enable MPLS and MPLS LDP on UPEs, SPEs, and Ps.
* Enable MPLS L2VPN on UPEs and SPEs.
* Establish tunnels between SPEs and between UPEs and SPEs for data transmission.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Establish remote LDP sessions if the SPEs or SPEs and UPEs are not directly connected.


[Configuring Static VPWS Accessing VPLS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6030.html)

This section describes how to configure static VPWS accessing VPLS when UPEs do not support VPLS.

[Configuring Dynamic VPWS Accessing VPLS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6031.html)

This section describes how to configure dynamic VPWS accessing VPLS when UPEs do not support VPLS.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6032.html)

After configuring VPWS accessing VPLS, you can check information about VPWS and VPLS connections, VPLS VSIs, outbound interfaces of VSI PWs, and tunnel policies applied to VSIs.