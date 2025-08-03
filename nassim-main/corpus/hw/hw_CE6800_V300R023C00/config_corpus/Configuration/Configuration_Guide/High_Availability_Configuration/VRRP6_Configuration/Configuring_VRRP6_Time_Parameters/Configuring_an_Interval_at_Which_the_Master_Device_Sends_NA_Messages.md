Configuring an Interval at Which the Master Device Sends NA Messages
====================================================================

Configuring an Interval at Which the Master Device Sends NA Messages

#### Context

To ensure that both the destination MAC address and the outbound interface on a downstream device connected to the master device in a VRRP6 group are quickly updated, the master device sends NA messages at a specified interval.


#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an interval at which the master device sends NA messages.
   ```
   [vrrp6 na interval interval](cmdqueryname=vrrp6+na+interval+interval)
   ```
   
   By default, the master device sends an NA message every 120s (2 minutes). After this interval is configured on the master device, it will send NA messages according to the new value.
3. (Optional) Disable the master device from sending NA messages at intervals.
   ```
   [vrrp6 na interval disable](cmdqueryname=vrrp6+na+interval+disable)
   ```
   
   After this command is run, the master device no longer periodically sends NA messages, and will only do so during a master/backup VRRP switchover.
4. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp6**](cmdqueryname=display+vrrp6) { **interface** *interface-type* *interface-number* [ *virtual-router-id* ] | *virtual-router-id* } **verbose** command to check detailed VRRP6 group information.