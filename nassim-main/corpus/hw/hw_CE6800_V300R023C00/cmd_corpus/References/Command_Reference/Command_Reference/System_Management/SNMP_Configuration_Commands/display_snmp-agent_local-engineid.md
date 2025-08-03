display snmp-agent local-engineid
=================================

display snmp-agent local-engineid

Function
--------



The **display snmp-agent local-engineid** command displays the engine ID of a local SNMP agent.




Format
------

**display snmp-agent local-engineid**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



On a device with the SNMP agent function enabled, you can run this command to view the engine ID of the local SNMP agent.The SNMP engine ID uniquely identifies an SNMP agent in a management domain. The SNMP engine ID is an important component of the SNMP agent. It schedules and processes SNMP messages, which implements security authentication and access control.



**Prerequisites**



The SNMP agent function has been enabled using the **snmp-agent** command.An engine ID has been configured for the local SNMP agent using the **snmp-agent local-engineid** command.



**Precautions**

To set an engine ID for the local SNMP agent, run the **snmp-agent local-engineid** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the engine ID of a local SNMP agent with the SNMP agent function enabled.
```
<HUAWEI> display snmp-agent local-engineid
SNMP local EngineID: 000007DB7F0000013859

```

# Display the engine ID of a local SNMP agent with the SNMP agent function disabled.
```
<HUAWEI> display snmp-agent local-engineid
Error: SNMP agent is not enabled.

```

**Table 1** Description of the **display snmp-agent local-engineid** command output
| Item | Description |
| --- | --- |
| SNMP local EngineID | Engine ID of a local SNMP agent.  The engine ID can be specified by an administrator using the snmp-agent local-engineid command or be automatically calculated using an algorithm. |
| Error | Error. |