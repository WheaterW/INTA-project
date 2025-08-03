Enabling ALS on an Interface
============================

Enabling ALS on an Interface

#### Context

On an optical interface, ALS controls light emission by the laser in the optical module. When an optical fiber is not in position or an optical link is faulty, the corresponding laser automatically disables light emission to save energy and prevent laser-related eye injuries.

The constraints on ALS are as follows:

* ALS is supported only when optical interfaces are preconfigured with optical modules, optical interfaces are installed with optical modules, and COMBO interfaces are working in optical mode. Electrical interfaces do not support ALS.
* When optical interfaces transmit services unidirectionally, they do not support ALS.
* Split interfaces do not support ALS.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Enable ALS on the interface.
   
   
   ```
   [als enable](cmdqueryname=als+enable)
   ```
   
   
   
   By default, ALS is not enabled on an interface.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```