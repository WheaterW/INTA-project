Configuring Delayed Resending of MAC-Withdraw Messages
======================================================

This section describes how to configure delayed resending of MAC-Withdraw messages. This configuration allows a device to resend a MAC-Withdraw message to the peer PE after a specified delay if the VRRP status changes to backup.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172370157__en-us_cliref_0172382168_fig_dc_vrp_vpls_cfg_500305), the CE is dual-homed to PE1 and PE2. VRRP runs between the PEs, with PE1 functioning as the master device and PE2 the backup device. If the link between the CE and PE1 fails, a master/backup VRRP switchover is performed. PE1 then switches to the backup state, and PE2 transits to the master state. After the link between the CE and PE1 recovers, a master/backup VRRP switchback is performed if the VRRP group works in preemption mode. Then, PE1 returns to the master state, and PE2 to the backup state.**Figure 1** VPLS dual-homing networking  
![](figure/en-us_image_0000001229985187.png)  

Take a master/backup VRRP switchback as an example. When PE2 changes from the master state to the backup state, the PE2 interface connecting to PE3 goes down and sends a MAC Withdraw message to PE3 to clear the corresponding MAC address entries on PE3. Normally, PE3 no longer receives packets forwarded by PE2. Instead, PE3 receives only upstream packets forwarded by the master device PE1, and records the mapping between the CE's MAC address and PW1. However, during the switchback, the interface's forwarding status table on PE2 is updated slowly. As a result, PE2 still sends a few packets to PE3 after the switchback. Upon receipt, PE3 records the mapping between the CE's MAC address and PW2 again. In this case, PE3 incorrectly sends the downstream packets destined for the CE to PE2 through PW2. As a result, packets are lost, and packet forwarding can recover only after the local MAC address entry ages.

To solve this problem, configure delayed resending on PE1 and PE2. After the VRRP status changes to backup and then the specified resending delay elapses, PE2 resends a MAC Withdraw message to PE3 to clear the corresponding MAC address entries on PE3. This ensures that PE3 learns the correct mapping between the CE MAC address and the PW and sends downstream packets to the master device to prevent packet loss.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
   
   
   
   The VSI view is displayed.
3. Run [**vrrp-backup mac-withdraw**](cmdqueryname=vrrp-backup+mac-withdraw) **retry-interval** *retry-interval-time*
   
   
   
   Delayed resending of MAC-Withdraw messages is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.