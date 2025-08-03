Setting a Period During Which OSPF Keeps the Maximum Cost in Local LSAs
=======================================================================

Setting a Period During Which OSPF Keeps the Maximum Cost in Local LSAs

#### Prerequisites

Before setting a period during which OSPF keeps the maximum cost in local LSAs, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

When an OSPF interface changes from down to up, the OSPF neighbor relationship is re-established. After OSPF routes converge, traffic is switched back to the recovered link. In most cases, IGP routes converge quickly, although many services that depend on IGP routes may require a delayed switchback. In this case, you can run the [**ospf peer hold-max-cost**](cmdqueryname=ospf+peer+hold-max-cost) command to specify a period during which OSPF keeps the maximum cost in local LSAs. After the OSPF neighbor relationship reaches the Full state, the traffic forwarding path remains unchanged during the specified period. After this period expires, the maximum cost is restored to the original cost of the recovered link, and traffic is switched back to the recovered link.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Set a period during which OSPF keeps the maximum cost in local LSAs.
   
   
   ```
   [ospf peer hold-max-cost](cmdqueryname=ospf+peer+hold-max-cost) timer timer
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **brief** command to check brief OSPF information. The **Timers** field in the command output includes the period during which OSPF keeps the maximum cost in local LSAs.