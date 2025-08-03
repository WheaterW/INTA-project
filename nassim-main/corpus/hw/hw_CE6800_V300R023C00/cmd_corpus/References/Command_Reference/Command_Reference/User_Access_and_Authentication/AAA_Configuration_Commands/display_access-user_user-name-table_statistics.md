display access-user user-name-table statistics
==============================================

display access-user user-name-table statistics

Function
--------



The **display access-user user-name-table statistics** command displays statistics on users who access the network after the number of users is limited based on the user name.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display access-user user-name-table statistics** { **all** | **username** *username* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays statistics on all users. | - |
| **username** *username* | Displays statistics on users with a specified user name. | The value is a string of 1 to 253 case-sensitive characters. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After the number of access users is limited based on the user name using the **access-limit user-name max-num** command, you can run the display access-user user-name-table statistics command to check related statistics including the maximum number of access users and IP and MAC addresses of access users.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics on all users who access the network after the number of access users is limited based on the user name.
```
<HUAWEI> display access-user user-name-table statistics all
--------------------------------------------------------------------------------
 Username                Current num       Access limit max num                 
--------------------------------------------------------------------------------
 test@hw                 8                 8                                    
--------------------------------------------------------------------------------
 Total: 1, printed: 1

```

# Display detailed statistics on users with the user name test@hw who access the network after the number of access users is limited based on the user name.
```
<HUAWEI> display access-user user-name-table statistics username test@hw
                                                                                
Basic Info:                                                                     
 User name                   : test@hw                                          
 Current num                 : 1                                                
 Access limit max num        : 8                                                
Detail Info:                                                                    
--------------------------------------------------------------------------------
 UserID       Username                IP address       MAC                      
--------------------------------------------------------------------------------
 16016        test@hw                 192.168.8.139    00e0-fc12-3456                                 
--------------------------------------------------------------------------------
 Total: 1, printed: 1

```

**Table 1** Description of the **display access-user user-name-table statistics** command output
| Item | Description |
| --- | --- |
| Current num | Number of current access users. |
| Access limit max num | Maximum number of access users. |
| Total: m, printed: n | Total number (m) of entries and number (n) of displayed entries. |
| Basic Info | Basic information. |
| User name or Username | User name. |
| Detail Info | Detailed information. |
| UserID | User ID. |
| IP address | User IP address. |
| MAC | User MAC address. |