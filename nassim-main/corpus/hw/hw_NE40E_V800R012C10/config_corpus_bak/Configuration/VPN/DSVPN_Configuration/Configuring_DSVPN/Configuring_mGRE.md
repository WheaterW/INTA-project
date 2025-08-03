Configuring mGRE
================

Setting the tunnel interface type to mGRE allows multiple GRE tunnels to be established on the same tunnel interface, simplifying configuration.

#### Context

To implement DSVPN, create a tunnel interface and set the tunnel type to mGRE. You only need to configure the source address or source interface for the mGRE tunnel interface, but do not need to specify a destination address. Then multiple GRE tunnels can be established on the mGRE tunnel interface and correspond to multiple GRE peers, simplifying GRE configuration.

Perform the following configurations on the spokes and hub.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
   
   
   
   A tunnel interface is created, and its view is displayed.
3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
   
   
   
   An IP address is assigned to the tunnel interface.
4. Run [**tunnel-protocol**](cmdqueryname=tunnel-protocol) **gre** **p2mp**
   
   
   
   The tunnel encapsulation mode is set to mGRE.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The mGRE tunnels can be configured only on one-dimensional tunnel interfaces.
   
   
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   Modifying the tunnel encapsulation mode will delete the parameter settings of the tunnel interface, including the source address or source interface of the tunnel interface and NHRP.
5. Run [**source**](cmdqueryname=source) { *ip-address* | *ifName* | *ifType* *ifNum* }
   
   
   
   The source IP address or interface is specified for the tunnel.
6. (Optional) Run [**gre key**](cmdqueryname=gre+key) { **simple** *key-number-simple* | [ **cipher** ] *key-number-cipher* }
   
   
   
   A key that identifies a tunnel is set.
   
   If multiple mGRE tunnel interfaces use the same source address or source interface, you must configure a unique key for each mGRE tunnel.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   If **simple** is specified, the key is saved in the configuration file in cleartext, posing security risks. You are advised to select **cipher** to save the key in ciphertext in the configuration file.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.