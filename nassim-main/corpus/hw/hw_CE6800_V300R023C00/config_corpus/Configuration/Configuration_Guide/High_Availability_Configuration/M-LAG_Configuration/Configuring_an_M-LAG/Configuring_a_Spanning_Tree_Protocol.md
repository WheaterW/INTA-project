Configuring a Spanning Tree Protocol
====================================

Configuring a Spanning Tree Protocol

#### Context

To prevent loops on an M-LAG network, two M-LAG member devices are considered as one device for STP calculation and can work in root bridge mode, Virtual Spanning Tree Protocol (V-STP) mode, or Virtual VLAN-based Spanning Tree (V-VBST) mode. [Table 1](#EN-US_TASK_0000001563769161__table115834618389) describes the differences between the three modes.

**Table 1** Comparison between the root bridge, V-STP, and V-VBST modes
| Mode | Application Scenario | Configuration Method | Application Limitations |
| --- | --- | --- | --- |
| Root bridge mode | Applicable to scenarios where M-LAG master and backup devices function as root bridges on a Layer 2 network. | Configure the M-LAG master and backup devices as root bridges with the same bridge ID on the network running a spanning tree protocol so that the two devices are simulated into one root bridge. Set the root priority to the highest to ensure that the M-LAG is the root node. | * In this mode, only STP, RSTP, and MSTP are supported, and STP multi-process is not supported. * Multi-level M-LAG in root bridge mode is not supported. * Because the M-LAG master and backup devices need to be simulated into one root bridge, you need to disable STP on peer-link interfaces to ensure that the directly connected interfaces are not blocked. |
| V-STP mode | * Applicable to scenarios where an M-LAG connects to a network running a spanning tree protocol. * This mode applies to multi-level M-LAG deployment. | After the V-STP function is enabled, the spanning tree protocol status is synchronized between the M-LAG master and backup devices so that they are simulated into one device to perform STP calculation. | * In this mode, only STP and RSTP are supported, and STP multi-process is supported. * The M-LAG member interface configurations on the M-LAG master and backup devices must be the same. * Because the M-LAG master and backup devices need to exchange packets through the peer-link to perform STP virtualization calculation, you need to enable STP on peer-link interfaces. The STP configurations on the peer-link interfaces of the two devices must be the same. |
| V-VBST mode | * Applicable to scenarios where an M-LAG connects to a network running VBST. * This mode applies to multi-level M-LAG deployment. | After the V-VBST function is enabled, the VBST status is synchronized between the M-LAG master and backup devices so that they are simulated into one device to perform VBST calculation. | * Only VBST is supported in this mode. * The M-LAG member interface configurations on the M-LAG master and backup devices must be the same. * Because the M-LAG master and backup devices need to exchange packets through the peer-link to perform STP virtualization calculation, you need to enable VBST on peer-link interfaces. |

As shown in [Figure 1](#EN-US_TASK_0000001563769161__fig84229095120), DeviceA and DeviceB set up an M-LAG, so do DeviceC and DeviceD. The two M-LAGs are connected, simplifying the networking and allowing more servers to be dual-homed to the network. Multi-level M-LAG must be configured based on V-STP or V-VBST.

**Figure 1** Multi-level M-LAG networking  
![](figure/en-us_image_0000001513168942.png)

#### Procedure

* Configure the root bridge mode.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure the device as the root bridge.
     
     
     ```
     [stp](cmdqueryname=stp+root) [ instance instance-id ] root primary
     ```
     By default, a device does not function as the root bridge of any spanning tree. After the configuration is complete, the device's priority in a spanning tree is 0, which cannot be changed.![](../public_sys-resources/note_3.0-en-us.png) 
     
     If **instance** is not specified, the device is the root bridge in MSTI 0.
  3. Configure the bridge MAC address used by the device for spanning tree calculation.
     
     
     ```
     [stp bridge-address](cmdqueryname=stp+bridge-address) mac-address
     ```
     
     By default, a device uses its MAC address as the bridge MAC address for spanning tree calculation. You are advised to use the smaller MAC address of the M-LAG master and backup device as the bridge MAC address for spanning tree calculation.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the V-STP mode.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure the device to work in STP or RSTP mode.
     
     
     ```
     [stp mode](cmdqueryname=stp+mode) { [stp](cmdqueryname=stp) | [rstp](cmdqueryname=rstp) }
     ```
     
     By default, a device works in MSTP mode.
  3. (Optional) Configure the bridge MAC address used by the device for spanning tree calculation.
     
     
     ```
     [stp bridge-address](cmdqueryname=stp+bridge-address) mac-address
     ```
     
     By default, a device uses its MAC address as the bridge MAC address for spanning tree calculation.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     To prevent network flapping caused by device restart or DFS master/backup switchover and ensure switchback performance, you are advised to set a larger bridge MAC address for the M-LAG backup device when the M-LAG master and backup devices have the same priority.
  4. Enable the V-STP mode.
     
     
     ```
     [stp v-stp enable](cmdqueryname=stp+v-stp+enable)
     ```
     
     By default, the V-STP mode is disabled.
  5. (Optional) Configure the M-LAG member interface to send BPDUs with an extended port ID.
     
     
     ```
     [stp v-stp port-id-extension enable](cmdqueryname=stp+v-stp+port-id-extension+enable) 
     ```
     
     By default, the port ID carried in BPDUs sent by the M-LAG member interface in V-STP mode is 1.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     After the interface on the downstream device is configured to transparently transmit packets, BPDUs sent by M-LAG member interfaces are looped back to the two V-STP-enabled upstream devices. In this case, the system MAC address and port ID in BPDUs received by the M-LAG member interfaces on the upstream devices are the same as those of the interfaces. As a result, the M-LAG member interfaces are incorrectly blocked. You can run this command to change the port ID so that the port ID carried in BPDUs sent by the M-LAG member interface is different from the port ID of the interface, avoiding this problem.
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
  
  ![](../public_sys-resources/note_3.0-en-us.png) 
  + In a V-STP scenario, you are advised to configure M-LAG and connect cables in the following sequence:
    1. Configure V-STP.
    2. Configure a DFS group, DAD, and peer-link interfaces.
    3. Connect peer-link interfaces of M-LAG master and backup devices.
    4. Configure M-LAG member interfaces and use cables to connect M-LAG master and backup devices to user-side devices.
  + In a V-STP scenario, if uplink interfaces of the devices are VLANIF interfaces, disable STP on physical uplink interfaces or configure the physical uplink interfaces to work in Layer 3 mode. Otherwise, some interfaces may be incorrectly blocked, causing traffic interruption. In a virtual peer-link scenario, DFS group pairing fails.
* Configure the V-VBST mode.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure the device to work in VBST mode.
     
     
     ```
     [stp mode vbst](cmdqueryname=stp+mode+vbst)
     ```
     
     By default, a device works in MSTP mode.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     The VBST mode is mutually exclusive with the STP, RSTP, and MSTP modes.
     
     If 1:*N* (*N* > 1) mapping between instances and VLANs has been configured on the device, you must delete the mapping before changing the spanning tree protocol mode to VBST mode.
  3. Enable VBST.
     
     
     ```
     [stp enable](cmdqueryname=stp+enable)
     ```
  4. Enable VBST in a VLAN.
     
     
     ```
     [undo stp vlan](cmdqueryname=stp+vlan+disable) vlan-id1 [ to vlan-id2 ] [ vlan-id3 [ to vlan-id4 ] ] &<1-9> disable
     ```
     
     By default, a spanning tree protocol is enabled in all VLANs on the device.
  5. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  6. Enable VBST on the interface.
     
     
     ```
     [stp enable](cmdqueryname=stp+enable)
     ```
     
     By default, a spanning tree protocol is enabled on an interface of the device.
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
  
  ![](../public_sys-resources/note_3.0-en-us.png) 
  + After the [**stp mode vbst**](cmdqueryname=stp+mode+vbst) command and the peer-link interface are configured, the device automatically enables the V-VBST function.
  + In a V-VBST scenario, you are advised to configure M-LAG and connect cables in the following sequence:
    1. Configure V-VBST.
    2. Configure a DFS group, DAD, and peer-link interfaces.
    3. Connect peer-link interfaces of M-LAG master and backup devices.
    4. Configure M-LAG member interfaces and use cables to connect M-LAG master and backup devices to user-side devices.
  + In a V-VBST scenario, if uplink interfaces of the devices are VLANIF interfaces, disable STP on physical uplink interfaces or configure the physical uplink interfaces to work in Layer 3 mode. Otherwise, some interfaces may be incorrectly blocked, causing traffic interruption. In a virtual peer-link scenario, DFS group pairing fails.