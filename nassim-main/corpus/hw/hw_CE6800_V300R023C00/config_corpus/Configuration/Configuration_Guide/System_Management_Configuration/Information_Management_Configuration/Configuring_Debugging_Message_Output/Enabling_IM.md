Enabling IM
===========

Enabling IM

#### Context

The device outputs logs, traps, and debugging messages to the log host and console only after IM is enabled. By default, the IM function is enabled.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the IM function.
   
   
   ```
   [info-center enable](cmdqueryname=info-center+enable)
   ```
3. (Optional) Configure the name of the information channel with a specified number.
   
   
   ```
   [info-center channel](cmdqueryname=info-center+channel) channel-number [name](cmdqueryname=name) channel-name
   ```
   
   By default, the names of channels 0 to 9 are as follows:
   
   * Channel 0: console
   * Channel 1: monitor
   * Channel 2: loghost
   * Channel 3: trapbuffer
   * Channel 4: logbuffer
   * Channel 5: snmpagent
   * Channel 6: channel6
   * Channel 7: channel7
   * Channel 8: channel8
   * Channel 9: channel9
4. (Optional) Set the output priority for IM packets.
   
   
   ```
   [info-center syslog packet-priority](cmdqueryname=info-center+syslog+packet-priority) priority-level
   ```
   
   By default, the output priority of IM packets is 0.
5. (Optional) Set the timestamp format of debugging messages.
   
   
   ```
   [info-center timestamp](cmdqueryname=info-center+timestamp) debugging { boot | { date | short-date | format-date | rfc-3339 } [ precision-time { tenth-second | millisecond | second } ] } [ without-timezone ]
   ```
   
   By default, the date format is used as the timestamp format for output debugging messages.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```