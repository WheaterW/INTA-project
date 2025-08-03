Disabling an Interface from Receiving NTP Packets
=================================================

Disabling an Interface from Receiving NTP Packets

#### Context

If a host on a LAN does not need to synchronize its clock with a specified server, you can disable a specified interface from receiving NTP packets.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. (Optional) Disable an interface from receiving NTP packets.
   
   
   * Disable an interface from receiving IPv4 NTP packets.
     ```
     [ntp receive disable](cmdqueryname=ntp+receive+disable)
     ```
   * Disable an interface from receiving IPv6 NTP packets.
     ```
     [ntp ipv6 receive disable](cmdqueryname=ntp+ipv6+receive+disable)
     ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```