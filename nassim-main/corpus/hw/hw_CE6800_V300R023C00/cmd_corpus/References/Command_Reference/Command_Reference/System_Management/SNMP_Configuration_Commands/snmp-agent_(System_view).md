snmp-agent (System view)
========================

snmp-agent (System view)

Function
--------



The **snmp-agent** command enables the SNMP agent function.

The **undo snmp-agent** command disables the SNMP agent function.



By default, the SNMP agent function is disabled.


Format
------

**snmp-agent**

**undo snmp-agent**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The SNMP agent is a process running on a network device. It maintains data on the managed device, responds to the requests from the NMS, and sends collected data to the NMS. Before configuring SNMP, you must run the **snmp-agent** command to enable the SNMP agent function.You can also run the **snmp-agent** command with any parameter specified to enable the SNMP agent function. For example, if you run the **snmp-agent community** command, the SNMP agent function is enabled when a community name is created.

**Configuration Impact**

Running the **undo snmp-agent** command causes the configurations of all SNMP versions (SNMPv1, SNMPv2c, and SNMPv3) on the device to become invalid.

**Precautions**

The **undo snmp-agent** command disables the SNMP agent function but does not delete the SNMP configuration. After the **snmp-agent** command is run again, the original SNMP configuration still exists. To permanently delete an SNMP configuration, run the corresponding **undo** command.


Example
-------

# Enable the SNMP agent function.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent

```

# Disable the SNMP agent function.
```
<HUAWEI> system-view
[~HUAWEI] undo snmp-agent

```