(Optional) Configuring an Interface to Fill in DD Packets with Its Own MTU
==========================================================================

You can configure an interface to fill in the Interface MTU field of a DD packet with the interface MTU.

#### Context

To improve compatibility with a non-Huawei device, an OSPF-enabled Huawei device adds the MTU 0 (default value) in DD packets to be sent and does not check the MTUs in received DD packets, thereby allowing an OSPF neighbor relationship to be set up even if the two ends have different MTU settings.

However, under the default configuration, the non-Huawei device may discard an OSPF packet received from the Huawei device if the actual MTU in the packet is greater than the MTU of the non-Huawei device. If an LSU is discarded, an OSPF neighbor relationship can still be set up, but the routing information carried in the LSU fails to be learned, causing service interruption.

To resolve this issue, run the [**ospf mtu-enable**](cmdqueryname=ospf+mtu-enable) command to configure an interface to add the actual MTU in DD packets to be sent and check whether the MTU in a received DD packet is greater than the local MTU. If the interface MTU settings of the local and remote ends are different, an OSPF neighbor relationship cannot enter the Full state. In this manner, MTU inconsistency can then be identified in time.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Setting the MTU in a DD packet will have the neighbor relationship reestablished.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ospf mtu-enable**](cmdqueryname=ospf+mtu-enable)
   
   
   
   The interface is configured to fill in a DD packet with the interface MTU and check whether the MTU in the DD packet from the neighboring Router exceeds the MTU of the local Router.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.