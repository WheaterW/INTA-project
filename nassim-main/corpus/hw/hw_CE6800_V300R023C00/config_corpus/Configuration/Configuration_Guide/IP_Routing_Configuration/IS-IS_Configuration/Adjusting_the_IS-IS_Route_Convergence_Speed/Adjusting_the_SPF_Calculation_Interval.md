Adjusting the SPF Calculation Interval
======================================

Adjusting the SPF Calculation Interval

#### Context

If a network topology frequently changes, IS-IS performs SPF calculation frequently too, consuming excessive CPU resources, and adversely affecting other services.

To solve this problem, configure an intelligent timer to control the SPF calculation interval. With an intelligent timer, the interval for the SPF calculation at the beginning is short, ensuring fast IS-IS route convergence. When the IS-IS network stabilizes, the interval for SPF calculation doubles automatically, reducing unnecessary resource consumption.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Configure an intelligent timer for SPF calculation.
   
   
   ```
   [timer spf](cmdqueryname=timer+spf) max-interval [ init-interval [ incr-interval ] ]
   ```
   
   
   The intelligent timer works as follows:
   * The interval for the first SPF calculation is *init-interval*; the interval for the second SPF calculation is *incr-interval*. From the third time on, the delay in SPF calculation doubles each time until the delay reaches *max-interval*. If the network still flaps within the *max-interval*, the calculation delay remains *max-interval* until the time when the network does not flap throughout *max-interval* or when the IS-IS process is restarted. The delay then decreases to *init-interval*.
   * If *incr-interval* is not specified, *init-interval* is used as the interval for the first SPF calculation, and *max-interval* is used as the interval for subsequent SPF calculations.
   * If only *max-interval* is specified, the intelligent timer becomes a one-shot timer.
4. Configure a period for the device to delay route calculation when the device receives an LSP during route flapping.
   
   
   ```
   [suppress-flapping route-calculate](cmdqueryname=suppress-flapping+route-calculate) timer delay-interval
   ```
   
   
   
   By default, if a device receives an LSP during route flapping, it delays route calculation for 10s.
5. Configure a period for the device to delay route calculation when the device receives a purge LSP.
   
   
   ```
   [timer purge-zero-lsp route-calculate-delay](cmdqueryname=timer+purge-zero-lsp+route-calculate-delay) delay-interval
   ```
   
   By default, if a device receives a purge LSP, it delays route calculation for 10s.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```