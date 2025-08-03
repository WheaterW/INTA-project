(Optional) Enabling IPv6 FRR Poison Reverse
===========================================

To configure IPv6 FRR on an IP ring network, you need to enable IPv6 FRR poison reverse to prevent instantaneous traffic storms during route convergence.

#### Context

In [Figure 1](#EN-US_TASK_0000001171365900__fig20345859153119), IPv6 FRR is deployed on the IP ring network, and traffic enters the ring network from Device D and leaves the ring network from Device A. The primary and backup next hops of Device D are Device C and Device E, respectively. The primary and backup next hops of Device C are Device B and Device D, respectively. If the link between Device B and Device C fails and the traffic reaches Device C, Device C determines that the primary link fails and forwards the traffic to Device D. However, before the route convergence is complete, Device D cannot detect the link failure between Device B and Device C, and continues forwarding the traffic to Device C. As a result, an instantaneous traffic storm is generated between Device C and Device D. After Device D detects the link failure between Device B and Device C through route convergence, Device D forwards the traffic to its backup next hop (Device E). To prevent instantaneous traffic storms during route convergence and enable Device D to detect the link failure quickly, you can enable the IPv6 FRR poison reverse function. After the function is enabled, Device D searches its FIB based on the destination IP address to obtain the next hop and outbound interface+VLAN information. If the outbound interface is the primary interface and is up, Device D checks whether the outbound interface+VLAN is the same as the inbound interface+VLAN. If they are the same, Device D forwards the traffic through the backup interface. If the link between Device B and Device C fails, the traffic forwarded from Device D to Device C goes back to Device D. Device D does not send the traffic back to Device C; instead, it forwards the traffic to its backup next hop (Device E). Finally, the traffic leaves the ring network from Device A, as shown in [Figure 2](#EN-US_TASK_0000001171365900__fig8430154133319).

**Figure 1** IP ring network  
![](figure/en-us_image_0000001216287933.png)
**Figure 2** IP ring network with IPv6 FRR poison reverse enabled  
![](figure/en-us_image_0000001216606497.png)

#### Procedure

1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view or sub-interface view is displayed.
2. Run [**poison-reverse enable**](cmdqueryname=poison-reverse+enable)
   
   
   
   IPv6 FRR poison reverse is enabled.
   
   
   
   This command is used to prevent instantaneous traffic storms during route convergence in a scenario where IPv6 FRR is configured on an IP ring network.
   
   Poison reverse does not support load balancing.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.