Configuring a Reassembly Timeout Period for IPv6 Fragments
==========================================================

Configuring a Reassembly Timeout Period for IPv6 Fragments

#### Context

To improve device performance and prevent attacks, configure a proper reassembly timeout period for IPv6 fragments to ensure IPv6 fragments that have undergone a long reassembly wait are promptly aged.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a reassembly timeout period for IPv6 fragments.
   
   
   ```
   [ipv6 reassembling timeout](cmdqueryname=ipv6+reassembling+timeout) interval
   ```
   
   If a long reassembly timeout period is configured, a large number of IPv6 fragments are stored on the device, waiting to be reassembled. This consumes resources, reduces device performance, and may cause network attacks. Therefore, a long reassembly timeout period is not recommended.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```