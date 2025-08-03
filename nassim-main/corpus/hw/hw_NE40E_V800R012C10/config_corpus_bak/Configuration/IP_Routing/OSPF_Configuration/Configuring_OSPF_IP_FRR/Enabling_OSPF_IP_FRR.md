Enabling OSPF IP FRR
====================

With OSPF IP FRR and loop-free backup links, a device can switch traffic to a backup link immediately if the primary link fails.

#### Context

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* | **router-id** *router-id* | **vpn-instance** *vpn-instance-name* ] \*
   
   
   
   An OSPF process is started, and the OSPF view is displayed.
3. Run [**frr**](cmdqueryname=frr)
   
   
   
   The OSPF FRR view is displayed.
4. Run [**loop-free-alternate**](cmdqueryname=loop-free-alternate)
   
   
   
   OSPF IP FRR is enabled to generate a loop-free backup link.
5. (Optional) Run [**frr-policy route**](cmdqueryname=frr-policy+route) { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* }
   
   
   
   An OSPF IP FRR filtering policy is configured.
   
   After the OSPF IP FRR filtering policy is configured, only the OSPF backup routes that match the filtering conditions of the policy can be added to the forwarding table.
6. To configure remote LFA OSPF IP FRR, perform the following steps:
   1. Run [**remote-lfa**](cmdqueryname=remote-lfa) **tunnel** **ldp** [ **maximum-reachable-cost** *cost-value* ]
      
      
      
      Remote LFA OSPF IP FRR is enabled.
   2. (Optional) Run [**remote-lfa available-tunnel-destination**](cmdqueryname=remote-lfa+available-tunnel-destination) **ip-prefix** *ip-prefix-name*
      
      
      
      A filtering policy is configured to filter PQ nodes.
      
      After a filtering policy is configured, only the nodes that meet the filtering conditions become PQ nodes, which facilitates network optimization.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the OSPF view.
   4. (Optional) Run [**avoid-microloop frr-protected**](cmdqueryname=avoid-microloop+frr-protected)
      
      
      
      The OSPF microloop avoidance is enabled.
   5. (Optional) Run [**avoid-microloop frr-protected rib-update-delay**](cmdqueryname=avoid-microloop+frr-protected+rib-update-delay) *rib-update-delay*
      
      
      
      The delay after which OSPF delivers routes is configured.
      
      If OSPF remote LFA FRR is enabled and the primary link fails, traffic is switched to the backup link. If route convergence occurs again, traffic is switched from the backup link to a new primary link. During the switchover, microloop may occur. To prevent this problem, OSPF anti-microloop is enabled and delays the switching. To configure the delay, run the [**avoid-microloop frr-protected rib-update-delay**](cmdqueryname=avoid-microloop+frr-protected+rib-update-delay) command. After the command is run, OSPF does not switch traffic to the backup link until the delay elapses.
   6. Run [**frr**](cmdqueryname=frr)
      
      
      
      The OSPF FRR view is displayed.
7. (Optional) Run [**tiebreaker**](cmdqueryname=tiebreaker) { **node-protecting** | **lowest-cost** | **ldp-sync hold-max-cost** | **srlg-disjoint** } **preference** *value*
   
   
   
   The solution of selecting a backup path for OSPF IP FRR is set.
   
   
   
   By default, the solution of selecting a backup path for OSPF IP FRR is node-protection path first. In actual networking scenarios, the solution may need to be changed to smallest-cost path first due to considerations such as the interface forwarding capability and link cost. In [Figure 1](#EN-US_TASK_0172365618__en-us_cliref_0172379289_fig_tiebreaker_ospf), the primary path is Link-1 (DeviceS -> DeviceE -> DeviceD), and Link-2 and Link-3 (DeviceS -> DeviceN -> DeviceD) are backup path candidates. By default, Link-3 is selected as the backup path. To change the solution of selecting a backup path for OSPF IP FRR to smallest-cost path first so that Link-2 is selected as the backup path, perform this step.**Figure 1** Solution of selecting a backup path for OSPF IP FRR  
   ![](figure/en-us_image_0000001229453511.png)
   
   [Figure 2](#EN-US_TASK_0172365618__en-us_cliref_0172379289_fig_tiebreaker_ospf02) shows an inter-board scenario, where Link-1 (Device A -> Device D) is the primary path, and Link-2 (Device A -> Device E -> Device D) is the backup path. After the primary path Link-1 fails, Link-2 becomes the new primary path, and the new backup path is Link-3 (Device A->Device B->Device C->Device D). If Link-1 goes up again but the LDP session has not gone up, OSPF enters the Hold-max-cost state. Consequently, the primary path is still Link-2, and the backup path is still Link-3. If the LDP session goes up but **ldp-sync hold-max-cost** is not configured, OSPF exits the Hold-max-cost state when the timer used to delay sending an LDP session Up message expires. In this case, OSPF switches the primary path back to Link-1. Because the upstream and downstream entries reside on different boards and the downstream entry has not been updated when downstream traffic arrives, packet loss occurs. To resolve the problem, configure **ldp-sync hold-max-cost** so that OSPF preferentially selects the path with the maximum cost set by LDP-IGP synchronization when OSPF is in the Hold-max-cost state. The backup path is switched to Link-1, and backup forwarding entries are delivered in advance. When the timer used to delay sending an LDP session Up message expires, OSPF exits the Hold-max-cost state and switches the primary path to Link-1. Because the downstream backup entry is available, no packet loss occurs.**Figure 2** Maximum-cost (set by LDP-IGP synchronization) path first solution  
   ![](figure/en-us_image_0000001184213782.png)
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.