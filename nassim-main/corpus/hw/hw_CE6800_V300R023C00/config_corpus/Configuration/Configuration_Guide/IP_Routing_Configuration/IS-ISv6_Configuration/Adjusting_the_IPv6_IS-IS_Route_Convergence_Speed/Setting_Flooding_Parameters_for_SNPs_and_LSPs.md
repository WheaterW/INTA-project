Setting Flooding Parameters for SNPs and LSPs
=============================================

Setting Flooding Parameters for SNPs and LSPs

#### Prerequisites

Before setting flooding parameters for SNPs and LSPs, you have completed the following task:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0011.html).

#### Context

LSPs are used to exchange link state information. You can configure attributes for LSPs to control their length and maximum lifetime. To speed up LSP flooding and accelerate network convergence, you can either enable LSP fast flooding or reduce the minimum interval at which LSPs are sent and the LSP update interval. However, if the network topology changes frequently, too many CPU resources will be consumed. To prevent this problem, configure the intelligent timer for LSP generation to speed up emergency response and accelerate network convergence. In addition, this timer will increase the LSP generation interval if the network changes frequently, preventing excessive consumption of CPU resources.

SNPs include CSNPs and PSNPs. A CSNP contains summaries of all LSPs in an LSDB, which ensures LSDB synchronization between neighboring routing devices. The operation mechanism on broadcast links is slightly different from that on P2P links.

* On broadcast network links, CSNPs are sent periodically by the DIS. If a neighbor finds that its LSDB is not synchronized, it sends PSNPs to request missing LSPs.
* On a P2P link, CSNPs are sent only during initial establishment of neighbor relationships. If a request is acknowledged, a neighbor sends a PSNP in response to a CSNP. If a neighbor finds that its LSDB is not synchronized, it sends PSNPs to request missing LSPs.

[Table 1](#EN-US_TASK_0000001176662185__table197318147154) describes the parameters that can be configured for SNPs and LSPs to speed up LSDB synchronization.

**Table 1** Parameters of SNPs and LSPs
| Parameter | Function | Usage Scenario |
| --- | --- | --- |
| Interval at which CSNPs are sent | Controls the frequency for sending CSNPs on a broadcast network. | On a broadcast network, devices use CSNPs periodically sent by the DIS to synchronize LSDBs. Upon receipt of a CSNP, if a device finds that the local LSDB does not have a specific LSP or an existing LSP is not the most recently updated one, it sends a PSNP to request the corresponding LSP from the DIS. |
| Maximum length of LSPs | Controls the maximum length of LSPs that can be generated and the maximum length of LSPs that can be accepted. | When the LSDB size is too large, you can increase the maximum length of LSPs that can be generated so that more information is carried in each LSP to be sent. In addition, you can configure the maximum length of LSPs that can be accepted. |
| Maximum lifetime of LSPs | Ensures the validity of an LSP before its updated LSP is received. | When a device generates a system LSP, it fills in the LSP with its maximum lifetime, which decreases with time. If a device has not received any update of an LSP when the lifetime of the LSP decreases to 0, the device keeps the LSP for another 60s. If the device still receives no updates throughout the 60s, the device deletes the LSP from its LSDB. Setting a proper maximum lifetime for LSPs ensures the validity of an LSP before its updates are received. |
| LSP update interval | Controls the periodic update of LSP flooding to maintain LSBD synchronization. | On an IS-IS network, LSDB synchronization is implemented through LSP flooding. If the LSP flooding interval is too short, LSPs will be frequently updated, consuming excessive bandwidth resources. If the LSP flooding interval is too long, the device cannot update network state changes in time. You can set an LSP update interval to control the LSP flooding interval. |
| Hold-max-cost timer for IS-IS to keep the maximum cost in local LSPs | Controls the period during which IS-IS keeps the maximum cost in LSPs sent by the local device. | When an IS-IS interface changes from down to up, the IS-IS neighbor relationship is re-established. After IS-IS routes converge, traffic is switched back. In normal cases, IGP routes converge quickly. However, many services that depend on IGP routes may require a delayed switchback. To delay traffic switchback, you can configure a hold-max-cost timer for IS-IS to keep the maximum cost (16777214 in cost style wide and 63 in cost style narrow) in local LSPs. In this way, traffic is still forwarded along the original path before the timer expires. When the timer expires, the cost in local LSPs is restored to the original value, and traffic is switched back to normal. |
| Minimum interval at which LSPs are sent | Controls the frequency for sending the same LSPs during LSP update. | Reducing the minimum interval at which LSPs are sent speeds up LSP flooding. |
| Intelligent timer for LSP generation | Intelligently controls the frequency for generating LSPs to balance between speeding up route convergence and reducing system load. | On an IS-IS network, if the local routing information changes, a device needs to generate new LSPs to notify this change. If the local routing information changes frequently and new LSPs are generated immediately, a large number of system resources are consumed, impacting system performance. To speed up network convergence without compromising system performance, you can configure an intelligent timer for LSP generation. This timer can automatically adjust the delay in generating LSPs based on the routing information change frequency. |
| LSP fast flooding | Control the number of LSPs flooded by an interface each time to speed up IS-IS network convergence. | When an IS-IS device receives updated LSPs, it updates the corresponding LSPs in its LSDB and periodically floods the updated LSPs based on a timer. With LSP fast flooding, a device floods received updated LSPs before calculating routes, speeding up LSDB synchronization. |
| Interval at which LSPs are retransmitted over a P2P link | Controls the interval for retransmitting LSPs to ensure LSDB synchronization over a P2P link. | Over a P2P link, devices at both ends synchronize LSDBs with each other by flooding LSPs. Upon receipt of an LSP, each end replies with a PSNP. If one end does not receive any PSNP in response to its LSP from the other end throughout the configured period, the local end retransmits the LSP. |
| Remaining lifetime of LSPs | Controls the remaining lifetime of LSPs to ensure correct route calculation. | When the remaining lifetime of an LSP reaches 0, the LSP is deleted. If the remaining lifetime of an LSP is abnormal, the LSP is aged too fast or too slowly, and routes cannot converge normally. To prevent this problem, you can set a remaining lifetime for LSPs. |




#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Configure parameters in the IS-IS view or interface view as follows:
   
   
   * [Table 2](#EN-US_TASK_0000001176662185__table11193183701717) describes how to modify parameters for SNPs and LSPs in the IS-IS view.
     
     **Table 2** Configuring parameters for SNPs and LSPs in the IS-IS view
     | Operation | Command | Description |
     | --- | --- | --- |
     | Configure the maximum length for LSPs. | [**lsp-length**](cmdqueryname=lsp-length) **originate** *max-size* | The command configures the maximum length of LSPs that can be generated.  NOTE:  The maximum length of LSPs that can be generated must be less than or equal to the maximum length of LSPs that can be accepted.  When running the [**lsp-length**](cmdqueryname=lsp-length) command, ensure that the value of *max-size* and local interface MTUs meet the following conditions:  + The MTU value of each Ethernet interface must be greater than or equal to *max-size* plus 3. + The MTU of each P2P interface must be greater than or equal to *max-size*. |
     | [**lsp-length**](cmdqueryname=lsp-length) **receive** *max-size* | The command configures the maximum length of LSPs that can be accepted. NOTE:  The maximum length of LSPs that can be generated must be less than or equal to the maximum length of LSPs that can be accepted.   When running the [**lsp-length**](cmdqueryname=lsp-length) command, ensure that the value of *max-size* and local interface MTUs meet the following conditions:  + The MTU value of each Ethernet interface must be greater than or equal to *max-size* plus 3. + The MTU of each P2P interface must be greater than or equal to *max-size*. |
     | Configure the maximum lifetime for LSPs. | [**timer lsp-max-age**](cmdqueryname=timer+lsp-max-age) *max-age-value* | By default, the maximum lifetime of IS-IS LSPs is 1200 seconds. |
     | Configure an LSP update interval. | [**timer lsp-refresh**](cmdqueryname=timer+lsp-refresh) *refresh-value* | The LSP update interval must be at least 300 seconds shorter than the maximum lifetime configured for LSPs using the **timer lsp-max-age** command to ensure that updated LSPs can reach all devices in the local area before the original LSPs expire. |
     | Configure an intelligent timer for LSP generation. | [**timer lsp-generation**](cmdqueryname=timer+lsp-generation) *max-interval* [ *init-interval* [ *incr-interval* ] ] [ **level-1** | **level-2** ] | Configuring an intelligent timer for LSP generation ensures the balance between speeding up route convergence and reducing system load. The intelligent timer involves three parameters, and the parameters are described as follows: + If only *max-interval* is specified, the intelligent timer becomes a one-shot timer. + If *init-interval* and *incr-interval* are specified, *init-interval* is used as the first delay in generating an LSP, and *incr-interval* is used as the second delay in generating the LSP with the same LSP ID. From the third delay on, the delay doubles each time the corresponding route changes until the delay reaches *max-interval*. + If *init-interval* is specified and *incr-interval* is not, *init-interval* is used as the first delay in generating an LSP, and *max-interval* is used as the delay in generating subsequent LSPs. |
     | [**suppress-flapping lsp-generation**](cmdqueryname=suppress-flapping+lsp-generation) **timer** *delay-interval* [ **threshold** *threshold-value* ] | The command configures a delay in generating the same LSP during route flapping. By default, the delay is 10s. |
     | Configure LSP fast flooding. | [**suppress-flapping lsp-flood**](cmdqueryname=suppress-flapping+lsp-flood) **timer** *delay-interval* [ **threshold** *threshold-value* ] | The command configures a delay in flooding LSPs during route flapping. By default, the delay is 10s. |
     | Configure a remaining lifetime for LSPs. | [**lsp-remaining-lifetime refresh timer**](cmdqueryname=lsp-remaining-lifetime+refresh+timer) { *refreshvalue* | **lsp-max-age** } | By default, the remaining lifetime of IS-IS LSPs is **lsp-max-age**. |
     | [**undo lsp-remaining-lifetime refresh disable**](cmdqueryname=undo+lsp-remaining-lifetime+refresh+disable) | The command enables automatic adjustment of the remaining lifetime for IS-IS LSPs. By default, the function is enabled. |
   * [Table 3](#EN-US_TASK_0000001176662185__table1560863385) describes how to modify parameters for SNPs and LSPs in the IS-IS interface view.
     
     **Table 3** Configuring parameters for SNPs and LSPs in the IS-IS interface view
     | Operation | Command | Description |
     | --- | --- | --- |
     | Configure an interval at which CSNPs are sent by an interface. | [**isis timer csnp**](cmdqueryname=isis+timer+csnp) *csnp-interval* [ **level-1** | **level-2** ] | The **level-1** and **level-2** parameters are configured only on broadcast interfaces. |
     | Configure a hold-max-cost timer for IS-IS to keep the maximum cost in local LSPs. | [**isis peer hold-max-cost timer**](cmdqueryname=isis+peer+hold-max-cost+timer) *timer-val* | The command configures a hold-max-cost timer for IS-IS to keep the maximum cost in local LSPs. |
     | Set the period during which IS-IS keeps the specified cost in local LSPs. | [**isis peer hold-cost**](cmdqueryname=isis+peer+hold-cost) *cost-val* **timer** *timer-val* | This command sets the period during which IS-IS keeps the specified cost in local LSPs. |
     | Set the minimum interval at which LSPs are sent and the maximum number of LSPs that can be sent during the interval. | [**isis timer lsp-throttle**](cmdqueryname=isis+timer+lsp-throttle) *throttle-interval* [ **count** *count* ] | The *count* parameter specifies the maximum number of LSPs that can be sent during *throttle-interval*. |
     | Configure an interval at which LSPs are retransmitted over a P2P link. | [**isis circuit-type**](cmdqueryname=isis+circuit-type) **p2p** | An interval at which LSPs are retransmitted takes effect only on P2P interfaces. Therefore, to configure the interval on a broadcast interface, change the broadcast interface to a P2P interface first. |
     | [**isis timer lsp-retransmit**](cmdqueryname=isis+timer+lsp-retransmit) *retransmit-interval* | The command configures an interval at which LSPs are retransmitted over a P2P link. |
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```