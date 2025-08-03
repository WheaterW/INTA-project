Configuring High-Precision NTP
==============================

For a network that requires high time precision, you can enable the high-precision NTP function, which filters network noise to improve clock precision.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure the high-precision NTP function.
   * To specify the interval at which packets are sent by the high-precision NTP client, run the **[**ntp-service high-precision-time client enable poll-interval**](cmdqueryname=ntp-service+high-precision-time+client+enable+poll-interval)** [ *poll-interval-time* ] command.
   * To enable the high-precision NTP server function, run the **[**ntp-service high-precision-time server enable**](cmdqueryname=ntp-service+high-precision-time+server+enable)** command.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.