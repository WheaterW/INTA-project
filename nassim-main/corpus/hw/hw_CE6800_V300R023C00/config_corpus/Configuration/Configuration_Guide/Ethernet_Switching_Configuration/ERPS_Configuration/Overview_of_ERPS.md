Overview of ERPS
================

Overview of ERPS

#### Definition

Ethernet Ring Protection Switching (ERPS) is a protocol defined by the International Telecommunication Union-Telecommunication Standardization Sector (ITU-T) to prevent loops at Layer 2. ERPS is also called G.8032 because its standard number is ITU-T G.8032/Y.1344. It defines the ring automatic protection switching (R-APS) messages and protection switching mechanism.


#### Purpose

Redundant links (such as those on a ring network) are usually used on an Ethernet switched network to provide link backup and improve network reliability. The use of redundant links, however, may cause loops, leading to broadcast storms and unstable MAC address entries. As a result, the communication quality deteriorates, and communication services may even be interrupted. To prevent loops, the device supports the ring network protocols listed in [Table 1](#EN-US_CONCEPT_0000001188054499__tab_dc_fd_erps_0001).

**Table 1** Ring network protocols supported by the device
| Ring Network Protocol | Advantage | Disadvantage |
| --- | --- | --- |
| STP/RSTP/MSTP | * STP, RSTP, and MSTP apply to all Layer 2 networks. * STP, RSTP, and MSTP are standard IEEE protocols that allow the device to communicate with devices from other vendors. | STP, RSTP, and MSTP provide slow convergence, which is affected by the network size and cannot meet carrier-class reliability requirements. |
| ERPS | * ERPS provides fast convergence, which meets carrier-class reliability requirements. * ERPS is a standard ITU-T protocol that allows the device to communicate with devices from other vendors. * ERPSv2 supports both single-ring and multi-ring topologies. | The network topology must be planned, and the configuration is complex. |


As a standard loop prevention protocol defined by the ITU-T, ERPS overcomes the drawbacks of STP, RSTP, and MSTP. ERPS provides fast convergence, meets carrier-class reliability requirements, and supports multiple networking modes. It has good compatibility and allows the device to communicate with devices from other vendors. Therefore, ERPS is widely used on Layer 2 ring networks.