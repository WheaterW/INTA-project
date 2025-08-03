Configuring a Device to Discard ICMP Messages Carrying Route Options
====================================================================

Configuring a Device to Discard ICMP Messages Carrying Route Options

#### Prerequisites

Before configuring a device to discard ICMP messages carrying route options, configure link layer protocol parameters for interfaces to ensure that the link layer protocol status of the interfaces is up.


#### Context

When a device receives a large number of ICMP messages carrying route options, network loads increase and device performance deteriorates. To address this issue, configure the device to discard ICMP messages carrying route options. This improves network performance and security.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the device to discard ICMP messages carrying route options.
   
   
   ```
   [icmp with-options drop](cmdqueryname=icmp+with-options+drop+all+slot) { all | slot slot-id }
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```