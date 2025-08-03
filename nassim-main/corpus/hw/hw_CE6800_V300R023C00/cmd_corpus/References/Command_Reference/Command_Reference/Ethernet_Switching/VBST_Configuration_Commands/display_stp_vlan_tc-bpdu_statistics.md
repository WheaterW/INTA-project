display stp vlan tc-bpdu statistics
===================================

display stp vlan tc-bpdu statistics

Function
--------



The **display stp vlan tc-bpdu statistics** command displays statistics of sent and received topology change (TC) and topology change notification (TCN) BPDUs on interfaces.




Format
------

**display stp vlan** [ *vlan-id* ] **tc-bpdu** **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Display statistics on sent and received TC and TCN BPDUs on ports in a specified VLAN.  If vlan vlan-id is not specified, statistics on sent and received TC and TCN BPDUs on ports in all VLANs are displayed. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If you need to know whether a fault has occurred on interfaces that send and receive TC/TCN BPDUs, you can run this command to view statistics of these BPDUs and locate the fault.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics on sent and received TC and TCN BPDUs on ports running VBST.
```
<HUAWEI> display stp vlan 10 tc-bpdu statistics
VBST TC/TCN information:                                                                                                            
---------------------------------------------------------------------------                                                         
VLANID Interface              TC(Send/Receive)       TCN(Send/Receive)                                                              
---------------------------------------------------------------------------                                                         
    10 100GE1/0/1             (0)/(0)                (0)/(0)                                                                        
    10 100GE1/0/2             (2)/(6)                (0)/(0)                                                                        
---------------------------------------------------------------------------

```

**Table 1** Description of the **display stp vlan tc-bpdu statistics** command output
| Item | Description |
| --- | --- |
| VLANID | VLAN ID. |
| Interface | Interface name. |
| TC(Send/Receive) | Statistics of sent and received TC BPDUs. |
| TCN(Send/Receive) | Statistics of sent and received TCN BPDUs. ("-" indicates that MSTP instances except MSTP instance 0 do not have TCN BPDUs sent and received.). |