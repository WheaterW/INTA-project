display fips-mode algorithm self-check(System view)
===================================================

display fips-mode algorithm self-check(System view)

Function
--------



The **display fips-mode algorithm self-check** command displays whether the algorithms used by cryptographic modules of the device comply with FIPS.




Format
------

**display fips-mode algorithm self-check** [ **all** | **slot** *slotId* [ **cpu** *cpuId* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays algorithm self-check information about all slots and CPUs. | - |
| **slot** *slotId* | Specifies a slot ID. | - |
| **cpu** *cpuId* | Specifies a CPU ID. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can run the **display fips-mode algorithm self-check** command to check whether the algorithms used by cryptographic modules of the device comply with FIPS, preventing cryptographic modules from being tampered with.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Check whether the algorithms used by cryptographic modules of the device comply with FIPS.
```
<HUAWEI> system-view
[HUAWEI] display fips-mode algorithm self-check all
Info: This operation needs several seconds, please wait for a moment.......
Algorithm self-check result:
-----------------------------------------------------
Slot  CPU  Module  Result
-----------------------------------------------------
1     0    OPENSSL Pass
1     0    CRYPTO  Pass
-----------------------------------------------------
Note: If the self-check fails, the password module may have been tampered with. Try to reset the board.

```

**Table 1** Description of the **display fips-mode algorithm self-check(System view)** command output
| Item | Description |
| --- | --- |
| Slot | Slot ID. |
| CPU | CPU ID. |
| Module | Cryptographic modules:   * OPENSSL: OpenSSL open-source cryptographic module. * CRYPTO: Crypto open-source cryptographic module. |
| Result | Self-check result:   * Pass: The self-check is passed. * Fail: The self-check fails. |