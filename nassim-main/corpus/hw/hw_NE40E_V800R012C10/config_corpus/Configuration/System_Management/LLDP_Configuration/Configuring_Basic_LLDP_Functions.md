Configuring Basic LLDP Functions
================================

After devices are configured with LLDP, the NMS can obtain network topology information, and information about the capabilities, management address, device ID, and interface ID of each device.

#### Usage Scenario

LLDP is used to obtain neighbor information and discover network topology. As shown in [Figure 1](#EN-US_TASK_0172360364__fig_dc_vrp_lldp_cfg_000301), if the NMS needs to collect topology information about Device A and Device B, you can enable LLDP for Device A and Device B. Device A and Device B send packets encapsulated with status information to each other, allowing the NMS to obtain the topology information.

**Figure 1** Networking diagram for the LLDP application  
![](images/fig_dc_vrp_lldp_cfg_000301.png)

#### Pre-configuration Tasks

Before configuring LLDP, complete the following tasks:

* Configuring reachable routes between devices and the NMS and configuring SNMP parameters
* Configuring an IP address for LLDP management on a device


[Enabling LLDP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_lldp_cfg_0004.html)

When LLDP is enabled on a device, the device sends LLDP packets carrying its status information to its LLDP-capable neighbors and obtains their status information by receiving LLDP packets from them.

[(Optional) Configuring an LLDP Management IP Address](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_lldp_cfg_0005.html)

This section describes how to configure an LLDP management IP address, so that an NMS can identify a device based on this management address to detect network topologies.

[(Optional) Configuring Types of TLVs Allowed to Be Advertised by LLDP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_lldp_cfg_0006.html)

During the process of exchanging Link Layer Discovery Protocol (LLDP) packets between devices, the LLDP data unit (LLDPDU) encapsulated in an LLDP packet carries different type-length-values (TLVs) as needed. A device sends its status information and receives neighbor status information based on these different TLVs.

[(Optional) Optimizing LLDP Performance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_lldp_cfg_0007.html)

This section describes how to adjust LLDP parameters based on the load of a network to reduce the consumption of system resources and optimize the LLDP performance.

[Verifying the Configuration of Basic LLDP Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_lldp_cfg_0008.html)

After configuring basic LLDP functions, verify the configuration.