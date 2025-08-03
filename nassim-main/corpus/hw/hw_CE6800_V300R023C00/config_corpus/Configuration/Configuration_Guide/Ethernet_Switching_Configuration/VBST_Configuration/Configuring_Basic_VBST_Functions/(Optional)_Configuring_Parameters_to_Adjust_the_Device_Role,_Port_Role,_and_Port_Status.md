(Optional) Configuring Parameters to Adjust the Device Role, Port Role, and Port Status
=======================================================================================

(Optional) Configuring Parameters to Adjust the Device Role, Port Role, and Port Status

#### Context

The message priority vector in BPDUs is related to the device priority, port priority, and path cost. Adjusting the settings for these parameters will affect spanning tree calculation, which involves the device role, port role, and port status in the spanning tree.

As the logic center of a spanning tree, the root bridges can either be calculated automatically or specified manually. You can manually specify the root bridge and secondary root bridges or configure the device priorities to affect root bridge election. It is recommended that you manually specify the root bridge and secondary root bridges.

* On a network running a spanning tree protocol, configure a device with high performance and at a high network layer as the root bridge to ensure the stability of the Layer 2 network. Failing to do so may cause temporary service interruptions if deployment of new devices on the network triggers switchover of the root bridge.
* Each spanning tree has only one root bridge that takes effect. When two or more devices are specified as root bridges for a spanning tree, the device with the smallest MAC address serves as the root bridge.
* Multiple secondary root bridges can be specified for a spanning tree. If the root bridge fails or is powered off, the secondary root bridge with the smallest MAC address will serve as the new root bridge, unless a new root bridge is specified manually.
* A device's roles in spanning trees are independent of one another. On an MSTP network, a device can function as the root bridge or a secondary root bridge in one or more spanning trees; however, it cannot function as both the root bridge and secondary root bridge in the same spanning tree.

Path cost is an important metric in spanning tree calculation, and it can affect root port selection. On a non-root bridge, the port with the lowest path cost to the root bridge is selected as the root port. On a VBST network, different path costs can be set for the same port in different VLANs to enable traffic of different VLANs to be forwarded through different physical links. This implements load balancing of VLAN traffic.

The path cost calculation method determines the path cost value range. It is recommended that you set a small path cost value for ports with high link rates, and a large path cost value for ports with low link rates. This enables ports with low link rates to be elected as blocked ports through spanning tree calculation.

Port priority determines whether a port will be elected as a designated port. To block a port for loop prevention, set the port priority to a larger value than the default value, enabling the port to be elected as a blocked port.

In addition to the device priority, port priority, and path cost, other parameters can affect the VBST topology convergence. For details, see [Configuring VBST Parameters That Affect VBST Convergence](galaxy_vbst_cfg_0013.html).

![](public_sys-resources/note_3.0-en-us.png) 

* If the device has been configured as the root bridge or secondary root bridge in a specified VLAN using a command and you want to change the priority of the device in the VLAN, run the [**undo stp vlan root**](cmdqueryname=stp+vlan+root) command to cancel the root bridge or secondary root bridge configuration, and then run the [**stp vlan priority**](cmdqueryname=stp+vlan+priority) command to set a new priority for the device.
* To prevent frequent network flapping, ensure that the Hello Time, Forward Delay, and Max Age timer values conform to the following formulas:
  + 2 x (Forward Delay â 1.0 second) â¥ Max Age
  + Max Age â¥ 2 x (Hello Time + 1.0 second)


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set the device priority in a specified VLAN to adjust the device's role in the spanning tree. Perform any of the following operations as required.
   
   
   * Configure the device as the root bridge in the specified VLAN.
     ```
     [stp vlan](cmdqueryname=stp+vlan+root) vlan-id1 [ to vlan-id2 ] [ vlan-id3 [ to vlan-id4 ] ] &<1-9> root primary
     ```
     
     By default, a device does not function as the root bridge in any spanning tree. After the command is configured, the priority of the device will be 0 in this VLAN and cannot be changed.
   * Configure the device as a secondary root bridge in the specified VLAN.
     ```
     [stp vlan](cmdqueryname=stp+vlan+root) vlan-id1 [ to vlan-id2 ] [ vlan-id3 [ to vlan-id4 ] ] &<1-9> root secondary
     ```
     
     By default, a device does not function as a secondary root bridge in any spanning tree. After the command is configured, the priority of the device will be 4096 in this VLAN and cannot be changed.
   * Set the device priority in the specified VLAN. A smaller value indicates a higher priority. A device with a higher priority is more likely to be elected as the root bridge.
     ```
     [stp vlan](cmdqueryname=stp+vlan+priority) vlan-id1 [ to vlan-id2 ] [ vlan-id3 [ to vlan-id4 ] ] &<1-9> priority priority-value
     ```
     
     The default priority of a device in a spanning tree is 32768.
     
     If the device has been configured as the root bridge or secondary root bridge in a specified VLAN using a command and you want to change the priority of the device in the VLAN, run the [**undo stp vlan root**](cmdqueryname=stp+vlan+root) command to cancel the root bridge or secondary root bridge configuration, and then run the [**stp vlan priority**](cmdqueryname=stp+vlan+priority) command to set a new priority for the device.
3. (Optional) Configure the path cost calculation method.
   
   
   ```
   [stp pathcost-standard](cmdqueryname=stp+pathcost-standard) { dot1d-1998 | dot1t | legacy }
   ```
   
   The default path cost calculation method is IEEE 802.1t (**dot1t**).
   
   All devices on a network must use the same path cost calculation method.
4. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
5. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
6. Set a path cost value for the current port in the specified VLAN.
   
   
   ```
   [stp vlan](cmdqueryname=stp+vlan+cost) vlan-id1 [ to vlan-id2 ] [ vlan-id3 [ to vlan-id4 ] ] &<1-9> cost cost
   ```
   
   
   * When the **legacy** calculation method is used, the *cost* value range is from 1 to 200000.
   * When the **dot1d-1998** calculation method is used, the *cost* value range is from 1 to 65535.
   * When the **dot1t** calculation method is used, the *cost* value range is from 1 to 200000000.
7. Set the port priority in the specified VLAN.
   
   
   ```
   [stp vlan](cmdqueryname=stp+vlan+port+priority) vlan-id1 [ to vlan-id2 ] [ vlan-id3 [ to vlan-id4 ] ] &<1-9> port priority priority-value
   ```
   
   The default priority of a device port is 128.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```