Configuring the Association Between EFM OAM and an Interface
============================================================

When the primary and backup links are deployed, you can associate EFM OAM with an interface to perform rapid service switchovers.

#### Usage Scenario

A device configured with IP services is usually connected to an IP network over the primary and backup links to improve network robustness and service reliability. In the current mainstream design, devices configured with IP services usually use VRRP to perform primary and backup link detection and switchovers. As a result, reliability cannot be ensured for carrier-class services.

After EFM OAM is associated with an interface, the link layer protocol status of the interface is set to Down if a link fault is detected. This association triggers rapid route convergence to block services at the link layer and implement rapid route switchovers.

**Figure 1** Association between EFM OAM and an interface  
![](images/fig_dc_vrp_efm_cfg_202301.png)  


#### Pre-configuration Tasks

Before associating EFM OAM with an interface, [configure basic EFM OAM functions](dc_vrp_efm_cfg_2003.html).


[Associating EFM OAM with an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_efm_cfg_2030.html)

You can associate EFM OAM with an interface to perform rapid service switchovers.

[(Optional) Setting the Time During Which the EFM OAM Status of an Interface Remains Down](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_efm_cfg_2031.html)

After EFM OAM is associated with an interface, you can adjust the delay in changing the EFM OAM status of an interface from Down to Up by setting the time during which the EFM OAM status of the interface remains Down, if a link connectivity fault is rectified.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_efm_cfg_2032.html)

After associating EFM OAM with an interface, verify the configurations.