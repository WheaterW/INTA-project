Configuring a Blackhole MAC Address Entry
=========================================

Configuring a Blackhole MAC Address Entry

#### Context

Blackhole MAC address entries can be used to filter out invalid MAC addresses. To prevent a MAC address from being used to attack a user device or network, configure the MAC address of an untrusted user as a blackhole MAC address. After a device receives packets with a destination or source blackhole MAC address, the device directly discards these packets if the VLAN information carried in these packets matches that specified in a blackhole MAC address entry.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a blackhole MAC address entry.
   
   
   * Configure a blackhole MAC address entry with a VLAN specified.
     ```
     [mac-address blackhole](cmdqueryname=mac-address+blackhole) mac-address vlan vlan-id
     ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display mac-address blackhole**](cmdqueryname=display+mac-address+blackhole) [ **vlan** *vlan-id* ] [ **verbose** ] command to check configured blackhole MAC address entries.