Domain-based User Management
============================

An NAS performs domain-based user management. A domain is a group of users and each user belongs to a domain. A user uses only AAA configuration information in the domain to which the user belongs.

In [Figure 1](#EN-US_CONCEPT_0000001564115741__fig_dc_cfg_aaa_602202), configurations including an AAA scheme, a server template, and authorization information are bound to a domain for unified management.

* AAA scheme: includes an authentication scheme, an authorization scheme, and an accounting scheme, which define the authentication, authorization, and accounting methods and the order in which the methods take effect. If server authentication, authorization, and accounting are used, you need to configure a server template. If local authentication and authorization are used, you need to configure a local user.
* Server template: is used to configure a server for authentication, authorization, and accounting. When a server is configured for authorization, you can obtain the authorization information from the server and domain.
* Authorization information in a domain: can be configured in a domain.

Authorization information can be delivered by a server or configured in a domain. Whether a user obtains authorization information delivered by a server or configured in a domain depends on the authorization method configured in the authorization scheme. For details, see [Authorization Scheme](galaxy_aaa_cfg_0005.html).

**Figure 1** AAA configuration information in a domain  
![](figure/en-us_image_0000002013599361.png)
#### Domain to Which a User Belongs

As shown in [Figure 2](#EN-US_CONCEPT_0000001564115741__fig13720105918158), the domain to which a user belongs is determined by the user name for logging in to the NAS. If the user name does not contain the domain name or the domain name contained in the user name is not configured on the NAS, the NAS cannot determine the domain to which the user belongs. In this case, the NAS adds the user to the global default domain based on the user type.

**Figure 2** Determining domains based on user names  
![](figure/en-us_image_0000001563875905.png)

[Table 1](#EN-US_CONCEPT_0000001564115741__table123700558183) provides the mapping between AAA-supported user access modes and global default domains.

**Table 1** Mapping between AAA-supported user access modes and global default domains
| User Type | User Access Mode | Global Default Domain |
| --- | --- | --- |
| Administrator | Is also called a login user and refers to the user who can log in to the NAS.  Includes users who log in to the NAS through FTP, SSH, Telnet, the console port, SNMP, MD-CLI, and HTTP. | default\_admin |
| Access user | Includes 802.1X authentication users. | default |



#### Format of User Names Sent by an NAS to the RADIUS Server

An NAS can determine whether a user name sent to the RADIUS server contains the domain name based on the RADIUS server requirements.

You can set the format of user names sent by an NAS to the RADIUS server using the commands in [Table 2](#EN-US_CONCEPT_0000001564115741__t1).

**Table 2** Setting the format of user names sent by an NAS to the RADIUS server
| Command | User Name Format | User-entered User Name | User Name Sent by an NAS to the RADIUS Server |
| --- | --- | --- | --- |
| **radius-server user-name original** | User-entered original user name | user-name@huawei.com | user-name@huawei.com |
| user-name | user-name |
| **radius-server user-name domain-included** | Domain name included | user-name@huawei.com | user-name@huawei.com |
| user-name | user-name@default  Assume that users use the default domain named **default**. |
| **undo radius-server user-name domain-included** | Domain name excluded | user-name@huawei.com | user-name |
| user-name | user-name |