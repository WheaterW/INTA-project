Checking Backup Information
===========================

You can run display commands to check backup information.

#### Context

After the preceding configurations are complete, run the following **display** commands to view backup information and check the configurations. For details, see *HUAWEI NE40E-M2 series Universal Service Router Command Reference*.


#### Procedure

1. Run the [**display remote-backup-profile**](cmdqueryname=display+remote-backup-profile) { **slot** *slot-number* } [ *profile-name* ] command to check RBP information.
2. Run the [**display remote-backup-service**](cmdqueryname=display+remote-backup-service) [ *service-name* [ **verbose** ] ] command to check RBS information.
3. Run the [**display multicast-rui statistic all**](cmdqueryname=display+multicast-rui+statistic+all) command to check multicast hot backup statistics.