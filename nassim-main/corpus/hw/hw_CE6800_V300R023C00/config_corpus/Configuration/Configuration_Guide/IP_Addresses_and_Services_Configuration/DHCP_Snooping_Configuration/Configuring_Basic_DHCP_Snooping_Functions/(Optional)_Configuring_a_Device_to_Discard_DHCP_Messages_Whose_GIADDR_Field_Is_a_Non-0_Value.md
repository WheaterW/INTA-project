(Optional) Configuring a Device to Discard DHCP Messages Whose GIADDR Field Is a Non-0 Value
============================================================================================

(Optional) Configuring a Device to Discard DHCP Messages Whose GIADDR Field Is a Non-0 Value

#### Context

The GIADDR (gateway IP address) field in a DHCP message records the IP address of the first DHCP relay agent through which the message passes. If the DHCP server and client are on different network segments, the first DHCP relay agent fills its own IP address in the GIADDR field before forwarding the message to the DHCP server. After receiving the message, the DHCP server determines the network segment where the client resides based on this field, selects a proper address pool, and allocates an IP address in this network segment to the client.

As shown in [Figure 1](#EN-US_TASK_0000001512681130__fig296114171592), to ensure that a device can obtain parameters such as the user MAC address when generating DHCP snooping binding entries, DHCP snooping needs to be applied to the access device on the Layer 2 network or the first DHCP relay agent (for example, DHCP relay agent A in the figure). Therefore, the value of the GIADDR field in a DHCP message received by the DHCP snooping-enabled device must be 0. Otherwise, the device considers the message invalid and discards it. This function is recommended if DHCP snooping is enabled on the DHCP relay agent.

Usually, the GIADDR field value in a DHCP message sent by a client is 0. If the value is not 0, the DHCP server may allocate an incorrect IP address. To prevent the client from forging a DHCP message whose GIADDR field is a non-0 value to apply for an IP address, you are advised to configure this function.

**Figure 1** DHCP message processing when multiple DHCP relay agents exist (DHCPREQUEST messages are used as an example)  
![](../images/en-us_image_0000001564120421.png)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the device to check whether the GIADDR field value in a DHCPREQUEST message is not 0.
   
   
   * In the system view, enable the device to check whether the GIADDR field value in a DHCPREQUEST message is not 0.
     ```
     [dhcp snooping check dhcp-giaddr enable](cmdqueryname=dhcp+snooping+check+dhcp-giaddr+enable) vlan { vlan-id1 [ [to](cmdqueryname=to) vlan-id2 ] } &<1-10>
     ```
   * In the interface view, enable the device to check whether the GIADDR field value in a DHCPREQUEST message is not 0.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     portswitch
     [dhcp snooping check dhcp-giaddr enable](cmdqueryname=dhcp+snooping+check+dhcp-giaddr+enable)
     [quit](cmdqueryname=quit)
     ```
   * In the VLAN view, enable the device to check whether the GIADDR field value in a DHCPREQUEST message is not 0.
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [dhcp snooping check dhcp-giaddr enable](cmdqueryname=dhcp+snooping+check+dhcp-giaddr+enable)
     [quit](cmdqueryname=quit)
     ```
   
   By default, a device does not check whether the GIADDR field value in a DHCPREQUEST message is not 0.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```