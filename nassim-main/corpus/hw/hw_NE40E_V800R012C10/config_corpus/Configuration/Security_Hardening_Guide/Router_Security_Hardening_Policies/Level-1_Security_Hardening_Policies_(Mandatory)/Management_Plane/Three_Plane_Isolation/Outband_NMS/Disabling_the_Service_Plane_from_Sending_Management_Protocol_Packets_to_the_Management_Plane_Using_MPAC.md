Disabling the Service Plane from Sending Management Protocol Packets to the Management Plane Using MPAC
=======================================================================================================

Disabling the Service Plane from Sending Management Protocol Packets to the Management Plane Using MPAC

#### Networking Requirements

The service plane is disabled from sending management protocol packets to the management plane so that the management plane receives management protocol packets only from the management network interface.


#### Configuration Roadmap

Create two MPAC policy views: one for global application, and the other for interface application. Configure a rule to disable management protocol packets from being sent to the management plane in the globally applied profile. Configure a rule to allow only specific management protocol packets to be sent to the management plane in the profile applied to an interface. The configuration roadmap is as follows:

1. Create two MPAC policy profiles in the system view, with one being applied globally and the other being applied to an interface.
2. Disable management protocol packets from being sent to the management plane in the profile for global application, and allow only specific management protocol packets to be sent to the management plane in the profile for interface application.
3. Bind the global MPAC policy globally, and bind the interface-based policy to the management network interface GigabitEthernet0/0/0.
4. Check the configurations and the number of dropped packets.


#### Procedure

1. Create two MPAC policy profiles in the system view, with one being applied globally and the other being applied to an interface.
   ```
   [~HUAWEI] service-security policy ipv4 global
   ```
   ```
   [*HUAWEI-service-sec-global] commit
   [~HUAWEI-service-sec-global] quit
   ```
   ```
   [~HUAWEI] service-security policy ipv4 interface
   ```
   ```
   [*HUAWEI-service-sec-interface] commit
   [~HUAWEI-service-sec-interface] quit
   ```
2. Disable FTP, SNMP, SSH, Telnet, and TFTP protocol packets from being sent to the management plane in the profile for global application, and allow only FTP, SNMP, SSH, Telnet, and TFTP protocol packets to be sent to the management plane in the profile for interface application.
   ```
   [~HUAWEI] service-security policy ipv4 global
   ```
   ```
   [~HUAWEI-service-sec-global] rule deny protocol ftp
   ```
   ```
   [*HUAWEI-service-sec-global] rule deny protocol snmp
   ```
   ```
   [*HUAWEI-service-sec-global] rule deny protocol ssh
   ```
   ```
   [*HUAWEI-service-sec-global] rule deny protocol telnet
   ```
   ```
   [*HUAWEI-service-sec-global] rule deny protocol  
   ```
   ```
   [*HUAWEI-service-sec-global] commit
   [~HUAWEI-service-sec-global] quit
   ```
   ```
   [~HUAWEI] service-security policy ipv4 interface
   ```
   ```
   [~HUAWEI-service-sec-interface] rule permit protocol ftp
   ```
   ```
   [*HUAWEI-service-sec-interface] rule permit protocol snmp
   ```
   ```
   [*HUAWEI-service-sec-interface] rule permit protocol ssh
   ```
   ```
   [*HUAWEI-service-sec-interface] rule permit protocol telnet
   ```
   ```
   [*HUAWEI-service-sec-interface] rule permit protocol tftp
   ```
   ```
   [*HUAWEI-service-sec-interface] commit
   [~HUAWEI-service-sec-interface] quit
   ```
3. Bind the interface-based MPAC policy to the management network interface GigabitEthernet0/0/0, and bind the global MPAC policy globally.
   ```
   [~HUAWEI] interface GigabitEthernet0/0/0
   ```
   ```
   [~HUAWEI-GigabitEthernet0/0/0] service-security binding ipv4 interface
   [*HUAWEI-GigabitEthernet0/0/0] commit
   [~HUAWEI-GigabitEthernet0/0/0] quit
   ```
   ```
   [~HUAWEI] service-security global-binding ipv4 global
   [*HUAWEI] commit
   ```

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If only a global policy profile is configured and management protocol packets are disabled from being sent to the management plane in the profile, the device fails to be managed. To resolve this problem, allow specific service interfaces to send management protocol packets to the management plane first. Ensure that these interfaces are Up.



#### Verifying the Security Hardening Result

* Run the **display service-security statistics ipv4** command to check whether all service interfaces fail to send management protocol packets to the CPU and whether all management protocol packets are discarded by referring to packet statistics.
* Run the **display service-security binding ipv4** command to check MPAC policy information on interfaces.
* Run the **display service-security policy ipv4** command to check IPv4 MPAC policy configurations.