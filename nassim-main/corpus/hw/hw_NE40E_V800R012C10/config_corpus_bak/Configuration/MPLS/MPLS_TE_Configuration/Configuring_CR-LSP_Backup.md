Configuring CR-LSP Backup
=========================

CR-LSP backup is configured to provide end-to-end protection for a CR-LSP.

#### Usage Scenario

CR-LSP backup provides an end-to-end path protection for an entire CR-LSP.

CR-LSP backup is performed in either of the following modes:

* Hot standby: A backup CR-LSP is set up immediately after a primary CR-LSP is set up. If the primary CR-LSP fails, traffic switches to the backup CR-LSP. If the primary CR-LSP recovers, traffic switches back to the primary CR-LSP by default. Hot-standby CR-LSPs support best-effort paths.
* Ordinary backup: A backup CR-LSP is set up after a primary CR-LSP fails. If the primary CR-LSP fails, traffic switches to the backup CR-LSP. If the primary CR-LSP recovers, traffic switches back to the primary CR-LSP by default.
  
  For details about the differences between hot standby and ordinary backup, see [Table 1](#EN-US_TASK_0172368223__en-us_concept_0172355384_tab_dc_vrp_te-p2p_feature_001701).
  
  **Table 1** Differences between hot standby and ordinary backup
  | Item | Hot Standby | Ordinary Backup |
  | --- | --- | --- |
  | Time when a backup CR-LSP is established | Created immediately after the primary CR-LSP is established. | Created only after the primary CR-LSP fails. |
  | Primary and backup explicit paths | You can specify whether the primary and backup paths can overlap. If an explicit path is allowed for a backup CR-LSP, the explicit path is used as the constraint to set up the backup CR-LSP. | The path of the backup CR-LSP can partially overlap the path of the primary CR-LSP, regardless of whether the backup CR-LSP is set up over an explicit path. |
  | Whether a best-effort path is supported | Yes | No |
* Best-effort path
  
  The hot standby function supports the establishment of best-effort paths. If both the primary and hot-standby CR-LSPs fail, a best-effort path is established and takes over traffic.
  
  As shown in [Figure 1](#EN-US_TASK_0172368223__en-us_concept_0172355384_fig_dc_vrp_te-p2p_feature_001701), the primary CR-LSP uses the path PE1 -> P1 -> PE2, and the backup CR-LSP uses the path PE1 -> P2 -> PE2. If both the primary and backup CR-LSPs fail, Router triggers the setup of a best-effort path PE1 -> P2 -> P1 -> PE2.
  
  **Figure 1** Schematic diagram for a best-effort path  
  ![](images/fig_feature_image_0003991718.png)  
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  A best-effort path does not provide reserved bandwidth for traffic. The affinity attribute and hop limit are configured as needed.


#### Pre-configuration Tasks

Before configuring CR-LSP backup, complete the following tasks:

* Establish a primary RSVP-TE tunnel.
* Enable MPLS, MPLS TE, and RSVP-TE globally and in the physical interface view on each node along a bypass tunnel to be established. For configuration details, see [Enabling MPLS TE and RSVP-TE](dc_vrp_te-p2p_cfg_0004.html).
* (Optional) Configure the link bandwidth for the backup CR-LSP. (See [(Optional) Configuring TE Attributes](dc_vrp_te-p2p_cfg_0006.html).)
* (Optional) Configure an explicit path for the backup CR-LSP. (See [(Optional) Configure an explicit path](dc_vrp_te-p2p_cfg_0007.html).)


[Configuring CR-LSP Hot Standby](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0058.html)

A hot-standby CR-LSP is established immediately after a primary CR-LSP is set up. If the primary CR-LSP fails, traffic is switched to the hot-standby CR-LSP.

[Configuring a Best-Effort Path for a CR-LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0059.html)

A best-effort path is configured to take over traffic if both the primary and hot-standby CR-LSPs fail.

[Configuring Ordinary Backup for CR-LSPs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0142.html)

An ordinary backup CR-LSP is set up after the primary CR-LSP fails. If the primary CR-LSP fails, traffic is switched to the ordinary backup CR-LSP.

[Verifying the CR-LSP Backup Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0060.html)

After configuring CR-LSP backup, you can view information about backup CR-LSPs.