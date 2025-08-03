display local-aaa-user password policy
======================================

display local-aaa-user password policy

Function
--------



The **display local-aaa-user password policy** command displays the password policy of local users.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display local-aaa-user password policy** { **administrator** }

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**display local-aaa-user password policy** { **administrator** | **access-user** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **administrator** | Displays the password policy of local administrators. | - |
| **access-user** | Displays the password policy of local access users.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After configuring the password policy for local users, you can run this command to check whether the configuration is correct.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the password policy of local administrators.
```
<HUAWEI> display local-aaa-user password policy administrator
  Password control                 : Enable                                     
  Password expiration              : Enable (180 days)                          
  Password history                 : Enable (history records:5) 
  Password minimum length          : Enable (minimum length:3)                
  Password alert before expiration : 30 days                                    
  Password alert original          : Enable
  Password complexity              : Four-of-kinds                                                                                  
  Password similar to name check   : Enable

```

# Display the password policy of local access users.
```
<HUAWEI> display local-aaa-user password policy access-user
  Password control                 : Enable                                     
  Password expiration              : Enable (180 days)

```

**Table 1** Description of the **display local-aaa-user password policy** command output
| Item | Description |
| --- | --- |
| Password control | Whether the password control function is enabled:   * Enable. * Disable.   To configure this function, run the local-aaa-user password policy access-user or local-aaa-user password policy administrator command. |
| Password history | Whether the historical password recording function is enabled and the maximum number of historical passwords of each user.  To configure this function, run the password history record number command. |
| Password expiration | Whether the password expiration function is enabled and password expiration time.  To configure this function, run the password expire command. |
| Password alert before expiration | Password expiration prompt days.  To configure this function, run the password alert before-expire command. |
| Password alert original | Whether the device prompts users to change the first configured passwords:   * Enable. * Disable.   To configure this function, run the password alert original command. |
| Password minimum length | Minimum length of the password. |
| Password complexity | Password complexity function:   * Two-of-kinds: two out of four. * Three-of-kinds: three out of four. * Four-of-kinds: four out of four. |
| Password similar to name check | Whether the password and user name similarity check function is enabled:   * Enable. * Disable. |