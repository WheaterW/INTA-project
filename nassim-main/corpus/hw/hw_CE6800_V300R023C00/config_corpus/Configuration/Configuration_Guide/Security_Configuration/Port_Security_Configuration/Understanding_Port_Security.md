Understanding Port Security
===========================

Understanding Port Security

#### Classification of Secure MAC Addresses

**Table 1** Classification of secure MAC addresses
| Type | Description | Characteristic | Scenario |
| --- | --- | --- | --- |
| Dynamic secure MAC address | When port security is enabled on an interface, dynamic MAC address entries that have been learned by the interface are deleted, and MAC address entries learned subsequently are converted into dynamic secure MAC address entries. | After the device restarts or the interface goes down, the entries are lost and need to be relearned.  Dynamic secure MAC addresses do not age by default. They age only when the set aging time is reached.  The number of MAC addresses can be limited.  Protection actions can be configured for the interface, including: discarding the packets, reporting alarms, or shutting down the interface. | If users frequently change their access locations, you can configure the dynamic secure MAC address function on the user-side interface of the device. This function ensures security and deletes bound MAC address entries immediately when they age. |
| Sticky MAC address | When the sticky MAC address function is enabled following port security, the dynamic MAC address entries that have been converted into dynamic secure MAC address entries will be converted into sticky MAC address entries, and the newly learned dynamic MAC address entries will be directly converted into sticky MAC address entries. | The entries are not lost after the device restarts or the interface goes down.  Sticky MAC address entries will not age.  The number of MAC addresses can be limited.  Protection actions can be configured for the interface, including: discarding the packets, reporting alarms, or shutting down the interface. | If users seldom change access locations, you can configure the sticky MAC address function on the user-side interface of the device. This function ensures security without losing bound MAC address entries. |


![](public_sys-resources/note_3.0-en-us.png) 

After the sticky MAC address function is disabled on an interface, sticky MAC address entries on the interface are converted into dynamic secure MAC address entries. After port security is disabled on an interface, existing dynamic secure MAC address entries on the interface are deleted. The interface then learns dynamic MAC address entries again.



#### Aging of Secure MAC Addresses

Only dynamic secure MAC addresses will age when the set aging time is reached.

* Absolute aging time: If the absolute aging time is 5 minutes, the system checks whether there is traffic from the MAC address every 5 minutes. If not, the dynamic secure MAC address is aged out immediately.
* Relative aging time: If the relative aging time is 5 minutes, the system checks whether there is traffic from the MAC address every 1 minute. If not, the dynamic secure MAC address is aged out 5 minutes later.
* Forcible aging time: The system calculates the lifetime of each MAC address once every minute. For example, if the forcible aging time is set to 5 minutes and the lifetime of a dynamic secure MAC address is greater than or equal to 5 minutes, this MAC address ages out immediately.

#### Port Security Protection Actions

After port security is enabled on an interface, if the interface receives packets sourced from a MAC address not existing in the MAC address table, the device considers that the packets are sent from an unauthorized user, regardless of whether the destination MAC address of packets exists, and takes the protection actions.

**Table 2** Port security protection actions
| Action | Description |
| --- | --- |
| restrict | Discards invalid packets and reports an alarm. This action is recommended. |
| protect | Discards invalid packets without reporting an alarm. |
| error-down | Discards invalid packets, sets the interface status to error-down, and reports an alarm.  By default, an interface in error-down state can be restored only after the [**restart**](cmdqueryname=restart) command is run in the interface view.  To enable an interface in error-down state to automatically go up after a period of time, run the [**error-down auto-recovery**](cmdqueryname=error-down+auto-recovery) **cause** **portsec-reachedlimit** **interval** *interval-value* command in the system view before the interface status becomes error-down. In this command, *interval-value* specifies the period of time after which an interface can automatically go up. |