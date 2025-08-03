dot1x abnormal-track cache-record-num
=====================================

dot1x abnormal-track cache-record-num

Function
--------



The **dot1x abnormal-track cache-record-num** command sets the maximum number of EAP packets that can be recorded for abnormal 802.1X authentication.

The **undo dot1x abnormal-track cache-record-num** command restores the default maximum number of EAP packets that can be recorded for abnormal 802.1X authentication.



By default, the device can record a maximum of 20 EAP packets for abnormal 802.1X authentication.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**dot1x abnormal-track cache-record-num** *cache-record-num*

**undo dot1x abnormal-track cache-record-num**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *cache-record-num* | Specifies the maximum number of EAP packets that can be recorded for abnormal 802.1X authentication. | The value is an integer that ranges from 0 to 30. The default value is 20. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If 802.1X authentication fails, you need to check the EAP packets to locate the fault. This command allows you to set the maximum number of EAP packets that the device can record for abnormal 802.1X authentication.


Example
-------

# Set the maximum number of EAP packets that can be recorded for abnormal 802.1X authentication to 30.
```
<HUAWEI> system-view
[~HUAWEI] dot1x abnormal-track cache-record-num 30

```