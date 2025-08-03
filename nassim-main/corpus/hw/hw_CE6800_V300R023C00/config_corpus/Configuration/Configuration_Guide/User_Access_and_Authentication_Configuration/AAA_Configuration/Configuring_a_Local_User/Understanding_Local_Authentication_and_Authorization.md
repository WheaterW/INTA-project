Understanding Local Authentication and Authorization
====================================================

Understanding Local Authentication and Authorization

#### Local AAA Server

A device functioning as an AAA server is called a local AAA server, which performs user authentication and authorization but not user accounting.

Similar to the remote AAA server, the local AAA server requires the configurations of local user names, passwords, and authorization information. The authentication and authorization speed of a local AAA server is faster than that of a remote AAA server, which reduces operation costs. However, the information storage capacity of a local AAA server is subject to the device hardware.


#### Local User Password Policy

The password policy for local users affects the security of local users. By default, the device has the following restrictions on the user name and password:

* User name: The user name must contain at least six characters.
* Password length and complexity requirements:
  
  + The password must contain at least eight characters.
  + The password must contain the following four types of characters: uppercase letters, lowercase letters, digits, and special characters.
  + The password cannot repeat or reverse the user name.
  + A new password cannot be the same as the last 10 passwords including the current password.
* Password change policy: The local administrator can change the password of a local user of the same or lower privilege level.