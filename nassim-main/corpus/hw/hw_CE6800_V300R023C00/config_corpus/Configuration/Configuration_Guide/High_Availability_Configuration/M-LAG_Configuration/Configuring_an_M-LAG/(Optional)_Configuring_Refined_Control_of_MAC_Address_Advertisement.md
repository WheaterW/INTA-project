(Optional) Configuring Refined Control of MAC Address Advertisement
===================================================================

(Optional) Configuring Refined Control of MAC Address Advertisement

#### Context

In an M-LAG, the local device synchronizes the actual MAC address of the local VLANIF interface to the peer device. The MAC address occupies resources in the software MAC address table of the peer device, which may affect the number of MAC addresses that can be dynamically learned by the peer device. You can run the [**mac-address m-lag notification vlanif disable**](cmdqueryname=mac-address+m-lag+notification+disable) command to disable the device from synchronizing the MAC address of the VLANIF interface to the peer device in the M-LAG.

In an M-LAG, the local device synchronizes the actual MAC address of the local VBDIF interface to the peer device. The MAC address occupies resources in the software MAC address table of the peer device, which may affect the number of MAC addresses that can be dynamically learned by the peer device. You can run the [**mac-address m-lag notification vbdif disable**](cmdqueryname=mac-address+m-lag+notification+disable) command to disable the device from synchronizing the MAC address of the VBDIF interface to the peer device in the M-LAG.

In an M-LAG, the local device synchronizes the actual MAC address of the local VBDIF interface to the peer device. After receiving the MAC address of the VBDIF interface synchronized from the local device, the peer device sends the MAC address to EVPN, occupying resources in the EVPN table. You can run the [**mac-address m-lag notification evpn disable**](cmdqueryname=mac-address+m-lag+notification+disable) command to disable the device from sending the MAC address of the VBDIF interface synchronized from the peer device in the M-LAG to EVPN.

![](../public_sys-resources/note_3.0-en-us.png) 

For the CE6885-LL (low latency mode): This function is not supported.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure refined control of MAC address advertisement.
   
   
   * Configure the device not to synchronize the MAC address of a VLANIF interface to the peer device.
     ```
     [mac-address m-lag notification vlanif disable](cmdqueryname=mac-address+m-lag+notification+disable)
     ```
   * Configure the device not to synchronize the MAC address of a VBDIF interface to the peer device.
     ```
     [mac-address m-lag notification vbdif disable](cmdqueryname=mac-address+m-lag+notification+disable)
     ```
     
     CE6820H, CE6820H-K, and CE6820S: This configuration is not supported.
   * Configure the device not to send the MAC address of a VBDIF interface synchronized from the peer device to EVPN.
     ```
     [mac-address m-lag notification evpn disable](cmdqueryname=mac-address+m-lag+notification+disable)
     ```
     
     CE6820H, CE6820H-K, and CE6820S: This configuration is not supported.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```