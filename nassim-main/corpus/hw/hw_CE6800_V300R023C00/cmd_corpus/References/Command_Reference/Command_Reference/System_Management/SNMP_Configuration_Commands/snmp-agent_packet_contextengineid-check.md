snmp-agent packet contextengineid-check
=======================================

snmp-agent packet contextengineid-check

Function
--------



The **snmp-agent packet contextengineid-check enable** command enables the consistency check between the contextEngineID and local engine ID.

The **snmp-agent packet contextengineid-check disable** command disables the consistency check between the contextEngineID and local engine ID.

The **undo snmp-agent packet contextengineid-check enable** command disables the consistency check between the contextEngineID and local engine ID.



By default, the consistency check between the contextEngineID and local engine ID is disabled.


Format
------

**snmp-agent packet contextengineid-check enable**

**snmp-agent packet contextengineid-check disable**

**undo snmp-agent packet contextengineid-check enable**


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

If the consistency between the contextEngineID and local engine ID is not checked, a connection can still be established even if the contextEngineID is different from the local engine ID.To improve system security, run the **snmp-agent packet contextengineid-check enable** command to check the consistency between the contextEngineID and local engine ID.

**Configuration Impact**



After the consistency check is enabled, packets cannot pass authentication if the contextEngineID is different from the local engine ID.



**Precautions**

This consistency check function applies only to SNMPv3.


Example
-------

# Enable the consistency check between the contextEngineID and local engine ID.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent packet contextengineid-check enable

```