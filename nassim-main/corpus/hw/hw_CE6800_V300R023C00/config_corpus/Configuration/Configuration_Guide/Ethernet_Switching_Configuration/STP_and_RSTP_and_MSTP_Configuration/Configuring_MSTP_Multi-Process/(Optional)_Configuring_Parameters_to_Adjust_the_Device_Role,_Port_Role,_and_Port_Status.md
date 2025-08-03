(Optional) Configuring Parameters to Adjust the Device Role, Port Role, and Port Status
=======================================================================================

(Optional) Configuring Parameters to Adjust the Device Role, Port Role, and Port Status

#### Context

The message priority vector in BPDUs is related to the device priority, port priority, and path cost. Adjusting the settings for these parameters will affect spanning tree calculation, which involves the device role, port role, and port status in the spanning tree.

As the logic center of a spanning tree, the root bridges can either be calculated automatically or specified manually. You can manually specify the root bridge and secondary root bridges or configure the device priorities to affect root bridge election. It is recommended that you manually specify the root bridge and secondary root bridges.

* On an STP, RSTP, or MSTP network, to ensure the Layer 2 network is stable, specify a device with high performance and a high network layer as the root bridge. Otherwise, new devices may trigger root bridge re-election, thereby causing temporary service interruptions.
* Each spanning tree has only one active root bridge. When two or more devices are specified as root bridges for a spanning tree, the device with the smallest MAC address serves as the root bridge.
* Multiple secondary root bridges can be specified for a spanning tree. If the root bridge fails or is powered off, the secondary root bridge with the smallest MAC address will serve as the new root bridge, unless a new root bridge is specified manually.
* A device's roles in spanning trees are independent of one another. On an MSTP network, a device can function as the root bridge or a secondary root bridge in one or more spanning trees; however, it cannot function as both the root bridge and secondary root bridge in the same spanning tree.

Path cost is an important metric in spanning tree calculation, and it can affect root port selection. On a non-root bridge, the port with the lowest path cost to the root bridge is selected as the root port. On an MSTP network, different path costs can be set for the same port in different MSTIs to enable traffic of different VLANs to be forwarded through different physical links. This implements load balancing of VLAN traffic.

The path cost calculation method determines the path cost value range. It is recommended that you set a small path cost value for ports with high link rates, and a large path cost value for ports with low link rates. This enables ports with low link rates to be elected as blocked ports through spanning tree calculation.

[Table 1](vrp_stp_cfg_1081.html#EN-US_TASK_0000001345238489__table75735403518) lists the path costs defined in the IEEE 802.1D-1998 standard, IEEE 802.1t standard, and Huawei calculation method. Different vendors use different standards.

Port priority determines whether a port will be elected as a designated port. To block a port for loop prevention, set the port priority to a larger value than the default value, enabling the port to be elected as a blocked port.

In addition to the device priority, port priority, and path cost, other parameters can affect the STP, RSTP, or MSTP topology convergence. For details, see [Configuring Parameters That Affect STP/RSTP/MSTP Topology Convergence](vrp_stp_cfg_1097.html).


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the MSTP process view.
   
   
   ```
   [stp process](cmdqueryname=stp+process) process-id
   ```
3. Set the device priority to adjust the device's role in an MSTI. Perform any of the following operations as needed.
   
   
   
   If you do not specify the instance, the following settings will take effect for instance 0.
   
   * Configure the device as the root bridge.
     ```
     [stp](cmdqueryname=stp) [ instance instance-id ] root primary
     ```
     
     By default, a device does not function as the root bridge for any spanning tree. After the command is configured, the priority of the device will be 0 and cannot be changed.
   * Configure the device as a secondary root bridge.
     ```
     [stp](cmdqueryname=stp) [ instance instance-id ] root secondary
     ```
     
     By default, a device does not function as a secondary root bridge for any spanning tree. After the command is configured, the priority of the device will be 4096 and cannot be changed.
   * Set the device priority. A smaller value indicates a higher priority. A device with a higher priority is more likely to be elected as the root bridge.
     ```
     [stp](cmdqueryname=stp) [ instance instance-id ] priority priority
     ```
     
     The default priority of a device in a spanning tree is 32768.
     
     To change the priority of a device that has been configured as the root bridge or a secondary root bridge, run the [**undo stp**](cmdqueryname=undo+stp) [ **instance** *instance-id* ] **root** command to disable the root bridge function or secondary root bridge function and then run the [**stp**](cmdqueryname=stp) [ **instance** *instance-id* ] **priority** *priority* command to set a new priority for the device.
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. (Optional) Configure the path cost calculation method.
   
   
   ```
   [stp pathcost-standard](cmdqueryname=stp+pathcost-standard) { dot1d-1998 | dot1t | legacy }
   ```
   
   The default path cost calculation method is IEEE 802.1t (**dot1t**).
   
   All devices on a network must use the same path cost calculation method.
   
   [Table 1](#EN-US_TASK_0000001292398360__en-us_task_0000001130623330_table917332515232) lists the path costs defined in the IEEE 802.1D-1998 standard, IEEE 802.1t standard, and Huawei calculation method. Different vendors use different standards.
   
   **Table 1** Path cost list
   | Port Rate | Port Mode | Recommended STP Path Cost | | |
   | --- | --- | --- | --- | --- |
   | IEEE 802.1D-1998 Standard | IEEE 802.1t Standard | Huawei Calculation Method |
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
   | 2500Mbps | Full-Duplex | 3 | 8000 | 17 |
   | Aggregated Link 2 Ports | 3 | 4000 | 12 |
   | Aggregated Link 3 Ports | 3 | 2666 | 7 |
   | Aggregated Link 4 Ports | 2 | 2000 | 2 |
   | 10Gbps | Full-Duplex | 2 | 2000 | 2 |
   | Aggregated Link 2 Ports | 1 | 1000 | 1 |
   | Aggregated Link 3 Ports | 1 | 666 | 1 |
   | Aggregated Link 4 Ports | 1 | 500 | 1 |
   | 40Gbps | Full-Duplex | 1 | 500 | 1 |
   | Aggregated Link 2 Ports | 1 | 250 | 1 |
   | Aggregated Link 3 Ports | 1 | 166 | 1 |
   | Aggregated Link 4 Ports | 1 | 125 | 1 |
6. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
7. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
8. Bind the port to an MSTP process.
   
   
   ```
   [stp binding process](cmdqueryname=stp+binding+process) process-id
   ```
9. Set a path cost value for the current port.
   
   
   ```
   [stp](cmdqueryname=stp) [ process process-id ] [ instance instance-id ] cost cost
   ```
   
   
   * When the **legacy** calculation method is used, the *cost* value is in the range from 1 to 200000.
   * When the **dot1d-1998** calculation method is used, the *cost* value is in the range from 1 to 65535.
   * When the **dot1****t** calculation method is used, the *cost* value is in the range from 1 to 200000000.
10. Set the port priority.
    
    
    ```
    [stp](cmdqueryname=stp) [ process process-id ] [ instance instance-id ] port priority priority
    ```
    
    The default priority of a device port is 128.
11. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```