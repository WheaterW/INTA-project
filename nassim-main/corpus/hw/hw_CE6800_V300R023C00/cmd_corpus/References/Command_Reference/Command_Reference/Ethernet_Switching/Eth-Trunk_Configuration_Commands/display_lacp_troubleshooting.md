display lacp troubleshooting
============================

display lacp troubleshooting

Function
--------



The **display lacp troubleshooting** command displays the reasons why LACP goes Down.




Format
------

**display lacp troubleshooting**


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



If LACP goes Down, run the **display lacp troubleshooting** command to check the reason. The command output helps locate the fault.The **display lacp troubleshooting** command can display the reasons for the latest five LACP Down events.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the reasons why LACP goes Down.
```
<HUAWEI> display lacp troubleshooting
Total counts: 1
--------------------------------------------------------------------------------
Sequence   Time                       Event Description                         
--------------------------------------------------------------------------------
1          2020-01-29 22:56:47        The interface bandwidth was invalid. Pleas
                                      e replace this interface. (Interface=100GE1/0/1
                                      , Eth-Trunk1)
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display lacp troubleshooting** command output
| Item | Description |
| --- | --- |
| Total counts | Number of times that LACP went Down. |
| Sequence | Sequence number. |
| Time | Date and time when LACP went Down. |
| Event Description | Reason why LACP went Down. |