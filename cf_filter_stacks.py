import boto3
from pprint import pprint
COMMA = ','

# status codes for CF stacks
GOOD_STATES = ('CREATE_COMPLETE,UPDATE_COMPLETE,UPDATE_ROLLBACK_COMPLETE').split(COMMA)
BUSY_STATES = ('CREATE_IN_PROGRESS,ROLLBACK_IN_PROGRESS,DELETE_IN_PROGRESS,UPDATE_IN_PROGRESS,UPDATE_COMPLETE_CLEANUP_IN_PROGRESS,UPDATE_ROLLBACK_IN_PROGRESS,UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS,REVIEW_IN_PROGRESS').split(COMMA)
BAD_STATES  = ('CREATE_FAILED,ROLLBACK_FAILED,DELETE_FAILED,UPDATE_ROLLBACK_FAILED,DELETE_COMPLETE,ROLLBACK_COMPLETE').split(COMMA)

regions = ['ca-central-1', 'us-east-1', 'us-east-2', 'ap-northeast-1', 'ap-southeast-1']

account_id = input("Enter the AWS Account Id:")

# create the custom session
session = boto3.session.Session()
cfn_rs = session.resource(service_name='cloudformation', region_name=regions[1])

good_stacks = [stack for stack in cfn_rs.stacks.all() if stack.stack_status in GOOD_STATES]
good_stack_names = [stack.name for stack in cfn_rs.stacks.all() if stack.stack_status in GOOD_STATES]

busy_stacks = [stack for stack in cfn_rs.stacks.all() if stack.stack_status in BUSY_STATES]
busy_stack_names = [stack.name for stack in cfn_rs.stacks.all() if stack.stack_status in BUSY_STATES]

bad_stacks = [stack for stack in cfn_rs.stacks.all() if stack.stack_status in BAD_STATES]
bad_stack_names = [stack.name for stack in cfn_rs.stacks.all() if stack.stack_status in BAD_STATES]

my_stacks = [stack for stack in cfn_rs.stacks.all() if stack.stack_status not in BAD_STATES]
my_stack_names = [stack.name for stack in cfn_rs.stacks.all() if stack.stack_status not in BAD_STATES]

# if we want further detailing of all the CF stacks.
pprint(dir(cfn_rs))
