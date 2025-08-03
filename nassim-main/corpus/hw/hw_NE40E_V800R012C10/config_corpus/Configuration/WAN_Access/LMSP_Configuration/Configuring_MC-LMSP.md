Configuring MC-LMSP
===================

Inter-device LMSP switchbacks can be performed by configuring
MC-LMSP.

#### Usage Scenario

[Figure 1](#EN-US_CONCEPT_0172364391__fig_dc_ne_lmsp_cfg_001001) shows an MC-LMSP network.
Two network-side devices back up each other, improving link reliability.
MC-LMSP needs to be configured on these two devices dual-homed to
RNCs. MC-LMSP provides higher security than single-chassis LMSP provides.
Single-chassis LMSP means interface, subcard, and board-based LMSP.

**Figure 1** Association between an MC-LMSP group and PW redundancy
  
![](images/fig_dc_ne_lmsp_cfg_001001.png)  



#### Pre-configuration Task

Before configuring
MC-LMSP, complete the following tasks:

* Configure an interface on the Router and ensure that the data link layer protocol run between the Router and the RNC is Up.
* Run an IGP protocol on the backbone network so that devices can
  communicate with each other.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In a PPP-based Layer
  3 IP forwarding scenario, if devices use a dynamic routing protocol,
  the dynamic routes have to be re-learned during an LMSP link switchover.
  In the route convergence process, which lasts for dozens of seconds,
  service traffic may be dropped. To prevent this problem, configure
  static routes on the LMSP interfaces of the master, device, backup
  device, and the RNC. This configuration can prevent traffic loss.

#### Configuration Procedures

**Figure 2** Flowchart for configuring MC-LMSP
  
![](images/fig_dc_ne_lmsp_cfg_001002.png)


[Specifying a Working Interface and a Protect Interface for an LMSP Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_lmsp_cfg_0011.html)

A working interface and a protection interface must be specified and added to an LMSP group before other LMSP configurations are performed.

[Configuring a Working Mode for an LMSP Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_lmsp_cfg_0012.html)

A working mode can be configured for an LMSP group. The NE40E supports LMSP working modes, including automatic LMSP switching and a delayed switchback with the wait to restore (WTR) time configured. An LMSP working mode must be configured on a protection interface.

[(Optional) Binding an LMSP Group to a BFD Session](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_lmsp_cfg_0013.html)



[(Optional) MC-LMSP Negotiation and Authentication Parameters](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_lmsp_cfg_0014.html)

MC-LMSP-enabled routers run the Protection Group Protocol (PGP) to exchange control messages. Negotiation and authentication parameters can be set for PGP message transmission, helping use MC-LMSP functions easily and securely.

[Adding Interfaces of an LMSP Group to a Trunk Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_lmsp_cfg_0015.html)

A working interface and a protection interface in an LMSP group must be added to a single trunk interface.

[Checking the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_lmsp_cfg_0016.html)

After configuring MC-LMSP, you can check the LMSP group's working mode, working interface, switchback time, and interface status.