Controlling Advertisement of Shared Address Pool UNRs
=====================================================

If BRASs work in load balancing mode, the BRASs must be configured to control advertisement of UNRs of configured address pools.

#### Context

In a dual-system hot backup scenario, BRASs control the advertisement of UNRs of configured address pools in either of the following modes:

* Manual control: If two BRASs work in load balancing mode, each BRAS is configured with two address pools. One is the primary address pool and the other is the secondary address pool. The primary address pool on one BRAS is the secondary address pool on the other BRAS. The cost value of the primary address pool must be smaller than that of the secondary address pool. The cost values can be set in a routing policy, which allows the UNR of the primary address pool to have higher route precedence than that of the secondary address pool. For detailed configurations, see [Configuring a Routing Policy](../vrp/dc_vrp_route-policy_cfg_0000.html) in *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - IP Routing*.
* Automatic control: This mode can be more easily deployed than manual control. Automatic control prevents the problem where UNRs cannot be advertised in time after a master/backup switchover is triggered by a BRAS fault and then the fault is rectified, improving link reliability. The default route cost can be used to control route preference. In dual-BRAS hot backup scenarios, the cost value of the UNR imported by a routing protocol is trusted to ensure that the host route has a higher priority.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**peer-backup route-cost**](cmdqueryname=peer-backup+route-cost) **auto-advertising**
   
   
   
   The BRAS is configured to use the default route cost to control route preference during route generation. The route can be an address pool UNR or a route to a loopback interface of the LAC on an L2TP tunnel.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Address pool UNRs are not updated in real time no matter whether the BRAS is configured to use the default route cost to control route preference. Route control takes effect only when the address pool is re-bound to the RBS.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
4. (Optional) Run [**track interface**](cmdqueryname=track+interface) { *interface-name* | *interface-type interface-number* } [ **weight** *weight* ]
   
   
   
   The RBS is enabled to track the network-side interface status so that it can adjust the policy for advertising shared address pool UNR when a fault or fault recovery event is detected. If devices have multiple uplinks with different bandwidth, configure different weights for uplink interfaces based on the uplink bandwidths, and implement on-demand switchovers with the help of switching policies. If the interfaces have different rates, configure the weights based on their rates. For example, configure a larger weight for a 10GE interface than a GE interface. If interface A is 10GE, and the bandwidth planned for RUI is 5 Gbit/s; interface B is GE, and the bandwidth planned for RUI is 1 Gbit/s; interface C is GE, and the bandwidth planned for RUI is 0.5 Gbit/s, when interface B is chosen as a reference interface with a configured weight 10, the weight of interface A is 50 and that of interface C is 5.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The formula is as follows: Fault rate = Total weight of faulty interfaces/Total weight of interfaces x 100%. If interfaces B and C are faulty, fault rate = (10 + 5)/(50 + 10 + 5) x 100% = 23%. If interface A is faulty, fault rate = 50/(50 + 10 + 5) x 100% = 77%.
5. (Optional) Run [**switchover uplink**](cmdqueryname=switchover+uplink) { **failure-ratio** *failure-ratio* | **duration** *duration* } \*
   
   
   
   The threshold for a primary/backup path switchover due to uplink failures and the duration before the switchover are configured.
   
   
   
   When you run the [**track interface**](cmdqueryname=track+interface) command, the weights specified must comply with the rules of the master/backup VRRP switchover. If a primary/backup path switchover is performed based on the fault rate of uplinks but a master/backup VRRP switchover is not performed, the backup device forwards the network-side traffic back to the master device for processing after receiving the traffic. In this case, the master device is congested with traffic because the primary/backup path switchover is not performed at the same time as the master/backup VRRP switchover.
   
   When you configure a primary/backup path switchover to be performed based on the fault rate of uplinks, also run the [**peer-backup route-cost auto-advertising**](cmdqueryname=peer-backup+route-cost+auto-advertising) command in the system view. In this situation, when a primary/backup path switchover is performed based on the fault rate of uplinks, the priority of a UNR is reduced, but no UNRs are withdrawn. This configuration prevents downlink traffic from being interrupted.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
7. (Optional) Run [**track monitor-group**](cmdqueryname=track+monitor-group) *group-name* **switchover** **failure-ratio** *percent*
   
   
   
   The RBS is enabled to track the status of the interface group. After you run the **track interface-group** command in the RBS view in which the [**track interface**](cmdqueryname=track+interface) command has been run, the device automatically deletes the [**track interface**](cmdqueryname=track+interface) and [**switchover uplink**](cmdqueryname=switchover+uplink) configurations and then determines whether to perform service switching based on the **track monitor-group** configuration.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before running the **track monitor-group switchover failure-ratio** command, you must have run the **monitor-group** command to create an interface monitoring group.
8. (Optional) Run [**track route-monitor-group**](cmdqueryname=track+route-monitor-group) *group-name* **switchover** **failure-ratio** *percent*
   
   
   
   The RBS is configured to track the status of the route monitoring group, and an uplink fault rate threshold for triggering a primary/backup path switchover is configured.
   
   
   
   If the [**track interface**](cmdqueryname=track+interface) command has been run in the RBS view, the device automatically deletes the [**track interface**](cmdqueryname=track+interface) configuration after the [**track route-monitor-group switchover failure-ratio**](cmdqueryname=track+route-monitor-group+switchover+failure-ratio) command is run. Then, the device determines whether to perform a service switchover based on the [**track route-monitor-group switchover failure-ratio**](cmdqueryname=track+route-monitor-group+switchover+failure-ratio) configuration.

#### Follow-up Procedure

To use a routing policy to allow the UNR to have the highest preference, perform any of the following operations:

* Run the [**import-route**](cmdqueryname=import-route) **unr route-policy** *route-policy-name* command in the IS-IS view.
* Run the [**import-route**](cmdqueryname=import-route) **unr route-policy** *route-policy-name* command in the OSPF view.
* Run the [**import-route**](cmdqueryname=import-route) **unr route-policy** *route-policy-name* command in the BGP view.

To reserve the cost values of UNRs imported by a routing protocol, perform any of the following operations based on the type of the routing protocol:

* Run the [**import-route**](cmdqueryname=import-route) **unr inherit-cost** command in the IS-IS view.
* Run the following commands in the OSPF view:
  1. [**default**](cmdqueryname=default) **cost inherit-metric**
  2. [**import-route**](cmdqueryname=import-route) **unr**
* Run the [**import-route**](cmdqueryname=import-route) **unr** command in the BGP view.