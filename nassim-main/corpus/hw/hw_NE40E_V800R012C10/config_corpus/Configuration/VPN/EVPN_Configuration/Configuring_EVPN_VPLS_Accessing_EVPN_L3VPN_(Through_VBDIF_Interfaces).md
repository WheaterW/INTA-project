Configuring EVPN VPLS Accessing EVPN L3VPN (Through VBDIF Interfaces)
=====================================================================

If EVPN VPLS is used to carry P2MP Layer 2 services and EVPN L3VPN is used to carry Layer 3 services, you need to configure EVPN VPLS accessing EVPN L3VPN on devices where Layer 2 and Layer 3 services converge.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0000001602704389__fig128162610614), the first layer is the user-side access network where Layer 2 services are carried between CPEs and UPEs to implement VLAN forwarding. The second layer is the aggregation network where services are carried using EVPN VPLS and EVPN VPLS is deployed between UPEs and NPEs. The third layer is the core network where services are carried using EVPN L3VPN. In this case, you need to configure EVPN VPLS accessing EVPN L3VPN on NPEs.

**Figure 1** EVPN VPLS accessing EVPN L3VPN  
![](figure/en-us_image_0000001602854261.png)
#### Pre-configuration Tasks

Before configuring EVPN VPLS accessing EVPN L3VPN, complete the following tasks:

* Ensure route reachability between UPEs and NPEs and between NPEs and gateways.
* Complete one of the following tasks on NPEs and UPEs:
  + [Configure EVPN VPLS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0023_copy.html).
  + [Configure EVPN VPLS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpls_over_srv6-te_policy_copy.html).
  + [Configure EVPN VPLS over MPLS (BD EVPN instance)](dc_vrp_evpn_cfg_0065.html).
* Complete one of the following tasks on NPEs and gateways:
  + [Configure EVPN L3VPN over IS-IS SRv6 BE](dc_vrp_evpn_cfg_0152_copy.html).
  + [Configure EVPN L3VPNv4 over SRv6 TE Policy](dc_vrp_cfg_evpn-l3vpn_over_srv6-te_policy_copy.html).
  + [Configure EVPN L3VPN over MPLS](dc_vrp_evpn_cfg_0038.html).

#### Procedure

* Configure a VBDIF interface on each of NPE1 and NPE2 for EVPN VPLS accessing EVPN L3VPN.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) **vbdif** *bd-id* command to create a VBDIF interface and enter its view.
  3. Run the [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name* command to bind the VBDIF interface to the VPN instance.
  4. Configure an IP address for the VBDIF interface to implement Layer 3 communication.
     
     If the EVPN VPLS service uses dual-homing active-active networking, the same IP address must be configured on NPE1 and NPE2.
     + For an IPv4 network, run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ] command to configure an IPv4 address.
     + For an IPv6 network, perform the following operations:
       1. Run the [**ipv6 enable**](cmdqueryname=ipv6+enable) command to enable IPv6 on the interface.
       2. Run the [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* } or [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* } **eui-64** command to configure a global unicast address for the interface.
  5. Run the [**mac-address**](cmdqueryname=mac-address) *mac-address* command to configure a MAC address for the interface.
     
     
     
     If the EVPN VPLS service uses dual-homing active-active networking, the same MAC address must be configured on NPE1 and NPE2.
  6. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure a VBDIF interface for EVPN VPLS accessing EVPN L3VPN on each of NPE1 and NPE2. Then configure VRRP on each of the devices.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) **vbdif** *bd-id* command to create a VBDIF interface and enter its view.
  3. Run the [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name* command to bind the VBDIF interface to the VPN instance.
  4. Configure an IP address for the VBDIF interface to implement Layer 3 communication.
     
     
     + For an IPv4 network, run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ] command to configure an IPv4 address.
     + For an IPv6 network, perform the following operations:
       1. Run the [**ipv6 enable**](cmdqueryname=ipv6+enable) command to enable IPv6 on the interface.
       2. Run the [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* } or [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* } **eui-64** command to configure a global unicast address for the VBDIF interface.
  5. Run the [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **virtual-ip** *virtual-address* command to create a VRRP group and assign a virtual IP address to it.
  6. (Optional) Run the [**vrrp passive**](cmdqueryname=vrrp+passive) command to enable VRRP passive, so that the device is forced to become the master device when the interface status is up.
     
     
     
     If the EVPN VPLS service uses dual-homing active-active networking, this command must be configured on NPE1 and NPE2.
  7. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

* Run the [**display bgp evpn all routing-table**](cmdqueryname=display+bgp+evpn+all+routing-table) command on NPEs to check information about EVPN routes received from UPEs.
* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* or [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* command on NPEs or UPEs to check information about VPN routes received from the remote end.