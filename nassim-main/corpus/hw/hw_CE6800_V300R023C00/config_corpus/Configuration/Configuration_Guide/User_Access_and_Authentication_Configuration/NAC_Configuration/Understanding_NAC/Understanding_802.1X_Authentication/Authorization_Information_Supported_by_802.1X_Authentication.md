Authorization Information Supported by 802.1X Authentication
============================================================

Authentication checks whether the identity of the user who attempts to access the network is valid. Authorization specifies the network access rights that an authorized user can have, that is, the resources that the authorized user can access. This section uses RADIUS server authorization as an example to describe several common authorization parameters and the configurations required on the access device and server. For details about other authorization modes and more authorization parameters, see [(Optional) Configuring a Service Scheme](galaxy_aaa_cfg_0014.html).

#### VLAN

To prevent unauthenticated users from accessing restricted network resources, such users and resources need to be allocated to different VLANs. After a user is authenticated, the authentication server authorizes the specified VLAN to the user. The access device then assigns the authorized VLAN to the user, without changing the interface configuration. The authorized VLAN takes precedence over the configured VLAN. That is, the authorized VLAN takes effect after the authentication succeeds, and the configured VLAN takes effect after the user goes offline.

VLAN authorization requires that VLANs have been deployed on the access device.

When the RADIUS server authorizes a VLAN, the following standard RADIUS attributes must be used together:

* Tunnel-Type: The value must be set to VLAN or 13.
* Tunnel-Medium-Type: The value must be set to 802 or 6.
* **Tunnel-Private-Group-ID**: Authorization can be performed based on the VLAN name, VLAN description, and VLAN ID, which are listed in ascending order of priority.


#### ACL

After a user is authenticated, the authentication server assigns an ACL to the user. Then the access device controls the user's packets according to the ACL.

* If the packets match the permit rule in the ACL, the access device permits the packets.
* If the packets match the deny rule in the ACL, the access device discards the packets.

The RADIUS server can assign ACLs using the following methods:

* Static ACL assignment: The RADIUS server uses the standard RADIUS attribute Filter-Id to assign an ACL ID to the user. In this method, the ACL and ACL rules need to be configured on the access device in advance.