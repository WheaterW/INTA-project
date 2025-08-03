display accounting-scheme
=========================

display accounting-scheme

Function
--------



The **display accounting-scheme** command displays the configuration of accounting schemes, including accounting scheme names and accounting modes.




Format
------

**display accounting-scheme** [ **name** *accounting-scheme-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *accounting-scheme-name* | Specifies the name of an accounting scheme. | The accounting scheme must already exist. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After the accounting scheme configuration is complete, run the display accounting-scheme command to view the configuration of accounting schemes.Before applying an accounting scheme to a domain, run the display accounting-scheme command to check whether configuration of the accounting scheme is correct.

**Precautions**

The display accounting-scheme command displays the detailed configuration if the name of an accounting scheme is specified. Otherwise, this command displays only the summary of accounting schemes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the summary of all accounting schemes.
```
<HUAWEI> display accounting-scheme
  Total of accounting-scheme: 3                                                 
 ------------------------------------------------------------------------                                                          
  Accounting-scheme-name              Accounting-method       scheme-index                                                          
  ------------------------------------------------------------------------ 
  default                             None                    0                                                                     
  radius-1                            RADIUS                    1
  tacas-1                             HWTACACS                2
  -------------------------------------------------------------------

```

# Display the detailed configuration of the default accounting scheme.
```
<HUAWEI> display accounting-scheme name default
  Accounting-scheme-name                : default
  Accounting-method                     : None
  Realtime-accounting-switch            : Disabled
  Realtime-accounting-interval(min)     : -
  Start-accounting-fail-policy          : Offline
  Realtime-accounting-fail-policy       : Online
  Realtime-accounting-failure-retries   : 3

```

**Table 1** Description of the **display accounting-scheme** command output
| Item | Description |
| --- | --- |
| Accounting-scheme-name | Name of an accounting scheme. To create an accounting scheme, run the accounting-scheme (AAA view) command. |
| Accounting-method | Accounting mode in the accounting scheme. The accounting modes are as follows:  HWTACACS: indicates that an HWTACACS server performs accounting.  None: indicates non-accounting.  RADIUS: indicates that a RADIUS server performs accounting.  To configure an accounting mode, run the accounting-mode command. |
| Realtime-accounting-switch | Whether the real-time accounting function is enabled:  Disabled: indicates that the real-time accounting function is disabled.  Enabled: indicates that the real-time accounting function is enabled.  To set the interval for real-time accounting, run the accounting realtime command. |
| Realtime-accounting-interval(min) | Interval for real-time accounting. To set the interval for real-time accounting, run the accounting realtime command. |
| Start-accounting-fail-policy | Policy used for accounting-start failures.  Offline: disconnects users.  Online: keeps users online.  To configure a policy for accounting-start failures, run the accounting start-fail command. |
| Realtime-accounting-fail-policy | Policy used for real-time accounting failures.  Offline: disconnects users.  Online: keeps users online.  To configure the policy used for real-time accounting failures, run the accounting interim-fail command. |
| Realtime-accounting-failure-retries | Number of retries before a real-time accounting failure is confirmed.  To set the number of real-time retries before a real-time accounting failure is confirmed, run the accounting interim-fail command. |