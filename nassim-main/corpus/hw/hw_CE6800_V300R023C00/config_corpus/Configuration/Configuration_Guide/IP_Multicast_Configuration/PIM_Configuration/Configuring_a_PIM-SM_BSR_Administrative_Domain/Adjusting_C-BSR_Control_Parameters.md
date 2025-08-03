Adjusting C-BSR Control Parameters
==================================

Adjusting C-BSR Control Parameters

#### Context

Initially, each C-BSR considers itself as the BSR and sends Bootstrap messages to all other devices on the network. You can adjust the C-BSR hash mask length carried by a Bootstrap message, C-RP priority, interval for sending Bootstrap messages, and the holdtime of Bootstrap messages on a device with a C-BSR configured.

The following rules are used to elect a BSR from multiple C-BSRs:

* The C-BSR that has the highest priority wins.
* If C-BSRs have the same priority, the one with the highest address wins.

Based on the BSR election result, a C-BSR performs the following operations:

* If it wins the election, it periodically sends Bootstrap messages to devices on the network. The Bootstrap messages carry its IP address and the RP-Set information.
* If it fails in the election, it is suppressed from sending Bootstrap messages.
* When the current BSR fails, C-BSRs automatically trigger a new round of BSR election to prevent service interruptions.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the PIM view.
   
   
   ```
   [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ]
   ```
3. Configure a global C-BSR hash mask length.
   
   
   ```
   [c-bsr hash-length](cmdqueryname=c-bsr+hash-length) hash-length
   ```
   
   
   
   The hash mask length carried by each Bootstrap message is used for RP calculation.
   
   By default, the global C-BSR hash mask length is 30.
4. Configure a global C-BSR priority.
   
   
   ```
   [c-bsr priority](cmdqueryname=c-bsr+priority) priority
   ```
   
   
   
   A larger priority value indicates a higher priority.
   
   By default, the global C-BSR priority is 0.
5. Configure an interval at which the C-BSR sends Bootstrap messages.
   
   
   ```
   [c-bsr interval](cmdqueryname=c-bsr+interval) interval
   ```
   
   
   
   By default, the interval at which the C-BSR sends Bootstrap messages is 60 seconds.
6. Set the holdtime of Bootstrap messages received from the BSR.
   
   
   ```
   [c-bsr holdtime](cmdqueryname=c-bsr+holdtime) interval
   ```
   
   
   
   The period during which a C-BSR retains the Bootstrap message received from the BSR must be longer than the interval at which the C-BSR sends Bootstrap messages. Otherwise, BSR election is frequently performed.
   
   The BSR periodically sends Bootstrap messages to other devices on the network. After receiving the Bootstrap messages, these devices retain them for a specified period, during which the BSR election is suspended. After this period expires, the C-BSRs trigger a new round of BSR election.
   
   By default, the holdtime of Bootstrap messages received from the BSR is 130 seconds.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```