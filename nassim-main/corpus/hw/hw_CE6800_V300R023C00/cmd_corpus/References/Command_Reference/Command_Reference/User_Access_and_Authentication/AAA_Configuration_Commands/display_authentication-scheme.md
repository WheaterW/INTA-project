display authentication-scheme
=============================

display authentication-scheme

Function
--------



The **display authentication-scheme** command displays the configuration of authentication schemes.




Format
------

**display authentication-scheme** [ **name** *authentication-scheme-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *authentication-scheme-name* | Specifies the name of an authentication scheme. | The authentication scheme name must already exist. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After the authentication scheme configuration is complete, run the display authentication-scheme command to view the configuration of authentication schemes.

**Precautions**

The display authentication-scheme command displays the detailed configuration if the command is executed in the authentication scheme view or the name of an authentication scheme is specified. Otherwise, this command displays only the summary of authentication schemes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the detailed configuration of the default authentication scheme.
```
<HUAWEI> display authentication-scheme name default
  Authentication-scheme-name          : default                                 
  Authentication-method               : Local  
  Radius authentication-type of admin : PAP(all) 
  Server no-response accounting       : NO
  Server no-response authorization    : NO 
  Location after radius reject        : None

```

# Display the summary of all authentication schemes.
```
<HUAWEI> display authentication-scheme
  Total of authentication scheme: 2
  --------------------------------------------------------------------------------------------------
  Authentication-scheme-name          Authentication-method                             scheme-index
  --------------------------------------------------------------------------------------------------
  default                             Local                                             0
  radius                              RADIUS                                            1
  --------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display authentication-scheme** command output
| Item | Description |
| --- | --- |
| Authentication-scheme-name | Name of an authentication scheme. |
| Authentication-method | Authentication mode in an authentication scheme. |
| Radius authentication-type of admin | Access type of administrators on whom CHAP authentication is performed. The value can be:   * PAP(all): PAP authentication is performed on the administrators of all access types when they are authenticated using RADIUS. * CHAP(ftp) PAP (other): CHAP authentication is performed on FTP users whose access types are displayed in brackets () when they are authenticated using RADIUS, and PAP authentication is performed on the administrators of other access types. |
| Server no-response accounting | Whether the device continues sending accounting packets after the server does not respond to a user's authentication request and the user then is authenticated using the local authentication mode. The value can be:   * YES: The device continues sending accounting packets. * NO: The device does not send accounting packets. |
| Location after radius reject | Whether a user is authenticated using another authentication mode after the user's RADIUS authentication request is rejected. The value can be:   * None: The user is not authenticated using another authentication mode after the user's RADIUS authentication request is rejected and the authentication process ends. * Local: The user is authenticated using the local authentication mode after the user's RADIUS authentication request is rejected. |
| Total of authentication scheme | Number of authentication schemes. |