Overview of MPLS-TP OAM
=======================

Working at the Multiprotocol Label Switching Transport Profile (MPLS-TP) client and server layers, MPLS-TP operation, administration and maintenance (OAM) can effectively detect, identify, and locate faults at the client layer and quickly switch traffic if links or nodes fail.

#### Definition

Multiprotocol Label Switching Protocol Transport Profile (MPLS-TP) is a transport technique that integrates MPLS packet switching with traditional transport network features. MPLS-TP networks are poised to replace traditional transport networks in the future. MPLS-TP Operations, Administration and Maintenance (MPLS-TP OAM) can effectively detect, identify, and locate faults at the MPLS-TP user plane and quickly switch services away from faulty links or nodes. OAM is an important part of any plan to reduce network maintenance expenditures.


#### Purpose

Both networks and services are part of an ongoing process of transformation and integration. New services like triple play services, Next Generation Network (NGN) services, carrier Ethernet services, and Fiber-to-the-x (FTTx) services are constantly emerging from this process. Such services demand more investment and have higher OAM costs. They require state-of-the-art QoS, full service access, and high levels of expansibility, reliability, and manageability of transport networks. Traditional transport network technologies such as Multi-Service Transfer Platform (MSTP), Wavelength Division Multiplexing (WDM), or Synchronous Digital Hierarchy (SDH) cannot meet these requirements because they lack a control plane. Unlike traditional technologies, MPLS-TP does meet these requirements because it can be used on next-generation transport networks that can process data packets, as well as on traditional transport networks.

Because traditional transport networks have high reliability and maintenance benchmarks, MPLS-TP must provide powerful OAM capabilities. MPLS-TP OAM provides the following functions:

* Fault management
* Performance monitoring
* Triggering protection switching

#### Benefits

* MPLS-TP OAM can rapidly detect link faults or monitor the connectivity of links, which helps measure network performance and minimizes OPEX.
* If a link fault occurs, MPLS-TP OAM rapidly switches traffic to the standby link to restore services, which shortens the defect duration and improves network reliability.

#### MPLS-TP OAM Components

MPLS-TP OAM functions are implemented by maintenance entities (MEs). An ME consists of a pair of maintenance entity group end points (MEPs) located at two ends of a link and a group of maintenance entity group intermediate points (MIPs) between them.

MPLS-TP OAM components are described as follows:

* ME
  
  An ME maintains a relationship between two MEPs. On a bidirectional label switched path (LSP) that has two MEs, MPLS-TP OAM detection can be performed on the MEs without affecting each other. One ME can be nested within another ME but cannot overlap with another ME.
  
  ME1 and ME2 in [Figure 1](#EN-US_CONCEPT_0172362376__en-us_concept_0172351562_fig_dc_vrp_mpls-tp_oam_cfg_000201) are used as an example:
  + ME1 consists of two MEPs only.
  + ME2 consists of two MEPs and two MIPs.**Figure 1** ME deployment on a point-to-point bidirectional LSP  
  ![](figure/en-us_image_0000001508416889.png)
* MEG
  
  A maintenance entity group (MEG) comprises one or more MEs that are created for a transport link. If the transport link is a point-to-point bidirectional path, such as a bidirectional co-routed LSP or pseudo wire (PW), a MEG comprises only one ME.
* MEP
  
  A MEP is the source or sink node in a MEG. [Figure 2](#EN-US_CONCEPT_0172362376__en-us_concept_0172351562_fig_dc_vrp_mpls-tp_oam_cfg_000202) shows ME node deployment.**Figure 2** ME node deployment  
  ![](images/fig_dc_vrp_mpls-tp_oam_cfg_000202.png)  
  + For a bidirectional LSP, only the ingress label edge router (LER) and egress LER can function as MEPs, as shown in [Figure 2](#EN-US_CONCEPT_0172362376__en-us_concept_0172351562_fig_dc_vrp_mpls-tp_oam_cfg_000202).
  + For a PW, only user-end provider edges (UPEs) can function as MEPs.MEPs trigger and control MPLS-TP OAM operations. OAM packets can be generated or terminated on MEPs.


#### Fault Management

[Table 1](#EN-US_CONCEPT_0172362376__en-us_concept_0172351562_tab_dc_vrp_mpls-tp_oam_cfg_000301) lists the MPLS-TP OAM fault management functions supported by the NE40E.

**Table 1** MPLS-TP OAM fault management functions
| Function | Description |
| --- | --- |
| Continuity check (CC) | Checks link connectivity periodically. |
| Connectivity verification (CV) | Detects forwarding faults continuously. |
| Loopback (LB) | Performs loopback. |
| Remote defect indication (RDI) | Notifies remote defects. |




#### Performance Monitoring

[Table 2](#EN-US_CONCEPT_0172362376__en-us_concept_0172351562_tab_dc_vrp_mpls-tp_oam_cfg_000302) lists the MPLS-TP OAM performance monitoring functions supported by the NE40E.

**Table 2** MPLS-TP OAM performance monitoring functions
| Function | Description |
| --- | --- |
| Loss measurement (LM) | Collects statistics about lost packets. LM includes the following functions:  * Single-ended packet loss measurement * Dual-ended packet loss measurement |
| Delay measurement (DM) | Collects statistics about delay and jitter. DM includes the following functions:  * One-way packet delay measurement * Two-way packet delay measurement |