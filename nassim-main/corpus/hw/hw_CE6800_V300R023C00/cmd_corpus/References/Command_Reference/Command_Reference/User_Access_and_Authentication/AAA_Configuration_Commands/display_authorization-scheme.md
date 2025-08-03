display authorization-scheme
============================

display authorization-scheme

Function
--------



The **display authorization-scheme** command displays the configuration of authorization schemes.




Format
------

**display authorization-scheme** [ **name** *authorization-scheme-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *authorization-scheme-name* | Specifies the name of an authorization scheme. | The value is a string of 1 to 32 case-sensitive characters, and cannot contain spaces. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After the authorization scheme configuration is complete, run the display authorization-scheme command to view the configuration of authorization schemes.Before applying an authorization scheme to a domain, run the display authorization-scheme command to check whether configuration of the authorization scheme is correct.

**Precautions**

The display authorization-scheme command displays the detailed configuration if the name of an authorization scheme is specified. Otherwise, this command displays only the summary of authorization schemes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the detailed configuration of the authorization scheme scheme0.
```
<HUAWEI> display authorization-scheme name scheme0
---------------------------------------------------------------------------
 Authorization-scheme-name   : scheme0
 Authorization-method        : Local
 Authorization-cmd level  0   : Disabled
 Authorization-cmd level  1   : Disabled 
 Authorization-cmd level  2   : Disabled
 Authorization-cmd level  3   : Disabled
 Authorization-cmd no-response-policy    : Online
---------------------------------------------------------------------------

```

# Display the summary of all authorization schemes.
```
<HUAWEI> display authorization-scheme
 Total of authorization-scheme: 2                                               
  --------------------------------------------------------------------------------------------------                                
  Authorization-scheme-name          Authorization-method                               scheme-index                                
  --------------------------------------------------------------------------------------------------
  default                             Local                                             0
  scheme0                             Local                                             1
  --------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display authorization-scheme** command output
| Item | Description |
| --- | --- |
| Authorization-scheme-name | Name of the authorization scheme. To create an authorization scheme, run the authorization-scheme (AAA view) command. |
| Authorization-method | Authorization mode set for the authorization scheme. To configure an authorization mode, run the authorization-mode command. |
| Authorization-cmd level | Whether the command line authorization function is enabled for a user with a specified level:   * Disabled: indicates that the command line authorization function is disabled. * Enabled: indicates that the command line authorization function is enabled.   To set the command line authorization function, run the authorization-cmd command. |
| Authorization-cmd no-response-policy | Policy for command line authorization failures, in which users are allowed to go online. |