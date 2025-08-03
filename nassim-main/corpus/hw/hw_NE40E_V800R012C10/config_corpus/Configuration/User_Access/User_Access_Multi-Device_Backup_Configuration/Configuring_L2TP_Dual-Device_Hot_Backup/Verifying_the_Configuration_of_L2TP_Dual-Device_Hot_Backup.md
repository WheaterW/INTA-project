Verifying the Configuration of L2TP Dual-Device Hot Backup
==========================================================

After configuring L2TP dual-device hot backup, verify the configuration.

#### Procedure

* Run the [**display remote-backup-profile**](cmdqueryname=display+remote-backup-profile) [ *profileName* ] command to check RBP information.
* In the User view, run the [**display l2tp tunnel rui**](cmdqueryname=display+l2tp+tunnel+rui) [ **tunnel-item** *tunnel-item* | **tunnel-name** *remote-name* | **remote-backup-profile** *profile-name* | **remote-backup-service** *service-name* ] command to check L2TP tunnel backup information.
* In the User view, run the [**display l2tp session rui**](cmdqueryname=display+l2tp+session+rui) [ **session-item** *session-id* | **source-ip** *source-ip-address* | **destination-ip** *destination-ip-address* | **bas-interface** { *interface-name* | *interface-type* *interface-number* } | **remote-backup-profile** *profile-name* | **remote-backup-service** *service-name* ] command to check L2TP session backup information.
* In the User view, run the [**display l2tp statistics rui**](cmdqueryname=display+l2tp+statistics+rui) [ **verbose** ] command to check L2TP tunnel backup statistics.
* Run the [**display access-user domain**](cmdqueryname=display+access-user+domain) *domain-name* command to display information about the access users in a specified domain.