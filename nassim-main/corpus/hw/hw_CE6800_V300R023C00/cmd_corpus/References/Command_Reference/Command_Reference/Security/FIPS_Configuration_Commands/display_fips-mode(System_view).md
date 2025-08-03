display fips-mode(System view)
==============================

display fips-mode(System view)

Function
--------



The **display fips-mode** command displays whether the FIPS mode is enabled on the device.




Format
------

**display fips-mode**


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

You can run the **display fips-mode** command to check whether the FIPS mode is enabled on the device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Check whether the FIPS mode is enabled on the device.
```
<HUAWEI> system-view
[~HUAWEI] display fips-mode
FIPS Mode: enable

```

**Table 1** Description of the **display fips-mode(System view)** command output
| Item | Description |
| --- | --- |
| FIPS Mode | FIPS mode status of the device:   * enable: The FIPS mode is enabled. * disable: The FIPS mode is disabled. |