Configuring MPLS OAM for a PW
=============================

This section describes how to configure MPLS OAM to check the connectivity of a PW.

#### Usage Scenario

On an MPLS L2VPN, traditional detection techniques can monitor the status of a PW but cannot send defect packets or report a defect type through the reverse tunnel of the PW. The shortcoming delays fault detection and link switchovers performed by an upper-layer application. To address this issue, configure MPLS OAM to monitor the PW.

MPLS OAM is a detection mechanism for the user plane separated from the network plane and can notify users of the PW status. A network administrator or maintenance engineer uses the information to evaluate network performance and maintain a network.

MPLS OAM can monitor the status of all PWs between two nodes or use a peer IP address, virtual circuit (VC) encapsulation type, and VC ID to identify a PW and obtain detailed information (including basic PW and OAM information and OAM detection information). The information can be used to maintain a network.

[Table 1](#EN-US_CONCEPT_0172362359__table_0000038019) describes the support of MPLS OAM detection for different types of PWs.

**Table 1** The support of MPLS OAM detection for different types of PWs
| Function | Static VPWS | Static VPLS |
| --- | --- | --- |
| CV/FFD | support | support |
| FDI | support | nonsupport |



#### Pre-configuration Tasks

Before configuring MPLS OAM for a PW, configure the PW.


[Configuring Basic Detection Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mplsoam_cfg_0013.html)

This section describes how to configure proper MPLS OAM parameters on both ends of a PW for network loads.

[Verifying the Configuration of MPLS OAM for a PW](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mplsoam_cfg_0015.html)

After configuring MPLS OAM for a PW, verify the configurations.