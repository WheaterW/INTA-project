Configuring an iNOF Zone
========================

Configuring an iNOF Zone

#### Prerequisites

Before configuring an iNOF zone, you have completed the following task:

* Enable the LLDP function on the device globally. If this function is disabled on an interface, the iNOF system cannot detect information about the hosts directly connected to the interface. For details, see "LLDP Configuration" in Configuration Guide > System Management Configuration.

#### Context

If the iNOF reflector function has been configured on the device, you can configure an iNOF zone only on the iNOF reflector, which then transmits the configured zone member information to each client.![](public_sys-resources/note_3.0-en-us.png) 

If two iNOF reflectors exist in an iNOF system, their zone configurations must be the same to ensure successful data backup between them.




[Creating an iNOF Customized Zone](galaxy_ai_inof_cfg_0010.html)



[(Optional) Configuring the Function of Automatically Adding Hosts to the iNOF Default Zone](galaxy_ai_inof_cfg_0011.html)



[(Optional) Configuring iNOF Zone Isolation](galaxy_ai_inof_cfg_0016.html)