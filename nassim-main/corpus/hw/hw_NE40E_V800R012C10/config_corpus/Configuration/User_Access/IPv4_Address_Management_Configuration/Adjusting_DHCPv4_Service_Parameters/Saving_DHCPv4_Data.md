Saving DHCPv4 Data
==================

After the DHCPv4 data of the NE40E that functions as a DHCPv4 server is saved to a storage
device, the data can be restored from the storage device when the NE40E fails.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcp server database**](cmdqueryname=dhcp+server+database) **enable**
   
   
   
   Saving DHCPv4 data to a storage device is enabled.
3. (Optional) Run [**dhcp server database**](cmdqueryname=dhcp+server+database) **write-delay** *interval*
   
   
   
   The delay for saving the data is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

The NE40E can save the current DHCPv4 data to a storage device and
restore the data from the storage device when the NE40E fails.

DHCPv4 data is saved with a fixed file name
on the storage device. Normally, the IP leasing information is saved
in the **lease.txt** file and the address conflict information
is saved in the **conflict.txt** file. Back up these two files
to other directories because information in these files is replaced
regularly.