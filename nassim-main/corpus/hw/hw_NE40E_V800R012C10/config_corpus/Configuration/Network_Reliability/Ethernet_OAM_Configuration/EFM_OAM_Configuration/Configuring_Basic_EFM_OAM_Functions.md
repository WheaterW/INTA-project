Configuring Basic EFM OAM Functions
===================================

You can configure basic EFM OAM functions to check link connectivity between two directly connected devices.

#### Usage Scenario

With the development of Ethernet services, carriers are increasingly focusing on device maintainability. During Ethernet expansion to MANs or WANs, there is an urgent need for implementing OAM on transport networks. Maintenance methods for link-level Ethernet, however, are limited. Ethernet OAM resolves this issue. The hierarchical and layered network architecture requires hierarchical and layered Ethernet OAM. The traditional Ethernet management function is implemented at the layers upper than the network layer.

EFM OAM is link-level OAM and defines Ethernet physical layer specifications and implements Ethernet OAM for user access. On a MAN, EFM OAM is usually applied between directly connected CEs and PEs, which ensures the reliability and stability of connections between the user network and carrier network. To check link connectivity between two directly connected devices on the network shown in [Figure 1](#EN-US_TASK_0172361995__fig_dc_vrp_efm_cfg_200301), configure basic EFM OAM functions.

**Figure 1** Configuring basic EFM OAM functions  
![](images/fig_dc_vrp_efm_cfg_200301.png)  


#### Pre-configuration Tasks

Before configuring basic EFM OAM functions, complete the following tasks:

* Power on the devices and ensure that they are working properly.
* Ensure that the link between two directly connected devices is an Ethernet physical link and that the link is working properly.


[Enabling EFM OAM Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_efm_cfg_2004.html)

You must enable EFM OAM globally before configuring EFM OAM functions.

[Configuring an EFM OAM Working Mode for an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_efm_cfg_2005.html)

An EFM OAM working mode is an attribute of an interface enabled with EFM OAM. An interface works in either active or passive mode.

[(Optional) Setting OAM PDU Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_efm_cfg_2033.html)

You can set the maximum OAM PDU size, interval at which OAM PDUs are sent, and interval at which OAM PDUs are received to effectively control OAM PDU transmission.

[Enabling EFM OAM on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_efm_cfg_2009.html)

Point-to-point EFM link detection can be performed only after EFM OAM is enabled on the interfaces at both ends of a link. Perform the following steps at both ends of a link:

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_efm_cfg_2010.html)

After configuring basic EFM OAM functions, verify the configurations.