(Optional) Configuring ERPS Self-Healing
========================================

(Optional) Configuring ERPS Self-Healing

#### Context

When an ERPS ring is stable and no fault occurs, if a non-owner node unexpectedly sends an R-APS PDU carrying the signal failure (SF) field, the RPL owner node on the ERPS ring may be unblocked, causing a loop. To eliminate the loop through status detection, enable ERPS self-healing.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) to enter the system view.
2. Run the [**erps ring**](cmdqueryname=erps+ring) **ring-id** command to enter the ERPS ring view.
3. Run the [**erps self-heal disable**](cmdqueryname=erps+self-heal+disable) command to disable ERPS self-healing.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.