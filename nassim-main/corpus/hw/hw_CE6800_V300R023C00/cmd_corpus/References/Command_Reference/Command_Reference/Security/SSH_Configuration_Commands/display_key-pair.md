display key-pair
================

display key-pair

Function
--------

The **display key-pair** command displays the information about the specified key-pairs.



Format
------

**display dsa key-pair**

**display dsa key-pair brief**

**display dsa key-pair label** *label-name*

**display ecc key-pair**

**display ecc key-pair brief**

**display ecc key-pair label** *label-name*

**display sm2 key-pair**

**display sm2 key-pair brief**

**display sm2 key-pair label** *label-name*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dsa** | Displays the information about all DSA key-pairs. | - |
| **brief** | Displays brief information about the specified key pairs. | - |
| **label** *label-name* | Displays information about the key pair with the specified label name. | The value is a string of 1 to 35 case-insensitive characters, spaces not supported. The string can contain only letters, digits, and underscores (\_). |
| **ecc** | Displays the information about all ECC key-pairs. | - |
| **sm2** | Displays the information about all SM2 key-pairs. | - |




Views
-----

All views



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To display all the information about the specified key pairs of the device functioning as a client, run the display key-pair command. Then, manually copy the displayed information to the server to enable the server to authenticate users and permit the login requests of authorized users.

**Prerequisites**

* To view the DSA key pair, run the **dsa key-pair label** command to generate a DSA key pair first.
* To view an ECC key pair, run the **ecc key-pair label** command to generate an ECC key pair first.
* To view an SM2 key pair, run the **sm2 key-pair label** command to generate an SM2 key pair first.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display information about the DSA key pair named dsakey001.
```
<HUAWEI> display dsa key-pair label dsakey001
=====================================
Label name: dsakey001
Modulus: 512
Time of Key pair created: 2013-11-06 15:39:45-08:00
=====================================
Key Code :
3081DC
  0240
    AE0AE467 2BF3587F 30FE81FF A14D8070 1FC2930B
    A34004C1 B37824BB D3160595 702901CD 53F0EAE0
    6CC46D2D BE78F6A4 3DC4AAEF C7228E01 9C2EF7CE
    87C63485
  0214
    94FC5624 DCEB09DA E9B88293 2AC88508 AB7C813F
  0240
    91FF0F2C 91996828 BAAD5068 CD2FE83E CEFA1CF4
    7BCA4251 9F04FD24 6CFB50A3 AD78CC0D 335DEFD2
    0B4C3530 DAA25592 DEAFA0EB 61225712 E4AF6139
    C986329F
  0240
    98CCB354 470D1C14 C139ECCB D3BE1001 45FE8781
    D201B6C9 1B1CFB86 B8F863C0 AEB412B9 6531F20C
    75FF3B72 489AA98F 14A05B70 AB1329A1 78AF23C7
    7EAC0363
=====================================

```

# Display information about all ECC key-pairs.
```
<HUAWEI> display ecc key-pair
=====================================                                                                                               
Label name: ecckey001
Modulus: 521                                                                                                                        
Time of Key pair created: 2016-03-03 20:48:26                                                                                       
                                                                    
=====================================                                                                                               
Key :                                                                                                                               
    0400F6A5 D962C5DA A710D61E 64C8EDEB 5209C897 3BBD31ED 0B09CF7E                                                                  
    9C59AB15 F508D518 7161F2DA D83F83CE 1BFE500F BB8049B6 D54C4CE8                                                                  
    389E453F 3C8E24D5 2E127501 26F00B25 26A332EC 21FCB570 10391599                                                                  
    E289FFED E6D523C8 10271047 28954F4F A354CDD5 EA384158 349299BA                                                                  
    39064277 58DBE66B A2F3DA72 23ADEB54 3AC14A90 84                                                                                 
=====================================                                                                                               
=====================================                                                                                               
Label name: ecckey002
Modulus: 521                                                                                                                        
Time of Key pair created: 2016-03-08 14:36:00                                                                                       
                                                                    
=====================================                                                                                               
Key :                                                                                                                               
    0400FCB0 9B89B39D 6A60B19A F12CF8D4 861C17FE 1EB7679A 73314769                                                                  
    819CDA57 2DCBED49 6D9FA3DD E0200D7F 76A67683 4F25355C 4403E1C2                                                                  
    263A20A0 1769E471 B3944501 4BCAFF21 587F3621 30DE3834 92033D1F                                                                  
    D11B205D 7B29F017 5BA2B200 E3FD01F2 A26001EF C6C71AD1 60F102E8                                                                  
    8C81C176 CE2C7718 74F2C5F0 687A5EA8 5F5B21B3 61                                                                                 
=====================================

```

# Display brief information about all ECC key-pairs.
```
<HUAWEI> display ecc key-pair brief
=====================================
Label name: ecckey001
Modulus: 521
Time of Key pair created: 2016-03-03 20:48:26

=====================================
=====================================
Label name: ecckey002
Modulus: 521
Time of Key pair created: 2016-03-08 14:36:00
=====================================

```

# Display detailed information about all SM2 key pairs.
```
<HUAWEI> display sm2 key-pair
=====================================
 Label Name: sm2key001
 Modulus: 521
 Time of Key pair created: 2018-06-19 15:39:45
=====================================
Key : 
    0474F110 F90F131B B6F6D929 9A23A41E F1AB1666 AC4BE4EE EF2CD876
    2B633F80 DD5CF42F 147A722F DE527F39 247F3744 C23296BE FE3BE502
    EEF7D9EC BC28A576 7E
=====================================

```

# Display brief information about all SM2 key pairs.
```
<HUAWEI> display sm2 key-pair brief
=====================================
 Label Name: sm2key001
 Modulus: 521
 Time of Key pair created: 2018-06-19 15:39:45
=====================================

```


**Table 1** Description of the
**display key-pair** command output

| Item | Description |
| --- | --- |
| Label name | Indicates the label name. |
| Time of Key pair created | Indicates the creation time of the key-pair. |
| Key fingerprint | Indicates the public key fingerprint. |
| Key/Key Code | Code of a public key. |
| Modulus | Indicates the modulus of a key-pair. |