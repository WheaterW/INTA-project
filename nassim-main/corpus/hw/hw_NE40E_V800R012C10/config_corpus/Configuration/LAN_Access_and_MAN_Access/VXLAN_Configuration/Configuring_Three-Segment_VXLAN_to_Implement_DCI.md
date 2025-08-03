Configuring Three-Segment VXLAN to Implement DCI
================================================

Three-Segment VXLAN can be configured to enable communication between VMs in different DCs.

#### 

#### Usage Scenario

To meet the requirements of inter-regional operations, user access, geographical redundancy, and other scenarios, an increasing number of enterprises are deploying DCs across multiple regions. Data Center Interconnect (DCI) is a solution that enables communication between VMs in different DCs. Using technologies such as VXLAN and BGP EVPN, DCI securely and reliably transmits DC packets over carrier networks. Three-segment VXLAN can be configured to enable communications between VMs in different DCs.


#### Pre-configuration Tasks

Before configuring three-segment VXLAN to implement DCI, complete the following tasks:

* Configure an IGP in DCs.


[Configuring Three-Segment VXLAN to Implement Layer 3 Interworking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan_cfg_1219.html)

The three-segment VXLAN can be configured to enable communications between inter-subnet VMs in DCs that belong to different ASs.

[Configuring Three-Segment VXLAN to Implement Layer 2 Interworking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan_cfg_1220.html)

Three-segment VXLAN tunnels can be configured to enable communication between VMs that belong to the same subnet but different DCs.

[Verifying the Configuration of Using Three-Segment VXLAN to Implement DCI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan_cfg_1221.html)

After configuring three-segment VXLAN to implement DCI, verify the configuration, such as EVPN instances and VXLAN tunnel information.