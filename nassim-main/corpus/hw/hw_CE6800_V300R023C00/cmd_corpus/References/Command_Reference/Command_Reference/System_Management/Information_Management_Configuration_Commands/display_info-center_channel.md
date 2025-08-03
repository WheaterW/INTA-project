display info-center channel
===========================

display info-center channel

Function
--------



The **display info-center channel** command displays channel information.




Format
------

**display info-center channel** [ *channel-number* | *channel-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *channel-number* | Displays information about the channel with a specified number. | The value is an integer ranging from 0 to 9. Default channel names are specified for channels 0 to 5. By default, the six channels (Channel 0 to Channel 5) correspond to six directions in which information is output. |
| *channel-name* | Displays information about the channel with a specified name. | The value is a string of 1 to 30 case-insensitive characters. The name cannot contain spaces or special characters, such as hyphens (-), slashes (/), or backslashes (\). |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can use this command to view information about a channel when you enable the information management function for information channels.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about channel 0.
```
<HUAWEI> display info-center channel 0
channel number:0, channel name:console
ModuID   Name     Enable LogLevel     Enable TrapLevel    Enable DebugLevel
ffffffff default  Y      warning      Y      debugging     Y     debugging

```

**Table 1** Description of the **display info-center channel** command output
| Item | Description |
| --- | --- |
| channel number | Channel Number. |
| ModuID | Module ID (ffffffff indicates the default value). |
| Name | Module name (default indicates the default module). |
| Enable | Whether logs are enabled (the first ENABLE):   * Y: enabled. * N: disabled. |
| LogLevel | Level of logs to be output. |
| TrapLevel | Level of traps to be output. |
| DebugLevel | The level of the debugging information to be output. |