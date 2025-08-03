login application
=================

login application

Function
--------



The **login application** command is used to log in to the application in the OAS.




Format
------

**login application** *application-name* **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *application-name* | Specifies the name of an application. | The value is a string of 1 to 63 case-sensitive characters without spaces. |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |



Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Users can log in to the application shell and enter the background to perform some maintenance operations. The login application shell requires user name and password authentication, and unauthorized users are prohibited from logging in.To support login to the container shell, the container image must meet the following requirements:

* The container image must provide the Login program (provided by Linux distributions by default).
* When creating a container image, you must preset the login user name, configure the initial password, and set the validity period of the initial password to 0 days.

Example
-------

# Log in to an application in the OAS.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] login application app1 slot 1

```