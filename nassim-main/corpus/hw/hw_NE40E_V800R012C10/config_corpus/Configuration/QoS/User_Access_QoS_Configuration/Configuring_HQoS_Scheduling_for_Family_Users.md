Configuring HQoS Scheduling for Family Users
============================================

HQoS for family users performs uniform scheduling for an entire family rather than individual terminals.

#### Context

A family may use multiple terminals to demand various services, such as VoIP, IPTV, and HSI. These services have different requirements for delay, jitter, and bandwidth. In addition, requirements of high-priority services must be satisfied preferentially when network resources are insufficient. Therefore, QoS scheduling must be performed based on a family rather than on each separate terminal.

After users log in, the device identifies services based on inner or outer VLAN IDs, 802.1p values, DSCP values, or DHCP Option 60 information carried in user packets. The packets matching the identification condition are mapped to a domain and are authenticated.

After user authentication succeeds, if the interface is configured with a QoS profile and the access information of user packets matches the scheduling defined in the QoS profile, the access users are considered as family users; otherwise, they are considered as common users.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The services on a BAS interface or different sub-interfaces can participate in uniform QoS scheduling for family users if they have the same family attributes.



#### Pre-configuration Tasks

Before configuring HQoS scheduling for family users, complete the following task:

Configure the BRAS functions on the NE40E to allow users to go online. For details, see HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - User Access.


[(Optional) Specifying a Resource Pool of Queues](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_013878.html)

This section describes how to specify a resource pool of queues for an interface, making full use of QoS resources.

[(Optional) Configuring a Flow Queue](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_hqos_cfg_5043_1.html)

You can configure scheduling parameters, traffic shaping, queue buffer resources, and more for a flow queue based on network requirements.

[(Optional) Configuring a Service Profile](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_hqos_cfg_5013_4.html)

You can configure a network header length in a service profile to compensate a processed packet with the length, precisely controlling traffic.

[Configuring User Queues Based on a QoS Profile](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_013819_2.html)

A QoS profile is the aggregate of QoS scheduling parameters. Configurable scheduling parameters for SQs include CIR, PIR, Flow Queue (FQ) profiles, and lengths for packet loss compensation of service profiles.

[Configuring a Service Identification Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_013821.html)

Service identification enables the system to determine which authentication domain is used based on the information about some fields carried in user packets.

[Binding a QoS Profile and a Service Identification Policy to a BAS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_013824.html)

You can apply a QoS profile to a type of user packets on an interface to perform HQoS for the user packets based on the scheduling parameters. You can also bind a service identification policy to the interface so that packets that meet specified conditions can be mapped to the domain for authentication.

[Defining a GQ Profile and Configuring Scheduling Parameters](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_5103_1.html)

A GQ profile contains user group queues' scheduling parameters, which include the CIR and PIR of user group queues.

[Applying a GQ Profile](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_5104_1.html)

For a user VLAN or a BAS interface through which users go online, you can apply a GQ profile to it in order to schedule traffic based on GQs.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_013825.html)

After HQoS is configured for family users, you can view information about the online users with specified IDs and the bandwidth consumed by them and applications of the QoS profile.