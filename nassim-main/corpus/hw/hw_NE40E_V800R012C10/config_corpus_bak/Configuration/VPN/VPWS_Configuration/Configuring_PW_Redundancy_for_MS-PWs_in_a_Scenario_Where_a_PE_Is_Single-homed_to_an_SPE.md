Configuring PW Redundancy for MS-PWs in a Scenario Where a PE Is Single-homed to an SPE
=======================================================================================

In a scenario where a PE is single-homed to an SPE, PW switching is configured on the SPE. PW redundancy is also configured on the SPE, and the negotiation mode is master/slave.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0172369889__fig_dc_vrp_cfg_01918401), MS-PWs are configured between PE1 and PE2. To improve reliability, PW redundancy is configured on the SPE. If public network tunnel protection is not configured, configure a bypass PW between PE2 and PE3 to forward packets during active/standby PW switching.

**Figure 1** PW redundancy for MS-PWs in a scenario where a PE is single-homed to an SPE  
![](images/fig_dc_vrp_cfg_01918401.png)

If PE2 is in the master state, PW2 on PE2 is the active PW. In normal situations, the traffic path is CE1 <-> PE1 <-> PW1 <-> SPE <-> PW2 <-> PE2 <->CE2.

* If the public network link between PE2 and the SPE fails and the public network tunnel is a TE tunnel with an explicit path, PW2 goes down, but PE2 is still the master. In this case, traffic is switched to the bypass PW and PW3 along the path CE1 <-> PE1 <-> PW1 <-> SPE <-> PW3 <-> PE3 <-> bypass PW <-> PE2 <-> CE2.
* If PE2 fails, traffic is switched to the path CE1 <-> PE1 <-> PW1 <-> SPE <-> PW3 <-> PE3 <-> CE2.
* If the AC link between CE2 and PE2 fails, PE2 remains in master state. In this case, traffic is switched to the path CE1 <-> PE1 <-> PW1 <-> SPE <-> PW2 <-> PE2 <-> bypass PW <-> PE3 <-> CE2.

#### Pre-configuration Tasks

Before configuring PW redundancy for MS-PWs in a scenario where a PE is single-homed to an SPE, complete the following tasks:

* Configure IP addresses and an IGP for PEs and the SPE, so that these devices can communicate.
* Establish a public network tunnel between the PE and SPE and between PE2 and PE3. The public network tunnels can be:
  
  + LDP tunnel: To establish an LDP tunnel, you must enable MPLS and MPLS LDP both globally and per interface on each public network node along the tunnel. If the PE and SPE are indirectly connected, set up a remote LDP session between them.
  + TE tunnel: To establish a TE tunnel, you must enable MPLS, MPLS TE, and RSVP-TE both globally and per interface on each public network node along the tunnel, and enable CSPF in the MPLS view of the tunnel ingress.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    If the public network tunnels are TE tunnels and L2VPN uses dynamic PWs, you need to enable MPLS LDP globally on the nodes at both ends of each TE tunnel and set up a remote MPLS LDP session (because dynamic PWs use LDP signaling extensions to distribute VPN labels).
    
    If the public network tunnels are not LDP tunnels, you must configure tunnel policies and apply them to these tunnels.
* Configure MPLS L2VPN on PEs and SPEs.


[Configuring Service PWs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_019185.html)

Service PWs consist of common PWs and bypass PWs. If tunnel protection is available on the public network, you do not need to configure any bypass PW.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_019189.html)

After the configuration is complete, you can view MS-PW information.