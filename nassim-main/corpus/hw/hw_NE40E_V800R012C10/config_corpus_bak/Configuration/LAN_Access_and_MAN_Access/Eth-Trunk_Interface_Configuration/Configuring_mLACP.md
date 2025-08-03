Configuring mLACP
=================

Configuring_mLACP

#### Usage Scenario

mLACP provides similar functions to E-Trunk, as shown in [Figure 1](#EN-US_TASK_0000001213773084__fig_dc_vrp_ethtrunk_feature_001901). In multi-chassis scenarios, the local device cannot obtain the configuration and negotiation parameters of a peer device that has Eth-Trunk in LACP mode configured, so master/backup protection cannot be implemented. mLACP can be used to resolve this issue. It synchronizes LACP configuration and status information between dual-homed devices through a reliable ICCP channel, making master/backup protection possible.

**Figure 1** mLACP  
![](figure/en-us_image_0000001214309530.png)


[Creating an ICCP Redundancy Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0053.html)



[Enabling mLACP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0054.html)



[Binding an Eth-Trunk Interface to an ICCP Redundancy Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0055.html)