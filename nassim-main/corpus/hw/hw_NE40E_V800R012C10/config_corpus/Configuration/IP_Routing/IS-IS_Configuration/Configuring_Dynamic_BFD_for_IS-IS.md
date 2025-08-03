Configuring Dynamic BFD for IS-IS
=================================

BFD can provide link failure detection featuring light load and high speed (within milliseconds). With dynamic BFD, routing protocols can dynamically trigger the establishment of BFD sessions.

#### Usage Scenario

On IS-IS networks, IS-IS neighbors periodically send Hello packets to detect neighbor status changes. For networks that require fast convergence and zero packet loss, IS-IS is unreliable to detect link faults. To address this issue, configure BFD for IS-IS.

BFD includes static BFD and dynamic BFD. In dynamic BFD, BFD session establishment is triggered by routing protocols. Dynamic BFD minimizes configuration errors caused by manual operations in static BFD and is easy to configure. Therefore, dynamic BFD is applicable to networks on which all devices require BFD. Dynamic BFD helps detect link faults rapidly and implement fast route convergence.


#### Pre-configuration Tasks

Before configuring dynamic BFD for IS-IS, complete the following tasks:


[Configuring BFD Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_0044.html)

Before configuring dynamic BFD for IS-IS, you need to enable BFD globally.

[Configuring BFD for an IS-IS Process](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_0045.html)

By configuring BFD for an IS-IS process, you can set parameters for dynamic BFD sessions and enable dynamic BFD for IS-IS on all IS-IS interfaces.

[(Optional) Configuring BFD on a Specified Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_0047.html)

You can configure dynamic BFD session parameters for a specified interface.

[Verifying the Configuration of Dynamic BFD for IS-IS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_0048.html)

After configuring dynamic BFD for IS-IS, check information about the BFD session and dynamic BFD for IS-IS on an interface.