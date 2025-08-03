hwtacacs-server timer quiet
===========================

hwtacacs-server timer quiet

Function
--------

The **hwtacacs-server timer quiet** command sets the quiet interval before the primary server reverts to the active state.

The **undo hwtacacs-server timer quiet** command restores the default quiet interval before the primary server reverts to the active state.

By default, the quiet interval before the primary HWTACACS server reverts to the active state is 5 minutes.



Format
------

**hwtacacs-server timer quiet** *value*

**undo hwtacacs-server timer quiet**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies the quiet interval before the primary server reverts to the active state. | The value is an integer that ranges from 0 to 255. The default value is 5. |




Views
-----

HWTACACS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

If the primary server is unavailable, the device automatically switches services to the standby server and sends packets to the standby server. After the quiet interval before the primary server reverts to the active state expires, the device attempts to establish a connection with the primary server.- If the primary server is still unavailable, the device continues to send packets to the standby server until the next interval expires. Such a process repeats.- If the primary server is available, the device switches services to the primary server and sends packets to the primary server.The quiet interval before the primary server reverts to the active state ensures that the primary server can be restored immediately and reduces the number of detection times during the switchover.The default value is recommended.

**Precautions**

When the quiet interval of the active server is set to 0, if the active server fails, the device sends packets to the standby server. When the active server is recovered, the device does not connect to the active server, but still sends packets to the standby server until the standby server fails.When you run the hwtacacs-server timer quiet command to change the quiet interval before the primary server reverts to the active state, the device does not check whether the HWTACACS server template is in use.



Example
-------

# Set the quiet interval before the primary server reverts to the active state to 3 minutes.
```
<HUAWEI> system-view
[~HUAWEI] hwtacacs-server template template1
[*HUAWEI-hwtacacs-template1] hwtacacs-server timer quiet 3

```