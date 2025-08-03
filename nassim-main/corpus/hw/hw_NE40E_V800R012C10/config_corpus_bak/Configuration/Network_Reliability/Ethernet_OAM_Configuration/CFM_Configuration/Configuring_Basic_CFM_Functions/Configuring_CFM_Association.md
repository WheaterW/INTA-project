Configuring CFM Association
===========================

This section describes how to configure connectivity fault management (CFM) association.

#### Usage Scenario

CFM can be associated with detection or application modules to detect link faults and ensure service reliability. For details about CFM association, see [Overview of CFM](dc_vrp_cfm_cfg_000002.html).


#### Pre-configuration Tasks

Before configuring CFM association, complete the following tasks:

* Configure basic CFM functions.
* Perform the following configurations based on the associated protocol type:
  + Configure basic Ethernet in the First Mile (EFM) functions if CFM needs to be associated with EFM.
  + Configure basic Bidirectional Forwarding Detection (BFD) functions if CFM needs to be associated with BFD.
  + Configure basic Virtual Router Redundancy Protocol (VRRP) functions if CFM needs to be associated with VRRP.


[Associating CFM with an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfm_cfg_000015.html)

This section describes how to associate connectivity fault management (CFM) with an interface.

[Configuring Fault Message Transmission Between Ethernet CFM and Its Bound Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfm_cfg_000035.html)

This section describes how to configure fault message transmission between Ethernet CFM and its bound interface in the OAM management view. After the configuration is complete, the link detection results of Ethernet CFM can be associated with the interface status.

[Associating CFM with EFM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfm_cfg_000017.html)

This section describes how to associate connectivity fault management (CFM) with Ethernet in the First Mile (EFM).

[Associating CFM with VRRP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfm_cfg_000019.html)

This section describes how to associate connectivity fault management (CFM) with Virtual Router Redundancy Protocol (VRRP).

[Associating CFM with BFD](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfm_cfg_000018.html)

This section describes how to associate connectivity fault management (CFM) with Bidirectional Forwarding Detection (BFD).

[Associating CFM with CFM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfm_cfg_000031.html)

If CFM is deployed at both sides, association between CFM and CFM can be configured. This allows CFM and CFM to notify each other of faults and ensures reliable service transmission.

[Configuring a CFM Association to Trigger ARP Entry Deletion](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfm_cfg_000029.html)

If CFM detects a link fault, it notifies the OAM management module. Upon receipt of the notification, the OAM management module deletes ARP entries mapped to the link and triggers link switching.

[Configuring a CFM Association to Trigger MAC Entry Deletion](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfm_cfg_000030.html)

If CFM detects link faults, it notifies a node. Upon receipt of the notification, the node deletes MAC entries within the configured VLAN range and triggers link switching.

[Configuring Association Between CFM and EVPN DF Election Results](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfm_cfg_000039.html)