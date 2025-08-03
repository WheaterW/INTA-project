Configuring an Eth-Trunk Interface to Work in Manual 1:1 Master/Backup Mode
===========================================================================

If intermediate devices exist between the devices at both ends of an Eth-Trunk link, configure Eth-Trunk interfaces in manual 1:1 master/backup mode on the devices at both ends, add two interfaces to each Eth-Trunk interface, and specify the master interface.

#### Usage Scenario

As more network services are deployed, high service reliability is required. If intermediate devices exist between the devices at both ends of an Eth-Trunk link, configure Eth-Trunk interfaces in manual 1:1 master/backup mode on the devices at both ends to provide 1:1 link backup.

On the network shown in [Figure 1](#EN-US_TASK_0172362877__fig_dc_vrp_ethtrunk_cfg_004901), an Eth-Trunk interface in manual 1:1 master/backup mode is configured on each of the two endpoint devices to provide 1:1 link backup for data transmission.**Figure 1** Eth-Trunk interfaces in manual 1:1 master/backup mode  
![](images/fig_dc_vrp_ethtrunk_cfg_004901.png)
#### Pre-configuration Tasks

Before configuring an Eth-Trunk interface in manual 1:1 master/backup mode, connect interfaces and set their physical parameters to ensure that the physical interface status is up.



[Creating an Eth-Trunk Interface in Manual 1:1 Master/Backup Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0022.html)

Before bundling physical interfaces into an Eth-Trunk interface, create this Eth-Trunk interface.

[Adding Interfaces to an Eth-Trunk Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0023.html)

An Eth-Trunk interface in manual 1:1 master/backup mode can contain only two member interfaces.

[(Optional) Specifying the Master Member Interface in an Eth-Trunk Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0024.html)

By default, the member interface that is first added to the Eth-Trunk interface and the interface status is up in manual 1:1 master/backup mode will automatically become the master one. To ensure a reliable communication, specifying a master interface is recommended.

[Enabling an Eth-Trunk Interface to Send Flush Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0025.html)

If an Eth-Trunk interface is enabled to send Flush packets, after the master and backup interfaces are switched, the new master interface sends Flush packets to instruct the peer end to age MAC addresses. This function prevents data interruption caused by asynchronous MAC addresses.

[Enabling an Intermediate Device to Receive Flush Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0026.html)

Link reliability can be implemented between master and backup links only after intermediate devices are enabled to receive Flush packets.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0027.html)

After configuring an Eth-Trunk interface in manual 1:1 master/backup mode, you can check the ID, working mode, and member interface status of the Eth-Trunk interface.