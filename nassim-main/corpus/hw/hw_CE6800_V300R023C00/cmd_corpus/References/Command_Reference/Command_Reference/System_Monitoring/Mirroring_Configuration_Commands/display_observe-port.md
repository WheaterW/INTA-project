display observe-port
====================

display observe-port

Function
--------



The **display observe-port** command displays the observing port configuration.




Format
------

**display observe-port** [ *index* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *index* | Index of the observing port. | The value is an integer ranging from 1 to 8. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The **display observe-port** command displays the observing port configuration.

**Precautions**



In equal-cost multi-route scenarios, interface in the **display observe-port** command output is displayed as ECMP.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the observing port configuration.
```
<HUAWEI> display observe-port
  -----------------------------------------------------------------------------
  Index    : 1
  Interface: 100GE1/0/1
  -----------------------------------------------------------------------------
  Index    : 2
  Interface: 100GE1/0/2
  CIR(kbps): 1000
  -----------------------------------------------------------------------------

  GroupId    MemberPorts
  -----------------------------------------------------------------------------
        1    100GE1/0/3            100GE1/0/4
  -----------------------------------------------------------------------------

```

**Table 1** Description of the **display observe-port** command output
| Item | Description |
| --- | --- |
| Index | Index of the observing port. |
| GroupId | ID of an observing port group. |
| MemberPorts | Member ports of an observing port group. |
| Interface | Observing port. |
| CIR(kbps) | Rate limit configured on the observing port. |