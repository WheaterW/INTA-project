Example for Configuring SNMP Proxy Using User-Defined Parameter Settings
========================================================================

This section describes how to configure Simple Network Management Protocol (SNMP) proxy using default parameter settings.

#### Networking Requirements

SNMP communicates management information between an NMS
and a device, such as a Router, so that the NMS can manage the device. If the NMS and device use
different versions of SNMP, the NMS cannot manage the device.

To solve this problem, configure SNMP proxy on a middle-point device between the NMS and managed device, as shown in [Figure 1](#EN-US_TASK_0172361047__fig_dc_vrp_snmp_cfg_003201). The NMS manages the middle-point device and managed device as an independent network element, reducing the number of managed network elements and management costs. **Figure 1** Networking diagram for configuring SNMP proxy using user-defined parameter settings  
![](figure/en-us_image_0000001578465988.png)

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configurations in this example are mainly performed on the PE.

In this example, Interface 1 and Interface 2 represent GE0/1/0 and GE0/1/1, respectively.

If you do not want the middle-point device to communicate with the managed device based on default parameter settings, configure SNMP proxy using user-defined parameter settings. After you configure SNMP proxy, the middle-point device communicates with the managed device based on the user-defined parameter settings.


#### Precautions

In this type of SNMP proxy configuration, you must configure SNMP on the managed device.


#### Configuration Roadmap

The configuration roadmap is as follows:

* Configure the middle-point device.
  
  1. Configure the IP addresses of interfaces that connect the middle-point device to the NMS and managed device.
  2. Configure a VPN instance and bind it to the interface connected to the NMS.
  3. Configure SNMP proxy on the middle-point device using user-defined parameter settings, so that you can use the middle-point device to manage the managed device.
* Configure the managed device.
  
  1. Configure the IP address of the interface that connects the managed device to the middle-point device.
  2. Configure SNMP for the managed device to communicate with the NMS.

#### Data Preparation

To complete the configuration, you need the following data:

* Types, numbers, and IP addresses of the interfaces that connect the middle-point device to the NMS and managed device and of the interface that connects the managed device to the middle-point device
* VPN instance name
* Proxy rules for SNMP packets, SNMP proxy community name, and target host names


#### Procedure

* Configure the middle-point device.
  
  
  1. Configure the interface IP addresses used by the middle-point device to communicate with the NMS and managed device.
     
     ```
     <HUAWEI> system-view
     ```
     ```
     [~HUAWEI] sysname PE
     ```
     ```
     [*HUAWEI] commit
     ```
     ```
     [~PE] interface gigabitethernet 0/1/0
     ```
     ```
     [~PE-GigabitEthernet0/1/0] ip address 3.1.1.1 24
     ```
     ```
     [*PE-GigabitEthernet0/1/0] commit
     ```
     ```
     [~PE-GigabitEthernet0/1/0] quit
     ```
     ```
     [~PE] interface gigabitethernet 0/1/1
     ```
     ```
     [~PE-GigabitEthernet0/1/1] ip address 192.168.1.1 24
     ```
     ```
     [*PE-GigabitEthernet0/1/1] commit
     ```
     ```
     [~PE-GigabitEthernet0/1/1] quit
     ```
  2. Configure a VPN instance and bind it to the interface connected to the NMS.
     
     ```
     [~PE] ip vpn-instance ccu_private_vpn
     ```
     ```
     [*PE-vpn-instance-ccu_private_vpn] quit
     ```
     ```
     [*PE] interface gigabitethernet 0/1/0
     ```
     ```
     [*PE-GigabitEthernet0/1/0] ip binding vpn-instance ccu_private_vpn
     ```
     ```
     [*PE-GigabitEthernet0/1/0] commit
     ```
     ```
     [~PE-GigabitEthernet0/1/0] quit
     ```
  3. Configure SNMP proxy.
     
     ```
     [~PE] snmp-agent password min-length 10
     ```
     ```
     [*PE] commit
     ```
     ```
     [~PE] snmp-agent proxy community snmpv3_proxy@ccu remote-engineid 800007DB0338EBD9210010
     ```
     ```
     [*PE] snmp-agent proxy rule proxy_rule_read@ccu read remote-engineid 800007DB0338EBD9210010 target-host proxy_host params-in securityname snmpv3 v3 authentication
     ```
     ```
     [*PE] snmp-agent proxy rule proxy_rule_write@ccu write remote-engineid 800007DB0338EBD9210010 target-host proxy_host params-in securityname snmpv3 v3 authentication
     ```
     ```
     [*PE] snmp-agent proxy rule proxy_rule_trap@ccu trap remote-engineid 800007DB0338EBD9210010 target-host proxy_host params-in securityname snmpv3 v3 authentication
     ```
     ```
     [*PE] snmp-agent proxy rule proxy_rule_inform@ccu inform remote-engineid 800007DB0338EBD9210010 target-host proxy_host params-in securityname snmpv3 v3 authentication
     ```
     ```
     [*PE] snmp-agent proxy target-host proxy_host@NMS address udp-domain 2.1.1.1 udp-port 162 vpn-instance ccu_private_vpn params securityname snmpv3 v3 authentication
     ```
     ```
     [*PE] snmp-agent proxy target-host proxy_host@ccu address udp-domain 192.168.1.100 udp-port 161 public-net params securityname snmpv3 v3 authentication
     ```
     ```
     [*PE] snmp-agent remote-engineid 800007DB0338EBD9210010 usm-user v3 snmpv3
     ```
     ```
     [*PE] snmp-agent proxy protocol source-status all-interface
     ```
     ```
     [*PE] commit
     ```
* Configure the managed device.
  
  
  1. Configure the interface IP address used by the managed device to communicate with the middle-point device.
     
     This step is similar to configuring the interface IP addresses used by the middle-point device to communicate with the NMS and managed device.
  2. Configure SNMP.
     
     + To configure SNMPv1, see [Example for Configuring a Device to Communicate with an NMS Through SNMPv1](dc_vrp_snmp_cfg_0023.html).
     + To configure SNMPv2c, see [Example for Configuring a Device to Communicate with an NMS Through SNMPv2c](dc_vrp_snmp_cfg_0024.html).
     + To configure SNMPv3, see [Example for Configuring a Device to Communicate with an NMS Through a USM SNMPv3 User](dc_vrp_snmp_cfg_0025.html).
* Verify the configuration.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The following operations can be performed only on the middle-point device.
  
  # Run the [**display snmp-agent proxy community**](cmdqueryname=display+snmp-agent+proxy+community) command to check SNMP Proxy community information.
  
  ```
  [~PE] display snmp-agent proxy community
  ```
  ```
     Proxy Community name : %#%#qTp*MccD#Z[sHw4"pbzVHzAfO]gWN;h#30K=)%}X1jIHNF<QdMskYG$9xj:9k\EZN6Mi!Hrt@\Oa8tqP%#%#
         Remote engine ID : 800007DB0338EBD9210010 active
         Storage-type     : nonVolatile
  ```
  
  # Run the [**display snmp-agent proxy rule**](cmdqueryname=display+snmp-agent+proxy+rule) command to check the proxy rules for SNMP packets.
  
  ```
  [~PE] display snmp-agent proxy rule
  ```
  ```
     Proxy Rule name : proxy_rule_inform@ccu
         Type             : inform
         Remote engine ID : 800007DB0338EBD9210010
         Host name        : proxy_host
         Security name    : snmpv3
         Version          : v3
         Level            : Authentication
  
     Proxy Rule name : proxy_rule_read@ccu
         Type             : read
         Remote engine ID : 800007DB0338EBD9210010
         Host name        : proxy_host
         Security name    : snmpv3
         Version          : v3
         Level            : Authentication
  
     Proxy Rule name : proxy_rule_trap@ccu
         Type             : trap
         Remote engine ID : 800007DB0338EBD9210010
         Host name        : proxy_host
         Security name    : snmpv3
         Version          : v3
         Level            : Authentication
  
     Proxy Rule name : proxy_rule_write@ccu
         Type             : write
         Remote engine ID : 800007DB0338EBD9210010
         Host name        : proxy_host
         Security name    : snmpv3
         Version          : v3
         Level            : Authentication
  ```
  
  Run the [**display snmp-agent proxy target-host**](cmdqueryname=display+snmp-agent+proxy+target-host) command to check target host information.
  
  ```
  [~PE] display snmp-agent proxy target-host
  ```
  ```
  Proxy target-host NO. 1
  -----------------------------------------------------------
    Host-name        : proxy_host@NMS
    IP-address       : 2.1.1.1
    Port             : 162
    Timeout          : 15
    Source interface : -
    VPN instance     : ccu_private_vpn
    Security name    : snmpv3
    Version          : v3
    Level            : Authentication
  -----------------------------------------------------------
  
  Proxy target-host NO. 2
  -----------------------------------------------------------
    Host-name        : proxy_host@ccu
    IP-address       : 192.168.1.100
    Port             : 161
    Timeout          : 15
    Source interface : -
    VPN instance     : -
    Security name    : snmpv3
    Version          : v3
    Level            : Authentication
  -----------------------------------------------------------
  ```

#### Configuration Files

```
#
sysname PE
#
interface GigabitEthernet0/1/0
 undo shutdown
 ip address 3.1.1.1 255.255.255.0
 ip binding vpn-instance ccu_private_vpn
#
interface GigabitEthernet0/1/1
 undo shutdown
 ip address 192.168.1.1 255.255.255.0
#
ip vpn-instance ccu_private_vpn
#
snmp-agent
snmp-agent password min-length 10
snmp-agent local-engineid 800007DB0338EBD9310010
#
snmp-agent sys-info version v3
#
snmp-agent proxy community cipher %$%$"P!/>~x\cUQ,_tK8-PY7,*!u%$%$ remote-engineid 800007DB0338EBD9210010
#
snmp-agent proxy protocol source-status all-interface
#
snmp-agent remote-engineid 800007DB0338EBD9210010 usm-user v3 snmpv3
#
snmp-agent proxy target-host proxy_host@NMS address udp-domain 2.1.1.1 udp-port 162 vpn-instance ccu_private_vpn params securityname snmpv3 v3 authentication
snmp-agent proxy target-host proxy_host@ccu address udp-domain 192.168.1.100 udp-port 161 public-net params securityname snmpv3 v3 authentication
#
snmp-agent proxy rule proxy_rule_read@ccu read remote-engineid 800007DB0338EBD9210010 target-host proxy_host params-in securityname snmpv3 v3 authentication
snmp-agent proxy rule proxy_rule_write@ccu write remote-engineid 800007DB0338EBD9210010 target-host proxy_host params-in securityname snmpv3 v3 authentication
snmp-agent proxy rule proxy_rule_trap@ccu trap remote-engineid 800007DB0338EBD9210010 target-host proxy_host params-in securityname snmpv3 v3 authentication
snmp-agent proxy rule proxy_rule_inform@ccu inform remote-engineid 800007DB0338EBD9210010 target-host proxy_host params-in securityname snmpv3 v3 authentication
#
return
```