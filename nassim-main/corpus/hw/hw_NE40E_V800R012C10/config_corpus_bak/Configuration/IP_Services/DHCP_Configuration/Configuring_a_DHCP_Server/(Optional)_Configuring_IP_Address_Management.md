(Optional) Configuring IP Address Management
============================================

IP address management includes backing up and restoring data in an address pool, configuring alarm thresholds, and reclaiming IP addresses.

#### Prerequisites

DHCP server packet receiving has been enabled using the [**dhcp server enable**](cmdqueryname=dhcp+server+enable) command on an interface if the interface needs to be used as a DHCP server.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* If multiple interfaces need to be used as DHCP servers, for security purposes, you are advised to preferentially run the [**dhcp server enable**](cmdqueryname=dhcp+server+enable) command on the interfaces to enable DHCP server packet receiving. If high security is not required, you run the [**dhcp server request-packet all-interface enable**](cmdqueryname=dhcp+server+request-packet+all-interface+enable) command in the system view to enable DHCP server packet receiving for all interfaces.
* If DHCP server packet receiving is not enabled, a DHCP server does not process DHCP request messages.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure DHCP data saving and restoration.
   1. Run [**dhcp server database**](cmdqueryname=dhcp+server+database) **enable**
      
      
      
      The system is enabled to save IP addresses assigned from a DHCP address pool to a CF card.
      
      
      
      After this command is run, the system generates and saves the **lease.txt** and **conflict.txt** files in the DHCP folder on a CF card. The **lease.txt** and **conflict.txt** files store address lease and conflict information, respectively. After one-to-many mapping between one MAC address and many sessions is enabled on a device, the device generates an option82\_index.data file to save Option 82 information.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      To configure an integrity authentication mode for the **lease.txt** and **conflict.txt** files, run the [**dhcp server database authentication-mode**](cmdqueryname=dhcp+server+database+authentication-mode) command. This prevents the files from being tampered with. After this command is run, an encrypted file integrity authentication code is added to the files. After the device restarts, the system decrypts this code and uses it to verify the file integrity before restoring the address lease and conflict information from the **lease.txt** and **conflict.txt** files. If the verification is successful, the data is restored; otherwise, it is discarded and a **DHCP\_FILE\_RECOVER\_FAIL** log is recorded.
   2. Run [**dhcp server database**](cmdqueryname=dhcp+server+database) **write-delay** *interval*
      
      
      
      The interval at which DHCP global address pool data is automatically saved is set.
   3. Run [**dhcp server database**](cmdqueryname=dhcp+server+database) **recover**
      
      
      
      The DHCP server is enabled to restore DHCP global address pool data from the CF card.
      
      
      
      After this function is enabled, the DHCP server restores DHCP global address pool data from the CF card after system restart.
3. Configure the address resource alarm function.
   1. Run [**ip pool**](cmdqueryname=ip+pool) *ip-pool-name* [ **server** ]
      
      
      
      The address pool view is displayed.
   2. Run [**warning-threshold**](cmdqueryname=warning-threshold) *threshold-value*
      
      
      
      The alarm threshold for the address usage of the address pool is specified.
      
      
      
      If the address usage exceeds a specified threshold, an alarm will be generated. If the address usage falls below 90% of the alarm threshold, this alarm will be cleared.
   3. Run [**warning-exhaust**](cmdqueryname=warning-exhaust)
      
      
      
      The address exhaustion alarm function is enabled for the address pool.
      
      
      
      When the address pool is exhausted, an alarm will be generated. When the address usage of the address pool falls below 90% of the threshold, this alarm will be cleared.
4. Configure the IP address reclaiming function.
   1. Run [**recycle**](cmdqueryname=recycle) *start-ip-address* [ *end-ip-address* ]
      
      
      
      The IP address status is configured as idle.
      
      
      
      When an IP address is being used by an offline client, the IP address can be reclaimed, preventing IP address waste.
   2. Run [**conflict auto-recycle**](cmdqueryname=conflict+auto-recycle) **interval** *interval-time*
      
      
      
      The interval at which conflicting addresses are automatically reclaimed is set.
      
      
      
      If conflicting addresses exist in an address pool, the DHCP server supports automatic IP address reclaiming by default. You can configure an IP address reclaiming interval as follows:
      * If the *interval-time* value is not 0 and the usage of IP addresses in the address pool exceeds the alarm threshold specified in the [**warning-threshold**](cmdqueryname=warning-threshold) command, the server automatically reclaims some conflicting IP addresses and re-assigns them to users when the address conflict time exceeds the *interval-time* value.
      * If the *interval-time* value is set to 0, the automatic address reclaim function is disabled, and conflicting addresses will not be assigned to users. In this case, you need to run the [**reset conflict-ip-address**](cmdqueryname=reset+conflict-ip-address) command to reclaim conflicting addresses.
5. Run [**lock**](cmdqueryname=lock)
   
   
   
   The address pool is locked.
   
   
   
   If you want to delete an address pool that is currently in use, you can run this command to lock the address pool and then delete the address pool after all the users using this address pool go offline.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.