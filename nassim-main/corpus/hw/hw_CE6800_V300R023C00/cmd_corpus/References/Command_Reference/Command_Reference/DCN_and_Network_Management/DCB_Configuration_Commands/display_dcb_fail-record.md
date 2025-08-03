display dcb fail-record
=======================

display dcb fail-record

Function
--------



The **display dcb fail-record** command displays DCB negotiation failure records on an interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dcb fail-record** [ **interface** { *interface-name* | *interface-type* *interface-num* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-num* | Displays DCB negotiation failure records on a specified interface.   * interface-type specifies the type of an interface. * interface-num specifies the number of an interface.   If this parameter is not specified, DCB negotiation failure records on all interfaces are displayed. | - |
| **interface** *interface-name* | Displays DCB negotiation failure records on a specified interface.   * interface-name specifies the name of an interface.   If this parameter is not specified, DCB negotiation failure records on all interfaces are displayed. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When PFC works in auto mode, interfaces at both ends of a link negotiate PFC parameters through DCBX.You can run the **display dcb fail-record** command to check the negotiation failure cause of the DCBX peers, which helps you locate faults.The system reserves only the latest five negotiation failure records.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display DCB negotiation failure records on all interfaces.
```
<HUAWEI> display dcb fail-record
DCB Fail-Record Show:                                                           
-------------------------------------------------------------------------------  
Interface           Fail-Record                                                 
------------------------------------------------------------------------------- 
100GE1/0/1          [2012-08-21 18:51:01]Neighbor does not exist.                 
                    [2012-08-21 18:59:43]PFC is not matched.                    
-------------------------------------------------------------------------------

```

**Table 1** Description of the **display dcb fail-record** command output
| Item | Description |
| --- | --- |
| Fail-Record | Negotiation failure records:  -Multi neighbor is not supported.  -Neighbor does not exist.  -PFC is not matched.  -ETS is not matched.  -OUI is not matched.  -Duplicate TLV is received.  -Packet length is overflowed.  -Total bandwidth is incorrect.  -ETS max tc is incorrect.  -Received LLDPDUs do not contain DCBX TLVs.  -No Fail-Record. |
| Interface | Name of an interface. |