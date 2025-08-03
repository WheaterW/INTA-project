Configuring VXLAN Accessing BRAS
================================

When telco cloud gateways use VXLAN for user access, you need to configure VXLAN accessing BRAS on the device responsible for user access.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0000001214336005__fig572613134213), telco cloud gateways (DCGW1 and DCGW2) connect to the aggregation device CPE through VXLAN tunnels. VXLAN is also deployed between the CPE and physical UP (pUP). To enable users to access the external network, configure VXLAN accessing BRAS on the pUP.

**Figure 1** Network diagram of VXLAN accessing BRAS  
![](figure/en-us_image_0000001214535909.png)

#### Pre-configuration Tasks

Before configuring VXLAN accessing BRAS, complete one of the following tasks on the CPE and pUP:

* [Configure VXLAN in centralized gateway mode for static tunnel establishment](dc_vrp_vxlan6_cfg_0017.html).
* [Configure VXLAN in centralized gateway mode using BGP EVPN](dc_vrp_vxlan_cfg_0017b.html).
* [Configure VXLAN in distributed gateway mode using BGP EVPN](dc_vrp_vxlan_cfg_1216.html).


[Creating an L2VE Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan_bras1.html)

Configure an L2VE interface on the pUP to terminate VXLAN services and bind the interface to a VE group.

[Creating an L3VE Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan_bras2.html)

Configure an L3VE interface used for BRAS access on the pUP and bind the L3VE interface to a VE group.

[Associating the L2VE Interface with a BD](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan_bras3.html)

Associate the L2VE interface with a BD on the pUP, so that VXLAN services can be terminated on the L2VE interface.

[Configuring the L3VE Interface as a BAS Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan_bras4.html)

Configure the L3VE interface on the pUP as a BAS interface for BRAS access.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan_bras5.html)

After configuring VXLAN accessing BRAS, you can view binding between the VE interfaces and VE group and VXLAN tunnel information on the pUP.