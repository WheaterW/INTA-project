Configuring MBGP Routing Policies
=================================

MBGP routing policies can be configured to flexibly control the sending and receiving of routes.

#### Usage Scenario

Routing policies can be used to set or re-set MBGP route attributes by using some predefined conditions, which provide a flexible and effective method to control MBGP route selection. The sending and receiving of routes can be flexibly controlled by applying MBGP routing policies.


#### Pre-configuration Tasks

Before configuring MBGP routing policies, [configure an MBGP peer](dc_vrp_multicast_cfg_1003.html).


[Configuring a Route-policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_1019.html)

A route-policy is used to filter routes.

[Configuring a Policy for Receiving MBGP Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_1020.html)

MBGP filters received routes by using a policy. Only the routes that match the policy can be added to a routing table.

[Configuring a Policy for Advertising MBGP Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_1021.html)

After MBGP filters the imported routes, only routes that pass the filtering are added to the local MBGP routing table and advertised to MBGP peers.

[Configuring MBGP Soft Resetting](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_1022.html)

MBGP soft resetting allows the system to refresh an MBGP routing table dynamically without tearing down any MBGP connection if routing policies are changed.

[Verifying the Configuration of Policies for Route Exchanges Between MBGP Peers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_1023.html)

After configuring policies for route exchange between MBGP peers, verify information about MBGP routes.