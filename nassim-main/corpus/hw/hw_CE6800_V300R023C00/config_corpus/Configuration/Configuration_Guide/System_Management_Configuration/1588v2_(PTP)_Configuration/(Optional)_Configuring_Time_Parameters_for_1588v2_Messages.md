(Optional) Configuring Time Parameters for 1588v2 Messages
==========================================================

(Optional) Configuring Time Parameters for 1588v2 Messages

#### Context

1588v2 devices exchange Announce, Sync, and Delay\_Req messages to transmit time information and maintain 1588v2 connections. You can configure the intervals at which a 1588v2 interface sends Announce, Sync, and Delay\_Req messages, as well as the maximum number of allowed timeouts for Announce messages on a 1588v2 interface. However, you are recommended to use the default values in normal cases.

If the interval for sending 1588v2 messages is set to a small value, 1588v2 devices frequently exchange such messages, consuming a significant number of bandwidth resources. If the interval for sending 1588v2 messages is set to a large value, the time synchronization precision cannot be guaranteed. If the requirements for time synchronization precision are met, set the interval for sending 1588v2 messages to as large a value as possible.

Perform the following steps on each 1588v2 device:


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   interface interface-type interface-number
   ```
3. Set time parameters for 1588v2 messages as required.
   
   
   
   **Table 1** Time parameters for 1588v2 messages
   | Operation | Command | Description |
   | --- | --- | --- |
   | Set the interval at which a 1588v2 interface sends Announce messages to 2n x 1/1024s, where n equals to the value of *announce-interval*. | [**ptp announce-interval**](cmdqueryname=ptp+announce-interval) *announce-interval* | By default, the value of *announce-interval* is 7. That is, the interval for sending Announce messages on a 1588v2 interface is 128/1024s.  Timeout interval for receiving Announce messages on the peer interface = Number of timeouts for receiving Announce messages on the peer interface (*receipt-timeout*) x Interval for sending Announce messages on the local interface (*announce-interval*) |
   | Set the maximum number of timeouts for receiving Announce messages on a 1588v2 interface. | [**ptp announce receipt-timeout**](cmdqueryname=ptp+announce+receipt-timeout) *receipt-timeout* | The default value is 3.  Timeout interval for receiving Announce messages on the local interface = Number of timeouts for receiving Announce messages on the local interface (*receipt-timeout*) x Interval for sending Announce messages on the peer interface (*announce-interval*) |
   | Set the interval at which a 1588v2 interface sends Sync messages to 2n x 1/1024s, where n equals to the value of *sync-interval*. | [**ptp sync-interval**](cmdqueryname=ptp+sync-interval) *sync-interval* | By default, the value of *sync-interval* is 3. That is, the interval for sending Sync messages on a 1588v2 interface is 8/1024s. |
   | Set the interval at which a 1588v2 interface sends Delay\_Req messages to 2n x 1/1024s, where n equals to the value of *min-delayreq-interval*. | [**ptp min-delayreq-interval**](cmdqueryname=ptp+min-delayreq-interval) *min-delayreq-interval* | By default, the value of *min-delayreq-interval* is 7. That is, the interval for sending Delay\_Req messages on a 1588v2 interface is 128/1024s. |
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```