(Optional) Configuring an Eth-Trunk Sub-interface
=================================================

To transmit both Layer 2 and Layer 3 services over the same physical link, create a sub-interface on a Layer 2 Eth-Trunk interface.

#### Context

If Layer 2 switching devices belong to different VLANs, and hosts in the VLANs need to communicate, you need to create sub-interfaces on the Eth-Trunk interface connecting a Layer 3 device to a Layer 2 switching device, bind a downstream user VLAN to each sub-interface, configure 802.1Q encapsulation on these sub-interfaces, and assign an IP address to each sub-interface.

After the configuration is complete, hosts in different VLANs can use Eth-Trunk sub-interfaces to communicate with each other. Eth-Trunk sub-interfaces can also be used in dot1q and QinQ VLAN tag termination scenarios.

After sub-interfaces are configured for Layer 2 Eth-Trunk interfaces, the Eth-Trunk interfaces provide Layer 2 functions, and their sub-interfaces provide Layer 3 functions.

**Figure 1** Typical usage scenario of Layer 2 Eth-Trunk sub-interfaces  
![](images/fig_dc_vrp_ethtrunk_cfg_003001.png)

For applications of Eth-Trunk sub-interfaces in VLAN services, see VLAN Configuration.

For applications of Eth-Trunk sub-interfaces in QinQ services, see QinQ Configuration.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id.subnumber*
   
   
   
   A sub-interface is created on a Layer 2 Eth-Trunk interface.
   
   
   
   A maximum of 4096 sub-interfaces can be created on an Eth-Trunk interface.
3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ]
   
   
   
   An IP address is assigned to the Eth-Trunk sub-interface.
   
   
   
   When more than one IP address is configured for an Eth-Trunk interface, the keyword **sub** must be used to indicate the second and subsequent IP addresses.
4. Run [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlan-id*
   
   
   
   The encapsulation type and associated VLAN ID are configured for the Eth-Trunk sub-interface.
   
   
   
   The VLAN IDs associated with the two communicating Eth-Trunk sub-interfaces must be the same.
   
   The VLAN IDs associated with a sub-interface of a Layer 2 Eth-Trunk interface cannot conflict with the VLAN IDs associated with the Layer 2 Eth-Trunk interface.
5. Run [**mtu**](cmdqueryname=mtu) *mtu*
   
   
   
   An MTU is configured for the Eth-Trunk sub-interface.
   
   
   
   The MTU of an Eth-Trunk interface ranges from 46 to 9600, in bytes.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If an interface with a small MTU receives large packets, too many packet fragments may be generated. Consequently, some packets may be discarded due to the insufficient length of a QoS queue. To avoid this situation, you can lengthen the QoS queue accordingly.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.