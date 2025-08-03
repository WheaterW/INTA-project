Devices Cannot Communicate Using VLANIF Interfaces
==================================================

Devices Cannot Communicate Using VLANIF Interfaces

#### Fault Symptom

In [Figure 1](#EN-US_TASK_0000001130782626__fig7173175418488), VLANIF 2 on DeviceA and VLANIF 2 on DeviceB are configured with an IP address. Although the two IP addresses are on the same network segment, DeviceA and DeviceB cannot ping each other.

**Figure 1** Devices cannot communicate with each other using VLANIF interfaces  
![](figure/en-us_image_0000001130622884.png)
#### Possible Causes

* A VLANIF interface goes down.
* The interfaces (interface 1 and interface 2 in this example) connecting DeviceA and DeviceB are not added to the target VLAN.
* The PVIDs of the interfaces connecting DeviceA and DeviceB are different.


#### Procedure

* Check whether the VLANIF interfaces are up.
  1. Check whether the VLANIF interfaces on DeviceA and DeviceB are up.
     
     
     ```
     [display interface](cmdqueryname=display+interface) vlanif [ vlan-id ]
     ```
     
     
     
     If either the **current state** or **Line protocol current state** field in the command output is **DOWN**, the VLANIF interface is down.
  2. If the VLANIF interfaces are down, rectify the fault according to [A VLANIF Interface Goes Down](vrp_vlan_cfg_0088.html).
* Check whether interface 1 and interface 2 are added to VLANs.
  1. On DeviceA and DeviceB, check whether there is an interface connecting the local device to the peer device.
     
     
     ```
     [display vlan](cmdqueryname=display+vlan) vlan-id [ verbose | to vlan-id2 ]
     ```
  2. Perform operations according to the command output.
     
     
     + If the **Ports** field is not displayed in the command output, add the local interface to the target VLAN. For details, see [Configuring Interface-based VLAN Assignment](vrp_vlan_cfg_0018.html#EN-US_TASK_0000001130622850__cmd159334395817).
     + If the **Ports** field is displayed in the command output but the interfaces on DeviceA and DeviceB are added to the target VLAN in different modes, that is, one interface is added in untagged mode (with UT displayed before the interface name) and the other interface is added in tagged mode (with TG displayed before the interface name), add the interfaces to the target VLAN in tagged mode. For details, see [Add interfaces to VLANs](vrp_vlan_cfg_0018.html#EN-US_TASK_0000001130622850__cmd159334395817).
     + If the **Ports** field is displayed but the local interface is down (with D displayed next to the interface name), rectify this fault.
* Check whether the PVIDs of interface 1 and interface 2 are the same.
  1. Check the PVID of interface 1 and interface 2 on DeviceA and DeviceB, respectively.
     
     
     ```
     [display port vlan](cmdqueryname=display+port+vlan) [ interface-type interface-number ] [ active ]
     ```
  2. Change the PVIDs of interface 1 and interface 2 to the same value. For details, see [Changing and Restoring the Default VLAN](vrp_vlan_cfg_0014.html).