Example for Configuring an 802.1X Supplicant
============================================

Example_for_Configuring_an_802.1X_Supplicant

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172372674__fig_dc_ne_cfg_8021x_0004011), the NE40E functions as an 802.1X supplicant and connects to an authenticator. 802.1X authentication is implemented to ensure that the NE40E will not be replaced.

**Figure 1** Typical networking for 802.1X supplicant authentication![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/2/0 .


  
![](images/fig_dc_ne_cfg_8021x_0004011.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

* Configure a RADIUS authentication scheme.
* Configure an authenticator.
* Configure an 802.1X supplicant template and enable the 802.1X supplicant function on an interface.

#### Data Preparation

To configure 802.1X authentication, you need the following data:

* Name of the 802.1X supplicant template, user name, password, and authentication mode
* Name of the interface on which the 802.1X supplicant function is enabled

#### Procedure

1. Create an 802.1X supplicant template numbered **1** and enter the 802.1X supplicant template 1 view.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [HUAWEI] dot1x-supplicant-template 1
   ```
2. Configure a user name and password for the 802.1X supplicant template 1 as **huawei** and **YsHsjx\_202206**, respectively.
   
   
   ```
   [HUAWEI-dot1x-supplicant-template-1] eap username huawei password cipher YsHsjx_202206
   ```
   ```
   [HUAWEI-dot1x-supplicant-template-1] quit
   ```
3. Enable the 802.1X supplicant function on GE 0/2/0 and specify the number of the 802.1X supplicant template as 1.
   
   
   ```
   [HUAWEI] interface Gigabitethernet 0/2/0
   ```
   ```
   [HUAWEI-Gigabitethernet0/2/0] dot1x supplicant enable template 1
   ```
   ```
   [HUAWEI-Gigabitethernet0/2/0] quit
   ```
4. Verify the configuration.
   
   
   ```
   <HUAWEI> display dot1x supplicant
   ```
   ```
   ---------------------------------------------------------------------------
   ```
   ```
    Interface                        Status                   Template Index  
   ```
   ```
   ---------------------------------------------------------------------------
   ```
   ```
    GigabitEthernet0/2/0             initial                  1               
   ```

#### Configuration Files

Configuration file of the NE40E

```
#
dot1x-supplicant-template 1
 eap username huawei password cipher %^%#J$iaV.oS4VZKv+Sui[<GZ%0=G=d^5Sr1@[BbvzBI%^%# 
#
interface GigabitEthernet0/2/0
 undo shutdown
 dot1x supplicant enable template 1
#
return
```