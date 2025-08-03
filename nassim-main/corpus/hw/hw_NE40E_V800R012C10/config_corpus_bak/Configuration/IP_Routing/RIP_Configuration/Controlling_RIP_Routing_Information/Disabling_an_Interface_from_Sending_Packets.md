Disabling an Interface from Sending Packets
===========================================

When you do not need an interface connected to an external
network to send routing information, disable the interface from sending
RIP packets.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0172365854__fig_dc_vrp_rip_cfg_001501), RIP-enabled Network 1 is connected to Network 2 through
the edge device Device A. You can disable the interface on Device A from sending packets.

**Figure 1** Scenario where an interface is disabled from sending packets
  
![](images/fig_dc_vrp_rip_cfg_001501.png)  



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run **interface** *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**undo rip output**](cmdqueryname=undo+rip+output)
   
   
   
   The interface is disabled from sending RIP packets.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.