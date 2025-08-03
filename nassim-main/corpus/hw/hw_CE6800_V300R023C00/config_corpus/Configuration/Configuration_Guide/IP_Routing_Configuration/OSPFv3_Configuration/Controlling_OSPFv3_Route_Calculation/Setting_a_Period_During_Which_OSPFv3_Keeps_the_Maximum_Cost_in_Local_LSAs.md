Setting a Period During Which OSPFv3 Keeps the Maximum Cost in Local LSAs
=========================================================================

Setting a Period During Which OSPFv3 Keeps the Maximum Cost in Local LSAs

#### Prerequisites

Before setting a period during which OSPFv3 keeps the maximum cost in local LSAs, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

When an OSPFv3 interface changes from down to up, the OSPFv3 neighbor relationship is re-established. After OSPFv3 routes converge, traffic is switched back to the recovered link. In most cases, IGP routes converge quickly, although many services that depend on IGP routes may require a delayed switchback. In this case, you can specify a period during which OSPFv3 keeps the maximum cost in local LSAs. After the OSPFv3 neighbor relationship reaches the Full state, the traffic forwarding path remains unchanged during the specified period. After this period expires, the maximum cost is restored to the original cost of the recovered link, and traffic is switched back to the recovered link.


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
4. Set a period during which OSPFv3 keeps the maximum cost in local LSAs.
   
   
   ```
   [ospfv3 peer hold-max-cost](cmdqueryname=ospfv3+peer+hold-max-cost) timer hold-max-cost-value [ instance instance-id ]
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **interface** [ **area** *area-id* ] [ *interface-type* *interface-number* ] command to check OSPFv3 interface information. The **Effective cost** field in the command output shows that the effective cost is the result of the [**ospfv3 peer hold-max-cost**](cmdqueryname=ospfv3+peer+hold-max-cost) configuration.