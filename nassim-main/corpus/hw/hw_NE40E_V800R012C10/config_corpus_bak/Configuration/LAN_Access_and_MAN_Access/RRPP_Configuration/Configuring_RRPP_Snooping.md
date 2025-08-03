Configuring RRPP Snooping
=========================

RRPP Snooping is a technology through which changes on an RRPP ring can be notified to a virtual private LAN service (VPLS) network. When RRPP Snooping is configured on sub-interfaces or VLANIF interfaces, the VPLS network can transparently transmit RRPP protocol packets, detect the changes on the RRPP rings, and upgrade the forwarding entries to ensure that traffic is switched in time to a congestion-free path.

#### Applicable Environment

UPEs constructing an RRPP ring access the virtual private LAN service (VPLS) network where UPEs reside, you need to configure the RRPP snooping on the NPE at the border of the RRPP ring and the VPLS network. In this manner, the VPLS network between NPEs can sense the change of the RRPP ring topology, and NPEs can timely update the MAC address table of the virtual switch instance (VSI). This ensures the continuity of VPLS.

As shown in [Figure 1](#EN-US_TASK_0172363685__fig_dc_vrp_rrpp_cfg_000101), VPLS is run between NPEs, and RRPP is run among NPE D, UPE A, and UPE B.

**Figure 1** Networking diagram of RRPP and VPLS
  
![](images/fig_dc_vrp_rrpp_cfg_000101.png)
#### Pre-configuration Tasks

Before configuring the RRPP snooping, complete the following tasks:

* Configure a VPLS network.
* Configure an RRPP ring.
* Ensure that the sub-interface or VLANIF interface enabled with the RRPP snooping allows the control VLAN packets sent by the master node of RRPP to pass through.


[Enabling RRPP Snooping](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rrpp_cfg_0002.html)

After being enabled with RRPP Snooping, an interface can detect the RRPP ring status through RRPP control packets. In addition, when the RRPP ring status changes, the interface notifies the bound virtual switch instance (VSI) to update the MAC address table.

[(Optional) Configuring the VSI Associated with RRPP Snooping](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rrpp_cfg_0003.html)

This part describes how to associate the sub-interface or VLANIF interface enabled with RRPP Snooping with other virtual switch instances (VSIs) related to the device. Therefore, the interface can inform the associated VSIs of the change in the RRPP ring status so that the VSIs can upgrade their MAC address tables accordingly.

[Verifying the RRPP Snooping Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rrpp_cfg_0004.html)

After the basic RRPP Snooping functions are successfully configured, you can view the interface enabled with RRPP Snooping and the names of the virtual switch instances (VSIs) that are associated with RRPP Snooping.