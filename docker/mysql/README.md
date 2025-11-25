mysqldump --databases native_api native_api_staging -uadmin -p -h native-api-uat-instance-1.cypidsjsn5do.ap-northeast-1.rds.amazonaws.com --where="true limit 10000" --set-gtid-purged=OFF > all.sql
