Enabling Multi-Path PE Load Balancing
=====================================

Enabling_Multi-Path_PE_Load_Balancing

#### Context

In an L3VPN route forwarding scenario, traffic forwarded from PE1 to a CE can be load-balanced between only two links by default.

On the network shown in [Figure 1](#EN-US_TASK_0000001174087716__fig6364167172914), to configure multi-path load balancing, run the [**load-balance extend-enhance enable**](cmdqueryname=load-balance+extend-enhance+enable) command on PE1 to enable multi-path PE load balancing.

**Figure 1** Multi-path PE load balancing in an L3VPN route forwarding scenario  
![](figure/en-us_image_0000001174088074.png)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**load-balance extend-enhance enable**](cmdqueryname=load-balance+extend-enhance+enable)
   
   
   
   Multi-path PE load balancing is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.