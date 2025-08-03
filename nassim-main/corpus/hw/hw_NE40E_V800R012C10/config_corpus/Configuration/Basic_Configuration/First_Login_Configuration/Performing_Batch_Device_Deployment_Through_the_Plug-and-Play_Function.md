Performing Batch Device Deployment Through the Plug-and-Play Function
=====================================================================

To batch deploy devices powered on for the first time, you can use the plug-and-play function based on DCN or DHCP.

#### Context

To remotely manage and control devices in a unified manner on large-scale networks and thereby improve deployment efficiency and reduce O&M costs, you can use the plug-and-play function based on either DCN or DHCP to batch deploy devices powered on for the first time:

* DCN: After devices are powered on, their IP addresses (NEIPs) are automatically generated based on their NEIDs. The mapping between the NEIPs and NEIDs is contained in link-state advertisements (LSAs), which are flooded by OSPF to form a core routing table. The NMS accesses the devices based on the IP address of the GNE and the target NEIDs reported by the GNE, and remotely manages all the devices through the GNE.
* DHCP: Zero touch provisioning (ZTP) is the main plug-and-play function implemented in DHCP mode. It allows unconfigured devices to obtain version files from a file server during the power-on and startup process and then automatically load the files.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If a device is powered on without loading the default configuration file containing the username and password, it enters the first-login process in which you are prompted to create a username and set a password. In this case, the device fails to go online through the plug-and-play function. In the preceding process, the prompt information and interaction confirmation information are transmitted between the device and the NMS through the SSH\_MSG\_CHANNEL\_DATA field defined in SSH. The packet structure is defined as follows:

```
byte      SSH_MSG_CHANNEL_DATA
uint32    recipient channel
string    data
```


#### Procedure

1. Power on the device.
2. The device enters the corresponding plug-and-play process.
   
   
   * If [DCN Configuration](dc_vrp_dcn_cfg_0000.html) is implemented, the NMS can communicate with the device for remote management.
   * If [Configuring Automatic ZTP Deployment Through DHCP](../ne/dc_ne_ztp_cfg_0002.html) is implemented, the device can obtain version files from the file server and automatically load the files.