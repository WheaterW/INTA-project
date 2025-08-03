info-center channel
===================

info-center channel

Function
--------



The **info-center channel name** command names a specified information channel.

The **undo info-center channel** command restores the default name of a channel.



By default, a device outputs information to various destinations through channels listed as following.

* channel number:0, channel name:console
* channel number:1, channel name:monitor
* channel number:2, channel name:loghost
* channel number:3, channel name:trapbuffer
* channel number:4, channel name:logbuffer
* channel number:5, channel name:snmpagent
* channel number:6, channel name:channel6
* channel number:7, channel name:channel7
* channel number:8, channel name:channel8
* channel number:9, channel name:channel9


Format
------

**info-center channel** *channel-number* **name** *channel-name*

**undo info-center channel** *channel-number*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *channel-number* | Specifies a channel number. | The value is an integer ranging from 0 to 9, indicating that the system has 10 channels. |
| **name** *channel-name* | Specifies the name of a channel. | The value is a string of 1 to 30 case-insensitive characters. The first character can be a letter only. The name cannot contain spaces or special characters, such as hyphens (-), slashes (/), or backslashes (\). |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To name a specified information channel, run the info-center channel name command. You can rename each channel to better remember and use them.

**Precautions**

When naming channels, the name of a channel cannot be identical with that of other channels. A preferred way is to associate the channel name with the practical function of the channel.


Example
-------

# Name channel 0 execconsole.
```
<HUAWEI> system-view
[~HUAWEI] info-center channel 0 name execconsole

```