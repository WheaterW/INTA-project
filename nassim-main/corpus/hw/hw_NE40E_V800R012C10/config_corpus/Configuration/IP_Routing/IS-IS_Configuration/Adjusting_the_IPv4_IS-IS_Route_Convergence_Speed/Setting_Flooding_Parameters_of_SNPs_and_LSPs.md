Setting Flooding Parameters of SNPs and LSPs
============================================

To speed up LSDB synchronization between devices, set proper values for flooding parameters of SNPs and LSPs.

#### Context

SNPs consist of CSNPs and PSNPs. CSNPs carry summaries of all LSPs in LSDBs, ensuring LSDB synchronization between neighboring routers. The operation mechanism on broadcast links is slightly different from that on P2P links.

* On a broadcast link, CSNPs are periodically sent by a DIS device. If a router detects that its LSDB is not synchronized with that on its neighboring router, the router will send PSNPs to apply for missing LSPs.
* On a P2P link, CSNPs are sent only during initial establishment of neighbor relationships. If a request is acknowledged, a neighboring router will send a PSNP in response to a CSNP. If a router detects that its LSDB is not synchronized with that on its neighboring router, the router will send PSNPs to apply for missing LSPs.

You can modify the following parameters of SNPs and LSPs on the NE40E to speed up LSDB synchronization:

* [Set an interval at which CSNPs are sent](#EN-US_TASK_0172365995__step_dc_vrp_isis_cfg_101901).
* [Configure the intelligent timer to control LSP generation](#EN-US_TASK_0172365995__step_dc_vrp_isis_cfg_101902).
* [Set the size of an LSP](#EN-US_TASK_0172365995__step_dc_vrp_isis_cfg_101903).
* [Set the LSP update interval](#EN-US_TASK_0172365995__step_dc_vrp_isis_cfg_101904).
* [Set the maximum lifetime for LSPs](#EN-US_TASK_0172365995__step_dc_vrp_isis_cfg_101905).
* [Set the maximum holdtime for the largest IS-IS route cost in local LSPs.](#EN-US_TASK_0172365995__step_dc_vrp_isis_cfg_101910)
* [Enable LSP fast flooding](#EN-US_TASK_0172365995__step_dc_vrp_isis_cfg_101907).
* [Set an interval at which LSPs are retransmitted over a P2P link](#EN-US_TASK_0172365995__step_dc_vrp_isis_cfg_101908).
* [Configure automatic IS-IS LSP Remaining Lifetime adjustment](#EN-US_TASK_0172365995__step_dc_vrp_isis_cfg_101909).


#### Procedure

* Set an interval at which CSNPs are sent.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**isis timer csnp**](cmdqueryname=isis+timer+csnp) *csnp-interval* [ **level-1** | **level-2** ]
     
     
     
     The interval at which CSNPs are sent is set on the specified interface.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Configure **Level-1** and **Level-2** only when a broadcast interface is specified.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the intelligent timer to control LSP generation.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run [**timer lsp-generation**](cmdqueryname=timer+lsp-generation) *max-interval* [ *init-interval* [ *incr-interval* ] ] [ **level-1** | **level-2** ]
     
     
     
     The intelligent timer is configured to control LSP generation.
     
     
     
     The intelligent timer involves three parameters, and the parameters are described as follows:
     + When only *max-interval* is used, the intelligent timer becomes a one-shot timer.
     + If both *init-interval* and *incr-interval* are configured, the initial interval for generating an LSP is *init-interval*, and the interval for generating an LSP with the same LSP ID for the second time is *incr-interval*. From the third time on, each time the route changes, the interval for generating an LSP doubles until the interval reaches *max-interval*. If the local routing information still changes frequently within *max-interval*, the delay remains *max-interval*. If the local routing information does not change after the interval specified by *max-interval* expires or the IS-IS process is restarted, the interval decreases to *init-interval*.
     + If *init-interval* is specified but *incr-interval* is not specified, *init-interval* is used as the interval for generating an LSP for the first time, and *max-interval* is used as the interval for generating subsequent LSPs. If the local routing information changes frequently within the interval specified by *max-interval*, the delay remains *max-interval*. If the local routing information does not change after the interval specified by *max-interval* expires or the IS-IS process is restarted, the interval decreases to *init-interval*.
  4. Run [**suppress-flapping lsp-generation**](cmdqueryname=suppress-flapping+lsp-generation) **timer** *delay-interval* [ **threshold** *threshold-value* ]
     
     
     
     A period is specified for the system to delay generating the same LSP during route flapping.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set the size of an LSP.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run [**lsp-length**](cmdqueryname=lsp-length) **originate** *max-size*
     
     
     
     The size of an LSP to be generated is set.
  4. Run [**lsp-length**](cmdqueryname=lsp-length) **receive** *max-size*
     
     
     
     The size of an LSP to be received is set.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     *max-size* of an LSP to be generated must be less than or equal to *max-size* of an LSP to be received.
     
     
     The value of *max-size* set using the [**lsp-length**](cmdqueryname=lsp-length) command must meet the following requirements; otherwise, the MTU status on the interface is considered down.
     + The MTU of an Ethernet interface must be greater than or equal to the sum of the value of *max-size* plus 3.
     + The MTU of a P2P interface must be greater than or equal to the value of *max-size*.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set the LSP update interval.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run [**timer lsp-refresh**](cmdqueryname=timer+lsp-refresh) *refresh-value*
     
     
     
     An LSP update interval is set.
     
     
     
     To ensure the synchronization of LSPs in the entire area, IS-IS periodically sends all the current LSPs.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Ensure that the LSP update interval is at least 300s shorter than the maximum LSP lifetime so that new LSPs can reach all routers in the area before the original LSPs expire.
     
     The larger a network, the greater the deviation between the LSP update interval and the maximum LSP lifetime.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set the maximum lifetime for LSPs.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run [**timer lsp-max-age**](cmdqueryname=timer+lsp-max-age) *max-age-value*
     
     
     
     The maximum lifetime is set for LSPs.
     
     
     
     When a device generates the system LSP, it fills in the maximum lifetime for this LSP. The lifetime of the LSP decreases with time. If the device does not receive any updated LSPs and the lifetime of the LSP is reduced to 0, the device keeps the LSP for another 60s. If the device fails to receive any updated LSPs within the 60s, it deletes the LSP from the LSDB.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set the maximum holdtime for the largest IS-IS route cost in local LSPs.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**isis**](cmdqueryname=isis) [ **process-id** *process-id* ] **peer hold-max-cost** **timer** *timer*
     
     
     
     The period during which IS-IS keeps the maximum cost in local LSPs is set.
     
     
     
     When an IS-IS interface changes from down to up, the IS-IS neighbor relationship is re-established. After IGP route convergence is completed, traffic is switched back. In most cases, IGP routes converge quickly. However, many services that depend on IGP routes may require a delayed IGP route switchback. To delay traffic switchback, you can configure a hold-max-cost timer using the [**isis peer hold-max-cost**](cmdqueryname=isis+peer+hold-max-cost) command for IS-IS to keep the maximum cost (16777214 when the cost style is wide and 63 when the cost style is narrow) in local LSPs. In this way, traffic is still forwarded along the original path before the timer expires. When the timer expires, the cost in local LSPs is restored to the original value, and traffic is switched back normally.
  4. (Optional) Run [**isis peer hold-cost**](cmdqueryname=isis+peer+hold-cost) *cost-val* **timer** *timer-val*
     
     
     
     The period during which IS-IS keeps the specified cost in local LSPs is set.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable LSP fast flooding.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**isis timer lsp-throttle**](cmdqueryname=isis+timer+lsp-throttle) *throttle-interval* [ **count***count* ]
     
     
     
     The minimum interval at which LSPs are sent by the interface and the maximum number of LSPs that can be sent within the interval are set.
     
     
     
     The *count* parameter specifies the maximum number of LSPs that can be sent within the interval specified by *throttle-interval*. The value is an integer ranging from 1 to 1000.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  6. Run [**suppress-flapping lsp-flood**](cmdqueryname=suppress-flapping+lsp-flood) **timer** *delay-interval* [ **threshold** *threshold-value* ]
     
     
     
     A period is specified for the system to delay LSP flooding during route flapping.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set an interval at which LSPs are retransmitted over a P2P link.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. (Optional) Run [**isis circuit-type**](cmdqueryname=isis+circuit-type) **p2p** [ **strict-snpa-check** ]
     
     
     
     The broadcast interface is simulated as a P2P interface.
     
     
     
     An interval at which LSPs are retransmitted takes effect only on P2P interfaces. Therefore, to configure the interval on a broadcast interface, change the broadcast interface to a P2P interface first.
  4. Run [**isis timer lsp-retransmit**](cmdqueryname=isis+timer+lsp-retransmit) *retransmit-interval*
     
     
     
     The interval at which LSPs are retransmitted over a P2P link is set.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure automatic IS-IS LSP Remaining Lifetime adjustment.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. (Optional) Run [**undo lsp-remaining-lifetime refresh disable**](cmdqueryname=undo+lsp-remaining-lifetime+refresh+disable)
     
     
     
     Automatic IS-IS LSP Remaining Lifetime adjustment is enabled.
  4. Run [**lsp-remaining-lifetime refresh timer**](cmdqueryname=lsp-remaining-lifetime+refresh+timer) { *refreshvalue* | **lsp-max-age** }
     
     
     
     An IS-IS LSP Remaining Lifetime value is set.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.