Configuring an Interval at Which the Master Device Sends Gratuitous ARP Packets
===============================================================================

Configuring an Interval at Which the Master Device Sends Gratuitous ARP Packets

#### Context

To ensure that both the destination MAC address and the outbound interface on a downstream device connected to the master device in a VRRP group are quickly updated, the master device sends gratuitous ARP packets at a specified interval. You can adjust this interval as required.


#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an interval at which the master device sends gratuitous ARP packets.
   ```
   [vrrp gratuitous-arp interval](cmdqueryname=vrrp+gratuitous-arp+interval) interval
   ```
   
   By default, the master device sends a gratuitous ARP packet every 120s (2 minutes). After this interval is configured on the master device, it will send gratuitous ARP packets according to the new value.
3. (Optional) Disable the master device from sending gratuitous ARP packets at intervals.
   ```
   [vrrp gratuitous-arp interval disable](cmdqueryname=vrrp+gratuitous-arp+interval+disable)
   ```
   
   After this command is run, the master device no longer periodically sends gratuitous ARP packets, and will only do so during a master/backup VRRP switchover.
4. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp**](cmdqueryname=display+vrrp) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-router-id* ] [ **verbose** ] command to check the VRRP group status.