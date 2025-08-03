display aaa configuration
=========================

display aaa configuration

Function
--------



The **display aaa configuration** command displays brief AAA information, for example, the domain, authentication scheme, authorization scheme, and accounting scheme.




Format
------

**display aaa configuration**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

AAA configurations are limited by system specifications. Before performing AAA configurations, run the **display aaa configuration** command to check whether there are sufficient resources.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display AAA summary. (The displayed data is for reference only.)
```
<HUAWEI> display aaa configuration
  Domain Name Delimiter            : @                                                                                              
  Domainname parse direction       : Left to right                                                                                  
  Domainname location              : After-delimiter                                                                                
  Administrator user default domain: default_admin                                                                                  
  Normal user default domain       : default                                                                                        
  Domain                           : total: 2048    used: 2                                                                         
  Authentication-scheme            : total: 128     used: 1                                                                         
  Accounting-scheme                : total: 128     used: 1                                                                         
  Authorization-scheme             : total: 128     used: 1                                                                         
  Service-scheme                   : total: 128     used: 0                                                                         
  Recording-scheme                 : total: 64      used: 0                                                                         
  Local-user                       : total: 1000    used: 0                                                                         
  Local-user block retry-interval  : 5 Min(s)                                                                                       
  Local-user block retry-time      : 3                                                                                              
  Local-user block time            : 5 Min(s)                                                                                       
  Remote-admin-user block retry-interval : 5 Min(s)                                                                                 
  Remote-admin-user block retry-time     : 30                                                                                       
  Remote-admin-user block time           : 5 Min(s)                                                                                 
  Session timeout invalid enable   : No

```

**Table 1** Description of the **display aaa configuration** command output
| Item | Description |
| --- | --- |
| Domain Name Delimiter | Domain name delimiter, which can be any of the following characters: \ / : < > | @ ' %. |
| Domain | Number of domains.   * total: indicates the total number of domains that can be created. * used: indicates the number of domains that have been created. |
| Domainname parse direction | Parsing direction of the domain name.   * Left to right. * Right to left. |
| Domainname location | Domain name location.   * After-delimiter: The domain name is placed behind the domain name delimiter. * Before-delimiter: The domain name is placed before the domain name delimiter. |
| Administrator user default domain | Default domain of administrators. |
| Normal user default domain | Default domain of common users. |
| Authentication-scheme | Number of authentication schemes.   * total: indicates the total number of authentication schemes that can be created. * used: indicates the number of authentication schemes that have been created. |
| Accounting-scheme | Number of accounting schemes.   * total: indicates the total number of accounting schemes that can be created. * used: indicates the number of accounting schemes that have been created. |
| Authorization-scheme | Number of authorization schemes.   * total: indicates the total number of authorization schemes that can be created. * used: indicates the number of authorization schemes that have been created. |
| Service-scheme | Number of service schemes.   * total: indicates the total number of service schemes that can be created. * used: indicates the number of service schemes that have been created. |
| Recording-scheme | Number of recording schemes.   * total: indicates the total number of recording schemes that can be created. * used: indicates the number of recording schemes that have been created. |
| Local-user | Number of local users.   * total: indicates the total number of local users that can be created. * used: indicates the number of local users that have been created. |
| Local-user block retry-interval | Authentication retry interval of a local account. |
| Local-user block retry-time | Maximum number of consecutive authentication failures for a local account. |
| Local-user block time | Lockout duration of a local account. |
| Session timeout invalid enable | * Yes: The device will not disconnect or reauthenticate users when the RADIUS server delivers Session-Timeout with the value 0. * No: The device will disconnect or reauthenticate users when the RADIUS server delivers Session-Timeout with the value 0. |
| Remote-user block retry-interval | Authentication retry interval of a remote AAA authentication user. |
| Remote-user block retry-time | Maximum number of consecutive authentication failures for a remote AAA authentication user. |
| Remote-user block time | Locking time of a remote AAA authentication user. |