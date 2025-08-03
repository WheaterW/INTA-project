display device esn
==================

display device esn

Function
--------



The **display device esn** command displays the Equipment Serial Number (ESN) in the system.




Format
------

**display device esn**


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

Before a license file is activated, check whether device information such as software versions, ESNs, and the system time on the device match those in the license file. You can run the display esn command to check ESNs of the device. If the device has a backplane e-label, the backplane ESN is displayed. There is no backplane label, the ESNs of the master and slave main control boards are displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the device ESN.
```
<HUAWEI> display device esn
 ESN of slot 1: ******

```

**Table 1** Description of the **display device esn** command output
| Item | Description |
| --- | --- |
| ESN of X | Device ESN. |