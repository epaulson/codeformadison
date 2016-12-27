CODE=YeGsu2znImihpiFV2PDOkzRHd50Gs6
CLIENT_SECRET=VpZ2J1EjPCPYdM1YxDbD7pdmxddtcjcZ1Kblvmfwc81n7SkIAW2RDVEZMMyFGRbHP6wU0pOzROs4dUerAvpb02qMf9N6iufrnHX51jUj9ORZnFxbdnldc7tQ253AE8ry
curl -v -v -v -X POST -d "grant_type=authorization_code&code=$CODE&redirect_uri=http://localhost:7000/" --user testapp:$CLIENT_SECRET http://localhost:8000/o/token/

