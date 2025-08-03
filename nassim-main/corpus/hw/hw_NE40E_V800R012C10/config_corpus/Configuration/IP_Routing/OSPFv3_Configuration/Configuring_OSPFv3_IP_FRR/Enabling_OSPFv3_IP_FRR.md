Enabling OSPFv3 IP FRR
======================

With OSPF IP FRR and loop-free backup links, a device can switch traffic to a backup link immediately if the primary link fails.

#### Context

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ] [ **vpn-instance** *vpnname* ]
   
   
   
   An OSPFv3 process is enabled, and the OSPFv3 view is displayed.
3. Run [**frr**](cmdqueryname=frr)
   
   
   
   The OSPFv3 FRR view is displayed.
4. Run [**loop-free-alternate**](cmdqueryname=loop-free-alternate)
   
   
   
   OSPFv3 IP FRR is enabled, and a loop-free backup link is generated.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   OSPFv3 can generate a loop-free backup link only when the OSPFv3 IP FRR traffic protection inequality is met.
5. (Optional) Run [**frr-policy route**](cmdqueryname=frr-policy+route) { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* }
   
   
   
   An OSPFv3 IP FRR filtering policy is configured.
   
   
   
   After the OSPFv3 IP FRR filtering policy is configured, only the OSPFv3 backup routes that match the filtering rules in the policy can be added to the forwarding table.
6. (Optional) Run [**tiebreaker**](cmdqueryname=tiebreaker) { **node-protecting** | **lowest-cost** } **preference** *value* 
   
   
   
   The solution of selecting a backup path for OSPFv3 IP FRR is configured.
   
   
   
   By default, the solution of selecting a backup path for OSPFv3 IP FRR is node-protection path first. In actual networking scenarios, the solution may need to be changed to smallest-cost path first due to considerations such as interface forwarding capacity and link cost. In [Figure 1](#EN-US_TASK_0172365760__en-us_cliref_0172379410_fig_tiebreaker_ospfv3), the primary path is Link-1 (DeviceS -> DeviceE -> DeviceD), and Link-2 and Link-3 (DeviceS -> DeviceN -> DeviceD) are backup path candidates. By default, Link-3 is selected as the backup path. To change the solution of selecting a backup path to smallest-cost path first, perform this step. After this step is performed, Link-2 is selected as the backup path.**Figure 1** Solution of selecting a backup path for OSPFv3 IP FRR
   
   ![](figure/en-us_image_0000001183892862.png)
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.