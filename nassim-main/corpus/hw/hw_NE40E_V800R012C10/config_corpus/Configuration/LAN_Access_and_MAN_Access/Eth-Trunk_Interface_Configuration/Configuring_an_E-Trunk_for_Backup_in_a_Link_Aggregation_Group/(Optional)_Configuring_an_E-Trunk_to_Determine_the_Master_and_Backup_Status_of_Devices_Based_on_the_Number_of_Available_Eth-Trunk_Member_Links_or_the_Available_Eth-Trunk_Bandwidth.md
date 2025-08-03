(Optional) Configuring an E-Trunk to Determine the Master/Backup Status of Devices Based on the Number of Available Eth-Trunk Member Links or the Available Eth-Trunk Bandwidth
===============================================================================================================================================================================

When devices added to an E-Trunk greatly differ in their available Eth-Trunk member links, to maximize link bandwidth utilization, you can configure the E-Trunk to determine the master/backup status of the devices based on the number of available Eth-Trunk member links. You can also configure the E-Trunk to determine the master/backup status of the devices based on the available Eth-Trunk bandwidth.

#### Prerequisites

* The Eth-Trunk interfaces added to the E-Trunk have been configured to work in static LACP mode using the [**mode lacp-static**](cmdqueryname=mode+lacp-static) command in the Eth-Trunk interface view.
* The Eth-Trunk interfaces added to the E-Trunk have been configured to work in automatic mode using the [**e-trunk mode auto**](cmdqueryname=e-trunk+mode+auto) command in the Eth-Trunk interface view.

#### Context

When E-Trunk member interfaces work in automatic mode, the E-Trunk determines the master/backup status of devices based on their E-Trunk priorities. If the E-Trunk priorities are the same, the E-Trunk determines the master/backup status of devices based on their system IDs. When devices added to an E-Trunk greatly differ in their available Eth-Trunk member links, to maximize link bandwidth utilization, you can configure the E-Trunk to determine the master/backup status of the devices based on the number of available Eth-Trunk member links. The device with a larger number of available Eth-Trunk member links is determined as the master, and the other device is then determined as the backup. You can also configure the E-Trunk to determine the master/backup status of the devices based on the available Eth-Trunk bandwidth. The device with a higher available Eth-Trunk bandwidth is determined as the master, and the other device is then determined as the backup.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
   
   
   
   The E-Trunk view is displayed.
3. Run [**e-trunk select**](cmdqueryname=e-trunk+select) { **link-number** | **bandwidth** }
   
   
   
   The E-Trunk is configured to determine master/backup status based on the number of available links or available bandwidth on Eth-Trunk interfaces.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.