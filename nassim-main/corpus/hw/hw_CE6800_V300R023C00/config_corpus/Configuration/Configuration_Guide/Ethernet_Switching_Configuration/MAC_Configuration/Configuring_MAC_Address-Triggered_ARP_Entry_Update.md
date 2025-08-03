Configuring MAC Address-Triggered ARP Entry Update
==================================================

Configuring MAC Address-Triggered ARP Entry Update

#### Context

On an Ethernet network, a host sends and receives Ethernet data frames based on MAC addresses. The Address Resolution Protocol (ARP) maps IP addresses to MAC addresses. When two devices on different network segments communicate with each other, they need to map IP addresses to MAC addresses and outbound interfaces according to ARP entries.

Generally, the outbound interfaces in the matching MAC address entries and ARP entries are consistent. As shown in [Figure 1](#EN-US_TASK_0000001176664483__macarpfunc), at T1, the outbound interface in both the MAC address entry and ARP entry is interface 1. The interface is then changed. At T2, after receiving a packet from a peer device, the outbound interface in the MAC address entry changes to interface 2, yet the outbound interface in the ARP entry is still interface 1. At T3, the aging time of the ARP entry expires, and the outbound interface in the ARP entry changes to interface 2 after ARP aging probe. Between T2 and T3, the outbound interface in the ARP entry is incorrect, causing communication interruption between devices on different network segments.

**Figure 1** MAC address-triggered ARP entry update is not enabled  
![](figure/en-us_image_0000001176744417.png "Click to enlarge")

MAC addressâtriggered ARP entry update enables a device to update the outbound interface in an ARP entry immediately after the outbound interface in the corresponding MAC address entry changes. As shown in [Figure 2](#EN-US_TASK_0000001176664483__macarpfunc1), MAC addressâtriggered ARP entry update is enabled. At T2, after the outbound interface in the MAC address entry changes to interface 2, the outbound interface in the ARP entry is immediately changed to interface 2. This function prevents interference between T2 and T3 caused by the incorrect outbound interface in the ARP entry.

**Figure 2** MAC address-triggered ARP entry update is enabled  
![](figure/en-us_image_0000001130784752.png "Click to enlarge")
![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL (low latency mode) does not support this function.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the MAC address-triggered ARP entry update function.
   
   
   ```
   [mac-address update arp enable](cmdqueryname=mac-address+update+arp+enable)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   This command affects only dynamic ARP entries. Static ARP entries are not updated even when the corresponding MAC address entries change.
   
   The [**mac-address update arp enable**](cmdqueryname=mac-address+update+arp+enable) command is mutually exclusive with the [**arp anti-attack entry-check**](cmdqueryname=arp+anti-attack+entry-check) { **fixed-mac** | **fixed-all** | **send-ack** } [**enable**](cmdqueryname=enable) command.
   
   After the MAC address-triggered ARP entry update function is enabled, the device updates an ARP entry only if the outbound interface in the corresponding MAC address entry changes.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check whether the MAC address-triggered ARP entry update function is successfully configured. If there is the configuration of the **undo mac-address update arp enable** command, the MAC address-triggered ARP entry update function is not configured on the device. If there is no configuration of the **undo mac-address update arp enable** command, the MAC address-triggered ARP entry update function is successfully configured on the device.