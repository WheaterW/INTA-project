Disabling an Interface from Receiving Packets
=============================================

If an interface does not need to learn routing information
from neighbors, you can disable the interface from receiving RIP packets.

#### Usage Scenario

On an enterprise network
where departments are not allowed to communicate with each other,
you can disable interfaces from receiving packets.

On the network
shown in [Figure 1](#EN-US_TASK_0172365856__fig_dc_vrp_rip_cfg_001601), if
you do not want Department 1 to learn routing information about Department
2, you can disable the interface on Device A from receiving packets.

**Figure 1** Scenario where an interface is disabled from receiving packets
  
![](images/fig_dc_vrp_rip_cfg_001601.png)  



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run **interface** *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**undo rip input**](cmdqueryname=undo+rip+input)
   
   
   
   The interface is disabled from receiving RIP packets.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.