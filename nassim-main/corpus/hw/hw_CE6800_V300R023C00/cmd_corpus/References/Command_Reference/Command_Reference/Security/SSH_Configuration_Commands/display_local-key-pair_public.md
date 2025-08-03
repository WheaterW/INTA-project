display local-key-pair public
=============================

display local-key-pair public

Function
--------

The **display local-key-pair public** command displays the public key information in the specified local key pair.



Format
------

**display rsa local-key-pair public**

**display dsa local-key-pair public**

**display ecc local-key-pair public**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dsa** | Displays the public key in the local DSA key pair. | - |
| **ecc** | Displays the public key in the local ECC key pair. | - |
| **rsa** | Displays the public key in the local RSA key pair. | - |




Views
-----

All views



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To display information about the public key in the specified key pair of the device functioning as an SSH client, run the display local-key-pair public command. Then, manually copy the displayed information to the server to enable the server to authenticate users and permit the login requests of authorized users.

**Prerequisites**

* Run the **dsa key-pair label** command to generate DSA key pairs if specified to display the public key information about DSA key pairs.
* Run the **ecc key-pair label** command to generate ECC key pairs if specified to display the public key information about ECC key pairs.
* Run the **rsa key-pair label** command to generate RSA key pairs if specified to display the public key information about RSA key pairs.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display information about the public key in the local RSA key pair on a client.
```
<HUAWEI> display rsa local-key-pair public
======================Host key==========================
Time of key pair created : 2022-05-03 03:08:31
Key name                 : Host
Key type                 : RSA encryption key
========================================================
Key code:
3082010A
  02820101
    00A8156F B1A79FED 471A99A6 738B1C5D 1BEF87C5
    8EC32FA3 6431F83C A03A188B E412C934 CC5324CE
    1B427F12 B5667658 22E183DE AA7B2369 8E3B1D55
    C0255731 2F9697D4 73FCC979 499E7B44 258D4413
    0947A18B 09E50C26 C1582A5C 73E6730E 9E1A419D
    52BF8005 59C296D9 18E8C644 176A6689 C39720D0
    97EB8E85 80ADCBBA 4D6D619E 9D4F7177 1C0D6AB8
    D0264239 C64935B3 644C6FC1 0F6DBE81 B3BC5900
    393019E9 FC0A14EC F6E71C82 5514A091 8B0D3C99
    DB8462CF D2B805E3 35D51A54 78B6E5F9 9D605240
    1302B423 4DF68D65 BAF5B454 8B2657AF 16B07ABF
    BA024681 CC992B06 72B6A4C9 3059771E B977C3D1
    60BCC77E FBC6273D 53ECCD68 37C03F28 C5
  0203
    010001

Host public key for PEM format code:
---- BEGIN SSH2 PUBLIC KEY ----
AAAAB3NzaC1yc2EAAAADAQABAAABAQCoFW+xp5/tRxqZpnOLHF0b74fFjsMvo2Qx
+DygOhiL5BLJNMxTJM4bQn8StWZ2WCLhg96qeyNpjjsdVcAlVzEvlpfUc/zJeUme
e0QljUQTCUehiwnlDCbBWCpcc+ZzDp4aQZ1Sv4AFWcKW2RjoxkQXamaJw5cg0Jfr
joWArcu6TW1hnp1PcXccDWq40CZCOcZJNbNkTG/BD22+gbO8WQA5MBnp/AoU7Pbn
HIJVFKCRiw08mduEYs/SuAXjNdUaVHi25fmdYFJAEwK0I032jWW69bRUiyZXrxaw
er+6AkaBzJkrBnK2pMkwWXceuXfD0WC8x377xic9U+zNaDfAPyjF
---- END SSH2 PUBLIC KEY ----

Public key code for pasting into OpenSSH authorized_keys file:
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCoFW+xp5/tRxqZpnOLHF0b74fFjsMvo2Qx+DygOhiL5BLJNMxTJM4bQn8StWZ2WCLhg96qeyNpjjsdVcAlVzEvlpfUc/zJeUmee0QljUQTCUehiwnlDCbBWCpcc+ZzDp4aQZ1Sv4AFWcKW2RjoxkQXamaJw5cg0JfrjoWArcu6TW1hnp1PcXccDWq40CZCOcZJNbNkTG/BD22+gbO8WQA5MBnp/AoU7PbnHIJVFKCRiw08mduEYs/SuAXjNdUaVHi25fmdYFJAEwK0I032jWW69bRUiyZXrxawer+6AkaBzJkrBnK2pMkwWXceuXfD0WC8x377xic9U+zNaDfAPyjF rsa-key

```

# Display information about the public key in the local ECC key pair on a client.
```
<HUAWEI> display ecc local-key-pair public
========================================================
Time of Key pair created : 2022-06-28 21:03:16
Key Name : Host_ECC
Key modulus : 256
Key Type : ECC Encryption Key
========================================================
Key Code:
  04784D25 9A25C8BD 9C8A298D 3B64DFE6 4E6A657E
  0962B8B6 4235B0F3 CD9BE00D 79FD02F5 43A35D34
  59F36439 4269A8FF BEEEBD79 1301EB52 EAFE057A
  4AE6FBF4 8C

Host public key for PEM format code:
---- BEGIN SSH2 PUBLIC KEY ----
AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHhNJZolyL2c
iimNO2Tf5k5qZX4JYri2QjWw882b4A15/QL1Q6NdNFnzZDlCaaj/vu69eRMB61Lq
/gV6Sub79Iw=
---- END SSH2 PUBLIC KEY ----

Public key code for pasting into OpenSSH authorized_keys file:
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAy
NTYAAABBBHhNJZolyL2ciimNO2Tf5k5qZX4JYri2QjWw882b4A15/QL1Q6NdNFnz
ZDlCaaj/vu69eRMB61Lq/gV6Sub79Iw= ecdsa-key

```

# Display information about the public key in the local DSA key pair on a client.
```
<HUAWEI> display dsa local-key-pair public
========================================================
Time of key pair created : 2022-06-28 22:21:49
Key name                 : Host_DSA
Key modulus              : 3072
Key type                 : DSA encryption key
========================================================
Key code:
30820324
  02820101
    00DEDEBA 5C8244DC B8E69691 7CEFEBC0 B3E6FB60
    BE8B9E36 D3E4EB9C D6EB7FD2 10219AC0 F41AD47B
    F1EACD43 5D39AFA8 FACB6A78 19305EE1 47E42891
    2E60452B 37CA17D6 11C2EE4C 46B4BC77 2654C268
    56A99ECF A5D80036 7B31A905 22F13949 6F4182DB
    FDAAB599 739AB021 85856A88 1F919736 8B92DBF6
    849D1C74 6BA27E12 F98A28E4 B6D0587D 655979A7
    505413E9 1EFC961C 3F792096 25CFA8D7 D469FA35
    A39E37B6 14047D53 5DCD63AF 3058B3A2 5B79C714
    B6326B7D B6067EBF 153CC1A7 20B0E1A7 E39C13FE
    B3BA26E6 B052DC5B FFEE7C5C 52148FE6 C240738F
    BB8F05D4 16B2B5DD 72E3629B B59244BF 9FA29C4F
    CD4EA0EE 501FC669 5D03D68D 519324E4 93
  0215
    00C6C484 E1F0076B 8AFCAD30 2B98B50A 3A542ABE
    BB
  02820100
    3AC11746 EE959CBD 30F669C5 7E290BC4 7CB5BBFD
    96AE9215 7A29C723 72FE8A02 EBED3B76 BE810B42
    21AD8D32 F7723F83 59F46B66 FF7805CC 3F86D5D6
    5BD424BD 70677EFF 1ACF9B3C CE02CD40 46560DA4
    2036205C 6EFAB148 66E6A106 0DF6258B EE31CFE7
    4B6C59B4 6FE59A9F BE64F982 EC36A669 FF597FB7
    9A56E32E C15A0659 3D17C407 29F587C7 74959017
    62B08070 24564B2E E79C6E1D 86793548 76CC662A
    1D3DE1D1 2C79E102 C0B10E5C 9C4428B3 AEB93278
    26D4CDE5 189A93EA 531E0FF8 2199EF35 DF038976
    4538434F F39924F0 5BF17AC8 8E340991 B5EA0A62
    A915EE63 F660C092 360C5D2D 796AF230 DB7461F7
    C15B6DBA 65C9EFAB 247DB13D 4942E2FF
  02820100
    62B4FAC6 4D5009E2 BA378727 AB97D6EE 1174F951
    6D1FA663 B950386E 7DD6BDDD 7447345B 5AE2ADBF
    BC0EEF48 39FB49B7 62D2A601 2E110DB9 AAA4DF0B
    B953DE0D D4370F48 017A185E 065E86F1 9214680A
    F6003562 9A29023F 8CCBD021 8948B4E0 D89FBFD5
    9EC1596E 2CA7C626 F4579757 0066AA47 964D4F73
    EC4291C4 1A540832 DB995272 C2F74617 B6CEE55E
    E8E35445 3831071C 03A9EAA9 C06CC3CE 1F602950
    599523A2 695805F0 2DA7827C 708128F4 B202B80C
    4383837B A275CD0B 79E26EAB 300BDB9F 87EFB248
    295B35F6 2C00E868 5A7A2947 B9E0F40B D6C6E143
    C59C12EC 623BF989 61AB4F51 5CE9E850 C2DFE43E
    4857526D C4DBBAE5 8870CC17 D17C3AFF

Host public key for PEM format code:
---- BEGIN SSH2 PUBLIC KEY ----
AAAAB3NzaC1kc3MAAAEBAN7eulyCRNy45paRfO/rwLPm+2C+i5420+TrnNbrf9IQ
IZrA9BrUe/HqzUNdOa+o+stqeBkwXuFH5CiRLmBFKzfKF9YRwu5MRrS8dyZUwmhW
qZ7PpdgANnsxqQUi8TlJb0GC2/2qtZlzmrAhhYVqiB+RlzaLktv2hJ0cdGuifhL5
iijkttBYfWVZeadQVBPpHvyWHD95IJYlz6jX1Gn6NaOeN7YUBH1TXc1jrzBYs6Jb
eccUtjJrfbYGfr8VPMGnILDhp+OcE/6zuibmsFLcW//ufFxSFI/mwkBzj7uPBdQW
srXdcuNim7WSRL+fopxPzU6g7lAfxmldA9aNUZMk5JMAAAAVAMbEhOHwB2uK/K0w
K5i1CjpUKr67AAABADrBF0bulZy9MPZpxX4pC8R8tbv9lq6SFXopxyNy/ooC6+07
dr6BC0IhrY0y93I/g1n0a2b/eAXMP4bV1lvUJL1wZ37/Gs+bPM4CzUBGVg2kIDYg
XG76sUhm5qEGDfYli+4xz+dLbFm0b+Wan75k+YLsNqZp/1l/t5pW4y7BWgZZPRfE
Byn1h8d0lZAXYrCAcCRWSy7nnG4dhnk1SHbMZiodPeHRLHnhAsCxDlycRCizrrky
eCbUzeUYmpPqUx4P+CGZ7zXfA4l2RThDT/OZJPBb8XrIjjQJkbXqCmKpFe5j9mDA
kjYMXS15avIw23Rh98Fbbbplye+rJH2xPUlC4v8AAAEAYrT6xk1QCeK6N4cnq5fW
7hF0+VFtH6ZjuVA4bn3Wvd10RzRbWuKtv7wO70g5+0m3YtKmAS4RDbmqpN8LuVPe
DdQ3D0gBehheBl6G8ZIUaAr2ADVimikCP4zL0CGJSLTg2J+/1Z7BWW4sp8Ym9FeX
VwBmqkeWTU9z7EKRxBpUCDLbmVJywvdGF7bO5V7o41RFODEHHAOp6qnAbMPOH2Ap
UFmVI6JpWAXwLaeCfHCBKPSyArgMQ4ODe6J1zQt54m6rMAvbn4fvskgpWzX2LADo
aFp6KUe54PQL1sbhQ8WcEuxiO/mJYatPUVzp6FDC3+Q+SFdSbcTbuuWIcMwX0Xw6
/w==
---- END SSH2 PUBLIC KEY ----

Public key code for pasting into OpenSSH authorized_keys file:
ssh-dss AAAAB3NzaC1kc3MAAAEBAN7eulyCRNy45paRfO/rwLPm+2C+i5420+TrnNbrf9IQIZrA9BrUe/HqzUNdOa+o+stqeBkwXuFH5CiRLmBFKzfKF9YRwu5MRrS8dyZUwmhWqZ7PpdgANnsxqQUi8TlJb0GC2/2qtZlzmrAhhYVqiB+RlzaLktv2hJ0cdGuifhL5iijkttBYfWVZeadQVBPpHvyWHD95IJYlz6jX1Gn6NaOeN7YUBH1TXc1jrzBYs6JbeccUtjJrfbYGfr8VPMGnILDhp+OcE/6zuibmsFLcW//ufFxSFI/mwkBzj7uPBdQWsrXdcuNim7WSRL+fopxPzU6g7lAfxmldA9aNUZMk5JMAAAAVAMbEhOHwB2uK/K0wK5i1CjpUKr67AAABADrBF0bulZy9MPZpxX4pC8R8tbv9lq6SFXopxyNy/ooC6+07dr6BC0IhrY0y93I/g1n0a2b/eAXMP4bV1lvUJL1wZ37/Gs+bPM4CzUBGVg2kIDYgXG76sUhm5qEGDfYli+4xz+dLbFm0b+Wan75k+YLsNqZp/1l/t5pW4y7BWgZZPRfEByn1h8d0lZAXYrCAcCRWSy7nnG4dhnk1SHbMZiodPeHRLHnhAsCxDlycRCizrrkyeCbUzeUYmpPqUx4P+CGZ7zXfA4l2RThDT/OZJPBb8XrIjjQJkbXqCmKpFe5j9mDAkjYMXS15avIw23Rh98Fbbbplye+rJH2xPUlC4v8AAAEAYrT6xk1QCeK6N4cnq5fW7hF0+VFtH6ZjuVA4bn3Wvd10RzRbWuKtv7wO70g5+0m3YtKmAS4RDbmqpN8LuVPeDdQ3D0gBehheBl6G8ZIUaAr2ADVimikCP4zL0CGJSLTg2J+/1Z7BWW4sp8Ym9FeXVwBmqkeWTU9z7EKRxBpUCDLbmVJywvdGF7bO5V7o41RFODEHHAOp6qnAbMPOH2ApUFmVI6JpWAXwLaeCfHCBKPSyArgMQ4ODe6J1zQt54m6rMAvbn4fvskgpWzX2LADoaFp6KUe54PQL1sbhQ8WcEuxiO/mJYatPUVzp6FDC3+Q+SFdSbcTbuuWIcMwX0Xw6/w== dsa-key

```


**Table 1** Description of the
**display local-key-pair public** command output

| Item | Description |
| --- | --- |
| Time of Key pair created | Time when the public key in the local DSA key pair is generated, in the format of YYYY-MM-DD HH:MM:SS . |
| Key Name | Name of the public key in the local DSA key pair. |
| Key modulus | Length of the local DSA key pair. The length can be 2048 bits. |
| Key Type | Type of the public key in the local DSA key pair. |
| Key Code | Code of the public key in the local DSA key pair configured using the dsa local-key-pair create command.  The public key coding formats from top to bottom are hexadecimal, PEM, and OpenSSH, which match the public key formats supported by the tool. Here, SSH2.0 public keys are displayed. |