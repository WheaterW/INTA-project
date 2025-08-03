Configuring Intra-VLAN Interface Isolation
==========================================

After you configure selected interfaces in a VLAN as isolated interfaces, these interfaces cannot communicate.

#### Usage Scenario

Intra-VLAN interface isolation disables specific interfaces in a VLAN from communicating.

To enable isolated interfaces to communicate, configure Layer 3 routing. This implementation allows you to flexibly manage and monitor VLAN users.

#### Pre-configuration Tasks

Before you configure intra-VLAN interface isolation, configure an interface-based VLAN.


[Configuring Interface Isolation for a Common VLAN](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_vlan_cfg_5003.html)

This section describes how to configure interface isolation for a common VLAN. 

[Configuring Interface Isolation for an Outside VLAN in VLAN Stacking or VLAN Mapping Scenarios](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_vlan_cfg_5006.html)

This section describes how to configure interface isolation for an outside VLAN in VLAN stacking or VLAN mapping scenarios.

[Enabling Intra-VLAN Proxy ARP](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_vlan_cfg_5004.html)

This section describes how to configure proxy ARP for isolated interfaces in a VLAN to communicate.

[Verifying the Intra-VLAN Interface Isolation Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_vlan_cfg_5005.html)

After interface isolation is configured for a common VLAN, verify the configuration.