Configuring a Port Bandwidth Allocation Mode
============================================

This section describes how to configure a bandwidth allocation mode for a port to meet bandwidth requirements.

#### Prerequisites

Before changing a port bandwidth allocation mode, perform the check tasks listed in the following table.

| Original Port Bandwidth Allocation Mode | Target Port Bandwidth Allocation Mode | Port Check | Flexible Subcard Check |
| --- | --- | --- | --- |
| **28x10GE**  NOTE:  Only the NE40E-M2H supports this mode. | **26x10GE+18xGE** | Check ports 26 and 27.   1. Check that the ports are shut down and not added to any VS. 2. (Required only during port deletion) Check that clock configurations do not exist on the ports. | N/A |
| **28x10GE**  NOTE:  Only the NE40E-M2H supports this mode. | **20x10GE+24xGE** | Check ports 20 to 27.   1. Check that the ports are shut down and not added to any VS. 2. (Required only during port deletion) Check that clock configurations do not exist on the ports. | N/A |
| **26x10GE+18xGE**  NOTE:  Only the NE40E-M2H supports this mode. | **28x10GE** | Check ports 26 to 43.   1. Check that the ports are shut down and not added to any VS. 2. (Required only during port deletion) Check that clock configurations do not exist on the ports. | N/A |
| **20x10GE+24xGE**  NOTE:  Only the NE40E-M2H supports this mode. | **28x10GE** | Check ports 20 to 43.   1. Check that the ports are shut down and not added to any VS. 2. (Required only during port deletion) Check that clock configurations do not exist on the ports. | Check flexible subcards excluding the CR5D00E1MF70/CR5D00E1NC79/CR5D08CWDM70/CR5D00L4XF72/CR5D3DMR4M01/CR5D3DMR4M02/CR5D1DMD1M01/CR5D1DMD1M03/CR5D1DMD1M02/CR5D1DMD1M05/CR5D1DMD1M04/CR5D1DMD1M07/CR5D1DMD1M06/CR5D1DMD1M08/CR5D2DMD2M02/CR5D2DMD2M04/CR5D2DMD2M03/CR5D2DMD2M01. |
| **2x100GE**  NOTE:  Only the NE40E-M2H supports this mode. | **1x100GE+4x10GE** | Check port 0.   1. Check that the port is shut down and not added to any VS. 2. (Required only during port deletion) Check that clock configurations do not exist on the ports. | N/A |
| **1x100GE+4x10GE**  NOTE:  Only the NE40E-M2K/-M2K-B supports this mode. | **2x100GE** | Check ports 2 to 5.   1. Check that the ports are shut down and not added to any VS. 2. (Required only during port deletion) Check that clock configurations do not exist on the ports. 3. Check that the ports are not virtual access internal communication ports. | N/A |
| **2x100GE**  NOTE:  Only the NE40E-M2K/-M2K-B supports this mode. | **1x100GE+4x10GE** | Check port 0.   1. Check that the ports are shut down and not added to any VS. 2. (Required only during port deletion) Check that clock configurations do not exist on the ports. 3. Check that the ports are not virtual access internal communication ports. | N/A |
| **1x100GE+4x10GE**  NOTE:  Only the NE40E-M2K/-M2K-B supports this mode. | **2x100GE** | Check ports 2 to 5.   1. Check that the ports are shut down and not added to any VS. 2. (Required only during port deletion) Check that clock configurations do not exist on the ports. 3. Check that the ports are not virtual access internal communication ports. | N/A |
| **eth-2x100G-30x10GF-10xgf**  NOTE:  Only the NE40E-M2K/-M2K-B supports this mode. | **eth-2x100g-26x10GF-14xgf** | Check ports 28 to 31.   1. Check that the ports are shut down and not added to any VS. 2. (Required only during port deletion) Check that clock configurations do not exist on the ports. 3. Check that the port is not a virtual access internal communication port. | Check flexible subcards excluding the CR5D000IE170/CR5D000IE171/CR5D000DE170/CR5D000DE171/CR5D00C4CF71/CR5D00EEGF71/CR5D00LAXF90/CR5D00E1NC98/CR5D00E2NF90/CR5D0E5XMF90/CR5DE2NE4X10/CR5DE2NE4X12/CR5D00E1NB20/CR5D00E4XF20/CR5D00E1MF70/CR5D00AUXQ10/CR5D00P4CF70/CR5DP2C1HF70/CR5D00E8GE71/CR5D00E8GF71/CR5DL1XE8G71/CR5D00EAGF70 /CR5D0EAGFH70. |
| **eth-2x100g-26x10GF-14xgf**  NOTE:  Only the NE40E-M2K/-M2K-B supports this mode. | **eth-2x100G-30x10GF-10xgf** | Check ports 28 to 31.   1. Check that the ports are shut down and not added to any VS. 2. (Required only during port deletion) Check that clock configurations do not exist on the ports. 3. Check that the port is not a virtual access internal communication port. | Check flexible subcards excluding the CR5D00EEGF71/CR5D00LAXF90/CR5D00E1NC98/CR5D00E2NF90/CR5D0E5XMF90/CR5DE2NE4X10/CR5DE2NE4X12/CR5D00E1NB20/CR5D00E4XF20/CR5D00AUXQ10/CR5D00E1MF70. |



#### Context

M2H subcards support the following port bandwidth allocation modes:

* eth-26x10gf-18xgf-mode: 44 valid ports, with 10GE bandwidth on each of the first 26 ports and 1GE bandwidth on each of the remaining 18 ports
* eth-28x10gf-mode: 28 valid ports, with 10GE bandwidth on each of the ports
* eth-20x10gf-24xgf-mode: 44 valid ports, with 10GE bandwidth on each of the first 20 ports and 1GE bandwidth on each of the remaining 24 ports

M2K subcards support the following port bandwidth allocation modes:

* eth-26x10gf-18xgf-mode: 44 valid ports, with 10GE bandwidth on each of the first 26 ports and 1GE bandwidth on each of the remaining 18 ports
* eth-28x10gf-mode: 28 valid ports, with 10GE bandwidth on each of the ports
* eth-20x10gf-24xgf-mode: 44 valid ports, with 10GE bandwidth on each of the first 20 ports and 1GE bandwidth on each of the remaining 24 ports

The MACsec 2 x 100GE subcards support the following port bandwidth allocation modes:

* eth-2x100ge-mode: 2 valid ports, with 100GE bandwidth on each of the ports
* eth-1x100ge-4x10gf-mode: 5 valid ports, with 100GE bandwidth on the first port and 10GE bandwidth on each of the remaining 4 ports

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**slot**](cmdqueryname=slot) *slot-id* command to enter the slot view.
3. Run the [**set service-mode card-bandwidth-mode**](cmdqueryname=set+service-mode+card-bandwidth-mode) *bandwidth-mode* **card** *card-id* command to configure a port bandwidth allocation mode.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

Run the [**display service-mode card-bandwidth-mode**](cmdqueryname=display+service-mode+card-bandwidth-mode) **slot** *slot-id* **card** *card-id* command to check the port bandwidth allocation mode.