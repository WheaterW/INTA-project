display arp fast-reply statistics
=================================

display arp fast-reply statistics

Function
--------



The **display arp fast-reply statistics** command displays statistics on ARP fast reply packets.




Format
------

**display arp fast-reply statistics**

**display arp fast-reply statistics interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface. | - |
| **interface** *interface-name* | Specifies an interface name. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to check the processing of ARP packets after the ARP fast reply function is enabled.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics on all ARP fast reply packets.
```
<HUAWEI> display arp fast-reply statistics
Status : Enable                                                                                                                     
                                                                                                                                    
Slot                      Received request          Sent reply                                                                      
-----------------------------------------------------------------------------                                                       
1                         67                        58                                                                              
-----------------------------------------------------------------------------

```

# Display statistics on ARP fast reply packets on Vlanif 100.
```
<HUAWEI> display arp fast-reply statistics interface Vlanif 100
Status : Enable                                                                                                                     
                                                                                                                                    
Interface                 Received request          Sent reply                                                                      
-----------------------------------------------------------------------------                                                       
Vlanif 100                0                         0

```

**Table 1** Description of the **display arp fast-reply statistics** command output
| Item | Description |
| --- | --- |
| Status | Status of ARP fast reply on the device:  Enable: ARP fast reply is enabled.  Disable: ARP fast reply is disabled. |
| Slot | Slot ID. |
| Received request | Number of received ARP requests. |
| Sent reply | Number of processed ARP requests. |
| Interface | Type and number of an interface. |