Configuring Inter-Chassis Hot Backup
====================================

Before configuring inter-chassis hot backup, familiarize yourself with the applicable environment, complete the pre-configuration tasks, and obtain the data required for the configuration.

#### Usage Scenario

If multiple CGN devices equipped with service boards exist on a network, you can configure a service board on a master device and a service board on a backup device to implement inter-chassis backup. The inter-chassis hot backup mechanism ensures that the data stored in CPUs of the service boards on the master and backup devices is consistent. If the master device, the service board on it, or the link between the master and backup devices fails, a master/slave switchover is triggered to ensure service continuity. In this case, services are properly transmitted, and users are unaware of the fault.

* If multiple CGN devices equipped with service boards exist on a network and provide access services for a limited number of users, you can configure inter-chassis 1:1 backup. In inter-chassis 1:1 backup, when the service board on the master device processes services, the service board on the backup device does not work. The service board on the master device backs up the user tables, session tables, and address pool entries to the service board on the backup device. Once the master device, the service board on it, or the link between the master and backup devices fails, the backup device becomes the master and processes services.
* If multiple CGN devices equipped with service boards exist on a network and provide access services for a large number of users, you can configure inter-chassis 1+1 backup. In inter-chassis 1+1 backup, the service boards on both the master and backup devices process services and back up the user tables, session tables, and address pool entries to each other. Once a service board, a device, or the link between the master and backup devices fails, the service board on the other device processes all services.

#### Pre-configuration Tasks

Before enabling inter-chassis hot backup, complete the following tasks:

* Load a license on devices, and ensure that the service boards are working properly.
* Complete the basic NAT/DS-Lite/NAT64 function configuration. For details, see NAT Configuration/DS-Lite Configuration/NAT64 Configuration in *NAT and IPv6 Transition*.


[Enabling HA Hot Backup](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cgn-reliability_cfg_0013.html)

HA hot backup must be enabled globally to implement inter-chassis hot backup.

[Binding a Service-Location Group to an Inter-chassis Backup Channel](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cgn-reliability_cfg_0014.html)

A dual-device inter-chassis backup channel needs to be configured in the service-location group view.

[Binding a Service-Location Group to a VRRP Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cgn-reliability_cfg_0015.html)

In the service-location group view, bind the service-location group to a configured VRRP group.

[Associating a Service-Location Group with a VRRP Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cgn-reliability_cfg_0016.html)

In the interface view, configure association between a service-location group and VRRP.

[(Optional) Configuring NAT Load Balancing over Inter-chassis Backup](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cgn-reliability_cfg_0030.html)

This section describes how to configure NAT load balancing over inter-chassis backup.

[(Optional) Configuring VPN over NAT Inter-chassis Hot Backup](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cgn-reliability_cfg_0017.html)

This section describes how to configure VPN over NAT inter-chassis hot backup to resolve NAT issues on a VPN.

[(Optional) Configuring Inter-Chassis Batch Backup](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cgn-reliability_cfg_0045.html)

Configure inter-chassis batch backup between the master and backup devices to ensure their data consistency and normal user login after a master/backup device switchover.

[Verifying the Inter-Chassis Hot Backup Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cgn-reliability_cfg_0018.html)

After inter-chassis hot backup is configured, check whether the configured members of the HA inter-chassis hot backup and master/slave relationships are correct.