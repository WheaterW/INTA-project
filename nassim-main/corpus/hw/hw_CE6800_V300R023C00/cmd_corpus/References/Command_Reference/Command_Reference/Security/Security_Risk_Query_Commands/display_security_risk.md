display security risk
=====================

display security risk

Function
--------



The **display security risk** command displays security risks in the system and suggested solutions for the risks.




Format
------

**display security risk** [ [ **feature** *feature-name* ] | [ **level** *level-para* ] | [ **type** *type-para* ] ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **feature** *feature-name* | Displays security risks of a specified feature. | The value is a string of 1 to 31 characters. |
| **level** *level-para* | Displays security risks of High, Medium, or Low level. | Security risk level. It can be any value of the following:   * high * medium * low |
| **type** *type-para* | Displays security risks of a specified type. | Security risk type. It can be any value of the following:   * insecure-algorithm * insecure-protocol * insecure-configuration |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

Some protocols used by users may have security risks due to different security performance of protocols.In this case, you can run this command to check security risks in the system and eliminate the risks according to the provided suggestions. For example, if SNMPv1 is configured, the system displays a message indicating that SNMPv3 is recommended because SNMPv1 has security risks.

**Precautions**

The security risks that are displayed vary with user levels. The system administrators can view all security risks in the system. Other users can only view the security risks whose level is lower than or equal to their levels.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all security risks related to Telnet.
```
<HUAWEI> display security risk feature telnet
2021-10-08 16:18:25.650
Risk Level         : medium
Feature Name       : TELNET
Risk Type          : insecure-protocol
Risk Information   : The Telnet server function is used  
Repair Action      : Use Stelnet

```

# Display all security risks in the system.
```
<HUAWEI> display security risk
2021-10-08 16:19:12.161
Risk Level         : high
Feature Name       : VTY 
Risk Type          : insecure-configuration
Risk Information   : Idle time-out is configured as 0, so session will never be 
                     disconnected because of timeout
Repair Action      : Configure idle time-out to a non-zero value

Risk Level         : high
Feature Name       : VTY
Risk Type          : insecure-configuration
Risk Information   : No authentication is configured, or password authentication
                      is configured but no password is specified on the vty inte
                     rface
Repair Action      : Use AAA authentication

Risk Level         : medium
Feature Name       : TELNET
Risk Type          : insecure-protocol
Risk Information   : The Telnet server function is used
Repair Action      : Use Stelnet

Risk Level         : medium
Feature Name       : VTY
Risk Type          : insecure-protocol
Risk Information   : TELNET is not a secure protocol.
Repair Action      : It is recommended to use SSH.

Risk Level         : low
Feature Name       : SSH_SERVER
Risk Type          : insecure-configuration
Risk Information   : The SSH server key is not updated, which brings security ri
                     sks.
Repair Action      : It is recommended to set the SSH server rekey interval to a
                      non-zero value.

Risk Level         : low
Feature Name       : TTY
Risk Type          : insecure-configuration
Risk Information   : Password authentication is configured on the console interf
                     ace.
Repair Action      : Use AAA authentication.

```

# Display information about all security risks of the "insecure protocol" type in the system.
```
<HUAWEI> display security risk type insecure-protocol
2021-10-08 15:55:51.590
Risk Level         : medium
Feature Name       : TELNET
Risk Type          : insecure-protocol
Risk Information   : The Telnet server function is used
Repair Action      : Use Stelnet

Risk Level         : medium
Feature Name       : VTY
Risk Type          : insecure-protocol
Risk Information   : TELNET is not a secure protocol.
Repair Action      : It is recommended to use SSH.

```

# Display information about all security risks of the "insecure configuration type" in the system.
```
<HUAWEI> display security risk type insecure-configuration
2021-10-08 15:55:58.332
Risk Level         : high
Feature Name       : VTY
Risk Type          : insecure-configuration
Risk Information   : Idle time-out is configured as 0, so session will never be 
                     disconnected because of timeout
Repair Action      : Configure idle time-out to a non-zero value

Risk Level         : high
Feature Name       : VTY
Risk Type          : insecure-configuration
Risk Information   : No authentication is configured, or password authentication
                      is configured but no password is specified on the vty inte
                     rface
Repair Action      : Use AAA authentication

Risk Level         : low
Feature Name       : SSH_SERVER
Risk Type          : insecure-configuration
Risk Information   : The SSH server key is not updated, which brings security ri
                     sks.
Repair Action      : It is recommended to set the SSH server rekey interval to a
                      non-zero value.

Risk Level         : low
Feature Name       : TTY
Risk Type          : insecure-configuration
Risk Information   : Password authentication is configured on the console interf
                     ace.
Repair Action      : Use AAA authentication.

```

# Display all high-level security risks in the system.
```
<HUAWEI> display security risk level high
2021-10-08 16:18:53.955
Risk Level         : high
Feature Name       : VTY
Risk Type          : insecure-configuration
Risk Information   : Idle time-out is configured as 0, so session will never be 
                     disconnected because of timeout
Repair Action      : Configure idle time-out to a non-zero value

Risk Level         : high
Feature Name       : VTY
Risk Type          : insecure-configuration
Risk Information   : No authentication is configured, or password authentication
                      is configured but no password is specified on the vty inte
                     rface
Repair Action      : Use AAA authentication

```

**Table 1** Description of the **display security risk** command output
| Item | Description |
| --- | --- |
| Risk Level | Security risk level. It can be any value of the following:   * high. * medium. * low. |
| Risk Information | Information about the security risks. |
| Risk Type | Security risk type. |
| Feature Name | Feature name. |
| Repair Action | Suggested solutions for the security risks. |