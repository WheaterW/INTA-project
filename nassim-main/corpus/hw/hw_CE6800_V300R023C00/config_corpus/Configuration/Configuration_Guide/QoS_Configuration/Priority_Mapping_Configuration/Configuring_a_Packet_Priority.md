Configuring a Packet Priority
=============================

Configuring a Packet Priority

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the 802.1p value of packets.
   
   
   ```
   [set priority 8021p](cmdqueryname=set+priority+8021p) 8021p-value
   ```
   
   
   
   By default, the 802.1p value is not configured for packets.
3. Configure the DSCP value of packets.
   
   
   ```
   [set priority dscp](cmdqueryname=set+priority+dscp) dscp-value
   ```
   
   
   
   By default, the DSCP value is not configured for packets.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```