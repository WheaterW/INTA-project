Example for Configuring a Device to Communicate with an NMS Through SNMPv2c
===========================================================================

This section provides an example to describe how to configure a device to communicate with an NMS through SNMPv2c and how to specify the MIB objects that can be managed by the NMS.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172361038__fig_dc_vrp_snmp_cfg_002401), two NMSs (NMS1 and NMS2) and the Router are connected across a public network. According to the network planning, NMS2 can manage every MIB object on the Router, and NMS1 does not manage the Router.

On the Router, only the modules that are enabled by default are allowed to send alarms to NMS2. This prevents an excess of unwanted alarms from being sent to NMS2. Excessive alarms make fault location difficult. Inform messages need to be used to ensure that alarms are received by NMS2 because alarms sent by the Router have to travel across the public network to reach NMS2.

Contact information of the device administrator needs to be configured on the Router. This helps the NMS administrator contact the device administrator if a fault occurs.

**Figure 1** Networking diagram for configuring a device to communicate with an NMS through SNMPv2c  
![](images/fig_dc_vrp_snmp_cfg_002401.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the SNMP agent.
2. Configure the Router to run SNMPv2c.
3. Configure a source interface for SNMP to receive and respond to NMS request packets.
4. Configure an ACL to allow NMS2 to manage every MIB object on the Router.
5. Configure the Inform function to allow the Router to send Inform messages to NMS2.
6. Configure the contact information of the device administrator.
7. Configure NMS2.

#### Data Preparation

To complete the configuration, you need the following data:

* SNMP version
* Community name
* ACL number
* IP address of the NMS
* Contact information of the device administrator

#### Procedure

1. Configure available routes between the Router and the NMSs. Details for the configuration procedure are not provided here.
2. Enable the SNMP agent.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] snmp-agent password min-length 10
   ```
   ```
   [*HUAWEI] snmp-agent
   ```
   ```
   [*HUAWEI] commit
   ```
3. Configure the Router to run SNMPv2c.
   
   
   ```
   [~DeviceA] snmp-agent sys-info version v2c
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Check the configured SNMP version.
   
   ```
   [~DeviceA] display snmp-agent sys-info version
   ```
   ```
   SNMP version running in the system:
   ```
   ```
              SNMPv2c SNMPv3
   ```
4. Configure a source interface for SNMP to receive and respond to NMS request packets.
   
   
   ```
   [~DeviceA] snmp-agent protocol source-interface Loopback0
   ```
   ```
   [*DeviceA] commit
   ```
5. Configure access permissions of the NMSs.
   
   # Configure an ACL to allow NMS2 to manage and disallow NMS1 from managing the Router.
   ```
   [~DeviceA] acl 2001
   ```
   ```
   [*DeviceA-acl4-basic-2001] rule 5 permit source 1.1.1.2 0.0.0.0
   ```
   ```
   [*DeviceA-acl4-basic-2001] rule 6 deny source 1.1.1.1 0.0.0.0
   ```
   ```
   [*DeviceA-acl4-basic-2001] commit
   ```
   ```
   [~DeviceA-acl4-basic-2001] quit
   ```
   
   # Configure a MIB view.
   
   ```
   [~DeviceA] snmp-agent mib-view excluded allexthgmp 1.3.6.1.4.1.2011.6.7
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure a community name to reference an ACL to allow NMS2 to manage the objects in the MIB view.
   
   ```
   [~DeviceA] snmp-agent community write adminnms2 mib-view allexthgmp acl 2001
   ```
   ```
   [*DeviceA] commit
   ```
6. Configure the trap function.
   
   
   ```
   [~DeviceA] snmp-agent target-host inform address udp-domain 1.1.1.2 params securityname cipher YsHsjx_202206 v2c
   ```
   ```
   [*DeviceA] snmp-agent inform timeout 5 resend-times 6 pending 7
   ```
   ```
   [*DeviceA] snmp-agent trap enable
   ```
   ```
   [*DeviceA] snmp-agent notification-log enable
   [*DeviceA] snmp-agent notification-log global-ageout 24
   ```
   ```
   [*DeviceA] commit
   ```
7. Configure the contact information of the device administrator.
   
   
   ```
   [~DeviceA] snmp-agent sys-info contact call Operator at 010-12345678
   ```
   ```
   [*DeviceA] commit
   ```
8. Configure NMS2.
   
   
   
   For details on how to configure NMS2, see the relevant NMS configuration guide.
9. Verify the configuration.
   
   
   
   After the configuration is complete, run the following commands to verify that the configuration has taken effect.
   
   # Check the configured SNMP version.
   
   ```
   [~DeviceA] display snmp-agent sys-info version
   ```
   ```
   SNMP version running in the system:
   ```
   ```
              SNMPv2c
   ```
   
   # Check information about the SNMP community name.
   
   ```
   <DeviceA> display snmp-agent community
   ```
   ```
      Community name: %#%#qTp*MccD#Z[sHw4"pbzVHzAfO]gWN;h#30K=)%}X1jIHNF<QdMskYG$9xj:9k\EZN6Mi!Hrt@\Oa8tqP%#%#
          Group name: %#%#qTp*MccD#Z[sHw4"pbzVHzAfO]gWN;h#30K=)%}X1jIHNF<QdMskYG$9xj:9k\EZN6Mi!Hrt@\Oa8tqP%#%#
          Acl: 2001        Storage-type: nonVolatile
   ```
   # Check the configured ACL.
   ```
   <DeviceA> display acl 2001
   ```
   ```
   Basic ACL 2001, 2 rules
   Acl's step is 5
    rule 5 permit source 1.1.1.2 0 (0 times matched)
    rule 6 deny source 1.1.1.1 0 (0 times matched)
   ```
   
   # Check the MIB view.
   
   ```
   <DeviceA> display snmp-agent mib-view viewname allexthgmp
   ```
   ```
   View name: allexthgmp
          MIB Subtree: huaweiUtility.7
          Subtree mask: FF80(Hex)
          Storage-type: nonVolatile
          View Type: excluded
          View status: active 
   
   ```
   
   # Check the target host.
   
   ```
   <DeviceA> display snmp-agent target-host
   Target-host NO. 1
   ---------------------------------------------------------------------------
     Host-name                        : -
     IP-address                       : 1.1.1.1
     Source interface                 : -
     VPN instance                     : -
     Security name                    : %#%#&NchK)p777^{b1BQtds=_<$O.<~qR.DDbwYS3_G6%#%#
     Port                             : 162
     Type                             : inform
     Version                          : v2c
     Level                            : No authentication and privacy
     NMS type                         : NMS
     With ext-vb                      : Yes
     Notification filter profile name : -
   ---------------------------------------------------------------------------
   ```
   
   # Check the contact information of the device administrator.
   
   ```
   <DeviceA> display snmp-agent sys-info contact
   The contact person for this managed node:
              call Operator at 010-12345678 
   ```

#### Configuration Files

```
#
sysname DeviceA
# 
acl number 2001
 rule 5 permit source 1.1.1.2 0.0.0.0
 rule 6 deny source 1.1.1.1 0.0.0.0
#
interface GigabitEthernet0/1/0
 undo shutdown
 ip address 1.1.2.1 255.255.255.0
#
interface loopback0
 ip address 1.1.3.1 255.255.255.255
#
ospf 1
 area 0.0.0.0
  network 1.1.2.0 0.0.0.255
  network 1.1.3.1 0.0.0.0
#
snmp-agent
snmp-agent password min-length 10
snmp-agent local-engineid 800007DB03360102101100
snmp-agent community write %#%#qTp*MccD#Z[sHw4"pbzVHzAfO]gWN;h#30K=)%}X1jIHNF<QdMskYG$9xj:9k\EZN6Mi!Hrt@\Oa8tqP%#%# mib-view allexthgmp acl 2001
#
snmp-agent protocol source-interface Loopback0
#
snmp-agent sys-info contact call Operator at 010-12345678
snmp-agent sys-info version v2c
snmp-agent target-host inform address udp-domain 1.1.1.2 params securityname cipher %#%#&NchK)p777^{b1BQtds=_<$O.<~qR.DDbwYS3_G6%#%# v2c
#
snmp-agent mib-view excluded allexthgmp hwCluster
#
snmp-agent inform timeout 5
snmp-agent inform resend-times 6
snmp-agent inform pending 7    
snmp-agent notification-log enable
snmp-agent notification-log global-ageout 24
#
snmp-agent trap enable
#
return
```