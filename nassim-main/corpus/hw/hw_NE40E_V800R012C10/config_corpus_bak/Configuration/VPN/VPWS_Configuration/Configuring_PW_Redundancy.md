Configuring PW Redundancy
=========================

To build a virtual private line from a gNodeB to an NGC, you can configure SS-PWs or MS-PWs between CSGs and RSGs. In addition, PW redundancy needs to be configured for link reliability.

#### Usage Scenario

Network deployment requires high L2VPN service reliability. Currently, many fast fault detection and protection switching mechanisms are available, such as BFD, OAM, and FRR. These mechanisms, however, address only link or node failures within a PSN, but not PE failures or AC link failures between PEs and CEs.

PW redundancy resolves problems related to AC link and PE failures. Its goal is to eliminate single points of failure on an emulated service path through AC link, PE, and PW redundancy. If two or more paths exist between CEs, how can we ensure that only one primary path exists at any time? In other words, how can we select a PW from two or more PWs on a PE to forward data packets? How can we quickly switch traffic to the backup path when a PE or AC fails? These are issues that PW redundancy addresses.

[Figure 1](#EN-US_TASK_0172369834__fig_dc_vrp_vpws_cfg_500701) shows a typical PW redundancy scenario. On the network shown in the figure, MS-PWs have been deployed between PE1 and PE2 and between PE1 and PE3. To improve network reliability, configure PW redundancy on SPEs or PE1.

**Figure 1** Configuring PW redundancy for MS-PWs  
![](images/fig_dc_vrp_vpws_cfg_500701.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Only PWE3 VPWS supports PW redundancy. After the [**mpls l2vpn default martini**](cmdqueryname=mpls+l2vpn+default+martini) command is run, VPWS does not support PW redundancy any longer.
* When configuring PW redundancy, be sure to configure the primary, secondary, and bypass PW parameters consistently. Otherwise, the secondary or bypass PW may fail to take over services when the primary PW fails.

The active/standby status of PWs is determined in the following modes:

* FRR: This is the default mode and does not need to be configured.
* Negotiation: This mode needs to be configured using a command.
  + Master/slave mode: The active and standby PWs are manually specified on the master device, which then notifies the slave device of the PW active/standby status. The combined use of PW redundancy in master/slave mode and the bypass PW can prevent network-side faults from affecting the AC side and AC-side faults from affecting the network side.
  + Independent mode: The active/standby status is determined through negotiation. When creating PWs on the local end, configure two PWs, with each connecting to a remote PE. At this time, the two remote PEs are both in the master state locally. The remote PEs then determine their status by means of E-Trunk or mVRRP, with one PE in the master state and the other in the backup state. Finally, the PW endpoints determine the active and standby PWs through negotiation. The independent mode applies to scenarios where PW redundancy is associated with E-Trunk. The independent mode, together with the bypass PW, can protect links on the AC side against faults on the network side, but cannot protect links on the network side against faults on the AC side.

#### Pre-configuration Tasks

Before configuring PW redundancy, complete the following tasks:

* Configure IP addresses and an IGP on PEs and SPEs.
* Configure basic MPLS functions on PEs.
* Establish a public network tunnel between PE1 and each SPE and between PE2 and PE3. The public network tunnel can be an LDP or TE tunnel.


[Configuring the Master/Slave Mode of PW Redundancy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_5008.html)

PW redundancy in master/slave mode implements fault isolation for public and AC links.

[Configuring the Independent PW Redundancy Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_5009.html)

The independent PW redundancy mode allows a public network fault to trigger only the public network link switchover.

[Configuring PW Status Negotiation](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6020.html)

In independent PW redundancy mode, the master/backup status of the local PE is determined by the signaling status sent from the remote PE.

[Binding Service PWs to an mPW](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6019.html)

After service PWs are bound to an mPW, the service PW status is determined by the mPW status.

[Configuring BFD for VPWS PW](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_5012-01.html)

Configuring BFD for VPWS PW accelerates PW fault detection, resulting in fast switching of upper-layer applications.

[(Optional) Configuring a Switching Delay for PW Switching](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6077.html)

When a switching delay is configured for a PW, the master PW fails, the traffic switches to the slave PW after the delay period expires.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_5010.html)