Using Telnet to Log In to the System
====================================

After you log in to a device through a console port and configure the device, you can use Telnet to log in to and remotely maintain the device.

#### Context

To log in to the system by using Telnet, use either the Windows Command Prompt or third-party software on the terminal. Use the Windows Command Prompt as an example.

Perform the following steps on the PC.

![](../../../../public_sys-resources/note_3.0-en-us.png) In the case of device login through a VTY channel, to avoid the access failure that occurs when the number of VTY connections exceeds the upper threshold, you can perform the following operations to check and configure the maximum number of VTY users that can log in to the device:

1. Run the [**display user-interface maximum-vty**](cmdqueryname=display+user-interface+maximum-vty) command to check the maximum number of VTY users that are supported.
2. Run the [**display user-interface**](cmdqueryname=display+user-interface) command to check user interface information. The plus sign (+) indicates an occupied channel. If all channels are occupied, subsequent users cannot log in to the device. If an online user logs out, the user may fail to log in again when its channel is occupied by another user. In this case, run the [**user-interface maximum-vty**](cmdqueryname=user-interface+maximum-vty) *number* command to configure the maximum number of users that are allowed to log in.



#### Procedure

1. Enter the Windows Command Prompt window.
2. Run the [**telnet**](cmdqueryname=telnet) *ip-address* command to use Telnet to log in to the device.
   
   
   1. Enter the IP address of the Telnet server.
   2. Press **Enter**. The command prompt of the user view, for example, **<HUAWEI>**, is displayed, indicating that you have accessed the Telnet server.

#### Follow-up Procedure

You can run the [**kill user-interface**](cmdqueryname=kill+user-interface) { *ui-number* | *ui-type ui-number1* } command to log out a user.

The parameter **console**  is supported only on the Admin-VS.