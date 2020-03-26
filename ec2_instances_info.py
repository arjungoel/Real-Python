import boto3
#from pprint import pprint
import csv
regions = ['ca-central-1', 'us-east-1', 'us-east-2', 'ap-northeast-1', 'ap-southeast-1']

account_id = input("Enter the AWS Account Id:")

session = boto3.session.Session(profile_name="iam_user_1")
resource = session.resource(service_name='ec2', region_name=input("Enter the region code:"))
csv_header = ['S_NO', 'IN_ID', 'IN_TYPE', 'IN_ARCHITECTURE', 'IN_LAUNCH_TIME']
S_NO = 1

file = open('ec2_inv.csv', 'w')
csv_writer = csv.writer(file)   
#csv_writer.writerow(csv_header)
for each_in in resource.instances.all():
    IN_ID = each_in.instance_id
    IN_TYPE = each_in.instance_type
    IN_ARCHITECTURE = each_in.architecture
    IN_LAUNCH_TIME = each_in.launch_time
    #IN_PRIVATE_IP_ADDRESS = each_in.private_ip_address
    print(S_NO, IN_ID, IN_TYPE, IN_ARCHITECTURE, IN_LAUNCH_TIME)
    csv_writer.writerow([S_NO, IN_ID, IN_TYPE, IN_ARCHITECTURE, IN_LAUNCH_TIME])
    S_NO +=1
    #pprint(dir(each_in))
    #break
file.close()