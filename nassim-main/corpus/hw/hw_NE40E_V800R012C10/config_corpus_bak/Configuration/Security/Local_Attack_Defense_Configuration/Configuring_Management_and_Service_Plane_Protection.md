Configuring Management and Service Plane Protection
===================================================

This section describes how to configure management and service plane protection. This function allows only specified protocol packets to be sent to CPUs, and reduces malicious packet attacks on these CPUs to ensure that devices work properly.

#### Applicable Environment

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Attacks intending to paralyze TCP/IP networks, especially network devices, continue to increase at alarming rates. MPAC servers better for protecting devices against such attacks. Using MPAC is recommended.

If the Router is likely to be controlled by unauthorized users through non-management interfaces or attacked by flooding packets, management and service plane protection needs to be deployed. The protection function ensures that only specified management interfaces will be allowed to receive management packets. Packets received by non-management interfaces will be directly dropped. This saves resources.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

FTP, SSH, SNMP, TELNET, and TFTP are usually disabled globally on a device but enabled on some specified interfaces. If the interfaces enabled with these protocols are all Down, the global configurations will cease to take effect (that is, these protocols will be automatically enabled on other interfaces), which ensures connectivity to the device.


![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration task is supported only on the Admin-VS.



#### Pre-configuration Tasks

Before configuring management and service plane protection, complete the following task:

* Configuring link layer protocol parameters for interfaces to ensure that the link layer protocol on the interfaces is Up


[Configuring a Global Policy for Management and Service Plane Protection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_hostdefend_cfg_0004.html)

A global policy for management and service plane protection can be applied to the entire device to filter packets of certain types.

[Configuring an interface board-based Policy for Management and Service Plane Protection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_hostdefend_cfg_0005.html)

An interface board-based policy for management and service plane protection can be applied to an interface board to filter packets of certain types.

[Configuring an Interface-based Policy for Management and Service Plane Protection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_hostdefend_cfg_0006.html)

An interface-based policy for management and service plane protection can be applied to an interface to filter packets of certain types.

[Verifying the Configuration of Management and Service Plane Protection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_hostdefend_cfg_0007.html)

After configuring management and service plane protection, you can run display commands to check the configuration.