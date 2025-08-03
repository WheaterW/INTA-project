display domain
==============

display domain

Function
--------



The **display domain** command displays domain configuration information.




Format
------

**display domain** [ **name** *domain-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *domain-name* | Specify the domain name. | If no domain name is specified, the summary information of all domains must be displayed. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After you create a domain using the **domain** command and complete the configuration under the domain, you can run the command to view the domain configuration information and check whether the configuration is correct.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# View the configuration information of all existing domains.
```
<HUAWEI> display domain
  Total: 5
-------------------------------------------------------------------------      
  index    DomainName                                                            
  -------------------------------------------------------------------------      
  0        default                                                               
  1        default_admin                                                         
  2        aaa.com                                                               
  3        bbb.com                                                               
  4        huawei                                                                
  -------------------------------------------------------------------------

```

# View the configuration of domain1.
```
<HUAWEI> display domain name domain1
  Domain-name                     : domain1 
  Domain-index                    : 0                                           
  Domain-state                    : Active                                      
  Authentication-scheme-name      : default                                     
  Accounting-scheme-name          : default                                     
  Authorization-scheme-name       : -                                           
  Service-scheme-name             : -                                           
  RADIUS-server-template          : default                                     
  Accounting-copy-RADIUS-template : -                                           
  HWTACACS-server-template        : -     
  LDAP-server-template            : -                                     
  Push-url-address                : -                                           
  Accounting-DualStack-Separate   : -

```

**Table 1** Description of the **display domain** command output
| Item | Description |
| --- | --- |
| index | Field index. |
| DomainName | Domain name. |
| Domain-name | Domain name. |
| Domain-state | Status of the domain. |
| Authentication-scheme-name | The authentication scheme name used by the domain. By default, the domain uses the default authentication scheme provided by the system. |
| Accounting-scheme-name | The name of the accounting scheme used by the domain. By default, the domain uses the default accounting scheme provided by the system. |
| Authorization-scheme-name | Authorization scheme name used by the domain. |
| Service-scheme-name | Business scenario name used by the domain. |
| RADIUS-server-template | Name of the RADIUS server template used by the domain. |
| HWTACACS-server-template | HWTACACS server template name used by the domain. |
| LDAP-server-template | Name of the LDAP server template used by the domain. |
| Push-url-address | The push URL used by the domain. |