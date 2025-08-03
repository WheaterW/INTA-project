Overview of Ethernet OAM
========================

Overview of Ethernet OAM

#### Definition

Easy-to-use Ethernet techniques support good bandwidth expansibility on low-cost hardware. With these advantages, Ethernet services and structures have been widely used on enterprise networks, metropolitan area networks (MANs), and wide area network (WANs). As Ethernet applications become increasingly popular, carriers are eager to use improved Ethernet Operations, Administration, and Maintenance (OAM) functions to maintain and operate Ethernets.

OAM mechanisms for server-layer services such as synchronous digital hierarchy (SDH) or for client-layer services such as IP are inapplicable to Ethernet networks. To monitor Ethernet link connectivity, pinpoint faults on Ethernet networks, and evaluate network usage and performance, Ethernet OAM is developed and used, which is different from client- or server-layer OAM. These functions help carriers provide services based on service level agreements (SLAs).

Ethernet OAM is used for Ethernet networks.

Ethernet OAM provides the following functions:

* Fault management
  
  + Ethernet OAM sends detection packets on demand or periodically to monitor network connectivity.
  + Ethernet OAM uses methods similar to Packet Internet Groper (PING) and traceroute used on IP networks to locate and diagnose faults on Ethernet networks.
  + Ethernet OAM is used together with a protection switching protocol to trigger a device or link switchover if a connectivity fault is detected. Switchovers help networks achieve carrier-class reliability by ensuring that network interruptions are less than or equal to 50 milliseconds.
* Performance management
  
  Ethernet OAM measures network transmission parameters including the frame loss rate, delay, and jitter and collects traffic statistics including the number of sent and received bytes and the number of frame errors. Carriers use this function to monitor network operation and dynamically adjust parameters in real time based on statistical data. This process reduces maintenance costs.


#### Ethernet OAM Network

[Table 1](#EN-US_CONCEPT_0172361887__en-us_concept_0172351690_tab_dc_vrp_feature_new_eoam_00000201) shows the hierarchical Ethernet OAM network structure.

**Table 1** Ethernet OAM network
| Layer | Description | Feature | Usage Scenario |
| --- | --- | --- | --- |
| Link-level Ethernet OAM | Monitors physical Ethernet links directly connecting carrier networks to user networks. For example, the Institute of Electrical and Electronics Engineers (IEEE) 802.3ah, also known as Ethernet in the First Mile (EFM), supports Ethernet OAM for the last-mile links and also monitors direct physical Ethernet links. | EFM supports link continuity check, fault detection, fault advertisement, and loopback for P2P Ethernet link maintenance. Unlike CFM that is used for a specific type of service, EFM is used on links transmitting various services. | EFM is mainly used between customer edges (CEs) and underlayer provider edges (UPEs) on the MAN shown in [Figure 1](#EN-US_CONCEPT_0172361887__en-us_concept_0172351690_fig_dc_vrp_feature_new_eoam_00000201), to ensure the reliability and stability of connections between user networks and carrier networks. EFM monitors and rectifies faults on P2P Ethernet physical links or simulated links. |
| Network-level Ethernet OAM | Checks network connectivity, pinpoints connectivity faults, and monitors E2E network performance at the access and aggregation layers. For example, IEEE 802.1ag (also known as Connectivity Fault management, CFM) and Y.1731 are used to implement network-level Ethernet OAM. | CFM defines OAM functions, such as continuity check (CC), loopback (LB), and link trace (LT), for Ethernet bearer networks. CFM applies to large-scale E2E Ethernet networks. | CFM is used on access and aggregation layers of the MAN shown in [Figure 1](#EN-US_CONCEPT_0172361887__en-us_concept_0172351690_fig_dc_vrp_feature_new_eoam_00000201). For example, CFM monitors links between a UPE and a PE. It monitors network-wide connectivity and detects connectivity faults. It is used together with protection switchover mechanisms to maintain network reliability. |
| Y.1731 is an OAM protocol defined by the Telecommunication Standardization Sector of the International Telecommunication Union (ITU-T). It covers items defined in IEEE 802.1ag and provides additional OAM messages for fault management and performance monitoring. Fault management includes alarm indication signal (AIS), remote defect indication (RDI), locked signal (LCK), test signal, maintenance communication channel (MCC), experimental (EXP) OAM, and vendor specific (VSP) OAM. Performance monitoring includes frame loss measurement (LM) and delay measurement (DM). | Y.1731 is a CFM enhancement that applies to access and aggregation networks. Y.1731 supports performance monitoring functions, such as LM and DM, in addition to fault management that CFM supports. |


**Figure 1** Typical MAN networking  
![](images/fig_feature_image_0003995347.png)  


#### Benefits

E2E CFM/P2P EFM/E2E Y.1731 is used to provide an Ethernet OAM solution, which brings the following benefits:

* Ethernet is deployed near user premises using remote terminals and roadside cabinets at remote central offices or in unattended areas. Ethernet OAM allows remote maintenance, saving the trouble of onsite maintenance. Engineers operate detection, diagnosis, and monitoring protocols and techniques from remote locations to maintain Ethernet networks. Remote OAM maintenance saves the trouble of onsite maintenance and helps reduce maintenance and operation expenditures.
* Ethernet OAM supports various performance monitoring tools that are used to monitor network operation and assess service quality based on SLAs. If a device using the tools detects faults, the device sends traps to a network management system (NMS). Carriers use statistics and trap information on NMSs to adjust services. The tools help ensure proper transmission of voice and data services.