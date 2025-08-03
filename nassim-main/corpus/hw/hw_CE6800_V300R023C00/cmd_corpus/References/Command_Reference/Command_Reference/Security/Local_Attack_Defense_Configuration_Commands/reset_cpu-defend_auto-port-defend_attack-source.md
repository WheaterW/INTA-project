reset cpu-defend auto-port-defend attack-source
===============================================

reset cpu-defend auto-port-defend attack-source

Function
--------



The **reset cpu-defend auto-port-defend attack-source** command clears information about auto port defend attack source.




Format
------

**reset cpu-defend auto-port-defend attack-source** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies a slot ID.  If slot slot-id is not specified, information about attack sources on the device is cleared. | The value must be set according to the device configuration. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To view information about auto port defend attack source in a specified period, run the **reset cpu-defend auto-port-defend attack-source** command to clear existing information about auto port defend attack source and run the **display cpu-defend auto-port-defend attack-source** command.

**Precautions**

After the **reset cpu-defend auto-port-defend attack-source** command is run, information about auto port defend attack source is cleared and cannot be restored.


Example
-------

# Delete existing auto port defend attack source information on the device.
```
<HUAWEI> reset cpu-defend auto-port-defend attack-source

```