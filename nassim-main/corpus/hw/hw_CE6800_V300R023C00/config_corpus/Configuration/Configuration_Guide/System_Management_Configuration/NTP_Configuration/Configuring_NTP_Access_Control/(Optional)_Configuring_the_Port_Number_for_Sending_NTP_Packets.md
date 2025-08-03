(Optional) Configuring the Port Number for Sending NTP Packets
==============================================================

(Optional) Configuring the Port Number for Sending NTP Packets

#### Context

You can set a fixed port that sends NTP packets. In this way, the user firewall can filter packets based on the port, improving the security of network packets.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Specify the number of the port that sends NTP packets.
   
   
   ```
   [ntp source-port](cmdqueryname=ntp+source-port) portNum
   ```
   
   By default, the port number for sending NTP packets is randomly allocated.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```