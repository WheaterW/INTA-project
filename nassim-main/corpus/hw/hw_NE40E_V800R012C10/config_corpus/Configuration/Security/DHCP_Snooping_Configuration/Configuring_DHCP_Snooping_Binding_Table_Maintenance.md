Configuring DHCP Snooping Binding Table Maintenance
===================================================

Dynamic Host Configuration Protocol (DHCP) snooping binding table maintenance allows the device to delete, back up, and transfer the DHCP binding table.

#### Applicable Environment

After DHCP snooping binding table maintenance is enabled, the device can perform the following operations:

* When a client goes offline, the DHCP snooping binding entry for the client needs to be updated. The update can be implemented by enabling client online status or deleting the DHCP snooping binding table manually.
* If a client obtains an IP address and goes online from an interface, the device creates a DHCP binding entry for the client. After DHCP snooping binding table transfer is enabled, the DHCP binding entry can be applied on other interfaces so that the client can go online from another interface.
* You can configure DHCP binding table backup to prevent the DHCP binding table from being lost after the system is restarted.


#### Pre-configuration Tasks

Before you configure DHCP snooping binding table maintenance, enable DHCP snooping and configure trusted interfaces.


[Configuring DHCP Binding Table Update](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0029_1.html)

The Dynamic Host Configuration Protocol (DHCP) binding table update function contains the client online status detection function and the DHCP snooping binding entry deletion function.