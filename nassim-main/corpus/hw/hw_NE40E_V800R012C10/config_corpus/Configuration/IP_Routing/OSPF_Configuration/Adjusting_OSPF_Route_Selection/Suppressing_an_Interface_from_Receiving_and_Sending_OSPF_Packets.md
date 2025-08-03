Suppressing an Interface from Receiving and Sending OSPF Packets
================================================================

After an interface is suppressed from receiving and sending OSPF packets, routing information can bypass a specific Router and the local Router can reject routing information advertised by another Router.

#### Context

Suppressing an interface from receiving and sending OSPF packets helps routing information to bypass a specific Router and enables the local Router to reject routing information advertised by another Router. This ensures that an optimal route is provided.

For example, there are three routes between DeviceA and DeviceB, as shown in [Figure 1](#EN-US_TASK_0172365567__fig_dc_vrp_ospf_cfg_203701). To allow the route with the outbound interface being Interface 2 to be preferred, you can suppress Interface 1 and Interface 3 from receiving and sending OSPF packets.

**Figure 1** Network diagram of suppressing the interfaces from sending and receiving OSPF packets  
![](images/fig_dc_vrp_ospf_cfg_203701.png)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**silent-interface**](cmdqueryname=silent-interface) { **all** | *interface-type* *interface-number* }
   
   
   
   An interface is suppressed from receiving and sending OSPF packets.
   
   The same interface in different processes can be suppressed from sending and receiving OSPF packets, but the [**silent-interface**](cmdqueryname=silent-interface) command is valid only for the OSPF interface in the local process.
   
   After an OSPF interface is configured to be in the silent state, the interface can still advertise its direct routes. Hello packets on the interface, however, cannot be forwarded. Therefore, no neighbor relationship can be established on the interface. This can enhance the networking adaptability of OSPF and reduce system resource consumption.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.