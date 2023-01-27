import requests
# "UYRVFUYRGF7473"
import datetime as dt

TOKEN="UYRVFUYRGF7473"
USERNAME="YOur username"
GRAPH_ID="graph1"

now=dt.datetime.now()
date=now.strftime("%Y%m%d")

pixela_endpoint="https://pixe.la/v1/users"
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
pixelpoint_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

request_body={
	"token":TOKEN,
	"username":USERNAME,
	"agreeTermsOfService":"yes",
	"notMinor":"yes",
	
}

request_header_key={
	"X-USER-TOKEN":TOKEN
}


graph_request_body={
	"id":"graph1",
	"name":"Rahul's Graph Test",
	"type":"float",
	"color":"shibafu",
	"unit":"kilometer"
}

pixel_request={
	"date":date,
	"quantity":"5",
	
}
# response=requests.post(url=pixela_endpoint,json=request_body)
# response=requests.post(url=graph_endpoint,json=graph_request_body,headers=request_header_key)

response=requests.post(url=pixelpoint_endpoint,json=pixel_request,headers=request_header_key)
print(response.text)
