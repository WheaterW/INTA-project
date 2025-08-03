(Optional) Configuring the Path Cost for a Port
===============================================

The STP/Rapid Spanning Tree Protocol (RSTP) path cost determines root port selection. The port from which to the root port costs the least is selected as the root port.

#### Context

A path cost is port-specific, which is used by STP/RSTP as a reference to select a link.

The range of the path cost value is determined by the calculation method. After the calculation method is determined, you are recommended to set a relatively small path cost value for the port at a high link rate.

Use the Huawei proprietary calculation method as an example. Different link rates correspond to default path cost values of ports. For details, see [Table 1](#EN-US_TASK_0172363543__tab_dc_vrp_stp_cfg_0008_01).

**Table 1** Mappings between link rates and path cost values
| Link Rate | Recommended value | Recommended Value Range | Value Range |
| --- | --- | --- | --- |
| 10 Mbit/s | 2000 | 200 to 20000 | 1 to 200000 |
| 100 Mbit/s | 200 | 20 to 2000 | 1 to 200000 |
| 1 Gbit/s | 20 | 2 to 200 | 1 to 200000 |
| 10 Gbit/s | 2 | 2 to 20 | 1 to 200000 |
| Over 10 Gbit/s | 1 | 1 to 2 | 1 to 200000 |


On a network where loops occur, you are recommended to set a relatively large path cost for the port at a low link rate. STP/RSTP puts the port with the large path cost in the Blocking state and blocks the link where this port resides.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**stp pathcost-standard**](cmdqueryname=stp+pathcost-standard) { **dot1d-1998** | **dot1t** | **legacy** }
   
   
   
   The path cost calculation method is configured.
   
   
   
   All devices on a network must use the same method to calculate path costs.
   
   [Table 2](#EN-US_TASK_0172363543__tab_stp_pathcost_standard_01) lists the path costs defined in the IEEE 802.1D-1998 standard method, IEEE 802.1t standard method, and Huawei-proprietary calculation method. Different vendors use different path cost calculation methods.
   
   **Table 2** Path cost list
   | Port Rate | Port Mode | STP Path Cost (Recommended) | | |
   | --- | --- | --- | --- | --- |
   | IEEE 802.1d-1998 Standard Method | IEEE 802.1t Standard Method | Huawei-Proprietary Calculation Method |
   | 0 | - | 65535 | 200,000,000 | 200,000 |
   | 10Mbps | Half-Duplex | 100 | 2,000,000 | 2000 |
   | Full-Duplex | 99 | 1,999,999 | 1999 |
   | Aggregated Link 2 Ports | 95 | 1,000,000 | 1800 |
   | Aggregated Link 3 Ports | 95 | 666,666 | 1600 |
   | Aggregated Link 4 Ports | 95 | 500,000 | 1400 |
   | 100Mbps | Half-Duplex | 19 | 200,000 | 200 |
   | Full-Duplex | 18 | 199,999 | 199 |
   | Aggregated Link 2 Ports | 15 | 100,000 | 180 |
   | Aggregated Link 3 Ports | 15 | 66,666 | 160 |
   | Aggregated Link 4 Ports | 15 | 50,000 | 140 |
   | 1000Mbps | Full-Duplex | 4 | 20,000 | 20 |
   | Aggregated Link 2 Ports | 3 | 10,000 | 18 |
   | Aggregated Link 3 Ports | 3 | 6666 | 16 |
   | Aggregated Link 4 Ports | 3 | 5000 | 14 |
   | 10Gbps | Full-Duplex | 2 | 2000 | 2 |
   | Aggregated Link 2 Ports | 1 | 1000 | 1 |
   | Aggregated Link 3 Ports | 1 | 666 | 1 |
   | Aggregated Link 4 Ports | 1 | 500 | 1 |
3. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of the Ethernet interface participating in STP calculation is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The following configuration can be configured both on a Layer 2 interface and a Layer 3 interface.
4. Run [**stp cost**](cmdqueryname=stp+cost) *cost*
   
   
   
   A path cost is set for the port.
   
   
   
   * If the Huawei proprietary calculation method is used, *cost* ranges from 1 to 200000.
   * If the IEEE 802.1d standard method is used, *cost* ranges from 1 to 65535.
   * If the IEEE 802.1t standard method is used, *cost* ranges from 1 to 2000,000,00.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.