(Optional) Enabling the Log Function for DHCP Message Exchange
==============================================================

(Optional) Enabling the Log Function for DHCP Message Exchange

#### Context

In scenarios such as intelligent O&M, after the log function for DHCP message exchange is enabled, the network analyzer uses this function to intelligently analyze why users fail to obtain IP addresses.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the log function for DHCP message exchange.
   
   
   ```
   [dhcp snooping packet-flow log enable](cmdqueryname=dhcp+snooping+packet-flow+log+enable)
   ```
   
   By default, the log function for DHCP message exchange is disabled.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```