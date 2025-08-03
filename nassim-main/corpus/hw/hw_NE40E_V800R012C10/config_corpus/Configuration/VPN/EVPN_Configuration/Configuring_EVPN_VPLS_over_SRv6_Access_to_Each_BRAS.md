Configuring EVPN VPLS over SRv6 Access to Each BRAS
===================================================

If EVPN VPLS over SRv6 is used to carry E-LAN services, configure EVPN VPLS over SRv6 on each device that functions as a BRAS that provides access services for users.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0214204255__fig572613134213), EVPN VPLS over SRv6 is deployed on Metro Edge Function (MEF) devices and vBRAS-physical user planes (vBRAS-pUPs) to carry E-LAN services. To allow users to access the Internet, configure EVPN VPLS over SRv6 on each vBRAS-pUP.

**Figure 1** EVPN VPLS over SRv6 accessing each BRAS  
![](figure/en-us_image_0214268527.png)

#### Pre-configuration Tasks

Before configuring EVPN VPLS over SRv6 access to each BRAS, complete the following tasks:

[Configuring EVPN VPLS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0023.html) or [Configuring EVPN VPLS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpls_over_srv6-te_policy.html) on each MEF device, P, and vBRAS-pUP.


[Creating an L2VE Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_vpls_over_srv6_bras1.html)

Configure an L2VE interface on a vBRAS-pUP to terminate EVPN services and bind the interface to a VE group.

[Creating an L3VE Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_vpls_over_srv6_bras2.html)

Configure an L3VE interface on a vBRAS-pUP and bind the L3VE interface to a VE group.

[(Optional) Configuring MAC Addresses for L2VE and L3VE Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_vpls_over_srv6_bras3.html)

If the MAC address of the L2VE or L3VE interface is the same as that of another interface on a vBRAS-pUP, configure a new MAC address for the L2VE or L3VE interface for proper communication.

[Associating an L2VE Interface with a BD](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_vpls_over_srv6_bras4.html)

Associate an L2VE interface with a BD on a vBRAS-pUP so that E-LAN services can be terminated on the L2VE interface.

[Configuring an L3VE Interface as a BAS Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_vpls_over_srv6_bras5.html)

Configure an L3VE interface on a vBRAS-pUP as a BAS interface to implement BRAS access.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_vpls_over_srv6_bras6.html)

After configuring EVPN VPLS over SRv6 accessing BRAS, verify the binding between the VE interface and VE group and EVPN route information on each vBRAS-pUP.