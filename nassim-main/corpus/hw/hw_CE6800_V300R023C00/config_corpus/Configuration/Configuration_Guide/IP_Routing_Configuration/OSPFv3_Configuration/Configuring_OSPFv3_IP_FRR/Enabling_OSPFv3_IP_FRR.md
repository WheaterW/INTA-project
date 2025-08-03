Enabling OSPFv3 IP FRR
======================

Enabling OSPFv3 IP FRR

#### Prerequisites

Before enabling OSPFv3 IP FRR, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. Enter the OSPFv3 IP FRR view.
   
   
   ```
   [frr](cmdqueryname=frr)
   ```
4. Enable OSPFv3 IP FRR so that OSPFv3 can generate a loop-free backup link.
   
   
   ```
   [loop-free-alternate](cmdqueryname=loop-free-alternate)
   ```
   
   OSPFv3 can generate a loop-free backup link only when OSPFv3 IP FRR meets the traffic protection inequalities. For detailed description, see [Understanding OSPFv3 IP FRR](vrp_ospfv3_cfg_0073_copy.html).
5. (Optional) Configure an OSPFv3 IP FRR route-policy to filter OSPFv3 backup routes.
   
   
   ```
   [frr-policy route](cmdqueryname=frr-policy+route) route-policy route-policy-name
   ```
   
   After the OSPFv3 IP FRR route-policy is configured, only the OSPFv3 backup routes that match the filtering rules in the policy can be added to the forwarding table.
6. (Optional) Set the solution of selecting a backup path for OSPFv3 IP FRR.
   
   
   ```
   [tiebreaker](cmdqueryname=tiebreaker) { node-protecting | lowest-cost } preference value
   ```
   By default, the solution of selecting a backup path for OSPFv3 IP FRR is node-protection path first. In actual networking scenarios, the solution may need to be changed to smallest-cost path first due to considerations such as interface forwarding capacity and link cost. In [Figure 1](#EN-US_TASK_0000001130623220__en-us_task_0275857964_en-us_cliref_0172379410_fig_tiebreaker_ospfv3), the primary path is Link-1 (DeviceS -> DeviceE -> DeviceD), and Link-2 (DeviceS -> DeviceE -> DeviceD) and Link-3 (DeviceS -> DeviceN -> DeviceD) are backup path candidates. By default, Link-3 is selected as the backup path. To change the solution of selecting a backup path to smallest-cost path first, run the [**tiebreaker**](cmdqueryname=tiebreaker) command. After the command is run, Link-2 is selected as the backup path.**Figure 1** Solution of selecting a backup path for OSPFv3 IP FRR
   
   ![](figure/en-us_image_0000001184283052.png)
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```