display ptp
===========

display ptp

Function
--------



The **display ptp** command displays 1588v2 running information.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ptp all** [ **config** | **state** ]

**display ptp interface** *interface-type* *interface-number*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **config** | Displays the configurations of all 1588v2-related modules on the current device. | - |
| **state** | Displays the protocol running status of all 1588v2-related modules on the current device. | - |
| **interface** *interface-type* *interface-number* | Displays statistics about the 1588v2 messages sent and received on a specified interface. | - |
| **all** | Displays all 1588v2 statistics on the current device. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



You can run this command to check the running status of a 1588v2-enabled device.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display 1588v2 module information.
```
<HUAWEI> display ptp all
  Device config info                                                            
  ------------------------------------------------------------------------------
  PTP state         :enabled              Domain  value      :2                 
  Slave only        :no                   Device type        :BC                
  Set port state    :no                   Local clock ID     :00259e1000000001  
  Acl               :no                   Virtual clock ID   :yes               
  Acr               :no                   Time lock success  :yes               
  Asymmetry measure :disable              Passive measure    :disable           
                                                                                
  BMC run info                                                                  
  ------------------------------------------------------------------------------
  Grand clock ID    :00259e1000000002                                           
  Receive number    :100GE1/0/1                                                  
  Parent clock ID   :00259e1000000002                                           
  Parent portnumber :4126                                                       
  Priority1         :190                 Priority2           :128               
  Step removed      :0                   Clock accuracy      :0x31              
  Clock class       :187                 Time Source         :0xa0              
  UTC Offset        :35                  UTC Offset Valid    :False             
  Timescale         :ARB                 Time traceable      :False             
  Leap              :None                Frequency traceable :False             
  Offset scaled     :0xffff              Sync uncertain      :False                                      
                                                                                
  Port info                                                                     
  Name                        State        Delay-mech Ann-timeout Type   Domain 
  ------------------------------------------------------------------------------
  100GE1/0/1                   slave        delay      4           BC     2      
  100GE1/0/2                   passive      delay      3           BC     2      
                                                                                
  Time Performance Statistics(ns): Slot 1  Card 0  Port 1                       
  ------------------------------------------------------------------------------
  Realtime(T2-T1)   :200                     Pathdelay     :0                   
  Max(T2-T1)        :215                                                        
  Min(T2-T1)        :-2740362189                                                
                                                                                
  Clock source info                                                             
  Clock       Pri1 Pri2 Accuracy Class TimeSrc Signal Switch Direction In-Status
  ------------------------------------------------------------------------------
  local       210  128  0x31     187   0xa0    -      -      -         -

```

# Display statistics about the 1588v2 messages sent and received on 100GE 1/0/1.
```
<HUAWEI> display ptp interface 100ge 1/0/1
  Port State      :slave                                                        
  Port Clock ID   :00259e1000000001                                             
  Port Number     :2052                                                         
  Port Precision Capability :High precision clock
  Port Precision Work Mode  :High precision clock
  Announce-interval :4                                                          
  Grand clock ID    :00259e1000000002                                           
  Receive number    :100GE1/0/1                                                  
  Parent clock ID   :00259e1000000002                                           
  Parent portnumber :4126                                                       
  Priority1         :190                 Priority2           :128               
  Step removed      :0                   Clock accuracy      :0x31              
  Clock class       :187                 Time Source         :0xa0              
  UTC Offset        :35                  UTC Offset Valid    :False             
  Timescale         :ARB                 Time traceable      :False             
  Leap              :None                Frequency traceable :False             
  Offset scaled     :0xffff              Sync uncertain      :False                                       
                                                                                
  Recv Packet Statistics                                                        
  -----------------------------------------------------------------------       
  Announce               :1338092    Sync                       :1338016        
  Req                    :0          Resp                       :1337958        
  Followup               :1338016    Pdelay_resp_followup       :0              
                                                                                
  Send Packet Statistics                                                        
  -----------------------------------------------------------------------       
  Announce               :75         Sync                       :72             
  Req                    :1337960    Resp                       :0              
  Followup               :72         Pdelay_resp_followup       :0              
                                                                                
  Discard Packet Statistics                                                     
  -----------------------------------------------------------------------       
  Announce               :7          Sync                       :80             
  Delayreq               :0          Pdelayreq                  :0              
  Resp                   :3          Pdelayresp                 :0              
  Followup               :80         Pdelay_resp_followup       :0

```

# Display the configurations of all PTP modules on the device.
```
<HUAWEI> display ptp all config
  Device config info
  ------------------------------------------------------------------------------
  PTP state         :enabled              Domain  value      :0
  Slave only        :no                   Device type        :no mode
  Set port state    :no                   Local clock ID     :00259e1000000001
  Acl               :no                   Virtual clock ID   :no
  Acr               :no                   Time lock success  :no
  Asymmetry measure :disable              Passive measure    :disable

  Clock source info
  Clock       Pri1 Pri2 Accuracy Class TimeSrc Signal Switch Direction In-Status
  ------------------------------------------------------------------------------
  local       120  128  0x31     187   0xa0    -      -      -         
System:
 ptp send-gm-wtr 0

```

**Table 1** Description of the **display ptp** command output
| Item | Description |
| --- | --- |
| ptp send-gm-wtr | The waiting time for sending the grand master information after the device changes from the unlocked state to the locked state is 0. Currently, the waiting time cannot be configured on the device. |
| Device config info | Device configuration information. |
| Device type | Device type. |
| PTP state | Whether 1588v2 is enabled. |
| Domain value | Device threshold. |
| Slave only | The slave-only attribute of the device. |
| Set port state | Whether static clock source selection is enabled. |
| Local clock ID | ID of a local clock. |
| Acl | Whether the clock source selection restriction function is enabled. |
| Virtual clock ID | Whether the virtual clock ID is set. |
| Acr | Whether statically 1588v2 adaptive clock recovery (ACR) is enabled. |
| Time lock success | Time lock status of the device. |
| Time Source | Time source that the GMC uses. |
| Time traceable | Whether the currentUtcOffset value of the GMC is synchronized with primary reference clock source. |
| Time Performance Statistics | Time attribute value of a device. |
| Time Performance Statistics(ns) | Time performance statistics (nanosecond). |
| Asymmetry measure | Whether automatic ring network measurement is enabled. |
| Passive measure | Whether performance monitoring is enabled on the passive interface. |
| BMC run info | Best master clock (BMC) running information. |
| Grand clock ID | ID of the grandmaster clock (GMC). |
| Receive number | Port for receiving the Ebest data set. |
| Parent clock ID | ID of the parent clock. |
| Parent portnumber | Parent clock port number. |
| Priority1 | Priority 1 of the grand master clock. |
| Priority2 | Priority 2 of the grand master clock. |
| Step removed | Number of communication channels between the local clock and the grand master clock. |
| Clock accuracy | Grand master clock precision. |
| Clock class | Grand master clock level. |
| Clock source info | Local clock source and BITS source information. |
| Clock | Clock information. |
| UTC Offset | UTC offset value of the GMC. |
| UTC Offset Valid | Whether the UTC offset value of the GMC is known to be correct. |
| Offset scaled | Grand master clock stability. |
| Timescale | Time-scale of the GMC. |
| Leap | Leap value of the GMC. |
| Frequency traceable | Whether the time-scale frequency of the GMC is synchronized with the primary reference clock source. |
| Sync | Statistics of Sync packets. |
| Sync uncertain | Unstable time synchronization flag. |
| Port info | Device port information. |
| Port Precision Capability | Precision capability supported by the subcard. |
| Port Precision Work Mode | Port precision working mode. |
| Port Number | Port number of the clock source. |
| Port Clock ID | Port clock ID. |
| Port State | Port status. |
| Realtime(T2-T1) | Real-time deviation between the T2 timestamp and the T1 timestamp. |
| Pathdelay | Path delay. |
| Max(T2-T1) | Indicates the maximum offset between the T2 timestamp and the T1 timestamp. |
| Min(T2-T1) | Indicates the minimum offset between the T2 timestamp and the T1 timestamp. |
| Pri1 | Priority 1. |
| Pri2 | Priority 2. |
| Accuracy | Accuracy. |
| Class | Clock stratum. |
| TimeSrc | Time source. |
| Signal | Signal type. |
| Switch | Signal switch. |
| Direction | Signal direction. |
| In-Status | Input source status. |
| Announce-interval | Announce packet sending interval. |
| Recv Packet Statistics | Statistics of received packets. |
| Announce | Number of Announce packets. |
| Req | Number of Req packets. |
| Resp | Number of Resp packets. |
| Followup | Number of Followup packets. |
| Pdelay\_resp\_followup | Number of Pdelay resp followup packets. |
| Send Packet Statistics | Statistics on sent packets. |
| Discard Packet Statistics | Statistics on discarded packets. |
| Delayreq | Statistics of Delayreq packets. |
| Pdelayreq | Statistics of Pdelayreq packets. |
| Pdelayresp | Statistics of Pdelayresp packets. |