(Optional) Disabling MTU Check on DD Packets
============================================

After you prevent an interface from checking the Maximum Transmission Unit (MTU) field in received Database Description (DD) packets, the device can receive packets with the MTU field as 0.

#### Context

Perform the following steps on the Router that runs OSPFv3:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ospfv3 mtu-ignore**](cmdqueryname=ospfv3+mtu-ignore) [ **instance** *instance-id* ]
   
   
   
   The MTU check on DD packets is disabled.
   
   After the command is used, the interface does not check the MTU field of received DD packets.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.