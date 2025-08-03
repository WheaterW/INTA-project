Disabling Specific Service Interfaces from Sending Management Protocol Packets to the Management Plane Using MPAC
=================================================================================================================

Disabling_Specific_Service_Interfaces_from_Sending_Management_Protocol_Packets_to_the_Management_Plane_Using_MPAC

#### Networking Requirements

Specific service interfaces are disabled from sending management protocol packets to the management plane so that the management plane receives management protocol packets only from the other service interfaces.


#### Configuration Roadmap

Create two MPAC policy views: one for global application, and the other for interface application. Configure a rule to disable management protocol packets from being sent to the management plane in the globally applied profile. Configure a rule to allow only specific management protocol packets to be sent to the management plane in the profile applied to an interface. The configuration roadmap is as follows:

1. Create two MPAC policy profiles in the system view, with one being applied globally and the other being applied to an interface.
2. Disable management protocol packets from being sent to the management plane in the profile for global application, and allow only specific management protocol packets to be sent to the management plane in the profile for interface application.
3. Bind the global MPAC policy globally, and bind the interface-based MPAC policy to GE 0/1/0.
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
   [~HUAWEI-service-sec-global] quit
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
   [*HUAWEI-service-sec-global] rule deny protocol tftp
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
3. Bind the interface-based MPAC policy to GE 0/1/0, and bind the global MPAC policy globally.
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/0
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0] service-security binding ipv4 interface
   [*HUAWEI-GigabitEthernet0/1/0] commit
   [~HUAWEI-GigabitEthernet0/1/0] quit
   ```
   ```
   [~HUAWEI] service-security global-binding ipv4 global
   [*HUAWEI] commit
   ```
4. Verify the configuration.
   ```
   [~HUAWEI] display service-security binding ipv4
   ```
   ```
     Configured : Global
     Policy Name: global
     
   Interface  : GigabitEthernet0/1/0
     Policy Name: interface
   
   ```
   ```
   [~HUAWEI] display service-security policy ipv4
   ```
   ```
     Policy Name : global
     Step        : 5
      rule 5 deny protocol ftp
      rule 10 deny protocol snmp
      rule 15 deny protocol ssh
      rule 20 deny protocol tftp
      rule 25 deny protocol telnet
   
   Policy Name : interface
   Step        : 5
    rule 5 permit protocol ftp
    rule 10 permit protocol snmp
    rule 15 permit protocol ssh
    rule 20 permit protocol tftp
    rule 25 permit protocol telnet
   ```

#### Verifying the Security Hardening Result

* Run the **display service-security statistics ipv4** command to check whether all service interfaces fail to send management protocol packets to the CPU and whether all management protocol packets are discarded by referring to packet statistics.
* Run the **display service-security binding ipv4** command to check MPAC policy information on an interface.
* Run the **display service-security policy ipv4** command to check IPv4 MPAC policy configurations.