Configuring Basic VRRP Functions
================================

VRRP works in either master/backup or load balancing mode, implementing device backup and efficient and stable data forwarding.

#### Usage Scenario

A VRRP group consists of two or more devices and functions as an egress gateway for hosts. If a device fails, another device takes over. VRRP ensures continuous and reliable network communication.


#### Pre-configuration Tasks

Before configuring basic VRRP functions, configure network layer attributes for interfaces to ensure network connectivity.


[Creating a VRRP Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp_cfg_0131.html)

You can create a Virtual Router Redundancy Protocol (VRRP) backup group and set VRRP priorities to determine the master and backup Routers. The master Router transmits data traffic. You can create multiple VRRP groups to load-balance data traffic.

[(Optional) Configuring VRRP Stability Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp_cfg_0106.html)

To help a VRRP group work stably, enable the preemption function, set a preemption delay, and specify an interval at which VRRP Advertisement packets are sent. The configuration can minimize impact of network flapping resulted from frequent master/backup VRRP switchovers on data forwarding.

[(Optional) Configuring a VRRP Security Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp_cfg_0107.html)

A VRRP security policy can be configured to protect a network requiring high security against attacks.

[(Optional) Optimizing VRRP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp_cfg_0108.html)

To optimize VRRP, enable ping to a virtual IP address, set the interval at which the master device sends gratuitous ARP packets, and disable a device from checking TTL values in received VRRP Advertisement packets.

[(Optional) Configuring Smooth VRRP Switching](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp_cfg_0145.html)

After smooth VRRP switching is enabled, the backup devices learn the smooth switching time and retain their status within the smooth switching time, preventing service traffic loss resulted from a master/backup VRRP switchover.

[Verifying the VRRP Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp_cfg_0109.html)

After the configurations of a Virtual Router Redundancy Protocol (VRRP) backup group are complete, you can view the status of the VRRP group.