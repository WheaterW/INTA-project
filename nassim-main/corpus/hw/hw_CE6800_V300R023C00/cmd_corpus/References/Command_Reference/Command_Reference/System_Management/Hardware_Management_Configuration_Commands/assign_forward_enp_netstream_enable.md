assign forward enp netstream enable
===================================

assign forward enp netstream enable

Function
--------



The **assign forward enp netstream enable** command enables the NetStream mode.

The **undo assign forward enp netstream enable** command disables the NetStream mode.



By default, the NetStream mode is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**assign forward enp netstream enable**

**undo assign forward enp netstream enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the NetStream mode is enabled, more DDR memory space can be allocated.If the NetStream mode is disabled, the default DDR memory space is used.

**Precautions**

After enabling or disabling the NetStream mode, run the save command to save the configuration and restart the device to make the configuration take effect.In addition, the board is reset one more time in the following situations to restore the NetStream mode consistency:

1. Only the mode is changed, but the configuration is not saved to the configuration file. Then, the device is restarted.
2. After the mode is changed, the device is not restarted, and only the board is restarted.
3. Switch the configuration file and restart the device. The NetStream mode configured on the device is different from that configured on the original device.
4. A new board is installed, and the NetStream mode on the new board is different from that configured on the device.
5. If a board is restarted or powered off during configuration restoration, the board may be reset one more time.

Example
-------

# Disable the NetStream mode.
```
<HUAWEI> system-view
[~HUAWEI] undo assign forward enp netstream enable
Info: Please save the configuration and reboot to take effect.

```

# Enable the NetStream mode.
```
<HUAWEI> system-view
[~HUAWEI] assign forward enp netstream enable
Info: Please save the configuration and reboot to take effect.

```