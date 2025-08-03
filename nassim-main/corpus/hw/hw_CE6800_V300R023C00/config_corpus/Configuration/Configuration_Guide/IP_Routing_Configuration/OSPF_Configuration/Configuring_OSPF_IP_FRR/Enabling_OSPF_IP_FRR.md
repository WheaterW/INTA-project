Enabling OSPF IP FRR
====================

Enabling OSPF IP FRR

#### Prerequisites

Before enabling OSPF IP FRR, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id | router-id router-id | vpn-instance vpn-instance-name ] *
   ```
   
   *process-id* specifies the ID of an OSPF process, and the default value is 1.
3. Enter the OSPF IP FRR view.
   
   
   ```
   [frr](cmdqueryname=frr)
   ```
4. Enable OSPF IP FRR so that OSPF can generate a loop-free backup link.
   
   
   ```
   [loop-free-alternate](cmdqueryname=loop-free-alternate)
   ```
   
   OSPF can generate a loop-free backup link only when OSPF IP FRR meets the traffic protection inequalities. For detailed description, see [Understanding OSPF IP FRR](vrp_ospf_cfg_0096_copy.html).
5. (Optional) Configure an OSPF IP FRR route-policy to filter OSPF backup routes.
   
   
   ```
   [frr-policy route](cmdqueryname=frr-policy+route) route-policy route-policy-name
   ```
   
   After the OSPF IP FRR route-policy is configured, only the OSPF backup routes that match the filtering rules in the policy can be added to the forwarding table.
6. (Optional) Set the solution of selecting a backup path for OSPF IP FRR.
   
   
   ```
   [tiebreaker](cmdqueryname=tiebreaker) { node-protecting | lowest-cost } preference value
   ```
   By default, the solution of selecting a backup path for OSPF IP FRR is node-protection path first. In actual networking scenarios, the solution may need to be changed to smallest-cost path first due to considerations such as the interface forwarding capability and link cost. In [Figure 1](#EN-US_TASK_0000001176742885__en-us_task_0275861843_en-us_cliref_0172379289_fig_tiebreaker_ospf), the primary path is Link-1 (DeviceS -> DeviceE -> DeviceD), and Link-2 (DeviceS -> DeviceE -> DeviceD) and Link-3 (DeviceS -> DeviceN -> DeviceD) are backup path candidates. By default, Link-3 is selected as the backup path. To change the solution of selecting a backup path for OSPF IP FRR to smallest-cost path first, run the [**tiebreaker**](cmdqueryname=tiebreaker) command. After the command is run, Link-2 is selected as the backup path.**Figure 1** Solution of selecting a backup path for OSPF IP FRR  
   ![](figure/en-us_image_0000001184442696.png)
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```