Configuring HQoS Scheduling for Common Users
============================================

HQoS for common users identifies services by priority and then performs uniform scheduling.

#### Context

If the access user is an IPoE user, family identification is not required. Such access is considered as a single user access and such a user is called a common user. IPoE users are identified using IP addresses. The common user, however, also demands various types of services. The demanded services need be differentiated according to priorities. The system obtains QoS information about common users from the QoS profile applied to the authentication domain.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

You can configure the RADIUS server to dynamically deliver QoS parameters during the authentication of common users. In such a case, configuring QoS parameter delivery on the NE40E is not required.

In user access scenarios, HQoS is by default disabled for downstream traffic when the eTM subcard is not installed, and configured HQoS is forcibly changed to CAR. To enable HQoS scheduling in such scenarios, run the [**access-user board-schedule enable outbound**](cmdqueryname=access-user+board-schedule+enable+outbound) command.



#### Pre-configuration Tasks

Before configuring HQoS scheduling for common users, complete the following task:

Configure the BRAS functions on the NE40E to allow users to go online. For details, see HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - User Access.


[(Optional) Specifying a Resource Pool of Queues](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_013878_1.html)

This section describes how to specify a resource pool of queues for an interface, making full use of QoS resources.

[(Optional) Configuring an Flow Queue](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_hqos_cfg_5043_common.html)

You can configure scheduling parameters and traffic shaping for FQs in common 8-CoS mode based on network requirements.

[(Optional) Configuring 4-CoS Flow Queues and Scheduling Parameters](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_50866.html)

You can configure parameters for a 4-CoS flow queue profile, which reduces the configuration workload required by an 8-CoS flow queue profile.

[(Optional) Configuring the Mappings Between 8-CoS and 4-CoS Priorities](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_6087.html)

You can define the mappings between 8-CoS and 4-CoS priorities to provide more flexible 4-CoS priority configurations.

[(Optional) Configuring a Service Profile](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_hqos_cfg_5013_5.html)

You can configure a network header length in a service profile to compensate a processed packet with the length, precisely controlling traffic.

[Configuring User Queues Based on a QoS Profile](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_013819.html)

A QoS profile is the aggregate of QoS scheduling parameters. Configurable scheduling parameters for SQs include CIR, PIR, Flow Queue (FQ) profiles, and lengths for packet loss compensation of service profiles.

[Applying a QoS Profile to a Domain](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_013832.html)

You can define a QoS profile and then apply it to the AAA domain to perform QoS scheduling for access user traffic.

[Defining a GQ Profile and Configuring Scheduling Parameters](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_5103.html)

A GQ profile contains user group queues' scheduling parameters, which include the CIR and PIR of user group queues.

[Applying a GQ Profile](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_5104.html)

For a user VLAN or a BAS interface through which users go online, you can apply a GQ profile to it in order to schedule traffic based on GQs.

[Configuring QoS in a Domain](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_013829.html)

You can configure a rate limiting mode for common users and configure the service traffic of users in a domain not to participate in QoS scheduling for family users as required.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_013833.html)

After HQoS scheduling is configured for common users, you can view the configuration and application information about the specified QoS profile.