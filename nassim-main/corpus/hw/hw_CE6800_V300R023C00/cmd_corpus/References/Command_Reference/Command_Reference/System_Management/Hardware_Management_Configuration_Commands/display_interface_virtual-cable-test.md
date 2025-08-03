display interface virtual-cable-test
====================================

display interface virtual-cable-test

Function
--------



The **display interface virtual-cable-test** command displays the result of the last virtual-cable-test test.




Format
------

**display interface** { *interface-type* *interface-number* | *interface-name* } **virtual-cable-test**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Interface Type. | The value depends on the device configuration. |
| *interface-number* | Specifies an interface index. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |



Views
-----

10GE interface view,25GE interface view,User view,Management interface view,System view


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command is used to query the result of the last cable test.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# View the result of the last virtual-cable-test test.
```
<HUAWEI> display interface 10GE 1/0/1 virtual-cable-test
 State Note
 OK      : Check succeeded.
 Open/Short  : There may be an open circuit. Please connect cables correctly.
 Crosstalk   : Check is affected by crosstalk. Please remove the interference
                 source.
 notSupport/not: Check is not supported. Please check whether the interface
                 supports the check.
 Unknown   : Check did not complete successfully, possibly due to user
                 configuration. Please check configuration on local and remote
                 interfaces.
--------------------------------------------------------------------------------
Last virtual-cable-test time: 2007-9-29 19:44:51
 Pair A length(meters): 1
 Pair B length(meters): 1
 Pair C length(meters): 1
 Pair D length(meters): 1
 Pair A state: Open
 Pair B state: Open
 Pair C state: Open
 Pair D state: Open

```

**Table 1** Description of the **display interface virtual-cable-test** command output
| Item | Description |
| --- | --- |
| Pair X length(meters) | Length of cable X. The displayed result is for reference only. You are advised to use a network cable analyzer to perform an accurate test.   * The length is the distance between the interface and the failure point if a fault occurs. * The length is the actual length of the cable when the cable works properly. * The default length is 0 m when the cable is not connected. The test result may vary according to chips. |
| Pair X state | Current status of cable X. The displayed result is for reference only. You are advised to use a network cable analyzer to perform an accurate test.   * OK: indicates that the circuit pair is terminated normally. * Open/Short: indicates that the circuit is open-circuited or short-circuited. * Crosstalk: indicates that the circuit pairs interfere with each other. * notSupport/not: indicates that the device does not support the check. * Unknown: indicates that the fault is caused by other unknown reasons. |