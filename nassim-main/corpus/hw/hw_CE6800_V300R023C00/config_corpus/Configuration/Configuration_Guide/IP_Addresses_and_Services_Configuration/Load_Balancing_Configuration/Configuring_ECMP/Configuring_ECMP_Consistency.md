Configuring ECMP Consistency
============================

Configuring ECMP Consistency

#### Context

If a path fails, ECMP re-hashes all traffic by default, which affects traffic forwarding on normal paths. To address this issue, configure ECMP consistency so that the device hashes the traffic only on the faulty path.

However, if a faulty member link recovers or a new link is added, ECMP consistency cannot ensure that the original forwarding path remains unchanged. ECMP consistency enhancement is implemented based on ECMP consistency. When a faulty link recovers, only traffic on the faulty link is re-hashed; when a new link is added, not all traffic needs to be re-hashed. This ensures link load balancing consistency.

The following is an example:

Assume that 12 data packets are forwarded through links A, B, C, and D. The initial packets allocated to the links are shown in the left part of [Figure 1](#EN-US_TASK_0000001563881105__fig78111195547). In this case, traffic is evenly distributed to each link. If ECMP consistency is configured and link D is disconnected, traffic on it is evenly distributed to the other three links, as shown in the right part of [Figure 1](#EN-US_TASK_0000001563881105__fig78111195547).

**Figure 1** Configuring ECMP consistency  
![](figure/en-us_image_0000001563761541.png)

If link D recovers but ECMP consistency enhancement is not configured, traffic distribution remains unchanged, as shown in the left part of [Figure 2](#EN-US_TASK_0000001563881105__fig013518491004). In this case, link D does not participate in traffic forwarding. If link D recovers and ECMP consistency enhancement is configured, link D participates in traffic forwarding, as shown in the right part of [Figure 2](#EN-US_TASK_0000001563881105__fig013518491004).

**Figure 2** Configuring ECMP consistency enhancement  
![](figure/en-us_image_0000001564121281.png)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure ECMP consistency.
   
   
   ```
   [load-balance ecmp stateful enable](cmdqueryname=load-balance+ecmp+stateful+enable)
   ```
3. (Optional) Configure ECMP consistency enhancement.
   
   
   ```
   [load-balance ecmp stateful enhanced enable](cmdqueryname=load-balance+ecmp+stateful+enhanced+enable)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   This command does not take effect in scenarios where the next hop for load balancing involves VXLAN tunnel forwarding. To enable ECMP consistency enhancement in such scenarios, run the **load-balance vxlan-overlay ecmp stateful** **enable** command.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```