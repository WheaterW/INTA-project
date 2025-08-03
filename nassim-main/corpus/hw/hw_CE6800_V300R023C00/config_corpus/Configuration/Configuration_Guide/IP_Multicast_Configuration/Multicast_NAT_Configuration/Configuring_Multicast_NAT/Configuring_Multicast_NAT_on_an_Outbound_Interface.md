Configuring Multicast NAT on an Outbound Interface
==================================================

Configuring Multicast NAT on an Outbound Interface

#### Context

This section describes how to configure multicast NAT on an outbound interface of multicast streams and specify a source IP address, destination IP address, source UDP port number, and destination UDP port number for post-translation multicast streams.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the outbound interface of multicast streams.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Specify the source IP address, destination IP address, source UDP port number, and destination UDP port number for post-translation multicast streams.
   
   
   ```
   [multicast-nat outbound](cmdqueryname=multicast-nat+outbound) id outbound-id [ name outbound-name ] [ src-ip source-address ] [ dst-ip destination-address ] [ src-udp-port source-port ] [ dst-udp-port port ]
   ```
5. Exit the interface view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```