virtual-cable-test
==================

virtual-cable-test

Function
--------



The **virtual-cable-test** command tests the working state of a cable connected to an Ethernet interface and displays the test result.




Format
------

**virtual-cable-test**


Parameters
----------

None

Views
-----

10GE interface view,25GE interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A cable fault may cause the interface to go down or the interface rate to become abnormal even if the interface is up. You can run this command to check whether a cable is faulty and locate the failure point. If the cable is not faulty, the length in the command output indicates the cable's total length. If the cable is faulty, the length in the command output is the length from the interface to the failure point.

**Precautions**



After the **virtual-cable-test** command is run, the interface goes Down, which may affect services on the interface in a short period of time. After the test is successful, the interface goes Up. Therefore, pay attention to services that are sensitive to interface Up and Down events.The distance error of the VCT test is about 10 m. The test result may not be accurate for cables manufactured by all manufacturers and therefore is for reference only.It is recommended that you remove the cable from the peer interface to prevent the peer signals from affecting the test result.The **virtual-cable-test** command can be used on GE electrical interfaces or optical interfaces that have GE copper modules installed.




Example
-------

# Run the virtual-cable-test command to test the cable connected to an Ethernet interface and display the test result.
```
<HUAWEI> system-view
[~HUAWEI] interface 10GE1/0/1
[~HUAWEI-10GE1/0/1] virtual-cable-test
Warning: This operation will take several minutes. Continue? [Y/N]:Y
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
 Pair A length(meters): 10
 Pair B length(meters): 10
 Pair C length(meters): 10
 Pair D length(meters): 10
 Pair A state: OK
 Pair B state: OK
 Pair C state: OK
 Pair D state: OK

```

**Table 1** Description of the **virtual-cable-test** command output
| Item | Description |
| --- | --- |
| Pair A length(meters) | Length of cable A. The displayed result is for reference only. You are advised to use a network cable analyzer to perform an accurate test.   * The length is the distance between the interface and the failure point if a fault occurs. * The length is the actual length of the cable when the cable works properly. * The default length is 0 m when the cable is not connected. The test result may vary according to chips. |
| Pair A state | Current status of cable A. The displayed result is for reference only. You are advised to use a network cable analyzer to perform an accurate test.   * OK: indicates that the circuit pair is terminated normally. * Open: indicates that the circuit pair is not terminated. * Short: indicates that the circuit pair is short circuited. * Crosstalk: indicates that the circuit pairs interfere with each other. * notSupport/not: indicates that the interface does not support the check. * Unknown: indicates that other unknown fault causes are detected or the detection result is inaccurate. |
| Pair A | The name of cable. |