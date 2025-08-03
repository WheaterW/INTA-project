Configuring ARP Interface Backup
================================

Configuring ARP Interface Backup

#### Context

In an M-LAG scenario, the ARP connection between the active firewall and a device may be faulty or the firewall itself may fail. To ensure network stability, the ARP connection needs to be switched from the active firewall to the standby firewall. In this case, you can configure the two interfaces of the active and standby firewalls to back up each other, implementing a fast and stable ARP connection switchover.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure Eth-Trunk interface 1.
   
   
   ```
   interface Eth-Trunk 1
   ```
3. Configure Eth-Trunk interface 2.
   
   
   ```
   interface Eth-Trunk 2
   ```
4. Configure the two interfaces to back up each other.
   
   
   ```
   [ip forward backup-group](cmdqueryname=ip+forward+backup-group) backup-group-name member { ifname1 | iftype1 ifnumber1 } { ifname2 | iftype2 ifnumber2 }
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   * Currently, only Layer 2 Eth-Trunk main interfaces are supported.
   * Two identical interfaces cannot be configured in the same backup group.
   * An interface that has been configured in one backup group cannot be configured in another backup group
   * An interface in a configured backup group can be modified, but it cannot be replaced with an interface configured in another backup group.
   * An Eth-Trunk main interface that has been configured in a backup group cannot be deleted. The backup group must be deleted before the interface can be deleted.
   * An Eth-Trunk main interface that has been configured in a backup group cannot be configured as a Layer 3 interface. The backup group must be deleted before the interface can be configured as a Layer 3 interface.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```