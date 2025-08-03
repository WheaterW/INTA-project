Increasing the Number of an Eth-Trunk Member Interface by 32768 When an Inter-Device Eth-Trunk Is Configured
============================================================================================================

Increasing the Number of an Eth-Trunk Member Interface by 32768 When an Inter-Device Eth-Trunk Is Configured

#### Context

Compared with M-LAG, inter-device Eth-Trunk â also known as M-LAG Lite â does not require the peer-link or physical link to establish an M-LAG dual-active system, simplifying deployment, reducing costs, and preventing service interruptions during an upgrade.

![](public_sys-resources/note_3.0-en-us.png) 

Unlike stacking and M-LAG, M-LAG Lite does not involve stacking.

In [Figure 1](#EN-US_TASK_0000001176741175__fig1802162218399), DeviceB and DeviceC are configured with the same Eth-Trunk ID, LACP system ID, LACP system priority, and different Eth-Trunk member interface numbers, ensuring successful Eth-Trunk negotiation between the two devices. Both devices also evenly load balance data. If one device fails, traffic can be forwarded through the other, implementing device-level reliability.

In this example, DeviceB and DeviceC must function as Layer 3 gateways but not Layer 2 transparent transmission devices. This is because if an upper-layer device functions as a gateway, the downstream devices' ARP/ND entries learned by the gateway will have two outbound interfaces, resulting in MAC address flapping. So, in this example, DeviceB and DeviceC which connect to DeviceA using an inter-device Eth-Trunk in LACP mode must be Layer 3 gateways on the network.

**Figure 1** Inter-device Eth-Trunk in LACP mode  
![](figure/en-us_image_0000001176741245.png)
When DeviceA is connected to DeviceB and DeviceC using an inter-device Eth-Trunk in LACP mode, the following parameters of the Eth-Trunk interfaces on DeviceB and DeviceC must be the same to ensure successful LACP negotiation:

* LACP system priority configured by the [**lacp priority**](cmdqueryname=lacp+priority) *priority* command.
* LACP system ID configured by the [**lacp system-id**](cmdqueryname=lacp+system-id) *mac-address* command.
* Eth-Trunk interface ID configured by the [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id* command.
* Interface rate. If Eth-Trunk member interfaces work at different rates, run the [**lacp mixed-rate link enable**](cmdqueryname=lacp+mixed-rate+link+enable) command to enable them to forward data packets after they are added to the Eth-Trunk interface.

In addition, to ensure that an inter-device Eth-Trunk in LACP mode can work properly, increase the numbers of Eth-Trunk member interfaces on either DeviceB or DeviceC by 32768 to ensure that the numbers of Eth-Trunk member interfaces on both devices are different.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of an Eth-Trunk interface.
   
   
   ```
   [interface](cmdqueryname=interface) eth-trunk trunk-id
   ```
3. Increase the number of an Eth-Trunk member interface by 32768.
   
   
   ```
   [lacp port-id-extension enable](cmdqueryname=lacp+port-id-extension+enable)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```