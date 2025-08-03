Configuration Precautions for ZTP
=================================

Configuration Precautions for ZTP

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| During ZTP running:  1. Do not run the mtp assistant disable or assistant scheduler suspend command to disable an OPS built-in script assistant.  2. Do not run the undo enable (OPS view) command to disable the OPS function.  Otherwise, the ZTP function is affected. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The names of the CC software package, configuration file, and patch file to be downloaded in the intermediate file cannot be the same as the names of the running CC software package, configuration file, and patch file on the device or the names of the CC software package, configuration file, and patch file specified for the next startup. ZTP does not download any file with the same name as a file running on the device or a file specified for the next startup. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| If the device needs to start using ZTP, the configuration file for the startup must be NULL or vrpcfg.zip. Otherwise, ZTP does not start. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| During device startup, the sub-interfaces with VPN instances generated in the pre-configuration script do not support ZTP. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| A device cannot be in the same broadcast domain with two or more DHCP servers. Otherwise, ZTP does not take effect. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When ZTP is used, the corresponding option (for example, 66, 67, or 59) needs to be specified for the DHCP server. Otherwise, ZTP will exit. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Before using ZTP for the next startup, check whether ZTP is enabled. If ZTP is disabled, enable it. Otherwise, the ZTP process cannot be started next time. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The address lease needs to be set for the DHCP server based on the site deployment period. If the lease is too short, a go-online failure occurs. You are advised to set a long period for the DHCP server address. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When ZTP is used, the manually configured device startup items (CC software package, configuration file, and patch file) may be overwritten by ZTP. In this case, you need to run the set ztp disable command to stop ZTP. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The set save-configuration or undo set save-configuration command cannot be run when ZTP is running.  Otherwise, ZTP cannot run properly, or user configurations may be invalid. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| ZTPv6 has the following restrictions:  1. Interconnection with the upstream Eth-Trunk interface cannot be performed.  2. VLAN learning on QinQ interfaces cannot be performed.  3. Address conflict detection is not performed, which may result in conflicts between obtained IPv6 addresses.  4. Transmission of DHCP Release messages. The DHCP server cannot receive DHCP Release messages for address release and can only rely on the address aging mechanism. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| ZTPv4 does not support VLAN learning on QinQ interfaces. Properly plan the configuration. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |