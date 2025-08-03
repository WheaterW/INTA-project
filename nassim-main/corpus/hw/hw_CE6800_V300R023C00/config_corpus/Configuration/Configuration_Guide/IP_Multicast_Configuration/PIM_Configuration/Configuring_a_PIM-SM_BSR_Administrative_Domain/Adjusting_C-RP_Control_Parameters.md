Adjusting C-RP Control Parameters
=================================

Adjusting C-RP Control Parameters

#### Context

C-RPs periodically send Advertisement messages to the BSR. The messages carry information including the C-RP priority. You can adjust the C-RP priority, interval for sending Advertisement messages, and holdtime of Advertisement messages on a C-RP.

The following rules are used to elect an RP from multiple C-RPs:

* The C-RP with the highest priority wins.
* In the case of the same priority, hash functions are executed. The candidate with the greatest result value wins.
* If all the preceding factors are the same, the C-RP with the highest address wins.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the PIM view.
   
   
   ```
   [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ]
   ```
3. Configure a global C-RP priority.
   
   
   ```
   [c-rp priority](cmdqueryname=c-rp+priority) priority
   ```
   
   
   
   A larger value indicates a lower priority. By default, the global C-RP priority is 0.
4. Configure an interval for the C-RP to send Advertisement messages.
   
   
   ```
   [c-rp advertisement-interval](cmdqueryname=c-rp+advertisement-interval) interval
   ```
   
   
   
   By default, a C-RP sends Advertisement messages at an interval of 60 seconds.
5. Configure the holdtime of Advertisement messages for the BSR to retain the Advertisement messages received from the C-RP.
   
   
   ```
   [c-rp holdtime](cmdqueryname=c-rp+holdtime) interval
   ```
   
   The period during which the BSR retains the Advertisement messages received from the C-RP must be longer than the interval at which the C-RP sends Advertisement messages.
   
   
   
   C-RPs periodically send Advertisement messages to the BSR, which extracts the holdtime from the messages and starts a timer. If the BSR does not receive any Advertisement message from the C-RP within the holdtime period, the BSR considers the C-RP invalid or unreachable.
   
   By default, the BSR retains the Advertisement messages received from a C-RP for 150 seconds.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```