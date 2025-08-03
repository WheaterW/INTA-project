Configuring Dynamic BFD for IPv6 IS-IS
======================================

BFD provides link failure detection featuring light load and high speed (within milliseconds). With dynamic BFD, routing protocols can dynamically trigger the establishment of BFD sessions.

#### Usage Scenario

If the network requires zero packet loss and fast convergence when the link status changes, you can configure dynamic BFD on IS-IS links.

BFD needs to be configured based on the actual network environment. If the time parameters are set improperly, network flapping may occur.


#### Pre-configuration Tasks

Before configuring dynamic BFD for IPv6 IS-IS, complete the following tasks:


[Configuring BFD Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_2004.html)

Before configuring dynamic BFD for IS-IS, enable BFD globally.

[Configuring BFD for an IS-IS IPv6 Process](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_2005.html)

By configuring BFD for an IPv6 IS-IS process, you can set parameters for dynamic BFD sessions and enable dynamic BFD for IPv6 IS-IS on all IPv6 IS-IS interfaces in the process.

[(Optional) Configuring BFD on a Specified IPv6 Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_2007.html)

You can configure dynamic BFD session parameters for a specified IPv6 interface.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_2008.html)

After configuring dynamic IPv6 BFD for IS-IS, check information about the BFD session and dynamic BFD for IS-IS on an interface.