display lldp tlv-config
=======================

display lldp tlv-config

Function
--------



The **display lldp tlv-config** command displays statistics about optional TLVs that all interfaces send or optional type-length-values (TLVs) that a specified interface sends.




Format
------

**display lldp tlv-config** [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays information about optional TLVs that a specified interface sends. | - |
| *interface-name* | Specifies an interface name. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To check whether the TLVs that need to be sent have been configured and whether the TLVs that do not need to be sent have been canceled, run the **display lldp tlv-config** command to check information about optional TLVs that can be sent by all interfaces or a specified interface.If no interface is specified, information about optional TLVs that can be sent by all interfaces on the device is displayed.



**Prerequisites**



LLDP has been globally enabled using the lldp enable command in the system view, and LLDP has also been enabled on interfaces using the lldp enable command in the interface view.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the optional TLVs that can be sent by 100GE 1/0/1.
```
<HUAWEI> display lldp tlv-config interface 100ge 1/0/1
LLDP tlv-config of port [100GE 1/0/1]:
-----------------------------------------------------
Name                                Status    Default
-----------------------------------------------------
                                                     
Basic optional TLV:                                  
-------------------------------------------------
Port Description TLV                Yes       Yes    
System Name TLV                     Yes       Yes    
System Description TLV              Yes       Yes    
System Capabilities TLV             Yes       Yes    
Management Address TLV              Yes       Yes    
                                                     
IEEE 802.1 extend TLV:                               
-------------------------------------------------
Port VLAN ID TLV                    Yes       Yes    
Port And Protocol VLAN ID TLV       Yes       Yes    
VLAN Name TLV                       Yes       Yes    
Protocol Identity TLV               No        No     
                                                     
IEEE 802.3 extend TLV:                               
-------------------------------------------------
MAC-Physic TLV                      Yes       Yes    
Link Aggregation TLV                Yes       Yes    
Maximum Frame Size TLV              Yes       Yes
DCBX TLV                            No        No        
Identity TLV                        No        No

```

**Table 1** Description of the **display lldp tlv-config** command output
| Item | Description |
| --- | --- |
| LLDP tlv-config of port | Information about optional TLVs that can be advertised. |
| Name | TLV type:   * Basic optional TLV: * Port Description TLV. * System Name TLV. * System Description TLV. * System Capabilities TLV. * Management-address TLV. * IEEE 802.1 extend TLV: * Port VLAN TLV. * Port And Protocol VLAN ID TLV. * VLAN Name TLV. * Protocol Identity TLV. * IEEE 802.3 extend TLV: * MAC-Physic TLV. * Link Aggregation TLV. * Maximum Frame Size TLV. * DCBX TLV. * Identity TLV. |
| Status | Whether an interface can advertise TLVs of specified types:   * Yes. * No. |
| Default | Whether an interface can advertise TLVs of specified types by default:   * Yes. * No. |