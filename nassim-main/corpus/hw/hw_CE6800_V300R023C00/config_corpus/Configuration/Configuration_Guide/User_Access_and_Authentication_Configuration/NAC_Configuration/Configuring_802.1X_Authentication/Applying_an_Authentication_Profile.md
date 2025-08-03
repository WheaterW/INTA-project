Applying an Authentication Profile
==================================

Applying an Authentication Profile

#### Prerequisites

1. An 802.1X access profile has been configured. For details, see [Configuring an 802.1X Access Profile](galaxy_nac_cfg_0048.html).
2. An authentication profile has been configured. For details, see [Configuring an Authentication Profile](galaxy_nac_cfg_0054.html).

#### Context

After an access profile is bound to an authentication profile and the authentication profile is applied to the interface through which users go online, NAC authentication is enabled on the interface.

* **NAC support on different interfaces**:
  + 802.1X authentication is supported on Layer 2 physical interfaces and Eth-Trunk interfaces.
  + When NAC is configured on a main interface, service functions on its sub-interfaces will be affected.
  + When users go online or are re-authenticated through an inter-board Eth-Trunk interface, resetting one of the boards may disconnect the users.
* Users who have static MAC address entries configured can obtain network access rights without authentication. If these users need to be authenticated, you need to delete their static MAC address entries.
* Interconnection with a Cisco ISE server through Central Web Authentication (CWA) is not supported.
* The number of NAC users cannot exceed the maximum number of MAC address entries supported by the device.


#### Procedure

* Apply an authentication profile to an interface.
  
  
  1. Enter the system view.
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode to Layer 2.
     ```
     [portswitch](cmdqueryname=portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Apply an authentication profile to an interface.
     ```
     [authentication-profile](cmdqueryname=authentication-profile) authentication-profile-name
     ```
     
     By default, no authentication profile is applied to an interface.
  5. Commit the configuration.
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display authentication interface**](cmdqueryname=display+authentication+interface) *interface-type interface-number* command to check the NAC authentication mode on a specified interface.