display eth-trunk troubleshooting
=================================

display eth-trunk troubleshooting

Function
--------



The **display eth-trunk troubleshooting** command displays reasons for Eth-Trunk interface failures.




Format
------

**display eth-trunk troubleshooting**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



If an Eth-Trunk interface has a failure, such as a negotiation failure or status flapping, run the **display eth-trunk troubleshooting** command to check the failure reasons. The command output helps locate the failure and maintain the device.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the reasons for failures of Eth-Trunk 10.
```
<HUAWEI> display eth-trunk troubleshooting
Eth-Trunk10:
WorkingMode: STATIC            Operate status: Down
Member ports:
  100GE1/0/1            Status: Down      
    Reason: The remote interface is not selected.
    Advice: Check interface configuration
  100GE1/0/2            Status: Down      
    Reason: The remote interface is not selected.
    Advice: Check interface configuration

```

**Table 1** Description of the **display eth-trunk troubleshooting** command output
| Item | Description |
| --- | --- |
| Operate status | Eth-Trunk interface status:   * Down. * Up. |
| Member ports | Eth-Trunk member interfaces. |
| Eth-Trunk10 | Failed Eth-Trunk interface. |
| WorkingMode | Working mode of the Eth-Trunk interface.   * NORMAL: manual load balancing mode. * STATIC: static LACP mode. * DYNAMIC: dynamic LACP mode. |
| Status | Member interface status:   * Down. * Up. |
| Reason | Cause of the member interface fault. |
| Advice | Processing suggestion. |