SSHUSER=bill
jump=h-ops-0.aws-sea-1.test.native.host.intra.native.org

autossh -M 14701 -f -N -L 0.0.0.0:10701:localhost:10701 $SSHUSER@$jump

autossh -M 14801 -f -N -L 0.0.0.0:10801:localhost:10801 $SSHUSER@$jump
autossh -M 14802 -f -N -L 0.0.0.0:10802:localhost:10802 $SSHUSER@$jump
autossh -M 14803 -f -N -L 0.0.0.0:10803:localhost:10803 $SSHUSER@$jump
autossh -M 14804 -f -N -L 0.0.0.0:10804:localhost:10804 $SSHUSER@$jump
autossh -M 14805 -f -N -L 0.0.0.0:10805:localhost:10805 $SSHUSER@$jump
autossh -M 14806 -f -N -L 0.0.0.0:10806:localhost:10806 $SSHUSER@$jump
autossh -M 14807 -f -N -L 0.0.0.0:10807:localhost:10807 $SSHUSER@$jump

autossh -M 16374 -f -N -L 0.0.0.0:6374:native-redis-uat-001.native-redis-uat.ca1nai.apne1.cache.amazonaws.com:6379 $SSHUSER@$jump
autossh -M 16375 -f -N -L 0.0.0.0:6375:110.0.11.248:30079 $SSHUSER@$jump

# #TOKYO
# lsof -ti :3307 | xargs kill
# lsof -ti :6374 | xargs kill
#
# #EU
# lsof -ti :3308 | xargs kill
# lsof -ti :6375 | xargs kill
#
# ssh -f -N -L 3307:native-api-uat-instance-1.cypidsjsn5do.ap-northeast-1.rds.amazonaws.com:3306 $SSHUSER@h-ops-0.aws-sea-1.test.native.host.intra.native.org
# ssh -f -N -L 3308:native-eu-mysql-prod-instance-1.ctk6irxso8ht.eu-west-1.rds.amazonaws.com:3306 $SSHUSER@h-ops-0.aws-sea-1.test.native.host.intra.native.org
#
# ssh -f -N -L 0.0.0.0:6374:native-redis-uat-001.native-redis-uat.ca1nai.apne1.cache.amazonaws.com:6379 $SSHUSER@h-ops-0.aws-sea-1.test.native.host.intra.native.org
# ssh -f -N -L 0.0.0.0:6375:110.0.11.248:30079 $SSHUSER@h-ops-0.aws-sea-1.test.native.host.intra.native.org
