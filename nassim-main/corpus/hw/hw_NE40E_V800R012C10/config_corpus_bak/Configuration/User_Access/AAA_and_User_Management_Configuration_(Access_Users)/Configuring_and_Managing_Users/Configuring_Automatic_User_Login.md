Configuring Automatic User Login
================================

Configuring_Automatic_User_Login

#### Usage Scenario

In a Dynamic Host Configuration
Protocol version 4 (DHCPv4) user access scenario, when the Router is restarted or its board, subcard, or interface is faulty, DHCPv4
users are logged out and their information is lost. If a DHCPv4 client
does not detect the fault, the DHCPv4 client does not resend a DHCP
request packet to the Router or redial up after the fault is rectified. As a result, the DHCPv4
user cannot go online again. To prevent this issue, configure automatic
user login. After this configuration, user information is saved automatically
to the memory before any fault occurs, and the users can go online
automatically after the fault is rectified.

If the Router is powered off and restarted, user information saved in the high-end
memory will be lost. Before the Router is powered off, write the user information saved in the high-end
memory to the CF card. After the Router is restarted, restore the user information saved in the CF card
to the high-end memory.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The following DHCPv4 user information is saved: MAC address, IP address, VLAN/PVC, access interface, VPN instance name, domain name, lease, Option 82, Option 60, Option 61, and IP address of the DHCPv4 server. The DHCPv4 user information is used only when the DHCPv4 users go online automatically. To ensure security, do not save DHCPv4 user information in the CF card for a long time and clear it in time.




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**access-user dhcp auto-save enable**](cmdqueryname=access-user+dhcp+auto-save+enable) **max-user-number** *max-user-number*
   
   
   
   Automatic backup of DHCPv4 user information is enabled globally,
   and the maximum number of DHCPv4 users whose information can be backed
   up in all domains is specified.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The device backs up only information about the configured maximum number of DHCPv4 users in all domains. The excessive part of DHCPv4 user information is not backed up. Specify *max-user-number* as the total number of DHCPv4 users whose information needs to be backed up in all domains.
   
   The **access-user dhcp auto-save** command applies for a memory space based on the maximum number of DHCPv4 users. If the command cannot apply for the size of contiguous memory space, the command fails to be executed, and automatic backup of DHCPv4 user information is disabled.
3. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
4. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The AAA domain view is displayed.
5. Run [**access-user dhcp auto-save enable**](cmdqueryname=access-user+dhcp+auto-save+enable)
   
   
   
   Automatic backup of DHCPv4 user information is enabled in
   the domain.
   
   
   
   Information
   about online DHCPv4 users in the domain is saved in the high-end memory,
   which is a storage medium. The larger the configured maximum number
   of the DHCPv4 users, the more memory space the user information takes
   up. For example, information about 64000 DHCPv4 users takes up 50
   MB of memory.
   
   In a dual-system hot
   backup scenario, DHCPv4 user information is backed up using the dual-system
   hot backup mechanism, so the device does not save information about
   these DHCPv4 users in the high-end memory.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the AAA view.
7. Run [**access-trigger lease-end-time original**](cmdqueryname=access-trigger+lease-end-time+original)
   
   
   
   The Router is configured to apply the original lease time to users
   that go online again after going offline abnormally.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
9. Run [**access-user dhcp auto-recover enable**](cmdqueryname=access-user+dhcp+auto-recover+enable)
   
   
   
   Automatic DHCPv4 user login is enabled.
10. (Optional) Run [**access-user
    dhcp auto-recover nosend-packet**](cmdqueryname=access-user+dhcp+auto-recover+nosend-packet)
    
    
    
    The device is disabled from sending DHCPv4 messages to a
    remote DHCPv4 server when users automatically re-log in to the device
    after the device recovers from a fault. This prevents user login failures
    caused by IP address conflicts.
11. (Optional) Run [**access-user dhcp auto-recover speed**](cmdqueryname=access-user+dhcp+auto-recover+speed) { **slow** | **normal** | **fast** }
    
    
    
    The rate at which DHCPv4 users automatically go online after
    the Router recovers from a fault is configured.
    
    * If **slow** is configured, the maximum
      rate at which DHCPv4 users automatically go online after the Router recovers from a fault is 100/s.
    * If **normal** is configured, the maximum
      rate at which DHCPv4 users automatically go online after the Router recovers from a fault is 300/s.
    * If **fast** is configured, the maximum
      rate at which DHCPv4 users automatically go online after the Router recovers from a fault is 500/s.
12. To allow users to go online automatically after the Router is powered off and restarted, perform the following operations additionally:
    
    
    1. Before the device is powered off, run [**access-user dhcp save-file**](cmdqueryname=access-user+dhcp+save-file) *file-path-name*
       
       DHCPv4 user
       information saved in the high-end memory is written to the CF card,
       and the directory and file name are specified.
       
       ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
       
       If there is a large amount of DHCPv4 user information saved in the high-end memory, it takes a long time for the **access-user dhcp save-file** command to write the information to the CF card, which may affect services. Exercise caution when you run this command.
    2. After the device is restarted, run [**access-user dhcp
       recover-file**](cmdqueryname=access-user+dhcp+recover-file) *file-path-name*
       
       DHCPv4 user information saved in the CF card is restored to
       the high-end memory.
       
       The device reads DHCPv4 user information in the CF card and saves the information in the high-end memory. The new information does not override the original DHCPv4 user information saved in the high-end memory.
13. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

Run the [**display access-user auto-save user-info**](cmdqueryname=display+access-user+auto-save+user-info) { **online** | **wait-recover** | **mac-address** *mac-address* [ **interface** { *interface-name* | *interface-type* *interface-number* } [ **pevlan** *pevlan* **cevlan** *cevlan* ] ] } command to check DHCPv4 user
information saved in the high-end memory.

Run the [**display
access-user auto-save statistics**](cmdqueryname=display+access-user+auto-save+statistics) command to check
statistics about DHCPv4 user information saved in the high-end memory
after automatic backup is enabled.