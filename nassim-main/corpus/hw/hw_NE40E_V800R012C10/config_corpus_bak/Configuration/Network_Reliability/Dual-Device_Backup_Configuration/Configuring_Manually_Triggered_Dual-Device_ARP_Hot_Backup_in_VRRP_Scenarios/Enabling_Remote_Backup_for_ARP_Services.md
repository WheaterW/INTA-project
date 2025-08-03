Enabling Remote Backup for ARP Services
=======================================

This section describes how to enable remote backup for Address Resolution Protocol (ARP) services.

#### Context

Dual-device ARP hot backup prevents downlink traffic from being interrupted because the backup device does not learn ARP entries from a device on the user side during a master/backup VRRP switchover, which improves network reliability. After you establish a dual-device backup platform, enable remote backup for ARP services to ensure that ARP entries and host routing information are the same on the master and backup devices.

Perform the following steps on both the master and backup devices:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
   
   
   
   An RBP is created, and the RBP view is displayed.
3. Run [**service-type arp**](cmdqueryname=service-type+arp)
   
   
   
   Remote backup is enabled for ARP services.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

Perform the following steps to bind the RBP to a specified interface or sub-interface so that remote backup can take effect for ARP services:

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [.*subinterface-number* ] command to enter the interface or sub-interface view.
3. Run the [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name* command to bind the RBP to the interface or sub-interface.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.