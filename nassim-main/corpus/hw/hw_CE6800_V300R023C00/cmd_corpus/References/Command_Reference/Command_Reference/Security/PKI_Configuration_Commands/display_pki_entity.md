display pki entity
==================

display pki entity

Function
--------



The **display pki entity** command displays information about PKI entities.




Format
------

**display pki entity** [ *entity-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **entity** *entity-name* | Specifies the name of a PKI entity. If the entity-name parameter is not specified, information about all entities is displayed. | The value must be an existing PKI entity name. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command displays information about PKI entities, including names, common names, countries, province, and location where the entities reside, and organizations to which entities belong.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all PKI entities.
```
<HUAWEI> display pki entity
PKI Entity Information:

  Entity Name      : a                                                          
  Common name      : chi                                                        
  Country          : -                                                          
  State            : A                                                          
  Locality         : -                                                          
  Organization     : A                                                          
  Organization unit: -                                                          
  FQDN             : www. e                                                     
  IP address       : -                                                          
  Email            : - 
 Total Number: 1

```

**Table 1** Description of the **display pki entity** command output
| Item | Description |
| --- | --- |
| PKI Entity Information | Information of the PKI entity. |
| Entity Name | Entity name. It is configured using the pki entity command. |
| Common name | Common name of the entity. It is configured using the common-name command. |
| Country | Country where a PKI entity resides. It is configured using the country (PKI entity view) command. |
| State | Province where a PKI entity resides. It is configured using the state (PKI entity view) command. |
| Locality | Location of a PKI entity. It is configured using the locality command. |
| Organization | Organization unit to which a PKI entity belongs. It is configured using the organization-unit command. |
| Organization unit | Organization unit to which a PKI entity belongs. It is configured using the organization-unit command. |
| FQDN | FQDN name of a PKI entity. It is configured using the fqdn command. |
| IP address | IP address of a PKI entity. It is configured using the ip-address command. |
| Email | Email address. It is configured using the email command. |
| Total Number | The total number. |