Enabling Layer 2 Protocol Tunneling on an Interface
===================================================

If you want backbone network devices to transparently transmit Layer 2 PDUs from user networks, enable Layer 2 protocol tunneling on the device interfaces.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The user-side interface view is displayed.
3. Run [**l2protocol-tunnel**](cmdqueryname=l2protocol-tunnel) { **all** | *protocol* } **enable**
   
   
   
   Layer 2 protocol tunneling is enabled on the interface.
   
   
   
   In some special networking scenarios, if you want to prevent PDUs of some Layer 2 protocols run between user networks from traversing a backbone network, run the [**l2protocol-tunnel**](cmdqueryname=l2protocol-tunnel) { **all** | *protocol* } **drop** command to enable the interface to discard them. Then, upon receipt of such packets, the interface directly discards them.
   
   
   
   To protect an interface enabled with Layer 2 protocol tunneling against PDU attacks, run the [**l2protocol-tunnel drop-threshold**](cmdqueryname=l2protocol-tunnel+drop-threshold) command to configure a drop threshold for Layer 2 PDUs on the interface. The interface then drops excess Layer 2 PDUs when the number of Layer 2 PDUs received in 1s exceeds the configured drop threshold.
   
   
   
   If each interface of a backbone network device has multiple user networks accessed and the Layer 2 PDUs sent by the user networks carry VLAN tags, to allow these Layer 2 PDUs to be transparently transmitted over the backbone network, run the [**l2protocol-tunnel**](cmdqueryname=l2protocol-tunnel) { **all** | *protocol* } { [ **reverse** ] **vlan** *low-id* [ **to** *high-id* ] } &<1-10> command to enable Layer 2 protocol tunneling on the tagged interfaces.
   
   
   
   On some special networks, for example, a network with both Huawei and non-Huawei devices, to ensure that the Huawei device can communicate with the non-Huawei device, run the [**l2protocol-tunnel**](cmdqueryname=l2protocol-tunnel) { **all** | *protocol* } **reverse** [ **drop** ] command to enable reverse Layer 2 protocol tunneling on the Huawei device's interface that connects to the non-Huawei device, so that the interface replaces a specified multicast MAC address with the multicast destination MAC address in Layer 2 PDUs.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The [**l2protocol-tunnel vlan**](cmdqueryname=l2protocol-tunnel+vlan) and [**l2protocol-tunnel**](cmdqueryname=l2protocol-tunnel) { **all** | *protocol* } **enable** commands with the same Layer 2 protocol specified cannot be run on the same interface. If you run both commands on the same interface, the system prompts a configuration conflict.
   * The [**l2protocol-tunnel**](cmdqueryname=l2protocol-tunnel) { **all** | *protocol* } **reverse** and [**l2protocol-tunnel**](cmdqueryname=l2protocol-tunnel) { **all** | *protocol* } **reverse** **vlan** *low-id* [ **to** *high-id* ] commands with the same Layer 2 protocol specified cannot be run on the same interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.