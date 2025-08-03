display ldap-server template
============================

display ldap-server template

Function
--------



The **display ldap-server template** command displays the configurations of an LDAP server template.




Format
------

**display ldap-server template** [ **name** *template-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *template-name* | Specifies the name of an LDAP server template. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

If no template is specified, the configurations of all LDAP servers are displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configurations of the LDAP server template temp.
```
<HUAWEI> display ldap-server template name temp
  -------------------------------------------------------------------
  Server-template-name                :  temp
  Server-type                         :  AD LDAP
  Base DN                             :  dc=my-domain,dc=com
  Administrator anonymous bind        :  No
  Manager DN                          :  cn=administrator
  Manager password                    :  ****************
  Bind manager with Base DN           :  Yes
  Primary-authentication-server       :  10.1.1.1:389
  Secondary-authentication-server     :  -:0
  Third-authentication-server         :  -:0
  Bind user when authorization        :  Yes
  Source-IP-address                   :  -                 
  Source-LoopBack                     :  -   
  Source-VLAN                         :  - 
  -------------------------------------------------------------------

```

**Table 1** Description of the **display ldap-server template** command output
| Item | Description |
| --- | --- |
| Server-template-name | Name of an LDAP server template. |
| Base DN | Base DN of an LDAP server. |
| Administrator anonymous bind | Whether to allow the administrator to access an LDAP server anonymously:   * Yes: allows the administrator to access the LDAP server anonymously. * No: blocks the administrator from accessing the LDAP server anonymously. |
| Manager DN | Administrator Base DN for accessing an LDAP server. |
| Manager password | Administrator password for accessing an LDAP server. |
| Bind manager with Base DN | Whether to attach the Base DN to the administrator DN:   * Yes: attaches the Base DN to the administrator DN. * No: does not attach the Base DN to the administrator DN. |
| Bind user when authorization | Whether to configure user binding during AD authorization. |
| Primary-authentication-server | IP address and port of the primary LDAP server. |
| Secondary-authentication-server | IP address and port of the secondary LDAP server. |
| Third-authentication-server | IP address and port of the third LDAP server. |
| Source-IP-address, Source-LoopBack, or Source-VLAN | Source IP address for communicating with the LDAP server. |