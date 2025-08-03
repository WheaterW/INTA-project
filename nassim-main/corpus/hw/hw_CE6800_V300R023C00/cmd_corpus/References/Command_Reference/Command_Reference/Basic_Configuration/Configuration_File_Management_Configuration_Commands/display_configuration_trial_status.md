display configuration trial status
==================================

display configuration trial status

Function
--------



The **display configuration trial status** command displays the trial running status of a system configuration.




Format
------

**display configuration trial status**


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



To view the trial running status of a system configuration, run the display configuration trial status command.Trial running is initiated by NETCONF. If the trial running packets carry the persistency mark, the trial running status information of a system configuration contains the persistency mark.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the trial running status of a system configuration when trial running is not configured and no persistency mark is carried.
```
<HUAWEI> system-view
[~HUAWEI] display configuration trial status
Trial status: INACTIVE 
Trial time left (sec): 0

```

# Display the trial running status of a system configuration when trial running is configured and no persistency mark is carried.
```
<HUAWEI> system-view
[~HUAWEI] display configuration trial status
Trial status:  ACTIVE
Trial time left (sec): 51

```

# Display the trial running status of a system configuration when trial running is initiated by NETCONF and the persistency mark is carried.
```
<HUAWEI> system-view
[~HUAWEI] display configuration trial status
Trial status: ACTIVE 
Persist id: IQ,d4668
Trial time left (sec): 30

```

**Table 1** Description of the **display configuration trial status** command output
| Item | Description |
| --- | --- |
| Trial status | Trial running status of a system configuration. The value can be:   * INACTIVE: The configuration is not in the trial running status. * ACTIVE: The configuration is in the trial running status. * CANCELING: The trial run of the configuration is being canceled. * WAITCANCEL: The trial run of the configuration is waiting to be canceled. |
| Trial time left (sec) | Remaining time of a trial run. |
| Persist id | Persistency mark. |