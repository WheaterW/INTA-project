Configuring Traffic Suppression in a BD
=======================================

Configuring Traffic Suppression in a BD

#### Context

To rate-limit incoming broadcast packets, unknown multicast packets, or unknown unicast packets in a BD so as to prevent broadcast storms, you can configure traffic suppression for the corresponding type of packets in the BD. Once the rate reaches the configured threshold, the device will then discard excess packets. Traffic suppression in a BD is supported only by the CE8851-32CQ8DQ-P, CE8850-HAM, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6881H, CE6881H-K, CE8851K, CE6860-SAN, CE8850-SAN, CE6866K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE8855, CE8851-32CQ4BQ, CE6885-SAN, and CE6855-48XS8CQ.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
3. Configure traffic suppression in a BD.
   
   
   ```
   [storm suppression](cmdqueryname=storm+suppression) { broadcast | multicast | unknown-unicast } cir cir-value [ gbps | kbps | mbps ] [ cbs cbs-value [ bytes | kbytes | mbytes ] ]
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```