(Optional) Configuring MDN
==========================

(Optional) Configuring MDN

#### Context

MDN obtains the MAC addresses of non-Huawei devices. When the NMS needs to collect topology information about a Huawei device and a non-Huawei device, you can enable MDN on the non-Huawei device. Then the Huawei device can receive non-standard discovery protocol packets sent by the non-Huawei device and obtain the MAC address of the non-Huawei device. In this manner, the NMS can obtain the topology information between the two devices.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable MDN.
   
   
   
   You can enable MDN globally or on an interface.
   
   * Enable MDN globally.
     ```
     [lldp mdn enable](cmdqueryname=lldp+mdn+enable)
     ```
   * Enable MDN on an interface.
     1. Enter the interface view.
        ```
        [interface](cmdqueryname=interface) interface-type interface-number
        ```
     2. Enable MDN on the interface.
        ```
        [lldp mdn enable](cmdqueryname=lldp+mdn+enable)
        ```
   
   MDN adopts the following longest-match rules:
   
   * If MDN is configured globally and on a specified interface, only the configuration on the interface takes effect.
   * If MDN is not configured on any interface, the global MDN configuration takes effect.
   * If MDN is not configured globally, the MDN configuration on interfaces takes effect.
3. (Optional) Configure a delay in sending MDN neighbor information change traps to the NMS.
   
   
   
   After the LLDP trap function is enabled for a device, the device sends traps to the NMS if MDN neighbor information changes. If MDN neighbor information changes frequently, the device frequently sends traps to the NMS, causing network flapping. Setting a delay effectively prevents network flapping caused by traps being frequently sent to the NMS. To set a delay for the device to send traps about MDN neighbor information changes to the NMS, run the following command:
   
   
   
   ```
   [lldp mdn trap-interval](cmdqueryname=lldp+mdn+trap-interval) trap-interval
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The delay for sending traps about MDN neighbor information changes must be appropriate. You can flexibly adjust this parameter based on the network load:
   
   * The longer the delay, the lower the frequency of network topology changes. However, if the delay for sending traps about MDN neighbor information changes is too long, the NMS cannot trace changes of the neighbor status. As a result, the NMS cannot refresh network topology in a timely manner.
   * The shorter the delay, the higher the frequency of sending local status information to neighbors. This helps the neighbors dynamically refresh the network topology. However, if the delay is too short, the NMS refreshes status information about neighbors frequently. This causes flapping of network topology, increases the load on the system, and wastes resources.
   * The default delay time is recommended.
4. (Optional) Disable MDN on a specified interface.
   
   
   
   After the MDN function is enabled globally, all interfaces can receive packets discovered using non-standard protocols and identify MDN neighbors based on source MAC addresses of packets. This increases system resource consumption and affects service running. You can run the [**lldp mdn disable**](cmdqueryname=lldp+mdn+disable) command on a specified interface to disable MDN on the interface.
   
   1. Enter the interface view.
      ```
      [interface](cmdqueryname=interface) interface-type interface-number
      ```
   2. Disable MDN on the interface.
      ```
      [lldp mdn disable](cmdqueryname=lldp+mdn+disable)
      ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```