Example for Configuring a Device to Communicate with an NMS Using an SNMP Proxy
===============================================================================

Example for Configuring a Device to Communicate with an NMS Using an SNMP Proxy

#### Networking Requirements

An NMS can manage NEs through SNMP. However, an increase in the number of NEs is directly proportional to higher management costs.

To reduce management costs, configure a middle-point device as the SNMP proxy, as shown in [Figure 1](#EN-US_TASK_0000001512830830__fig_dc_cfg_snmp_0076). After the configuration is complete, the NMS considers the middle-point device and managed device as an independent NE. This reduces the number of NEs that the NMS needs to manage, which in turn reduces management costs.**Figure 1** Network diagram for configuring a device to communicate with an NMS using an SNMP proxy![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001563990733.png)


#### Configuration Roadmap

The configuration roadmap is as follows:

* Configure the middle-point device.
  
  1. Configure IP addresses for interfaces that connect the middle-point device to the NMS and managed device.
  2. Configure the middle-point device as an SNMP proxy, enabling it to access the managed device based on the configured parameters for management.
* Configure the managed device.
  
  1. Configure an IP address for the interface that connects the managed device to the middle-point device.
  2. Configure SNMP for the managed device to communicate with the NMS.

#### Procedure

1. Configure an IP address for the interface on the middle-point device.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan 100
   [*DeviceA-vlan100] quit
   [*DeviceA] interface vlanif 100
   [*DeviceA-Vlanif100] ip address 10.1.1.1 24
   [*DeviceA-Vlanif100] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk pvid vlan 100
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 100
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] vlan 200
   [*DeviceA-vlan200] quit
   [*DeviceA] interface vlanif 200
   [*DeviceA-Vlanif200] ip address 192.168.1.1 24
   [*DeviceA-Vlanif200] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] port trunk pvid vlan 200
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 200
   [*DeviceA-100GE1/0/2] quit
   ```
2. Configure the middle-point device as the SNMP proxy.
   
   
   ```
   [*DeviceA] snmp-agent remote-engineid 800007DB0338EBD9210010 usm-user v3 snmpv3
   [*DeviceA] snmp-agent remote-engineid 800007DB0338EBD9210010 usm-user v3 snmpv3 authentication-mode sha
   Please configure the authentication password (8-255)                            
   Enter Password:              
   Confirm Password:           
   
   ```
   ```
   [*DeviceA] snmp-agent remote-engineid 800007DB0338EBD9210010 usm-user v3 snmpv3 privacy-mode aes256
   Please configure the privacy password (8-255)                                   
   Enter Password:          
   Confirm Password: 
   ```
   ```
   [*DeviceA] snmp-agent proxy rule proxy_rule_read read remote-engineid 800007DB0338EBD9210010 target-host proxy_host params-in securityname snmpv3 v3 privacy
   [*DeviceA] snmp-agent proxy rule proxy_rule_write write remote-engineid 800007DB0338EBD9210010 target-host proxy_host params-in securityname snmpv3 v3 privacy
   [*DeviceA] snmp-agent proxy target-host proxy_host@NMS address udp-domain 10.1.2.1 udp-port 162 params securityname snmpv3 v3 privacy
   [*DeviceA] commit
   [~DeviceA] quit
   ```
3. Configure the managed device.
   
   
   
   For details about how to configure SNMPv3, see [Example for Configuring a Device to Communicate with NMSs Using SNMPv3 USM Users](vrp_snmp_cfg_0049.html).
4. Verify the configuration.
   
   
   
   # Check the proxy rules for SNMP messages.
   
   ```
   <DeviceA> display snmp-agent proxy rule
      Proxy rule name : proxy_rule_read
          Type             : read
          Remote engine ID : 800007DB0338EBD9210010
          Host name        : proxy_host
          Security name    : snmpv3
          Version          : v3
          Level            : Privacy
   
      Proxy rule name : proxy_rule_write
          Type             : write
          Remote engine ID : 800007DB0338EBD9210010
          Host name        : proxy_host
          Security name    : snmpv3
          Version          : v3
          Level            : Privacy
   ```
   
   # Check the target host information of the SNMP proxy.
   
   ```
   <DeviceA> display snmp-agent proxy target-host
   Proxy target host NO. 1
   -----------------------------------------------------------
     Host name        : proxy_host@NMS
     IP address       : 10.1.2.1
     Port             : 162
     Timeout          : 15
     Source interface : -
     VPN instance     : -
     Security name    : snmpv3
     Version          : v3
     Level            : Privacy
   -----------------------------------------------------------
   ```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
vlan batch 100 200
#
interface Vlanif100
 ip address 10.1.1.1 255.255.255.0
#
interface Vlanif200
 ip address 192.168.1.1 255.255.255.0
#
interface 100GE1/0/1
 port link-type trunk                                                           
 port trunk pvid vlan 100                                                       
 port trunk allow-pass vlan 100      
#
interface 100GE1/0/2
 port link-type trunk                                                           
 port trunk pvid vlan 200                                                       
 port trunk allow-pass vlan 200      
#
snmp-agent                                                                      
snmp-agent local-engineid 800007DB03001974593301 
#
snmp-agent sys-info version v3  
#                                                                              
snmp-agent remote-engineid 800007DB0338EBD9210010 usm-user v3 snmpv3         
snmp-agent remote-engineid 800007DB0338EBD9210010 usm-user v3 snmpv3 authentication-mode sha cipher %+%##!!!!!!!!!"!!!!"!!!!*!!!!PR=uJ|5'u%{Ku|VKwEyE-uN:Pp9K`O+oLF,!!!!!2jp5!!!!!!<!!!!6r!o;)ju=D<fXX.r3a`QWe'gPol7aEif^M'!!!!!%+%#                         
snmp-agent remote-engineid 800007DB0338EBD9210010 usm-user v3 snmpv3 privacy-mode aes256 cipher %+%##!!!!!!!!!"!!!!"!!!!*!!!!PR=uJ|5'u%B.79IwRIE3(xTzFsYNQ5iH4;X!!!!!2jp5!!!!!!<!!!!A"X3:)AC815G!a6]bVc8-wj'EK9!&V<M0HP!!!!!%+%#                           
#                                                                               
snmp-agent proxy target-host proxy_host@NMS address udp-domain 10.1.2.1 udp-port 162 params securityname snmpv3 v3 privacy                                
#                                                                               
snmp-agent proxy rule proxy_rule_read read remote-engineid 800007DB0338EBD9210010 target-host proxy_host params-in securityname snmpv3 v3 privacy               
snmp-agent proxy rule proxy_rule_write write remote-engineid 800007DB0338EBD9210010 target-host proxy_host params-in securityname snmpv3 v3 privacy             
#                                                    
return
```