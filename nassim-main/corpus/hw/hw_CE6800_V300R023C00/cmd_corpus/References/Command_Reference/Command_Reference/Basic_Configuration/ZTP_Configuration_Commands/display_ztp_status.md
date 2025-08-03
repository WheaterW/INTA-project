display ztp status
==================

display ztp status

Function
--------



The **display ztp status** command displays whether a device is in the ZTP deployment process or whether the ZTP deployment process will be executed next time the device starts without any configuration file.




Format
------

**display ztp status**


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

During ZTP deployment, you can log in to a device through the console port and run this command to check whether the device is in the ZTP deployment process or whether the ZTP deployment process will be executed next time the device starts without any configuration file. In addition, you can run the set ztp { enable | disable } command to configure whether the device starts the ZTP deployment process when it starts without any configuration file.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Check whether the device is in the ZTP deployment process.
```
<HUAWEI> display ztp status
-------------------------------------------------------------                                                                       
Slot   Current startup ZTP status    Next startup ZTP status                                                                        
-------------------------------------------------------------                                                                       
1      disable                       enable                                                                                         
-------------------------------------------------------------

```

**Table 1** Description of the **display ztp status** command output
| Item | Description |
| --- | --- |
| Slot | Slot ID. |
| Current startup ZTP status | Whether the device is in the ZTP deployment process:   * enable: yes. * disable: no. |
| Next startup ZTP status | Whether to execute the ZTP process upon the next startup without any configuration file.   * enable: yes. * disable: no. |