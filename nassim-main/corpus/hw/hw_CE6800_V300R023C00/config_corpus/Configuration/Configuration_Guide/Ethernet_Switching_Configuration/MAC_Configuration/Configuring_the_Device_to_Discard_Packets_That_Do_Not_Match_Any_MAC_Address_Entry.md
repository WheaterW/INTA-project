Configuring the Device to Discard Packets That Do Not Match Any MAC Address Entry
=================================================================================

Configuring the Device to Discard Packets That Do Not Match Any MAC Address Entry

#### Context

When a DHCP user goes offline, the MAC address entry of the user is aged out. If there are packets destined for this user, the device cannot find a matching MAC address entry and instead broadcasts the packets to all interfaces in the VLAN from which packets are originated. In this scenario, as all users in the VLAN will receive these packets, possible security risks are introduced. To reduce the load on the device and enhance security, configure the device to discard packets that do not match any MAC address entry.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Configure the device to discard packets that do not match any MAC address entry.
   
   
   ```
   [mac-address miss action discard](cmdqueryname=mac-address+miss+action+discard)
   ```
   
   By default, a device broadcasts packets that do not match any MAC address entry in the VLAN to which it belongs.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```