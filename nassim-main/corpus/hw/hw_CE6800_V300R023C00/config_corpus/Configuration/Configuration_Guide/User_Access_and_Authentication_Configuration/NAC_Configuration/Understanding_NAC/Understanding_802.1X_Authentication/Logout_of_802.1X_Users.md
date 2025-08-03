Logout of 802.1X Users
======================

If a user goes offline but the access device and RADIUS server do not detect this event, the following problems may occur:

* The RADIUS server still performs accounting for the user, causing incorrect accounting.
* An unauthorized user can use this user's IP address and MAC address to access the network.
* If there are many offline users, these users continue to occupy user specifications, meaning that other users may fail to access the network.

To avoid such problems, the access device needs to detect the user logout immediately, delete the user entry, and notify the RADIUS server to stop accounting for the user.

A user may log out in the following scenarios: The user proactively logs out of the client, the access device controls user logout, and the RADIUS server controls user logout.

#### The Client Proactively Logs Out

A user sends an EAPoL-Logoff packet through the client software to log out. Upon receipt of the packet, the access device returns an EAP-Failure packet to the client and changes the port state from authorized to unauthorized.

**Figure 1** Client logout process  
![](figure/en-us_image_0000001512681274.png)

#### The Access Device Controls User Logout

You can enable the access device to control user logout using the following methods:

* Configure user detection on the access device to check whether a user is online. If the user does not respond within a specified period, the access device considers the user offline and deletes the user entry.

If an administrator detects that an unauthorized user is online or wants a user to go offline and then go online again for testing purposes, the administrator can run a command on the access device to disconnect the user. For a user in normal access state, the access device checks the user state through ARP probing. If the access device detects that the user goes offline, it disconnects the user and deletes the user entry.

**Figure 2** User logout detection process (using the default three handshakes as an example)  
![](figure/en-us_image_0000001563880401.png)

1. The user sends a packet to trigger 802.1X authentication through the client, and the detection timer starts.
2. If the access device receives traffic from the client within several T periods, it determines that the user is online.
3. The user sends the last packet. If the access device receives traffic from the client when the current T period ends, the access device determines that the user is online and resets the detection timer. Assume that the handshake period is T and the number of handshakes is 3 (configured using the **authentication timer handshake-period** *handshake-period* **handshake-times***handshake-times-value* command), that is, *handshake-period* is T and *handshake-times-value* is 3. In the following situations, the access device deletes the user entry and logs out the user.
   1. If the access device does not receive traffic from the client within the first T period, the access device sends the first ARP request and the client does not respond.
   2. If the access device does not receive traffic from the client within the second T period, the access device sends the second ARP request and the client does not respond.
   3. If the access device does not receive traffic from the client after the third T period, ARP probing fails and the access device deletes the user entry.

#### The RADIUS Server Controls User Logout

The RADIUS server controls user logout using either of the following methods:

* Sends a Disconnect Message (DM) to the access device to disconnect a user who needs to be disconnected.
* Uses the standard RADIUS attributes Session-Timeout and Termination-Action. Session-Timeout specifies the online duration timer value of a user. If the value of Termination-Action is set to 0, the user is disconnected when the online duration timer expires.