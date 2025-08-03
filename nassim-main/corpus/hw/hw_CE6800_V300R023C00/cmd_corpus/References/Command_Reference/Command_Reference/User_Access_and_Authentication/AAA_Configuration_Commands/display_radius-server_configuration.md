display radius-server configuration
===================================

display radius-server configuration

Function
--------



The **display radius-server configuration** command displays the configurations of RADIUS server templates.




Format
------

**display radius-server configuration** [ **template** *template-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **template** *template-name* | Specifies the name of a RADIUS server template.  If this parameter is not specified, the configurations of all the RADIUS server templates are displayed. | The RADIUS server template must exist. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After the configuration of a RADIUS server template is completed or a RADIUS fault needs to be rectified, you can run this command to check whether the configuration of the RADIUS server template is correct.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of the RADIUS server template named shiva.
```
<HUAWEI> display radius-server configuration template shiva
  ------------------------------------------------------------------------------
  Server-template-name          :  shiva    
  Server-template-index         :  14                                      
  Protocol-version              :  standard                                     
  Traffic-unit                  :  B                                            
  Shared-secret-key             :  ****************                             
  Group-filter                  :  class                                        
  Timeout-interval(in second)   :  5                                            
  Retransmission                :  3                                            
  EndPacketSendTime             :  3                                            
  Dead time(in minute)          :  5                                            
  Domain-included               :  Original                                     
  NAS-IP-Address                :  -                                            
  Calling-station-id MAC-format :  xxxx-xxxx-xxxx                               
  Called-station-id MAC-format  :  XX-XX-XX-XX-XX-XX                            
  NAS-Port-ID format            :  New                                          
  Service-type                  :  -                                            
  Server algorithm              :  master-backup 
  Source ip address             :  1.1.1.1
  Source ipv6 address           :  2001:db8:1::11            
  Detect-interval(in second)    :  60                                           
  Detect up-server(in second)   :  0                                            
  Detect timeout(in second)     :  3                                            
  Testuser-username             :  test                                         
  Testuser-ciperpwd             :  ****************                             
  Chargeable-user-identity      :  Not Support                                  
  CUI Not reject                :  No                                           
  Authentication Server 1       :  10.7.66.67 Port:1812  Weight:80  [up]   
                                   Vrf:-                                        
                                   Source Interface:NULL                        
                                   Source IP: ::                                
  Authentication Server 2       :  10.7.66.66 Port:1812  Weight:80  [up]   
                                   Vrf:-                                        
                                   Source Interface:NULL                        
                                   Source IP: ::                                
  Accounting Server     1       :  10.7.66.67 Port:1813  Weight:80  [up]   
                                   Vrf:-                                        
                                   Source Interface:NULL                        
                                   Source IP: ::                                
  Accounting Server     2       :  10.7.66.66 Port:1813  Weight:80  [up]   
                                   Vrf:-                                        
                                   Source Interface:NULL                        
                                   Source IP: ::                                
  ------------------------------------------------------------------------------

```

**Table 1** Description of the **display radius-server configuration** command output
| Item | Description |
| --- | --- |
| Server-template-name | Name of a RADIUS server template. |
| Server-template-index | Index of the RADIUS server template. |
| Protocol-version | RADIUS protocol version:   * standard. * huawei. * iphotel. |
| Traffic-unit | Traffic unit in the RADIUS server template:   * B: Byte. * KB: Kilobyte. * MB: Megabyte. * GB: Gigabyte. |
| Shared-secret-key | Shared key in the RADIUS server template. |
| Group-filter | Filtering field of a user group. Currently, only the class field can be used as the filtering field of a user group. |
| Timeout-interval(in second) | Response timeout period of a RADIUS server. |
| Retransmission | Number of times RADIUS packets are retransmitted. |
| EndPacketSendTime | Number of times RADIUS Accounting-Stop packets are retransmitted. |
| Dead time(in minute) | Interval for the primary RADIUS server to revert to the active state. |
| Domain-included | Whether the RADIUS user name contains the domain name.   * YES: The user name contains the domain name. * NO: The user name does not contain the domain name. * Original: The device does not modify the user name entered by the user. * NO except eap: Configure other authentication modes except EAP authentication so that the user name in the packets sent from the device to the RADIUS server does not contain the domain name. |
| NAS-IP-Address | NAS-IP-Address attribute in RADIUS packets. |
| Calling-station-id MAC-format | Encapsulation format of the MAC address in the calling-station-id attribute of RADIUS packets. |
| Called-station-id MAC-format | Encapsulation format of the MAC address in the called-station-id attribute of RADIUS packets. |
| NAS-Port-ID format | Format of the NAS-Port-ID attribute on the RADIUS server. |
| Service-type | Service type. |
| Server algorithm | Algorithm for selecting RADIUS servers. |
| Source ip address | Source IPv4 address for communication between the device and RADIUS server. |
| Detect-interval(in second) | Automatic detection interval for RADIUS servers in Down state. |
| Detect up-server(in second) | Automatic detection interval for RADIUS servers in Up state. |
| Detect timeout(in second) | Timeout period for automatic RADIUS server detection packets. |
| Testuser-username | User name for automatic RADIUS server detection. |
| Testuser-ciperpwd | User password for automatic RADIUS server detection. |
| Chargeable-user-identity | Whether the device supports the CUI attribute. |
| CUI Not reject | Whether the device does not process the CUI attribute. |
| Authentication Server 1 | IP address, interface number, weight, status, VPN instance, source interface, and source IP address of the primary RADIUS authentication server. |
| Authentication Server 2 | IP address, interface number, weight, status, VPN instance, source interface, and source IP address of the secondary RADIUS authentication server. |
| Accounting Server 1 | IP address, interface number, weight, status, VPN instance, source interface, and source IP address of the primary RADIUS accounting server. |
| Accounting Server 2 | IP address, interface number, weight, status, VPN instance, source interface, and source IP address of the secondary RADIUS accounting server. |