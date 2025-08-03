Configuring Network Slice Instances
===================================

Configuring network slice instances is the first step for implementing network slicing. Interfaces can be added to network slices only after network slice instances are configured.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**network-slice protocol-number**](cmdqueryname=network-slice+protocol-number) *number*
   
   
   
   The protocol number of a network slice in the IPv6 header is configured.
   
   This command is used only in HBH encapsulation scenarios.
   
   
   
   [**protocol-number**](cmdqueryname=protocol-number) *number* affects the value of the Next Header field in the IPv6 header. This field indicates that the next header is the HBH header.
   
   * In cases where all devices support network slicing, you can skip this step and use the default protocol number of 0, as these devices can identify the HBH header and import packets to a specified slice interface.
   * If the intermediate device does not support network slicing, you need to configure the protocol number on other devices. In this case, the intermediate device transparently transmits IPv6 packets without transmitting them over a network slice. This command must be configured in this scenario. Otherwise, the intermediate device fails to forward packets.
3. Run [**network-slice instance**](cmdqueryname=network-slice+instance) *netSliceInstId*
   
   
   
   A network slice instance is created, and its view is displayed.
   
   
   
   You can repeat this step to create multiple network slice instances.
4. (Optional) Run [**description**](cmdqueryname=description) *instDescrip*
   
   
   
   A description is configured for the network slice instance.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.