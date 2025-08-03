Restoring DHCPv4 Data
=====================

DHCPv4 data restoration allows the NE40E that functions as a DHCPv4 server capable of saving DHCPv4
data to a storage device to restore saved information
about address leases and address conflicts.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcp server database**](cmdqueryname=dhcp+server+database) **recover**
   
   
   
   DHCPv4 data is restored from the storage device.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.