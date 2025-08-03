display forward mode
====================

display forward mode

Function
--------



The **display forward mode** command displays the configured and currently used packet forwarding modes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display forward mode**


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

You can run the display forward mode command to view the configured and currently used packet forwarding modes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configured and currently used packet forwarding modes.
```
<HUAWEI> display forward mode
------------------------------------------------------                                                                              
Slot ID    Configure forward mode Current forward mode                                                                              
------------------------------------------------------                                                                              
1          store-and-forward      store-and-forward                                                                                 
------------------------------------------------------

```

**Table 1** Description of the **display forward mode** command output
| Item | Description |
| --- | --- |
| Slot ID | Slot ID of the device. |
| Configure forward mode | Configured packet forwarding mode. To configure the packet forwarding mode, run the assign forward mode { store-and-forward | cut-through } command. |
| Current forward mode | Currently used packet forwarding mode. |