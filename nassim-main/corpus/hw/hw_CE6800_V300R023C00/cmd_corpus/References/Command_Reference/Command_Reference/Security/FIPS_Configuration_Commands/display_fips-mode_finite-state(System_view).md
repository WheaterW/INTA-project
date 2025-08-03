display fips-mode finite-state(System view)
===========================================

display fips-mode finite-state(System view)

Function
--------



The **display fips-mode finite-state** command displays the historical records of FIPS mode status changes.




Format
------

**display fips-mode finite-state** [ **all** | **slot** *slot-id* [ **cpu** *cpu-id* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays the historical records of FIPS mode status changes in all slots. | - |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 49 case-sensitive characters, spaces not supported. |
| **cpu** *cpu-id* | Specifies the CPU ID. | The value is a string of 1 to 49 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can run the **display fips-mode finite-state** command to view the historical records of FIPS mode status changes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the historical records of FIPS mode status changes.
```
<HUAWEI> system-view
[HUAWEI] display fips-mode finite-state all
Slot:1 CPU:0
--------------------------------------------------------------------------------
Time                        State
--------------------------------------------------------------------------------
2020-08-04 16:43:22+00:00   Power on
2020-08-04 16:43:28+00:00   Power-Up Self_Tests
2020-08-04 16:43:30+00:00   FIPS Mode Init
2020-08-04 16:43:38+00:00   Ready
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display fips-mode finite-state(System view)** command output
| Item | Description |
| --- | --- |
| Time | Time when the FIPS mode status changes. |
| State | FIPS mode status:   * Power on: The device is powered on. * Power-Up Self\_Tests: The device performs self-check after startup. * FIPS Mode Init: The FIPS mode is initialized. * Ready: The system is ready. * None FIPS: The system is in non-FIPS mode. * Condition self test: The system performs a conditional self-test. * Crypto officer states: The system is in crypto officer state. * Software Error: The system receives a software error report. * Fatal Error: A fatal error occurs in the system. |
| Slot | Slot ID. |
| CPU | CPU ID. |