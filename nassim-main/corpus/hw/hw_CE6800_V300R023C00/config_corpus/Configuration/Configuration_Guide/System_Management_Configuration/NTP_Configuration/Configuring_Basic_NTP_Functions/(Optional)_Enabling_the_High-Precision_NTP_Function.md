(Optional) Enabling the High-Precision NTP Function
===================================================

(Optional) Enabling the High-Precision NTP Function

#### Context

For a network that requires high time precision, you can enable the high-precision NTP function, which filters network noise to improve clock precision.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the high-precision NTP function.
   
   
   * Specify the interval at which a high-precision NTP client sends packets.
     ```
     [ntp high-precision-time client enable poll-interval](cmdqueryname=ntp+high-precision-time+client+enable+poll-interval) [ poll-interval-time ]
     ```
     
     By default, the interval at which a high-precision NTP client sends packets is not set.
   * Enable the high-precision NTP server function.
     ```
     [ntp high-precision-time server enable](cmdqueryname=ntp+high-precision-time+server+enable)
     ```
     
     By default, the high-precision NTP server function is disabled.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```