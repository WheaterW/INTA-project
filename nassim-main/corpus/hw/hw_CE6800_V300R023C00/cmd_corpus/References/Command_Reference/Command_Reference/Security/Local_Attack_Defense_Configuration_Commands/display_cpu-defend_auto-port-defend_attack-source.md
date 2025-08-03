display cpu-defend auto-port-defend attack-source
=================================================

display cpu-defend auto-port-defend attack-source

Function
--------



The **display cpu-defend auto-port-defend attack-source** command displays source tracing information on interfaces.




Format
------

**display cpu-defend auto-port-defend attack-source** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value must be set according to the device configuration. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The source tracing information helps you locate attack sources.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the source tracing information on the interfaces of the device.
```
<HUAWEI> display cpu-defend auto-port-defend attack-source
Attack source table on Slot 1 :                                                                                                     
--------------------------------------------------------------------------------                                                    
Interface      Protocol            Expire(s) PacketRate(pps) LastAttackTime                                                         
--------------------------------------------------------------------------------                                                    
100GE1/0/1     arp-request         296       2854            2020-05-11 23:51:25                                                    
--------------------------------------------------------------------------------                                                    
Total: 1

```

**Table 1** Description of the **display cpu-defend auto-port-defend attack-source** command output
| Item | Description |
| --- | --- |
| Attack source table on Slot 1 | Source tracing information on the interfaces of device. |
| Interface | Name of the attacked interface. |
| Protocol | Attack packet type. |
| Expire(s) | Remaining time of the aging time for port attack defense.  If the Expire(s) field of an entry displays 0, this entry will be deleted after a certain period (a maximum of 10 seconds). |
| PacketRate(pps) | Rate of the last received attack packet. |
| LastAttackTime | Time when the last attack packet is received. |
| Total | Number of source tracing records. |